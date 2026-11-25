"""
Activity 101 — Centered Number Pyramid
Difficulty: 101 / 132

Context:
    What happens when the middle content of a centered pyramid is numbers
    separated by single spaces (`"2 2"`, `"3 3 3"`) instead of solid stars?
    Check its width! `i` single-digit numbers with `i - 1` spaces between them
    has length `i + (i - 1) = 2 * i - 1` — the EXACT SAME width formula as a
    star pyramid!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Implement `example_counting_pyramid(n)` returning a centered pyramid where
    1-based row `i` displays `1 2 ... i` separated by single spaces, padded
    symmetrically with `" " * (n - i)` on both left and right (`[]` if `n <= 0`).

Draw -> Index -> Rule (for n = 3, spaces shown as `·`):
    Draw:
        ··1··     (row 1: 2 left, "1",     2 right -> width 5)
        ·1·2·     (row 2: 1 left, "1 2",   1 right -> width 5)
        1·2·3     (row 3: 0 left, "1 2 3", 0 right -> width 5)
    Index (1-based i = 1..n):
        - `content = " ".join(str(k) for k in range(1, i + 1))`
        - `pad = " " * (n - i)`
    Rule:
        Row `i` = `pad + content + pad`.

Edge Cases:
    - `n <= 0` -> `[]`
    - `n == 1` -> `["1"]`

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem:
    Implement `solve_create_number_pyramid(n)` (a classic exam function!)
    returning a centered pyramid where 1-based row `i` holds the number `i`
    repeated `i` times, separated by single spaces, padded symmetrically on
    both left and right with `" " * (n - i)`.

Draw -> Index -> Rule (for n = 3, spaces shown as `·`):
    Draw:
        ··1··
        ·2·2·
        3·3·3
    Index (1-based i = 1..n):
        i = 1 -> pad = "  ", content = "1"     -> "  1  "
        i = 2 -> pad = " ",  content = "2 2"   -> " 2 2 "
        i = 3 -> pad = "",   content = "3 3 3" -> "3 3 3"
    Rule:
        - If `n <= 0`: return `[]`.
        - `pad = " " * (n - i)`
        - `content = " ".join([str(i)] * i)`
        - Row `i` = `pad + content + pad`.

Examples:
    solve_create_number_pyramid(0) -> []
    solve_create_number_pyramid(1) -> ["1"]
    solve_create_number_pyramid(3) -> [
        "  1  ",
        " 2 2 ",
        "3 3 3",
    ]
    solve_create_number_pyramid(4) -> [
        "   1   ",
        "  2 2  ",
        " 3 3 3 ",
        "4 4 4 4",
    ]
"""

from __future__ import annotations


def example_counting_pyramid(n: int) -> list[str]:
    """Return a centered pyramid where row ``i`` lists ``1..i`` space-separated."""
    if n <= 0:
        return []
    rows: list[str] = []
    for i in range(1, n + 1):
        pad = " " * (n - i)
        content = " ".join(str(k) for k in range(1, i + 1))
        rows.append(pad + content + pad)
    return rows


def solve_create_number_pyramid(n: int) -> list[str]:
    """Return a centered pyramid where row ``i`` repeats ``i`` space-separated."""
    pass


if __name__ == "__main__":
    for line in example_counting_pyramid(4):
        print(repr(line))
