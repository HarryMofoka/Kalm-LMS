"""
Activity 124: Methods Returning New Objects vs. Mutating State
Difficulty: 124 / 132

Every method makes an intentional design choice:
  - **Mutating (in-place)**: updates `self` (like `list.append()`).
  - **Non-mutating (pure / functional)**: leaves `self` untouched and returns a
    BRAND-NEW object (like `str.upper()` or `ExampleVector2D.add()`).

Knowing which one you are writing prevents the nastiest aliasing bugs in Python!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — ExampleVector2D (Non-Mutating)
===============================================================================
Problem:
    Build `ExampleVector2D(dx, dy)` where `add(other)` and `scale(factor)`
    return BRAND-NEW `ExampleVector2D` instances without modifying `self`.

Step-by-Step Breakdown:
    1. `v1 = ExampleVector2D(2, 3)` and `v2 = v1.scale(4)`:
       `v1` is STILL `(2, 3)` while `v2` is `(8, 12)`.
    2. Because neither vector mutates, you can safely share vectors across
       multiple physics calculations without surprises!

===============================================================================
PART 2: YOUR TURN ("YOU DO") — GridCursor (Mutating + Non-Mutating Preview)
===============================================================================
Problem:
    Implement `GridCursor` for navigating a `rows x cols` 2D grid with bounds
    clamping AND movement history:
      - `__init__(self, rows: int, cols: int, row: int = 0, col: int = 0) -> None`
        * Raises `ValueError` if `rows <= 0`, `cols <= 0`,
          `not (0 <= row < rows)`, or `not (0 <= col < cols)`.
        * Stores `self.rows`, `self.cols`, `self.row`, `self.col`.
        * Initializes `self.history: list[tuple[int, int]] = [(row, col)]`.
      - `position(self) -> tuple[int, int]`
        * Returns `(self.row, self.col)`.
      - `move(self, dr: int, dc: int) -> tuple[int, int]`  (MUTATING!)
        * Computes new row clamped to `[0, self.rows - 1]` and new col clamped
          to `[0, self.cols - 1]`.
        * Updates `self.row`, `self.col`, appends `(self.row, self.col)` to
          `self.history`, and returns `(self.row, self.col)`.
      - `preview_move(self, dr: int, dc: int) -> GridCursor`  (NON-MUTATING!)
        * Computes the same clamped `(new_row, new_col)`, does NOT mutate `self`
          or `self.history`, and returns a NEW `GridCursor(self.rows, self.cols, new_row, new_col)`!

    Examples:
        cur = GridCursor(3, 4)          # starts at (0, 0), history=[(0, 0)]
        cur.move(1, 2)                  -> (1, 2)
        cur.move(10, -5)                -> (2, 0)   # clamped inside 3x4!
        cur.history                     -> [(0, 0), (1, 2), (2, 0)]

        ghost = cur.preview_move(-1, 3) # NEW cursor at (1, 3)!
        ghost.position()                -> (1, 3)
        cur.position()                  -> (2, 0)   # unchanged!
        cur.history                     -> [(0, 0), (1, 2), (2, 0)]  # unchanged!

    Edge-case hints:
        - Clamping formula: `max(0, min(limit - 1, value))`.
        - Even if a clamped `move()` stays on the same cell (e.g., moving `(-1, 0)`
          from row `0`), `move()` STILL records the resulting cell in `self.history`!
"""
from __future__ import annotations


class ExampleVector2D:
    """An immutable-style 2D displacement vector whose operations return new objects."""

    def __init__(self, dx: int, dy: int) -> None:
        self.dx = dx
        self.dy = dy

    def add(self, other: ExampleVector2D) -> ExampleVector2D:
        """Return a NEW vector equal to self + other."""
        return ExampleVector2D(self.dx + other.dx, self.dy + other.dy)

    def scale(self, factor: int) -> ExampleVector2D:
        """Return a NEW vector scaled by `factor`."""
        return ExampleVector2D(self.dx * factor, self.dy * factor)

    def as_tuple(self) -> tuple[int, int]:
        """Return (dx, dy) as a plain tuple."""
        return (self.dx, self.dy)


class GridCursor:
    """A bounded grid cursor with clamped movement, history log, and pure preview."""

    def __init__(self, rows: int, cols: int, row: int = 0, col: int = 0) -> None:
        """Initialize cursor inside a rows x cols grid and start history log."""
        pass

    def position(self) -> tuple[int, int]:
        """Return current (row, col) coordinate."""
        pass

    def move(self, dr: int, dc: int) -> tuple[int, int]:
        """Move by (dr, dc), clamping inside bounds, append to history, and return pos."""
        pass

    def preview_move(self, dr: int, dc: int) -> GridCursor:
        """Return a NEW GridCursor at the clamped destination without mutating self."""
        pass


if __name__ == "__main__":
    v1 = ExampleVector2D(2, -1)
    v2 = v1.add(ExampleVector2D(3, 5))
    print("v1 (unchanged):", v1.as_tuple())
    print("v2 (new):      ", v2.as_tuple())
    print("v1 * 3 (new):  ", v1.scale(3).as_tuple())
