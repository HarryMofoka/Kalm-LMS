# Checkpoint 10 — Cinema Seat Grid & Group Allocator

- **Unlocked After:** Activity 060 *(2D Lists, Grids & Coordinate Logic)*
- **Difficulty:** ★★★☆☆ (Intermediate-Advanced)
- **Core Concepts:** Safe 2D grid creation (avoiding row aliasing), coordinate bounds validation, contiguous block scanning, pure 2D grid cloning, clean ASCII rendering (zero trailing spaces)

---

## Real-World Value

Every time you book movie tickets at **Ster-Kinekor or Nu Metro**, select concert seats on **Ticketmaster**, or pick adjacent airline seats during check-in, a 2D seat-reservation engine is working behind the scenes to guarantee:

1. **No double bookings** and strict coordinate bounds checking.
2. **Smart group seating:** Finding the first contiguous block of `N` adjacent seats in the same row so families and friends sit together.
3. **Zero aliasing bugs:** One of the most notorious Python bugs is creating a 2D grid with `[["O"] * cols] * rows` — which points every row to the **same** list in memory! Booking Row A suddenly books Row B, Row C, and Row D too!
4. **Crisp terminal / UI visualizations** with clean row labels (`A, B, C...`) and zero sloppy trailing whitespace.

In this checkpoint, you will build a complete, pure 2D Cinema Seat Grid & Group Allocator.

---

## Problem Statement

Build a pure (non-mutating) 2D cinema seat booking engine where `"O"` represents an open seat and `"X"` represents a booked seat. Your module must safely construct grids without row aliasing, book individual seats or contiguous groups while returning fresh grid copies, compute occupancy metrics (including full rows), and render a crisp labeled ASCII seat map with zero trailing spaces.

---

## How a Similar Functioning System Was Done (`worked_example.py`)

Study [`worked_example.py`](worked_example.py) — a **Parking Garage 2D Bay Allocator**.

A multi-level parking garage tracks open bays (`"."`) and parked cars (`"P"`) across levels and bay columns.

### Key Architectural Patterns in `worked_example.py`

1. **Row-Alias-Free Grid Creation (`create_garage`):**
   Uses `[["." for _ in range(bays_per_level)] for _ in range(levels)]` so every level has its own independent list object in memory.
2. **Deep-Copy Pure Updates (`_clone_grid` + `reserve_bay`):**
   Clones each row `[list(row) for row in garage]` before setting `updated[level][bay] = "P"`, ensuring callers can keep history or roll back cleanly without accidental side effects.
3. **Strict Non-Negative Coordinate Guards:**
   Explicitly checks `0 <= level < len(garage)` and `0 <= bay < len(garage[level])` so negative indices like `-1` never silently wrap around to the back of the garage!
4. **Zero-Trailing-Space ASCII Renderer (`render_garage_map`):**
   Joins cell tokens with `" ".join(row)` and rows with `"\n"`, guaranteeing every rendered line has no trailing spaces.

Run the reference demo:

```bash
python master_projects/checkpoint_10_cinema_seat_booking/worked_example.py
```

---

## Your Project Brief (`project.py`)

Implement the six functions in [`project.py`](project.py). Use `"O"` (`OPEN_SEAT`) for open seats and `"X"` (`BOOKED_SEAT`) for booked seats.

> **Pure / Non-Mutating Rule:** `book_seat` and `book_group` MUST return a **new** 2D list (cloned rows) and leave the input `seat_map` completely unchanged!

### 1. `create_seat_map(rows: int, cols: int) -> list[list[str]]`
- Validate `1 <= rows <= 26` (rows map to labels `A`–`Z`) and `cols >= 1`; raise `ValueError` otherwise.
- Return a `rows x cols` 2D list filled with `"O"`, with **no row aliasing** (every row is an independent list).

### 2. `book_seat(seat_map: list[list[str]], row: int, col: int) -> list[list[str]]`
- Validate `0 <= row < len(seat_map)` and `0 <= col < len(seat_map[row])`; raise `ValueError` if out of bounds (including negative indices!).
- If `seat_map[row][col]` is already `"X"`, raise `ValueError`.
- Return a **new** 2D list with `(row, col)` set to `"X"`, without mutating `seat_map`.

### 3. `find_contiguous_seats(seat_map: list[list[str]], group_size: int) -> tuple[int, int] | None`
- Validate `group_size >= 1`; raise `ValueError` if `group_size < 1`.
- Scan rows top-to-bottom (`0` to `rows - 1`) and columns left-to-right (`0` to `cols - group_size`).
- Return the **first** `(row, start_col)` where `group_size` consecutive seats in that same row are all `"O"`.
- Return `None` if no row can fit `group_size` contiguous open seats.

### 4. `book_group(seat_map: list[list[str]], group_size: int) -> tuple[list[list[str]], tuple[int, int]]`
- Use `find_contiguous_seats(seat_map, group_size)` to locate the first available block.
- If `group_size < 1` or no contiguous block is available (`None`), raise `ValueError`.
- Return `(updated_seat_map, (row, start_col))` with all `group_size` seats in that block set to `"X"`, without mutating `seat_map`.

### 5. `occupancy_stats(seat_map: list[list[str]]) -> dict[str, object]`
- Return a dictionary with exact keys:
  - `"total_seats"` (`int`): total number of seats in the grid
  - `"booked_seats"` (`int`): count of `"X"` seats
  - `"available_seats"` (`int`): count of `"O"` seats
  - `"occupancy_pct"` (`float`): `(booked_seats / total_seats) * 100` rounded to 2 decimal places (`0.0` if `total_seats == 0`)
  - `"full_rows"` (`int`): count of non-empty rows where every seat is `"X"`

### 6. `render_seat_map(seat_map: list[list[str]]) -> str`
- Render the 2D grid as a multi-line string using uppercase row labels `A`, `B`, `C`, ... (`chr(ord("A") + row_idx)`):
  ```text
  A: O X X O
  B: O O O O
  C: X X X X
  ```
- Each row has the exact format `f"{label}: {' '.join(row)}"`.
- **ZERO trailing spaces** on any line!
- Return `""` if `seat_map` is empty (`[]`).

---

## Running Tests

From the `ExamPrep/` directory:

```bash
python -m unittest master_projects/checkpoint_10_cinema_seat_booking/test_project.py -v
```
