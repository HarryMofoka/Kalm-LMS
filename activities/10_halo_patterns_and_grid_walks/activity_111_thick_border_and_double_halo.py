"""
Activity 111: Thick Border Frames & Concentric Double-Ring Halos
Difficulty: 111 / 132

Once you see a border as "distance from the nearest edge", thick frames and
multi-ring concentric halos fall out in ONE single formula!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Thick Border Square Frame
===============================================================================
Problem:
    Write `example_thick_border_square(size, thickness)` that returns a list of
    formatted lines for a `size x size` square whose `'#'` border is `thickness`
    cells thick on all four sides.
    - If `size <= 0`: return `[]`.
    - If `thickness <= 0`: return `[""] * size` (no `'#'` cells, no trailing spaces).
    - If `thickness >= (size + 1) // 2`: every cell is `'#'`.

Draw -> Index -> Rule:
    DRAW (size = 6, thickness = 2):
        # # # # # #
        # # # # # #
        # #     # #
        # #     # #
        # # # # # #
        # # # # # #

    INDEX — distance from the nearest edge ("layer"):
        layer(r, c) = min(r, c, size - 1 - r, size - 1 - c)

        0 0 0 0 0 0
        0 1 1 1 1 0
        0 1 2 2 1 0
        0 1 2 2 1 0
        0 1 1 1 1 0
        0 0 0 0 0 0

    RULE:
        A cell `(r, c)` is part of the thick border iff `layer(r, c) < thickness`!
        (Equivalently: `r < k or r >= size - k or c < k or c >= size - k`.)

    EDGE CASES:
        - `thickness = 1` reproduces the classic single-cell square halo.
        - Large `thickness` (e.g. `thickness = 5` on `size = 4`) fills the whole grid.

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Concentric Double-Halo Square
===============================================================================
Problem:
    Write `solve_double_halo_square(size: int) -> list[str]` that builds a
    `size x size` square with TWO concentric halo rings:
      - Outer ring (layer 0): `'#'`
      - Inner ring (layer 1): `'+'`
      - Hollow center (layer >= 2): `' '`
    Join each row with single spaces and ensure ZERO trailing spaces.
    Return `[]` if `size <= 0`.

    Examples:
        solve_double_halo_square(1) -> ["#"]
        solve_double_halo_square(2) -> ["# #", "# #"]
        solve_double_halo_square(3) -> [
            "# # #",
            "# + #",
            "# # #",
        ]
        solve_double_halo_square(5) -> [
            "# # # # #",
            "# + + + #",
            "# +   + #",
            "# + + + #",
            "# # # # #",
        ]

    Edge-case hints:
        - Compute `layer = min(row, col, size - 1 - row, size - 1 - col)`.
        - Sizes 1 and 2 have only `layer == 0` cells (no `'+'` cells fit yet).
        - Size 3 has a single `layer == 1` cell right in the center `(1, 1)`.
        - Size 4 has a 2x2 block of `'+'` cells with no hollow center yet.
        - Size 5 is the smallest size with outer `'#'`, inner `'+'`, AND hollow `' '`!
"""
from __future__ import annotations


def example_thick_border_square(size: int, thickness: int) -> list[str]:
    """Return a size x size square with a '#' border of the given thickness."""
    if size <= 0:
        return []
    lines: list[str] = []
    for row in range(size):
        cells: list[str] = []
        for col in range(size):
            layer = min(row, col, size - 1 - row, size - 1 - col)
            cells.append("#" if layer < thickness else " ")
        lines.append(" ".join(cells).rstrip(" "))
    return lines


def solve_double_halo_square(size: int) -> list[str]:
    """Return a concentric double-halo square with outer '#' and inner '+'."""
    pass


if __name__ == "__main__":
    print("Worked Example — 6x6 Thick Border (thickness=2):")
    for line in example_thick_border_square(6, 2):
        print(line)
