"""
Activity 117: Modulo Wrap-Around & Single Halo Runner
Difficulty: 117 / 132

Welcome to Question 3 of the Halo Patterns Workshop:
    "Where is a runner after `steps` moves?"  ->  PATH + MODULO + GRID!

The beauty of separating `walk` (a list of coordinates) from rendering is that
a runner can lap a track 1,000,000 times — OR run BACKWARDS — in O(1) time with
a single modulo operation: `path[steps % len(path)]`!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Square Halo Runner
===============================================================================
Problem:
    Write `example_square_runner_lines(size, steps)` returning a list of
    formatted strings showing:
      - `'o'` on every border cell of the `size x size` square
      - `'@'` on the runner's cell after `steps` clockwise moves from `(0, 0)`
      - `' '` on hollow interior cells
      - One space between cells and ZERO trailing spaces.
    Return `[]` if `size <= 0`.

Draw -> Index -> Rule:
    DRAW (size = 3, steps = 5):
        Walk path (len = 8):
          idx:   0      1      2      3      4      5      6      7
          cell: (0,0)  (0,1)  (0,2)  (1,2)  (2,2)  (2,1)  (2,0)  (1,0)

        5 % 8 == 5 -> runner stands on (2, 1):
          o o o
          o   o
          o @ o

    PIPELINE:
        1. Build `path = square_walk(size)`.
        2. Allocate blank `size x size` grid: `[[" "] * size for _ in range(size)]`.
        3. Paint every `(r, c)` in `path` with `'o'`.
        4. Compute `r, c = path[steps % len(path)]` and paint `grid[r][c] = '@'`.
        5. Format each row with `" ".join(cells).rstrip(" ")`.

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Bidirectional Rectangle Halo Runner
===============================================================================
Problem:
    Write `solve_rectangle_runner_lines(width: int, height: int, steps: int) -> list[str]`
    that draws the `width x height` rectangle outline with `'o'` and places `'@'`
    at the runner's position after `steps` moves from `(0, 0)`:
      - POSITIVE `steps` move CLOCKWISE around the perimeter.
      - NEGATIVE `steps` move COUNTER-CLOCKWISE around the perimeter!
      - ZERO `steps` leaves `'@'` at `(0, 0)`.
      - Works on thin rectangles (`4x1`, `1x3`, `1x1`) and returns `[]` if
        `width <= 0` or `height <= 0`.
      - Zero trailing spaces on every line!

    Examples:
        solve_rectangle_runner_lines(6, 4, 9) -> [
            "o o o o o o",
            "o         o",
            "o         o",
            "o o o o @ o",
        ]
        # Negative steps: on a 4x3 rectangle (perimeter = 10),
        # steps = -1 lands on path[9] = (1, 0) (one step CCW from (0, 0))!
        solve_rectangle_runner_lines(4, 3, -1) -> [
            "o o o o",
            "@     o",
            "o o o o",
        ]
        solve_rectangle_runner_lines(4, 1, -1) -> ["o o o @"]

    Edge-case hints:
        - In Python, `-1 % 10 == 9` and `-11 % 10 == 9`! Python's `%` operator
          always produces a non-negative index in `0 .. len(path) - 1` when
          `len(path) > 0`.
        - Reuse the thin-shape-safe rectangle walk from Activity 114!
"""
from __future__ import annotations


def _square_perimeter(size: int) -> list[tuple[int, int]]:
    """Build clockwise square outline from (0, 0) with zero duplicate cells."""
    if size <= 0:
        return []
    if size == 1:
        return [(0, 0)]
    last = size - 1
    path: list[tuple[int, int]] = []
    for col in range(0, last + 1):
        path.append((0, col))
    for row in range(1, last + 1):
        path.append((row, last))
    for col in range(last - 1, -1, -1):
        path.append((last, col))
    for row in range(last - 1, 0, -1):
        path.append((row, 0))
    return path


def example_square_runner_lines(size: int, steps: int) -> list[str]:
    """Return formatted lines of a square halo with '@' after `steps` moves."""
    if size <= 0:
        return []
    path = _square_perimeter(size)
    grid = [[" "] * size for _ in range(size)]
    for row, col in path:
        grid[row][col] = "o"
    runner_row, runner_col = path[steps % len(path)]
    grid[runner_row][runner_col] = "@"
    return [" ".join(cells).rstrip(" ") for cells in grid]


def solve_rectangle_runner_lines(width: int, height: int, steps: int) -> list[str]:
    """Return formatted lines of a rectangle halo with '@' after positive/negative `steps`."""
    pass


if __name__ == "__main__":
    print("Worked Example — Square Runner (size=3, steps=5):")
    for line in example_square_runner_lines(3, 5):
        print(line)
