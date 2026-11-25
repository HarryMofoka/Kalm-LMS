"""
Activity 114: Clockwise Legs Walk on Squares & Rectangles  [Unlocks Checkpoint 18!]
Difficulty: 114 / 132

Welcome to Question 2 of the Halo Patterns Workshop:
    "In what order do we visit the outline?"  ->  a PATH (list of `(row, col)` tuples)!

The #1 bug in perimeter walks is visiting corners TWICE — or walking the same
row/column backwards on thin `4x1` or `1x3` rectangles!
The cure is a **Legs Table** where every corner belongs to EXACTLY ONE leg.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Square Clockwise Walk
===============================================================================
Problem:
    Write `example_square_walk(size)` returning the outline cells of a
    `size x size` square in clockwise order starting at `(0, 0)`, with NO cell
    visited twice.

Draw -> Index -> Legs Table:
    DRAW & INDEX (size = 3, last = 2):
        (0,0) -> (0,1) -> (0,2)
          ^                 |
          |                 v
        (1,0)             (1,2)
          ^                 |
          |                 v
        (2,0) <- (2,1) <- (2,2)

    LEGS TABLE (for size >= 2, last = size - 1):
        | Leg    | Fixed      | Variable range            | Starts at        | Ends at         |
        |--------|------------|---------------------------|------------------|-----------------|
        | Top    | row = 0    | col: 0 -> last            | (0, 0)           | (0, last)       |
        | Right  | col = last | row: 1 -> last            | (1, last)        | (last, last)    |
        | Bottom | row = last | col: last - 1 -> 0 (down) | (last, last - 1) | (last, 0)       |
        | Left   | col = 0    | row: last - 1 -> 1 (down) | (last - 1, 0)    | (1, 0)          |

    INVARIANTS:
        - `size <= 0` -> `[]`
        - `size == 1` -> `[(0, 0)]`
        - `size >= 2` -> `len(path) == 4 * size - 4` and `len(path) == len(set(path))`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Rectangle Clockwise Walk (Thin-Shape Safe!)
===============================================================================
Problem:
    Write `solve_rectangle_walk(width: int, height: int) -> list[tuple[int, int]]`
    returning the outline cells of a `width x height` rectangle clockwise from
    `(0, 0)`, with ZERO duplicate cells — including thin shapes!

    LEGS TABLE (last_row = height - 1, last_col = width - 1):
        1. Top leg:    `(0, col)` for `col` in `0 .. last_col`
        2. Right leg:  `(row, last_col)` for `row` in `1 .. last_row`
        3. Bottom leg: ONLY if `height > 1`!  (Why? If `height == 1`, bottom IS top!)
                       `(last_row, col)` for `col` in `last_col - 1 .. 0`
        4. Left leg:   ONLY if `width > 1`!   (Why? If `width == 1`, left IS right!)
                       `(row, 0)` for `row` in `last_row - 1 .. 1`

    Examples:
        solve_rectangle_walk(4, 3) -> [
            (0, 0), (0, 1), (0, 2), (0, 3),
            (1, 3), (2, 3),
            (2, 2), (2, 1), (2, 0),
            (1, 0),
        ]
        solve_rectangle_walk(4, 1) -> [(0, 0), (0, 1), (0, 2), (0, 3)]
        solve_rectangle_walk(1, 3) -> [(0, 0), (1, 0), (2, 0)]
        solve_rectangle_walk(1, 1) -> [(0, 0)]
        solve_rectangle_walk(0, 5) -> []

    Edge-case hints:
        - For `width >= 2` and `height >= 2`, `len(path) == 2 * width + 2 * height - 4`.
        - Never forget the `if height > 1:` and `if width > 1:` guards! Without
          them, `4x1` walks backward across row 0 and duplicates cells!
"""
from __future__ import annotations


def example_square_walk(size: int) -> list[tuple[int, int]]:
    """Return outline cells of a size x size square clockwise from (0, 0)."""
    if size <= 0:
        return []
    if size == 1:
        return [(0, 0)]

    last = size - 1
    path: list[tuple[int, int]] = []
    for col in range(0, last + 1):           # Top:    (0, 0) -> (0, last)
        path.append((0, col))
    for row in range(1, last + 1):           # Right:  (1, last) -> (last, last)
        path.append((row, last))
    for col in range(last - 1, -1, -1):      # Bottom: (last, last-1) -> (last, 0)
        path.append((last, col))
    for row in range(last - 1, 0, -1):       # Left:   (last-1, 0) -> (1, 0)
        path.append((row, 0))
    return path


def solve_rectangle_walk(width: int, height: int) -> list[tuple[int, int]]:
    """Return outline cells of a width x height rectangle clockwise from (0, 0)."""
    pass


if __name__ == "__main__":
    print("Worked Example — 3x3 Square Clockwise Walk:")
    print(example_square_walk(3))
