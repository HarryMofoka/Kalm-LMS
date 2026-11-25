# Checkpoint 18 — Security Drone Perimeter Patrol Planner

- **Unlocked After:** Activity 114 — Halo Rules, Clockwise Walks & Modulo
- **Difficulty:** Hard (Tier 4 — Halo Patterns & Periodic Scheduling)
- **Core Concepts:** Clockwise rectangular perimeter walks, degenerate thin-shape handling (`1x1`, `1xW`, `Hx1`), even modulo spacing, GCD synchronization math, ASCII grid rendering with zero trailing spaces

---

## Real-World Value

Automated warehouse robots, autonomous security drones, and agricultural boundary monitors all share the same core geometry problem: **scheduling multiple moving agents along a closed perimeter loop without collisions or blind spots**.

By turning a 2D rectangular perimeter into a **1D ordered clockwise ring** (`list[tuple[int, int]]`), complex 2D motion collapses into simple **modulo arithmetic** (`(start + tick) % perimeter_len`), and fleet synchronization reduces to classic number theory (`gcd`). This directly bridges the Halo Patterns Workshop into real robotics & scheduling software!

---

## Problem Statement

Build a **Security Drone Perimeter Patrol Planner** for rectangular facilities of size `width x height`:
1. Compute the clockwise outer perimeter walk `(row, col)` without duplicating corners — even for degenerate `1x1`, `1xW`, and `Hx1` corridors.
2. Evenly space `num_drones` along the perimeter and compute their exact coordinates after any `tick`.
3. Render an ASCII patrol map using `'o'` for empty track, `'1'..'9'` (and `'D'` for 10th+ drones) for drones, `' '` inside, single spaces between cells, and **zero trailing spaces**.
4. Calculate how many ticks it takes for two drones moving at different speeds around a perimeter of length `perimeter_len` to next synchronize on the same cell.

---

## How a Similar Functioning System Was Done (`worked_example.py`)

Study **`worked_example.py`** — a complete **Conveyor Belt Inspection Station Scheduler** that coordinates evenly spaced optical sensors moving along a rectangular factory conveyor loop.

### Design Walkthrough

1. **Corner-Safe Clockwise Halo Walk (`conveyor_loop`)**:
   - Guard degenerate cases first:
     - `height == 1`: single left-to-right row `[(0, c) for c in range(width)]`.
     - `width == 1`: single top-to-bottom column `[(r, 0) for r in range(height)]`.
   - General `width >= 2, height >= 2` walks four half-open edges so no corner is ever added twice:
     - Top edge: `c = 0 .. width - 1`
     - Right edge: `r = 1 .. height - 1`
     - Bottom edge: `c = width - 2 .. 0`
     - Left edge: `r = height - 2 .. 1`
2. **Even Spacing via Integer Floor Division + Modulo (`sensor_coordinates`)**:
   - For perimeter length `P`, agent `i` starts at `(i * P) // num_agents`. When `num_agents <= P`, every agent is guaranteed a unique starting index!
   - Advancing `tick` steps simply evaluates `walk[(start_idx + tick) % P]`.
3. **Clean Grid Rendering (`render_factory_floor`)**:
   - Populates a `height x width` 2D grid of `' '`, stamps the loop with `'.'`, overlays sensor labels, and joins each row with `" ".join(row).rstrip()`.

Run the reference demo anytime:
```bash
python master_projects/checkpoint_18_perimeter_patrol_scheduler/worked_example.py
```

---

## Your Project Brief (`project.py`)

Implement the following four functions in `project.py`:

1. **`build_perimeter_walk(width: int, height: int) -> list[tuple[int, int]]`**
   - Raise `ValueError` if `width < 1` or `height < 1`.
   - Return clockwise `(row, col)` coordinates starting at `(0, 0)` with **no duplicate cells**.
   - Must handle `1x1` (`[(0, 0)]`), `1xW`, `Hx1`, and `WxH` cleanly.

2. **`drone_positions(width: int, height: int, num_drones: int, tick: int) -> list[tuple[int, int]]`**
   - Build the perimeter walk of length `P`.
   - Raise `ValueError` if `num_drones < 0` or `num_drones > P`.
   - Return `[]` if `num_drones == 0`.
   - For drone `i` in `0 .. num_drones - 1`, compute:
     `index = ((i * P) // num_drones + tick) % P`
     and return `[walk[index] for i in range(num_drones)]`.

3. **`render_patrol_map(width: int, height: int, num_drones: int, tick: int) -> list[str]`**
   - Build a `height x width` character grid filled with `' '`.
   - Mark every cell on the perimeter walk with `'o'`.
   - Overlay each drone `i` (0-indexed) at its position from `drone_positions`:
     - Drones `0..8` use `'1'..'9'` (`str(i + 1)`).
     - Drone `9` and beyond use `'D'`.
   - Join cells in each row with a single space `' '` and strip any trailing spaces so **zero trailing spaces** exist on every line.

4. **`ticks_until_sync(perimeter_len: int, speed_a: int, speed_b: int) -> int`**
   - Raise `ValueError` if `perimeter_len <= 0`.
   - Two drones start together at index `0` and move at integer speeds `speed_a` and `speed_b` cells per tick around a loop of length `perimeter_len`.
   - Return the smallest positive integer tick `t >= 1` at which `(speed_a * t) % perimeter_len == (speed_b * t) % perimeter_len`.
   - Hint: Think about `math.gcd(perimeter_len, abs(speed_a - speed_b))`!

---

## Running Tests

From the `ExamPrep/` root directory:

```bash
python -m unittest master_projects/checkpoint_18_perimeter_patrol_scheduler/test_project.py -v
```
