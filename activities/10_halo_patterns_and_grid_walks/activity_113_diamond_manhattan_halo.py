"""
Activity 113: Diamond & Manhattan-Distance Halo
Difficulty: 113 / 132

A square uses Chebyshev distance (`max(|r - mid|, |c - mid|)`).
A diamond uses **Manhattan distance** (`|r - mid| + |c - mid|`) — the number
of horizontal + vertical grid steps from the center!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Filled Manhattan Diamond
===============================================================================
Problem:
    Write `example_filled_diamond(radius)` that returns a list of formatted
    lines for a FILLED diamond of radius `radius` on a `(2 * radius + 1)` grid,
    with single spaces between cells and ZERO trailing spaces.
    - Return `[]` if `radius < 0`.
    - If `radius == 0`, return `["#"]`.

Draw -> Index -> Rule:
    DRAW (radius = 2, size = 5, center mid = 2):
            #
          # # #
        # # # # #
          # # #
            #

    INDEX — Manhattan distance `d = abs(r - 2) + abs(c - 2)`:
        4 3 2 3 4
        3 2 1 2 3
        2 1 0 1 2
        3 2 1 2 3
        4 3 2 3 4

    RULE:
        - Filled diamond: `abs(r - mid) + abs(c - mid) <= radius`
        - CRITICAL FORMATTING: cells to the right of the diamond are spaces `' '`.
          Always `.rstrip(" ")` each formatted row so there are ZERO trailing
          spaces while keeping the leading indentation!

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Hollow Diamond Halo
===============================================================================
Problem:
    Write `solve_diamond_halo(radius: int) -> list[str]` that returns the HOLLOW
    diamond outline as a list of formatted lines with ZERO trailing spaces!

    RULE:
        A cell `(r, c)` in a `(2 * radius + 1) x (2 * radius + 1)` grid with
        `mid = radius` lies on the diamond halo iff:
            abs(r - mid) + abs(c - mid) == radius

    Examples:
        solve_diamond_halo(-1) -> []
        solve_diamond_halo(0)  -> ["#"]
        solve_diamond_halo(1)  -> [
            "  #",
            "#   #",
            "  #",
        ]
        solve_diamond_halo(2)  -> [
            "    #",
            "  #   #",
            "#       #",
            "  #   #",
            "    #",
        ]

    Edge-case hints:
        - Look how `radius == 0` works automatically: `mid = 0`, `size = 1`,
          `abs(0 - 0) + abs(0 - 0) == 0` -> `["#"]`!
        - Never leave trailing spaces on top/bottom rows (`"    #"`, NOT `"    #    "`).
"""
from __future__ import annotations


def example_filled_diamond(radius: int) -> list[str]:
    """Return formatted lines of a filled Manhattan diamond with zero trailing spaces."""
    if radius < 0:
        return []
    size = 2 * radius + 1
    mid = radius
    lines: list[str] = []
    for row in range(size):
        cells = [
            "#" if abs(row - mid) + abs(col - mid) <= radius else " "
            for col in range(size)
        ]
        lines.append(" ".join(cells).rstrip(" "))
    return lines


def solve_diamond_halo(radius: int) -> list[str]:
    """Return formatted lines of a hollow Manhattan diamond halo with zero trailing spaces."""
    pass


if __name__ == "__main__":
    print("Worked Example — Filled Diamond (radius=2):")
    for line in example_filled_diamond(2):
        print(line)
