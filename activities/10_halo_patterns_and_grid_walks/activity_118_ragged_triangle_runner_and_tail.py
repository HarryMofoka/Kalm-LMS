"""
Activity 118: Ragged-Grid Triangle Runner & Glowing Comet Tail
Difficulty: 118 / 132

Not every 2D grid is rectangular!
In a right triangle, row `r` has ONLY `r + 1` cells — a **ragged grid**.
Allocating `[[" "] * (row + 1) for row in range(height)]` guarantees zero
wasted cells AND zero trailing spaces automatically!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Ragged-Grid Triangle Runner
===============================================================================
Problem:
    Write `example_triangle_runner_lines(height, steps)` returning the formatted
    lines of a hollow right triangle (`'o'` outline, `'@'` runner at
    `path[steps % len(path)]`). Return `[]` if `height <= 0`.

Draw -> Index -> Rule:
    DRAW (height = 5, steps = 6, perimeter = 12):
        path = [(0,0), (1,1), (2,2), (3,3), (4,4),
                (4,3), (4,2), (4,1), (4,0),
                (3,0), (2,0), (1,0)]
        path[6 % 12] = (4, 2)

        o
        o o
        o   o
        o     o
        o o @ o o

    RAGGED GRID ALLOCATION:
        grid = [[" "] * (row + 1) for row in range(height)]
        Row 0 has 1 cell, row 1 has 2 cells, ..., row `r` has `r + 1` cells!

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Triangle Runner with 3-Cell Glowing Tail
===============================================================================
Problem:
    Write `solve_triangle_runner_tail(height: int, steps: int) -> list[str]`
    that renders the triangle outline with a runner leaving a 3-cell glowing
    comet tail behind it!

    Symbols (painted along the clockwise triangle walk `path` of length `n`):
      - Runner head at `path[steps % n]`         -> `'@'`
      - 1 step behind at `path[(steps - 1) % n]` -> `'*'`
      - 2 steps behind at `path[(steps - 2) % n]`-> `'.'`
      - All other outline cells                  -> `'o'`
      - Interior cells                           -> `' '`

    OVERLAP / PRIORITY RULE (for tiny triangles where `n < 3`, e.g. `height == 1`):
      Head `'@'` ALWAYS takes priority over `'*'`, which ALWAYS takes priority
      over `'.'`, which takes priority over `'o'`!
      (Hint: paint in back-to-front order: `'o'`, then `'.'`, then `'*'`, then `'@'`!)

    Examples:
        solve_triangle_runner_tail(0, 5) -> []
        solve_triangle_runner_tail(1, 0) -> ["@"]
        solve_triangle_runner_tail(2, 0) -> [
            "@",
            "* .",
        ]
        solve_triangle_runner_tail(5, 6) -> [
            "o",
            "o o",
            "o   o",
            "o     o",
            "o o @ * .",
        ]

    Edge-case hints:
        - Check `height == 2, steps == 0`: path is `[(0,0), (1,1), (1,0)]` (`n = 3`).
          * `0 % 3 = 0` -> `(0, 0)` gets `'@'`
          * `-1 % 3 = 2` -> `(1, 0)` gets `'*'`
          * `-2 % 3 = 1` -> `(1, 1)` gets `'.'`
          So row 0 is `"@"` and row 1 is `"* ."`!
        - Works for negative `steps` too!
"""
from __future__ import annotations


def _triangle_perimeter(height: int) -> list[tuple[int, int]]:
    """Build clockwise right-triangle outline from (0, 0) with zero duplicates."""
    if height <= 0:
        return []
    if height == 1:
        return [(0, 0)]
    last = height - 1
    path: list[tuple[int, int]] = []
    for i in range(0, last + 1):
        path.append((i, i))
    for col in range(last - 1, -1, -1):
        path.append((last, col))
    for row in range(last - 1, 0, -1):
        path.append((row, 0))
    return path


def example_triangle_runner_lines(height: int, steps: int) -> list[str]:
    """Return formatted lines of a ragged-grid triangle halo with runner '@'."""
    if height <= 0:
        return []
    path = _triangle_perimeter(height)
    grid = [[" "] * (row + 1) for row in range(height)]
    for row, col in path:
        grid[row][col] = "o"
    runner_row, runner_col = path[steps % len(path)]
    grid[runner_row][runner_col] = "@"
    return [" ".join(cells).rstrip(" ") for cells in grid]


def solve_triangle_runner_tail(height: int, steps: int) -> list[str]:
    """Return triangle runner lines with 3-cell glowing tail '@', '*', '.'."""
    pass


if __name__ == "__main__":
    print("Worked Example — Triangle Runner (height=5, steps=6):")
    for line in example_triangle_runner_lines(5, 6):
        print(line)
