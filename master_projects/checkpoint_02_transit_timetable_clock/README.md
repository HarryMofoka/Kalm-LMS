# Checkpoint 02 — City Bus & Train Wrap-Around Timetable Engine

- **Unlocked After:** Activity 012 (`//`, `%`, Time Math & Formatting)
- **Difficulty:** Beginner–Intermediate
- **Core Concepts:** Integer division (`//`), modulo (`%`), 24-hour clock arithmetic, overnight wrap-around, zero-padded string formatting (`:02d`)

---

## Real-World Value

Public transit GTFS engines (Google Maps Transit, Citymapper, Gautrain / MyCiTi timetables), airline flight boards, and hospital shift schedulers all share one foundational trick: **never do arithmetic directly on `(hour, minute)` pairs**.

Adding 45 minutes to `23:40` or finding the duration of an overnight train departing `23:30` and arriving `00:15` produces messy nested `if` branches if you manipulate hours and minutes separately. Convert time into **total minutes since midnight (`0..1439`)**, apply `+`, `-`, `// 1440`, and `% 1440`, and format back to `"HH:MM"` only at the very end!

---

## Problem Statement

Build a city bus and train wrap-around timetable engine in `project.py` that:

1. Converts valid 24-hour `(hour, minute)` pairs into minutes since midnight (`0..1439`).
2. Formats any integer minute count into a zero-padded `"HH:MM"` 24-hour clock string (wrapping cleanly past midnight via `% 1440`).
3. Computes arrival clock time and `days_later` rollover count for trips of any duration (including multi-day journeys).
4. Computes shortest non-negative trip durations across overnight midnight boundaries.
5. Calculates the next scheduled departure clock time and wait duration in minutes given a service frequency and optional first-departure time.

---

## How a Similar Functioning System Was Done (`worked_example.py`)

Before writing your timetable engine, inspect and run **`worked_example.py`** — a complete **Global Conference Slot & Countdown Clock Formatter**.

```bash
python master_projects/checkpoint_02_transit_timetable_clock/worked_example.py
```

### Architectural Walkthrough

1. **Single Canonical Representation:** `hm_to_minutes(hour, minute)` validates bounds (`0 <= hour <= 23`, `0 <= minute <= 59`) and converts everything to linear minutes.
2. **Modular Clock Formatting:** `minutes_to_clock(total_minutes)` uses `total_minutes % 1440` so both overflow (`1500 -> "01:00"`) and negative offsets (`-30 -> "23:30"`) work automatically without special-case `if` blocks.
3. **Floor Division for Day Rollovers:** Python's `//` floors toward negative infinity, which means:
   - `raw = 1380 + 120 = 1500` -> `1500 // 1440 == +1` (next day!)
   - `raw = 60 - 180 = -120` -> `-120 // 1440 == -1` (previous day!)
   - `raw = 600 + 60 = 660` -> `660 // 1440 == 0` (same day!)
4. **Cascading `//` and `%` for Countdowns:** `format_countdown()` peels off days (`// 1440`), remaining hours (`(rem) // 60`), and minutes (`rem % 60`).

### Traced Example (`worked_example.py`)

Call: `convert_timezone_slot(hour=22, minute=30, offset_minutes=180)` (a 22:30 UTC talk viewed in UTC+3)

| Step | Expression | Result |
|---|---|---|
| 1. Convert to linear minutes | `22 * 60 + 30` | `1350` |
| 2. Apply timezone offset | `1350 + 180` | `1530` |
| 3. Day shift | `1530 // 1440` | `1` (next day) |
| 4. Wrapped local minutes | `1530 % 1440` | `90` |
| 5. Format `"HH:MM"` | `f"{90 // 60:02d}:{90 % 60:02d}"` | `"01:30"` |
| **Return** | `(local_clock, day_shift)` | `("01:30", 1)` |

---

## Your Project Brief (`project.py`)

Implement the following 5 functions in `project.py`:

### 1. `to_minutes(hour: int, minute: int) -> int`
- Validates `0 <= hour <= 23` and `0 <= minute <= 59` (raises `ValueError` otherwise).
- Returns `hour * 60 + minute`.

### 2. `format_clock_24h(total_minutes: int) -> str`
- Wraps `total_minutes` modulo `1440` and returns zero-padded `"HH:MM"` (e.g., `65 -> "01:05"`, `1440 -> "00:00"`, `-15 -> "23:45"`).

### 3. `arrival_time(depart_hour: int, depart_minute: int, duration_minutes: int) -> tuple[str, int]`
- Validates the departure time and checks `duration_minutes >= 0` (raises `ValueError` if negative).
- Returns `(hh_mm_str, days_later)` where `days_later = total // 1440`.
- Example: `arrival_time(23, 40, 45)` -> `("00:25", 1)`.

### 4. `trip_duration_minutes(depart_hour: int, depart_minute: int, arrive_hour: int, arrive_minute: int) -> int`
- Validates both times.
- Returns `(arrive_total - depart_total) % 1440`, cleanly handling overnight trips.
- Example: `trip_duration_minutes(23, 30, 0, 15)` -> `45`.

### 5. `next_departure(current_hour: int, current_minute: int, frequency_minutes: int, first_hour: int = 0, first_minute: int = 0) -> tuple[str, int]`
- Validates both times and requires `frequency_minutes >= 1` (raises `ValueError` otherwise).
- Buses depart every `frequency_minutes` starting from `(first_hour, first_minute)`.
- If current time is at or before the first departure (`now <= first`), the next departure is the first departure (`wait = first - now`).
- Otherwise, find the smallest non-negative `wait` until the next multiple of `frequency_minutes` after `first`:
  - If `now` lands exactly on a departure (`(now - first) % frequency_minutes == 0`), `wait = 0`.
  - Otherwise, `wait = frequency_minutes - ((now - first) % frequency_minutes)`.
- Returns `(format_clock_24h(now + wait), wait)`.
- Example: `next_departure(8, 7, 15)` -> `("08:15", 8)`.
- Example: `next_departure(23, 50, 20)` -> `("00:00", 10)`.

### Acceptance Criteria
- All 6 tests in `TestMasterProject` pass alongside the 5 tests in `TestWorkedExample`.
- Overnight rollovers and multi-day trips require zero special-case hacks.

### Fun Stretch Ideas (After Tests Pass)
- Add a `build_route_timetable(first_hour, first_minute, frequency_minutes, count)` helper that prints the next `N` departures for a bus stop display board.
- Format 12-hour AM/PM equivalents alongside 24-hour times.

---

## Running Tests

Run from the `ExamPrep/` directory:

```bash
python -m unittest master_projects/checkpoint_02_transit_timetable_clock/test_project.py -v
```
