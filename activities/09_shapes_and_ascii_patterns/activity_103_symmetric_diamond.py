"""
Activity 103 — Symmetric Diamond of Stars
Difficulty: 103 / 132

Context:
    A diamond is NOT two unrelated loops — it is a top half mirrored vertically
    around its middle row (OR a single loop using `abs(mid - i)`!). Seeing
    vertical symmetry makes diamonds, hourglasses, and alphabet diamonds
    effortless.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Implement `example_mirror_rows(top_half)` that takes the top half of a
    symmetric pattern (INCLUDING the center row at `top_half[-1]`) and returns
    a new list mirroring the rows above the center in reverse order — without
    duplicating the center row!

Draw -> Index -> Rule:
    Given `top_half`:
        r = 0: "  *  "
        r = 1: " *** "
        r = 2: "*****"   <-- center row (do NOT duplicate!)
    Mirroring `top_half[:-1][::-1]` (equivalently `top_half[-2::-1]`):
        r = 3: " *** "
        r = 4: "  *  "
    Rule:
        - If `not top_half`: return `[]`.
        - Return `list(top_half) + list(reversed(top_half[:-1]))`.

Edge Cases:
    - `[]` -> `[]`
    - `["*"]` -> `["*"]` (`top_half[:-1]` is empty!)
    - Never mutates `top_half`.

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem:
    Implement `solve_create_diamond(n)` returning a symmetric star diamond
    whose height and widest row are BOTH `n` (for positive ODD `n`), with exact
    left AND right space padding so every row has length `n`!

Draw -> Index -> Rule (for n = 5, mid = n // 2 = 2, spaces as `·`):
    Draw:
        ··*··   (i = 0: pad = |2 - 0| = 2, stars = 5 - 4 = 1)
        ·***·   (i = 1: pad = |2 - 1| = 1, stars = 5 - 2 = 3)
        *****   (i = 2: pad = |2 - 2| = 0, stars = 5 - 0 = 5)
        ·***·   (i = 3: pad = |2 - 3| = 1, stars = 5 - 2 = 3)
        ··*··   (i = 4: pad = |2 - 4| = 2, stars = 5 - 4 = 1)
    Rule:
        - If `n <= 0`: return `[]`.
        - If `n % 2 == 0`: raise `ValueError("n must be odd.")`.
        - For `i` in `range(n)`:
          `pad = abs(mid - i)`
          `stars = n - 2 * pad`
          row = `" " * pad + "*" * stars + " " * pad`
        (Or build the top `mid + 1` rows and mirror them!)

Examples:
    solve_create_diamond(1) -> ["*"]
    solve_create_diamond(5) -> [
        "  *  ",
        " *** ",
        "*****",
        " *** ",
        "  *  ",
    ]
    solve_create_diamond(0) -> []
    solve_create_diamond(4) -> raises ValueError("n must be odd.")
"""

from __future__ import annotations


def example_mirror_rows(top_half: list[str]) -> list[str]:
    """Mirror ``top_half`` vertically around its final row without duplicating it."""
    if not top_half:
        return []
    return list(top_half) + list(reversed(top_half[:-1]))


def solve_create_diamond(n: int) -> list[str]:
    """Return a centered star diamond of width and height ``n`` (odd ``n``).

    Raises:
        ValueError("n must be odd.") if ``n`` is positive and even.
    """
    pass


if __name__ == "__main__":
    top = ["  *  ", " *** ", "*****"]
    print("\n".join(example_mirror_rows(top)))
