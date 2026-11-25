"""
Activity 100 — Centered Star Pyramid (Constant Width `2n - 1`)
Difficulty: 100 / 132

Context:
    A classic exam trap: centered shapes like pyramids, diamonds, and
    hourglasses often specify **equal-width strings** — meaning BOTH left AND
    right spaces must be included so every row has exact width `2 * n - 1`!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Implement `example_pyramid_row(row_index, total_rows)` returning a SINGLE
    centered row (1-based `row_index` out of `total_rows`) of exact width
    `2 * total_rows - 1`, padded symmetrically on BOTH sides.

Draw -> Index -> Rule (for total_rows = 4, spaces shown as `·`):
    Draw:
        ···*···   (row 1: 3 left, 1 star,  3 right -> total 7)
        ··***··   (row 2: 2 left, 3 stars, 2 right -> total 7)
        ·*****·   (row 3: 1 left, 5 stars, 1 right -> total 7)
        *******   (row 4: 0 left, 7 stars, 0 right -> total 7)
    Index (1-based i = row_index, n = total_rows):
        - `pad = n - i` spaces on LEFT and `n - i` spaces on RIGHT
        - `stars = 2 * i - 1`
        - Width check: `(n - i) + (2 * i - 1) + (n - i) == 2 * n - 1`!
    Rule:
        `pad = " " * (total_rows - row_index)`
        `return pad + "*" * (2 * row_index - 1) + pad`

Edge Cases:
    - `total_rows <= 0` or `row_index < 1` or `row_index > total_rows` -> `""`

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem:
    Implement `solve_create_pyramid(n)` returning a centered star pyramid of
    `n` rows where EVERY row has exact constant width `2 * n - 1` (exact left
    AND right space padding!).

Rules:
    1. If `n <= 0`: return `[]`.
    2. For 1-based `i` in `range(1, n + 1)`:
       - `pad = " " * (n - i)`
       - `stars = "*" * (2 * i - 1)`
       - row = `pad + stars + pad`
    3. Every returned string MUST have `len(row) == 2 * n - 1`.

Examples:
    solve_create_pyramid(0) -> []
    solve_create_pyramid(1) -> ["*"]
    solve_create_pyramid(3) -> [
        "  *  ",
        " *** ",
        "*****",
    ]
    solve_create_pyramid(4) -> [
        "   *   ",
        "  ***  ",
        " ***** ",
        "*******",
    ]
"""

from __future__ import annotations


def example_pyramid_row(row_index: int, total_rows: int) -> str:
    """Return 1-indexed ``row_index`` of a centered star pyramid of height ``total_rows``."""
    if total_rows <= 0 or not (1 <= row_index <= total_rows):
        return ""
    pad = " " * (total_rows - row_index)
    stars = "*" * (2 * row_index - 1)
    return pad + stars + pad


def solve_create_pyramid(n: int) -> list[str]:
    """Return a centered star pyramid of ``n`` rows with constant width ``2n - 1``."""
    pass


if __name__ == "__main__":
    height = 4
    for r in range(1, height + 1):
        print(repr(example_pyramid_row(r, height)))
