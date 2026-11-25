"""
Activity 098 — Left-Aligned Star & Number Triangles
Difficulty: 98 / 132

Context:
    Once every row varies with its row number `i`, Draw -> Index -> Rule turns
    visual geometry into trivial 1-based formulas. Pay close attention to
    whether trailing spaces are forbidden: left-aligned triangles have
    NO trailing spaces!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Implement `example_left_star_triangle(n)` returning `n` rows where row `i`
    (1-based) contains `i` stars (`[]` when `n <= 0`, NO trailing spaces).

Draw -> Index -> Rule (for n = 4):
    Draw:
        *
        **
        ***
        ****
    Index (1-based i = 1..n):
        i = 1 -> 1 star  -> "*"
        i = 2 -> 2 stars -> "**"
        i = 3 -> 3 stars -> "***"
        i = 4 -> 4 stars -> "****"
    Rule:
        Row `i` = `"*" * i` for `i` in `range(1, n + 1)`.

Edge Cases:
    - `n <= 0` -> `[]`
    - `n == 1` -> `["*"]`

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem:
    Implement `solve_create_number_triangle(n)` returning a left-aligned
    triangle where 1-based row `i` is `str(i)` repeated `i` times, with NO
    trailing spaces!

Draw -> Index -> Rule (for n = 4):
    Draw:
        1
        22
        333
        4444
    Index:
        i = 1 -> "1" * 1 -> "1"
        i = 2 -> "2" * 2 -> "22"
        i = 3 -> "3" * 3 -> "333"
        i = 4 -> "4" * 4 -> "4444"
    Rule:
        - If `n <= 0`: return `[]`.
        - For `i` in `range(1, n + 1)`: `str(i) * i`.

Examples:
    solve_create_number_triangle(0) -> []
    solve_create_number_triangle(1) -> ["1"]
    solve_create_number_triangle(3) -> ["1", "22", "333"]
    solve_create_number_triangle(5) -> ["1", "22", "333", "4444", "55555"]
"""

from __future__ import annotations


def example_left_star_triangle(n: int) -> list[str]:
    """Return a left-aligned star triangle of height ``n`` (no trailing spaces)."""
    if n <= 0:
        return []
    return ["*" * i for i in range(1, n + 1)]


def solve_create_number_triangle(n: int) -> list[str]:
    """Return a left-aligned triangle where row ``i`` is ``str(i) * i``."""
    pass


if __name__ == "__main__":
    print("\n".join(example_left_star_triangle(4)))
