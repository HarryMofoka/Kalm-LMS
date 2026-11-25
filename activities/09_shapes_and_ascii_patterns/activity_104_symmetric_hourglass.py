"""
Activity 104 — Symmetric Hourglass of Stars
Difficulty: 104 / 132

Context:
    An hourglass is the exact inside-out twin of a diamond: widest at the top
    and bottom, pinching to a single `'*'` in the middle row! Notice how one
    tiny sign flip (`pad = mid - abs(mid - i)`) turns a diamond into an
    hourglass!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Implement `example_inverted_pyramid(n)` returning a centered upside-down
    star pyramid of `n` rows with exact constant width `2 * n - 1` (exact left
    and right space padding).

Draw -> Index -> Rule (for n = 3, width = 5, spaces as `·`):
    Draw:
        *****   (r = 0: pad = 0, stars = 5)
        ·***·   (r = 1: pad = 1, stars = 3)
        ··*··   (r = 2: pad = 2, stars = 1)
    Index (0-based r = 0..n-1):
        - `pad = r`
        - `stars = 2 * (n - r) - 1`
        - Width check: `r + (2n - 2r - 1) + r == 2n - 1`!
    Rule:
        - If `n <= 0`: return `[]`.
        - Row `r` = `" " * r + "*" * (2 * (n - r) - 1) + " " * r`.

Edge Cases:
    - `n <= 0` -> `[]`
    - `n == 1` -> `["*"]`

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem:
    Implement `solve_create_hourglass(n)` returning a symmetric star hourglass
    of height and width `n` (for positive ODD `n`), with exact left AND right
    padding so every row has length `n`.

Draw -> Index -> Rule (for n = 5, mid = n // 2 = 2, spaces as `·`):
    Draw:
        *****   (i = 0: pad = 2 - |2 - 0| = 0, stars = 5 - 0 = 5)
        ·***·   (i = 1: pad = 2 - |2 - 1| = 1, stars = 5 - 2 = 3)
        ··*··   (i = 2: pad = 2 - |2 - 2| = 2, stars = 5 - 4 = 1)
        ·***·   (i = 3: pad = 2 - |2 - 3| = 1, stars = 5 - 2 = 3)
        *****   (i = 4: pad = 2 - |2 - 4| = 0, stars = 5 - 0 = 5)
    Rule:
        - If `n <= 0`: return `[]`.
        - If `n % 2 == 0`: raise `ValueError("n must be odd.")`.
        - For `i` in `range(n)`:
          `pad = mid - abs(mid - i)`
          `stars = n - 2 * pad`
          row = `" " * pad + "*" * stars + " " * pad`

Examples:
    solve_create_hourglass(1) -> ["*"]
    solve_create_hourglass(5) -> [
        "*****",
        " *** ",
        "  *  ",
        " *** ",
        "*****",
    ]
    solve_create_hourglass(0) -> []
    solve_create_hourglass(4) -> raises ValueError("n must be odd.")
"""

from __future__ import annotations


def example_inverted_pyramid(n: int) -> list[str]:
    """Return a centered inverted star pyramid of ``n`` rows (width ``2n - 1``)."""
    if n <= 0:
        return []
    rows: list[str] = []
    for r in range(n):
        pad = " " * r
        stars = "*" * (2 * (n - r) - 1)
        rows.append(pad + stars + pad)
    return rows


def solve_create_hourglass(n: int) -> list[str]:
    """Return a centered star hourglass of width and height ``n`` (odd ``n``).

    Raises:
        ValueError("n must be odd.") if ``n`` is positive and even.
    """
    pass


if __name__ == "__main__":
    print("\n".join(example_inverted_pyramid(4)))
