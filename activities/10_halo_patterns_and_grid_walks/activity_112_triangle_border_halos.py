"""
Activity 112: Triangle Border Rules (Left-Aligned & Right-Aligned)
Difficulty: 112 / 132

Triangles break the "all rows are rectangles" comfort zone!
Look closely at the diagonal slope: every diagonal line on a grid obeys a simple
linear equation relating `row` and `col`.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Left-Aligned Right Triangle Halo
===============================================================================
Problem:
    Write `example_left_triangle_halo(height)` returning the hollow left-aligned
    right triangle of the given `height` as a list of formatted lines (zero
    trailing spaces). Return `[]` if `height <= 0`.

Draw -> Index -> Rule:
    DRAW (height = 5):
        #
        # #
        #   #
        #     #
        # # # # #

    INDEX (row `r` has `r + 1` cells, `col` in `0..r`):
        r=0: (0,0)
        r=1: (1,0) (1,1)
        r=2: (2,0)  .    (2,2)
        r=3: (3,0)  .     .    (3,3)
        r=4: (4,0) (4,1) (4,2) (4,3) (4,4)

    RULE:
        Within `0 <= r < height` and `0 <= c <= r`, `(r, c)` is on the border iff:
            c == 0             (left edge)
            or c == r          (diagonal slope)
            or r == height - 1 (bottom edge)

    EDGE CASES:
        - `height <= 0` -> `[]`
        - `height == 1` -> `["#"]`
        - `height == 2` -> `["#", "# #"]`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Right-Aligned Mirrored Triangle Halo
===============================================================================
Problem:
    Write `solve_right_triangle_halo(height: int) -> list[str]` returning the
    MIRRORED right-aligned hollow triangle of the given `height`, with ONE space
    between columns and ZERO trailing spaces!

Draw -> Index -> Rule (plan it carefully!):
    DRAW (height = 5):
                #
              # #
            #   #
          #     #
        # # # # #

    INDEX on a `height x height` grid (`0 <= r < height`, `0 <= c < height`):
        r=0:   .     .     .     .   (0,4)   <- 4 leading spaces -> "        #"
        r=1:   .     .     .   (1,3) (1,4)   <- "      # #"
        r=2:   .     .   (2,2)   .   (2,4)   <- "    #   #"
        r=3:   .   (3,1)   .     .   (3,4)   <- "  #     #"
        r=4: (4,0) (4,1) (4,2) (4,3) (4,4)   <- "# # # # #"

    RULE HINT:
        Notice the anti-diagonal slope coordinates: (0,4), (1,3), (2,2), (3,1), (4,0).
        What is `r + c` on EVERY single cell of that slope?!
        It's ALWAYS `height - 1`!
        And the other two edges are `c == height - 1` (right) and `r == height - 1` (bottom)!

    Examples:
        solve_right_triangle_halo(0) -> []
        solve_right_triangle_halo(1) -> ["#"]
        solve_right_triangle_halo(2) -> ["  #", "# #"]
        solve_right_triangle_halo(4) -> [
            "      #",
            "    # #",
            "  #   #",
            "# # # #",
        ]

    Edge-case hints:
        - Keep leading spaces (do NOT `.lstrip()`), and ensure zero trailing spaces.
        - Because column `height - 1` is ALWAYS `'#'`, `" ".join(cells)` on all
          `height` columns ends with `'#'` naturally!
"""
from __future__ import annotations


def example_left_triangle_halo(height: int) -> list[str]:
    """Return formatted lines of a hollow left-aligned right triangle."""
    if height <= 0:
        return []
    last = height - 1
    lines: list[str] = []
    for row in range(height):
        cells = [
            "#" if (col == 0 or col == row or row == last) else " "
            for col in range(row + 1)
        ]
        lines.append(" ".join(cells).rstrip(" "))
    return lines


def solve_right_triangle_halo(height: int) -> list[str]:
    """Return formatted lines of a hollow right-aligned triangle with zero trailing spaces."""
    pass


if __name__ == "__main__":
    print("Worked Example — Left Triangle Halo (height=5):")
    for line in example_left_triangle_halo(5):
        print(line)
