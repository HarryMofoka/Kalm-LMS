"""
Activity 099 — Inverted & Right-Aligned Triangles
Difficulty: 99 / 132

Context:
    Right-aligned shapes introduce your first **padding formula**: each row has
    a constant total width `n`, split between leading spaces on the left and
    stars on the right (still ZERO trailing spaces!).

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Implement `example_inverted_left_triangle(n)` returning an upside-down
    left-aligned star triangle of height `n` (no trailing spaces).

Draw -> Index -> Rule (for n = 4):
    Draw:
        ****
        ***
        **
        *
    Index (0-based r = 0..n-1):
        r = 0 -> 4 stars (`n - 0`)
        r = 1 -> 3 stars (`n - 1`)
        r = 2 -> 2 stars (`n - 2`)
        r = 3 -> 1 star  (`n - 3`)
    Rule:
        Row `r` = `"*" * (n - r)` (or count down `range(n, 0, -1)`).

Edge Cases:
    - `n <= 0` -> `[]`
    - `n == 1` -> `["*"]`

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem:
    Implement `solve_right_aligned_triangle(n)` returning a right-aligned star
    triangle of height `n` where EVERY row has exact width `n` (leading spaces
    + stars, NO trailing spaces).

Draw -> Index -> Rule (for n = 4, spaces shown as `·`):
    Draw:
        ···*
        ··**
        ·***
        ****
    Index (1-based i = 1..n):
        i = 1 -> spaces = 3 (`n - 1`), stars = 1 (`i`), width = 4
        i = 2 -> spaces = 2 (`n - 2`), stars = 2 (`i`), width = 4
        i = 3 -> spaces = 1 (`n - 3`), stars = 3 (`i`), width = 4
        i = 4 -> spaces = 0 (`n - 4`), stars = 4 (`i`), width = 4
    Rule:
        - If `n <= 0`: return `[]`.
        - Row `i` = `" " * (n - i) + "*" * i`.
        - Check: `(n - i) + i == n` -> constant width `n`!

Examples:
    solve_right_aligned_triangle(0) -> []
    solve_right_aligned_triangle(1) -> ["*"]
    solve_right_aligned_triangle(3) -> ["  *", " **", "***"]
    solve_right_aligned_triangle(4) -> ["   *", "  **", " ***", "****"]
"""

from __future__ import annotations


def example_inverted_left_triangle(n: int) -> list[str]:
    """Return an inverted left-aligned star triangle of height ``n``."""
    if n <= 0:
        return []
    return ["*" * count for count in range(n, 0, -1)]


def solve_right_aligned_triangle(n: int) -> list[str]:
    """Return a right-aligned star triangle of constant width ``n``."""
    pass


if __name__ == "__main__":
    print("\n".join(example_inverted_left_triangle(4)))
