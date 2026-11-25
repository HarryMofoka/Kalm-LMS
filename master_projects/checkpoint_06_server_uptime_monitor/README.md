# Checkpoint 06 — Server Heartbeat & SLA Uptime Analyzer

- **Unlocked After:** Activity 036 *(Loops, Streaks & Analytics)*
- **Difficulty:** ★★☆☆☆ (Intermediate)
- **Core Concepts:** Loop state machines, streak tracking, interval/window detection, percentage rounding, summary reporting

---

## Real-World Value

Every serious cloud platform — **UptimeRobot, Datadog Synthetics, PagerDuty, AWS CloudWatch, and Pingdom** — runs heartbeat probes against production servers every few seconds or minutes.

When a company promises customers a **"two nines" (99.0%)** or **"three nines" (99.9%) Service Level Agreement (SLA)**, Site Reliability Engineers (SREs) need software that answers four mission-critical questions automatically:

1. **What is our exact uptime percentage** over the monitoring window?
2. **How long was our worst uninterrupted outage streak?** (A single 1-minute blip is a hiccup; 5 consecutive minutes down wakes up the on-call engineer!)
3. **Exactly when did every outage start and end?** (Incident post-mortems require exact `(start, end)` incident windows.)
4. **Did we meet our SLA, or is the service degraded / critical?**

In this checkpoint, you will build a clean, production-style SRE Heartbeat & SLA Analyzer module.

---

## Problem Statement

Given a chronological sequence of server heartbeat checks (`list[bool]`, where `True` means the server responded `200 OK` and `False` means the probe timed out or failed), build an analytics engine that computes uptime percentage, tracks the longest consecutive outage streak, extracts every contiguous outage window as `(start_idx, end_idx)` tuples, and assembles a complete SLA status report dictionary.

---

## How a Similar Functioning System Was Done (`worked_example.py`)

Before writing your server monitor, study [`worked_example.py`](worked_example.py) — an **IoT Weather Station Sensor Health Analyzer**.

An outdoor weather station logs hourly temperature readings (`list[float | None]`). Hardware glitches show up as `None` (dropped packet) or physically impossible spikes outside `[-50.0, 60.0]` °C.

### Key Architectural Patterns in `worked_example.py`

1. **Single-Responsibility Predicate (`is_valid_reading`):**
   Centralizes the definition of "healthy" in one small helper so `calculate_health_pct`, `longest_error_streak`, and `find_error_bursts` never drift out of sync.
2. **Running Streak Counter (`longest_error_streak`):**
   Maintains `current_streak` and `best_streak`. Every bad reading increments `current_streak` and updates `best_streak`; every good reading resets `current_streak = 0`.
3. **Boundary-Aware Window Scanner (`find_error_bursts`):**
   Tracks `burst_start: int | None`. When entering an invalid reading while `burst_start is None`, record `burst_start = idx`. When returning to a valid reading, close the window `(burst_start, idx - 1)`. **Crucial edge case:** after the loop ends, check if `burst_start is not None` to close an outage that reaches the very last reading!
4. **Composed Report Builder (`sensor_health_summary`):**
   Reuses the smaller analytics functions rather than duplicating loops, returning a structured dictionary ready for JSON APIs, dashboards, or alerting webhooks.

Run the reference demo to see it in action:

```bash
python master_projects/checkpoint_06_server_uptime_monitor/worked_example.py
```

---

## Your Project Brief (`project.py`)

Implement the four functions in [`project.py`](project.py). Each heartbeat list contains booleans: `True` = server UP, `False` = server DOWN.

### 1. `calculate_uptime_pct(heartbeats: list[bool]) -> float`
- Compute the percentage of `True` heartbeats rounded to **2 decimal places** (`round(up / total * 100, 2)`).
- Return `0.0` if `heartbeats` is empty.

### 2. `longest_outage_streak(heartbeats: list[bool]) -> int`
- Return the length of the longest consecutive run of `False` values.
- Return `0` if `heartbeats` is empty or contains no `False` values.

### 3. `find_outage_windows(heartbeats: list[bool]) -> list[tuple[int, int]]`
- Find every contiguous run of one or more `False` values and return them in chronological order as inclusive `(start_idx, end_idx)` tuples.
- Example: `[True, False, False, True, False]` -> `[(1, 2), (4, 4)]`.
- Return `[]` if `heartbeats` is empty or all `True`.

### 4. `sla_report(heartbeats: list[bool], target_sla: float = 99.0) -> dict[str, object]`
- Compose the functions above and return a dictionary with these exact keys:
  - `"total_checks"` (`int`): total heartbeats inspected
  - `"up_checks"` (`int`): count of `True` heartbeats
  - `"down_checks"` (`int`): count of `False` heartbeats
  - `"uptime_pct"` (`float`): uptime percentage (rounded to 2 decimal places)
  - `"target_sla"` (`float`): the target SLA threshold passed in
  - `"sla_met"` (`bool`): `True` if `total_checks > 0` and `uptime_pct >= target_sla`, otherwise `False`
  - `"longest_outage"` (`int`): longest consecutive `False` streak
  - `"outage_windows"` (`list[tuple[int, int]]`): all `(start_idx, end_idx)` outage windows
  - `"incident_count"` (`int`): number of distinct outage windows (`len(outage_windows)`)
  - `"status"` (`str`): determined by these exact rules:
    - `"NO_DATA"` if `total_checks == 0`
    - `"HEALTHY"` if `sla_met` is `True` and `longest_outage < 3`
    - `"DEGRADED"` if (`sla_met` is `True` and `longest_outage >= 3`) OR (`sla_met` is `False` and `uptime_pct >= target_sla - 5.0`)
    - `"CRITICAL"` if `total_checks > 0` and `uptime_pct < target_sla - 5.0`

---

## Running Tests

From the `ExamPrep/` directory:

```bash
python -m unittest master_projects/checkpoint_06_server_uptime_monitor/test_project.py -v
```

- `TestWorkedExample` should pass 100% right away.
- `TestMasterProject` starts red and turns green as you implement `project.py`!
