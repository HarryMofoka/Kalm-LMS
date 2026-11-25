"""
Activity 110: Square & Rectangle Border Predicates and Halos
Difficulty: 110 / 132

A "halo" is the hollow outline of a shape!
In the Halo Patterns Workshop, Question 1 is always:
    "Which cells are on the outline?"  ->  a boolean RULE function!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Square Border & Square Halo
===============================================================================
Problem:
    1. `is_square_border(row, col, size) -> bool`
       Return True iff `(row, col)` lies inside a `size x size` grid AND is on
       one of its four outer edges.
    2. `example_square_halo_lines(size) -> list[str]`
       Return the hollow square as a list of formatted strings (one space
       between cells, zero trailing spaces). Return `[]` for `size <= 0`.

Draw -> Index -> Rule:
    DRAW (size = 4):
        # # # #
        #     #
        #     #
        # # # #

    INDEX (rows 0..3, cols 0..3, last = size - 1 = 3):
        (0,0) (0,1) (0,2) (0,3)   <- row == 0     (top edge)
        (1,0)  .     .    (1,3)   <- col == 0 or col == last
        (2,0)  .     .    (2,3)   <- col == 0 or col == last
        (3,0) (3,1) (3,2) (3,3)   <- row == last  (bottom edge)

    RULE:
        A valid cell `(row, col)` is on the square border when:
            row == 0 or row == last or col == 0 or col == last

    EDGE CASES:
        - `size <= 0` -> `is_square_border` is False; halo is `[]`
        - Out-of-bounds `(row, col)` -> `is_square_border` is False
        - `size == 1` -> `["#"]`
        - `size == 2` -> `["# #", "# #"]`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Rectangle Border & Rectangle Halo
===============================================================================
Problem:
    Generalize from one dimension (`size`) to TWO dimensions (`width`, `height`)!
    Remember: `height` is the number of ROWS and `width` is the number of COLUMNS!

    1. `is_rectangle_border(row: int, col: int, width: int, height: int) -> bool`
       Return True iff `width > 0`, `height > 0`, `0 <= row < height`,
       `0 <= col < width`, AND `(row, col)` is on the outer edge of the rectangle.

    2. `solve_rectangle_halo_lines(width: int, height: int) -> list[str]`
       Return the hollow `width x height` rectangle as a list of formatted lines
       with `'#'` on border cells, `' '` inside, one space between cells, and
       zero trailing spaces. Return `[]` if `width <= 0` or `height <= 0`.

    Examples:
        solve_rectangle_halo_lines(6, 3) -> [
            "# # # # # #",
            "#         #",
            "# # # # # #",
        ]
        solve_rectangle_halo_lines(4, 1) -> ["# # # #"]       # thin horizontal!
        solve_rectangle_halo_lines(1, 3) -> ["#", "#", "#"]   # thin vertical!
        solve_rectangle_halo_lines(1, 1) -> ["#"]             # single cell!

    Edge-case hints:
        - Watch the parameter order: `(row, col, width, height)`!
          `row` is checked against `height`; `col` is checked against `width`.
        - Thin shapes (`4x1`, `1x3`, `1x1`) work automatically when your border
          rule uses `last_row = height - 1` and `last_col = width - 1`!
"""
from __future__ import annotations


def is_square_border(row: int, col: int, size: int) -> bool:
    """Return True if (row, col) is on the outline of a size x size square."""
    if size <= 0 or not (0 <= row < size and 0 <= col < size):
        return False
    last = size - 1
    return row == 0 or row == last or col == 0 or col == last


def example_square_halo_lines(size: int) -> list[str]:
    """Return formatted lines of a hollow size x size square."""
    if size <= 0:
        return []
    lines: list[str] = []
    for row in range(size):
        cells = [
            "#" if is_square_border(row, col, size) else " "
            for col in range(size)
        ]
        lines.append(" ".join(cells).rstrip(" "))
    return lines


def is_rectangle_border(row: int, col: int, width: int, height: int) -> bool:
    """Return True if (row, col) is on the outline of a width x height rectangle."""
    pass


def solve_rectangle_halo_lines(width: int, height: int) -> list[str]:
    """Return formatted lines of a hollow width x height rectangle."""
    pass


if __name__ == "__main__":
    print("Worked Example — 5x5 Square Halo:")
    for line in example_square_halo_lines(5):
        print(line)
