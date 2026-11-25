"""
Activity 109: Grid Coordinate Indexing & format_row
Difficulty: 109 / 132

Welcome to Module 10: Halo Patterns & Grid Walks!
Before drawing glowing borders or animating runners around shapes, every grid
programmer must master two core habits:
  1. Seeing every cell by its (row, col) coordinate (rows go DOWN, cols go RIGHT).
  2. Formatting rows cleanly with ONE space between cells and ZERO trailing spaces.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Coordinate Label Grid
===============================================================================
Problem:
    Write `example_coordinate_grid(rows, cols)` that builds a 2D list of strings
    where cell `(r, c)` holds the label `f"({r},{c})"`.
    Return `[]` if `rows <= 0` or `cols <= 0`.

Draw -> Index -> Rule:
    DRAW (2 rows x 3 cols):
        (0,0) (0,1) (0,2)
        (1,0) (1,1) (1,2)

    INDEX:
        - Outer loop controls `row` from `0` to `rows - 1` (top -> bottom).
        - Inner loop controls `col` from `0` to `cols - 1` (left -> right).

    RULE:
        grid[r][c] = f"({r},{c})"

    EDGE CASES:
        - `rows <= 0` or `cols <= 0` -> return `[]`
        - `1 x 1` -> `[["(0,0)"]]`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — format_row & 2D Character Grid Renderer
===============================================================================
Problem:
    Implement two functions:
    1. `format_row(cells: list[str]) -> str`
       Join the cell strings with a SINGLE space `" "` between adjacent cells,
       and strip any trailing spaces on the right while PRESERVING leading spaces!
       Examples:
           format_row(["#", " ", "#"])       -> "#   #"
           format_row([" ", " ", "#"])       -> "    #"
           format_row(["#", " ", " "])       -> "#"
           format_row([" ", " "])            -> ""
           format_row([])                    -> ""

    2. `solve_render_grid(grid: list[list[str]]) -> str`
       Render a 2D character grid (possibly ragged — rows may have different
       lengths!) into a single multi-line string:
       - Format each row with `format_row(row)`.
       - Join formatted lines with `"\n"`.
       - Return `""` if `grid` is empty.
       - Every single line in the returned string MUST have ZERO trailing spaces.

    Examples:
        solve_render_grid([["#", "#"], ["#", " "]]) -> "# #\n#"
        solve_render_grid([[" " , "#"], ["#", "#"]]) -> "  #\n# #"
        solve_render_grid([]) -> ""

    Edge-case hints:
        - Do NOT call `.strip()` — that would destroy LEADING spaces needed for
          right-aligned triangles and diamonds! Use `.rstrip(" ")`.
        - Ragged grids like `[["#"], ["#", "#"]]` work naturally when iterating
          `for row in grid:`.
"""
from __future__ import annotations


def example_coordinate_grid(rows: int, cols: int) -> list[list[str]]:
    """Build a rows x cols 2D grid of '(r,c)' coordinate labels."""
    if rows <= 0 or cols <= 0:
        return []
    return [
        [f"({row},{col})" for col in range(cols)]
        for row in range(rows)
    ]


def format_row(cells: list[str]) -> str:
    """Join cell strings with one space and remove any trailing spaces.

    Leading spaces MUST be preserved.
    """
    pass


def solve_render_grid(grid: list[list[str]]) -> str:
    """Render a 2D character grid into a newline-joined string with zero trailing spaces."""
    pass


if __name__ == "__main__":
    print("Worked Example — 3x4 Coordinate Grid:")
    coord_grid = example_coordinate_grid(3, 4)
    for row_cells in coord_grid:
        print(" ".join(row_cells))
