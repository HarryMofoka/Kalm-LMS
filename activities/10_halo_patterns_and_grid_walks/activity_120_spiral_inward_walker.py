"""
Activity 120: Spiral-Inward Walker & Perimeter-to-Interior Sweep  [Unlocks Checkpoint 19!]
Difficulty: 120 / 132

BOSS LEVEL OF MODULE 10!
What is an inward spiral walk of a matrix?
It is NOTHING MORE than peeling **concentric rectangle halos** one ring at a
time — shrinking `(top, bottom, left, right)` inward until every single cell
in the grid has been visited!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Peel One Clockwise Outer Ring
===============================================================================
Problem:
    Write `example_peel_outer_ring(top, bottom, left, right)` returning the
    clockwise perimeter coordinates of the inclusive sub-rectangle
    `top <= row <= bottom`, `left <= col <= right`, with ZERO duplicate cells.
    Return `[]` if `top > bottom` or `left > right`.

Draw -> Index -> Legs Table:
    DRAW (top=1, bottom=2, left=1, right=3):
        (1,1) -> (1,2) -> (1,3)
          ^                 |
          |                 v
        (2,1) <- (2,2) <- (2,3)

    LEGS TABLE:
        | Leg    | Guard           | Coordinates                                  |
        |--------|-----------------|----------------------------------------------|
        | Top    | (always)        | (top, c)    for c in range(left, right + 1)  |
        | Right  | (always)        | (r, right)  for r in range(top + 1, bottom+1)|
        | Bottom | if top < bottom | (bottom, c) for c in range(right - 1, left - 1, -1) |
        | Left   | if left < right | (r, left)   for r in range(bottom - 1, top, -1)     |

    Notice those TWO guards (`if top < bottom` and `if left < right`) are the
    EXACT same thin-shape guards from Activity 114!
    - When `top == bottom` (single remaining row), only Top runs.
    - When `left == right` (single remaining col), only Top (1 cell) + Right run.
    - When `top == bottom and left == right` (center 1x1 cell), only Top runs -> 1 cell!

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Full Inward Spiral Walk of an m x n Grid
===============================================================================
Problem:
    Write `solve_spiral_walk(rows: int, cols: int) -> list[tuple[int, int]]`
    that starts at `(0, 0)` and spirals clockwise inward across an entire
    `rows x cols` grid, visiting ALL `rows * cols` cells EXACTLY ONCE!

    Algorithm:
        1. If `rows <= 0` or `cols <= 0`: return `[]`.
        2. Initialize 4 shrinking boundaries:
               top, bottom = 0, rows - 1
               left, right = 0, cols - 1
        3. While `top <= bottom and left <= right`:
               peel the ring `(top, bottom, left, right)` onto `result`
               top += 1; bottom -= 1; left += 1; right -= 1
        4. Return `result`.

    Examples:
        solve_spiral_walk(3, 3) -> [
            (0, 0), (0, 1), (0, 2),
            (1, 2), (2, 2), (2, 1),
            (2, 0), (1, 0), (1, 1),
        ]
        solve_spiral_walk(3, 4) -> [
            (0, 0), (0, 1), (0, 2), (0, 3),
            (1, 3), (2, 3), (2, 2), (2, 1),
            (2, 0), (1, 0), (1, 1), (1, 2),
        ]
        solve_spiral_walk(1, 4) -> [(0, 0), (0, 1), (0, 2), (0, 3)]
        solve_spiral_walk(4, 1) -> [(0, 0), (1, 0), (2, 0), (3, 0)]
        solve_spiral_walk(1, 1) -> [(0, 0)]
        solve_spiral_walk(0, 3) -> []

    Edge-case hints:
        - Always verify two invariants:
            1. `len(path) == rows * cols`
            2. `len(path) == len(set(path))` (zero duplicates!)
        - Rectangular grids like `3x4` (final inner piece is a 1x2 horizontal strip)
          and `4x3` (final inner piece is a 2x1 vertical strip) test your thin-ring
          guards!
"""
from __future__ import annotations


def example_peel_outer_ring(
    top: int,
    bottom: int,
    left: int,
    right: int,
) -> list[tuple[int, int]]:
    """Return clockwise coordinates of one rectangular ring bounded inclusively."""
    if top > bottom or left > right:
        return []

    ring: list[tuple[int, int]] = []
    for col in range(left, right + 1):               # Top edge
        ring.append((top, col))
    for row in range(top + 1, bottom + 1):           # Right edge
        ring.append((row, right))
    if top < bottom:                                 # Bottom edge (guard thin row)
        for col in range(right - 1, left - 1, -1):
            ring.append((bottom, col))
    if left < right:                                 # Left edge (guard thin col)
        for row in range(bottom - 1, top, -1):
            ring.append((row, left))
    return ring


def solve_spiral_walk(rows: int, cols: int) -> list[tuple[int, int]]:
    """Return full clockwise inward spiral coordinate walk of a rows x cols grid."""
    pass


if __name__ == "__main__":
    print("Worked Example — Peel Outer Ring (0..2, 0..3):")
    print(example_peel_outer_ring(0, 2, 0, 3))
    print("Worked Example — Inner Strip Ring (1..1, 1..2):")
    print(example_peel_outer_ring(1, 1, 1, 2))
