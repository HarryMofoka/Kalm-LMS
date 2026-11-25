# Refactoring Mission 10 — Grid Aliasing Disaster (CP 10)

## Backstory & Problem Statement

A warehouse floor-mapping script (`build_warehouse_map`) looked totally fine when tested on an empty floor or a single aisle (`1 x 4`). Even `create_empty_grid(3, 4) == [[".", ".", ".", "."], ...]` passed!

Then the logistics team tried placing crates on row `0` and row `2` of a `3 x 4` warehouse — and suddenly **ghost crates cloned themselves into every single row**!

Why? Because `create_empty_grid` used Python's most infamous 2D-list trap:

```python
[["."] * cols] * rows
```

Multiplying an outer list does **not** copy the inner row — it puts `rows` references to the **exact same list object** inside the grid! On top of that, `render_grid` and `build_warehouse_map` are packed with cryptic single-letter index variables (`g, i, j, k, m, x, y`).

Your mission: eliminate the row-aliasing disaster and clean up the cryptic grid loops!

## Code Smells Checklist

- [ ] **2D list row-aliasing bug (`[[fill] * cols] * rows`)** — every row in the grid points to the same list in memory (`grid[0] is grid[1]`).
- [ ] **Cryptic single-letter variables (`g, k, m, x, y, i, j`)** obscuring what rows, columns, and coordinates mean.
- [ ] **Clunky manual index loops** in `render_grid` and `build_warehouse_map` where direct iteration, tuple unpacking (`for row, col in crates:`), and `" ".join(row)` are vastly cleaner.

## Worked Refactoring Walkthrough (Before -> After)

Open [`worked_example.py`](worked_example.py) to compare a 2D board initializer before and after fixing row aliasing:

### Before (`before_make_board`)
```python
def before_make_board(rows, cols, fill="."):
    return [[fill] * cols] * rows
```
Setting `board[0][0] = "X"` turns **every** row into `["X", ".", ".", "."]`!

### After (`after_make_board`)
```python
def after_make_board(rows, cols, fill="."):
    return [[fill for _ in range(cols)] for _ in range(rows)]
```
Now every row is an **independent list object** (`board[0] is not board[1]`), so updating `board[0][0]` affects ONLY row `0`!

## Your Refactoring Mission

Refactor [`messy_code.py`](messy_code.py) so that:

1. **`create_empty_grid(rows, cols, fill=".")` creates independent row lists** (no `[[...] * cols] * rows` aliasing — every row is a distinct list object!).
2. **Placing a crate on row `0` never modifies rows `1` or `2`**.
3. **`build_warehouse_map(rows, cols, crates)` places crates ONLY at the exact `(row, col)` coordinates** without contaminating any other rows.
4. **Clean up cryptic single-letter loops** in `build_warehouse_map`, `place_crate`, and `render_grid` (try tuple unpacking `for row, col in crates:` and `"\n".join(" ".join(row) for row in grid)`!).
5. **All `TestBehaviorSafetyNet` tests remain 100% GREEN!**

## Run the Tests

Run from the `ExamPrep` directory:

```bash
python -m unittest refactoring_projects/refactor_10_grid_aliasing_disaster/test_refactor.py -v
```
