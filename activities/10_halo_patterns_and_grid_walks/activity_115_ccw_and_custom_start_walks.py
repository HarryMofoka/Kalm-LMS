"""
Activity 115: Counter-Clockwise & Custom-Start Perimeter Walks
Difficulty: 115 / 132

Real patrol robots don't always walk clockwise or start at the top-left corner!
Learn both how to reverse a legs table (counter-clockwise) and how to rotate
any closed perimeter cycle so it starts at ANY border cell you choose.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Counter-Clockwise Square Walk from (0, 0)
===============================================================================
Problem:
    Write `example_square_walk_ccw(size)` returning the outline cells of a
    `size x size` square in COUNTER-CLOCKWISE order starting at `(0, 0)`.

Draw -> Index -> Legs Table:
    DRAW & INDEX (size = 3, last = 2):
        (0,0) <- (0,1) <- (0,2)
          |                 ^
          v                 |
        (1,0)             (1,2)
          |                 ^
          v                 |
        (2,0) -> (2,1) -> (2,2)

    LEGS TABLE (for size >= 2, last = size - 1):
        | Leg    | Fixed      | Variable range            | Starts at        | Ends at         |
        |--------|------------|---------------------------|------------------|-----------------|
        | Left   | col = 0    | row: 0 -> last            | (0, 0)           | (last, 0)       |
        | Bottom | row = last | col: 1 -> last            | (last, 1)        | (last, last)    |
        | Right  | col = last | row: last - 1 -> 0 (down) | (last - 1, last) | (0, last)       |
        | Top    | row = 0    | col: last - 1 -> 1 (down) | (0, last - 1)    | (0, 1)          |

    EDGE CASES:
        - `size <= 0` -> `[]`
        - `size == 1` -> `[(0, 0)]`
        - Notice: every cell after `(0, 0)` is the EXACT reverse of clockwise!

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Clockwise Rectangle Walk from ANY Border Cell
===============================================================================
Problem:
    Write `solve_rectangle_walk_from(width: int, height: int, start: tuple[int, int]) -> list[tuple[int, int]]`
    that returns the CLOCKWISE perimeter walk of a `width x height` rectangle
    starting at the chosen border cell `start = (row, col)`!

    Rules:
    - First build the thin-shape-safe clockwise walk starting from `(0, 0)`.
    - If `width <= 0` or `height <= 0` or `start` is NOT on the rectangle border,
      raise `ValueError`.
    - Otherwise, rotate the cycle so `start` is index `0`, preserving the exact
      clockwise order around the perimeter!

    Examples:
        solve_rectangle_walk_from(4, 3, (2, 3)) -> [
            (2, 3), (2, 2), (2, 1), (2, 0),
            (1, 0), (0, 0), (0, 1), (0, 2),
            (0, 3), (1, 3),
        ]
        solve_rectangle_walk_from(4, 1, (0, 2)) -> [(0, 2), (0, 3), (0, 0), (0, 1)]
        solve_rectangle_walk_from(1, 1, (0, 0)) -> [(0, 0)]
        solve_rectangle_walk_from(4, 3, (1, 1)) -> raises ValueError (interior cell!)

    Edge-case hints:
        - Once you have `path` starting at `(0, 0)`, rotating a list to index `idx`
          is simply: `path[idx:] + path[:idx]`!
        - Check `if start not in path: raise ValueError(...)` — that catches
          interior cells, out-of-bounds coordinates, AND non-positive dimensions!
"""
from __future__ import annotations


def example_square_walk_ccw(size: int) -> list[tuple[int, int]]:
    """Return outline cells of a size x size square counter-clockwise from (0, 0)."""
    if size <= 0:
        return []
    if size == 1:
        return [(0, 0)]

    last = size - 1
    path: list[tuple[int, int]] = []
    for row in range(0, last + 1):           # Left:   (0, 0) -> (last, 0)
        path.append((row, 0))
    for col in range(1, last + 1):           # Bottom: (last, 1) -> (last, last)
        path.append((last, col))
    for row in range(last - 1, -1, -1):      # Right:  (last-1, last) -> (0, last)
        path.append((row, last))
    for col in range(last - 1, 0, -1):       # Top:    (0, last-1) -> (0, 1)
        path.append((0, col))
    return path


def solve_rectangle_walk_from(
    width: int,
    height: int,
    start: tuple[int, int],
) -> list[tuple[int, int]]:
    """Return clockwise rectangle outline starting at `start`, or raise ValueError."""
    pass


if __name__ == "__main__":
    print("Worked Example — 3x3 Counter-Clockwise Square Walk:")
    print(example_square_walk_ccw(3))
