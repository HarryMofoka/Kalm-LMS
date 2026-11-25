# Checkpoint 19 — Retro Arcade Track & Multi-Runner Race Simulator

- **Unlocked After:** Activity 120 — Advanced Grid Simulation & Halo Tracks
- **Difficulty:** Hard (Tier 5 — Multi-Entity Grid Simulation)
- **Core Concepts:** 2D walled grid construction, inner clockwise halo loops, `divmod` lap tracking, multi-entity tick simulation, collision detection, immutable inputs, zero trailing spaces

---

## Real-World Value

Turn-based strategy games, arcade engines (Snake, Tron, Pac-Man), and warehouse traffic simulators are all built on the exact same architecture: **a discrete tick loop that advances entity states, detects cell collisions, updates counters, and renders a fresh frame without corrupting the base board**.

Separating **simulation state** (positions, lap counters, collision events) from **rendering** (converting a board + entities to ASCII rows) lets you write deterministic unit tests, replay bugs from event logs, and swap out the renderer (CLI, web canvas, Pygame) without touching a single line of physics logic!

---

## Problem Statement

Build a **Retro Arcade Track & Multi-Runner Race Simulator**:
1. Construct a walled arena (`#`) containing a clockwise inner halo track (`.`) and an open courtyard (` `).
2. Advance any runner along the track using `divmod` to compute both the wrapped index and the number of full laps gained in a single tick.
3. Simulate `ticks` rounds of a multi-racer race without mutating the caller's input list, detecting every cell collision at every tick, tracking final coordinates & lap counts, and rendering the final board with **zero trailing spaces**.

---

## How a Similar Functioning System Was Done (`worked_example.py`)

Study **`worked_example.py`** — a complete **Mars Rover Grid Mission Simulator** that executes N/E/S/W commands on a rocky grid with immutable state transitions, obstacle/boundary collision checks, battery tracking, and ASCII visualization.

### Design Walkthrough

1. **Immutable State Transitions (`step_rover`)**:
   - Instead of mutating the input `state` dictionary in place, `step_rover` builds and returns a brand-new `dict` (including a fresh copy of `trail`). That makes step-by-step replay and testing effortless.
2. **Boundary & Obstacle Guards**:
   - Every candidate move `(nr, nc)` is checked against `0 <= nr < height`, `0 <= nc < width`, and `(nr, nc) not in obstacles` before updating position.
3. **Decoupled Renderer (`render_mars_board`)**:
   - Starts from a clean map (`create_mars_map`), overlays trail markers `*`, stamps the rover `R`, and joins rows with `" ".join(row).rstrip()`.

Run the reference demo anytime:
```bash
python master_projects/checkpoint_19_retro_snake_board_engine/worked_example.py
```

---

## Your Project Brief (`project.py`)

Implement the following three functions in `project.py`:

1. **`create_race_board(width: int, height: int) -> tuple[list[list[str]], list[tuple[int, int]]]`**
   - Raise `ValueError` if `width < 4` or `height < 4` (minimum size for an outer wall + 2x2 inner loop).
   - Build a `height x width` 2D list of single-character strings:
     - Outer perimeter (`r == 0`, `r == height - 1`, `c == 0`, `c == width - 1`): `'#'`
     - Inner halo (one cell inside the walls: `r in {1, height - 2}` or `c in {1, width - 2}` within `1..height-2` and `1..width-2`): `'.'`
     - Inner courtyard (anything deeper inside when `width >= 5` and `height >= 5`): `' '`
   - Build `track_path`: the clockwise ordered `list[tuple[int, int]]` of inner halo cells starting at `(1, 1)` (top inner edge left-to-right, right inner edge top-to-bottom, bottom inner edge right-to-left, left inner edge bottom-to-top — no duplicate corners!).
   - Return `(board, track_path)`.

2. **`step_runner(path: list[tuple[int, int]], current_index: int, speed: int) -> tuple[int, int]`**
   - Raise `ValueError` if `path` is empty, `current_index < 0`, or `speed < 0`.
   - Normalize `start = current_index % len(path)` and compute `laps_gained, new_index = divmod(start + speed, len(path))`.
   - Return `(new_index, laps_gained)`.

3. **`simulate_race(width: int, height: int, racers: list[dict], ticks: int) -> dict`**
   - Raise `ValueError` if `ticks < 0`.
   - Each item in `racers` is a dict: `{"name": str, "symbol": str, "start": int, "speed": int}`.
   - **Never mutate** the caller's `racers` list or its dictionaries.
   - Start each racer at `index = racer["start"] % len(track_path)` with `laps = 0`.
   - For each tick `t` from `1` to `ticks` (inclusive):
     - Advance every racer with `step_runner(track_path, idx, racer["speed"])`, updating `idx` and adding `laps_gained` to `laps`.
     - Check for **cell collisions**: any cell occupied by 2 or more racers at the end of tick `t` records an event:
       `{"tick": t, "cell": (r, c), "racers": [name1, name2, ...]}`
       (Preserve input order for `racers` inside each event; if multiple cells collide on the same tick, order events by `track_path.index(cell)`.)
   - Render the final board from a fresh copy of `board`:
     - Place each racer's `symbol` at its final coordinate.
     - If 2 or more racers finish on the same cell, render `'X'` on that cell.
     - Convert each row using `" ".join(row).rstrip()` (**ZERO trailing spaces**!).
   - Return:
     ```python
     {
         "positions": {name: (row, col), ...},
         "indices": {name: final_index, ...},
         "laps": {name: total_laps, ...},
         "collisions": [{"tick": int, "cell": (r, c), "racers": [str, ...]}, ...],
         "board": list[str],
     }
     ```

---

## Running Tests

From the `ExamPrep/` root directory:

```bash
python -m unittest master_projects/checkpoint_19_retro_snake_board_engine/test_project.py -v
```
