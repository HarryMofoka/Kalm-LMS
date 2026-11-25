"""
Activity 106 — Hollow Diamond & Alphabet Diamond
Difficulty: 106 / 132

Context:
    Hollow diamonds combine THREE concepts you already mastered:
      1. Outer padding (`n - 1 - level`)
      2. Inner hollow gap (`2 * level - 1`) — careful: `level == 0` has ONLY
         ONE character and NO inner gap!
      3. Vertical mirroring (`level = r if r < n else total_rows - 1 - r`)
    And turning `*` into `'A', 'B', 'C', ...` takes just `chr(ord('A') + level)`!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Implement `example_hollow_star_diamond(n)` where `n` is the number of
    levels from the top tip to the widest middle row (`total_rows = 2 * n - 1`,
    constant width `2 * n - 1`, `[]` if `n <= 0`).

Draw -> Index -> Rule (for n = 3, width = 5, total_rows = 5, spaces as `·`):
    Draw:
        ··*··   (r = 0 -> level = 0: outer = 2, single '*')
        ·*·*·   (r = 1 -> level = 1: outer = 1, '*', inner = 1, '*')
        *···*   (r = 2 -> level = 2: outer = 0, '*', inner = 3, '*')
        ·*·*·   (r = 3 -> level = 1: outer = 1, '*', inner = 1, '*')
        ··*··   (r = 4 -> level = 0: outer = 2, single '*')
    Index:
        - `level = r if r < n else (2 * n - 2) - r`
        - `outer = " " * (n - 1 - level)`
        - If `level == 0`: `outer + "*" + outer`
        - Else: `inner = " " * (2 * level - 1)` -> `outer + "*" + inner + "*" + outer`
        - Width check (level > 0): `(n-1-L) + 1 + (2L-1) + 1 + (n-1-L) == 2n - 1`!

Edge Cases:
    - `n <= 0` -> `[]`
    - `n == 1` -> `["*"]`

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem:
    Implement `solve_create_alphabet_diamond(n)` (a famous exam question!)
    returning a hollow diamond built from the first `n` uppercase English
    letters (`'A'` at the tips, widening to `chr(ord('A') + n - 1)` at the
    middle row), with exact symmetric left & right padding (width `2 * n - 1`).

Rules:
    1. If `n <= 0`: return `[]`.
    2. If `n > 26`: raise `ValueError("n must be at most 26.")`.
    3. Use `letter = chr(ord("A") + level)` in place of `'*'`!

Examples:
    solve_create_alphabet_diamond(0) -> []
    solve_create_alphabet_diamond(1) -> ["A"]
    solve_create_alphabet_diamond(3) -> [
        "  A  ",
        " B B ",
        "C   C",
        " B B ",
        "  A  ",
    ]
    solve_create_alphabet_diamond(4) -> [
        "   A   ",
        "  B B  ",
        " C   C ",
        "D     D",
        " C   C ",
        "  B B  ",
        "   A   ",
    ]
    solve_create_alphabet_diamond(27) -> raises ValueError("n must be at most 26.")
"""

from __future__ import annotations


def example_hollow_star_diamond(n: int) -> list[str]:
    """Return a hollow star diamond of ``2n - 1`` rows and width ``2n - 1``."""
    if n <= 0:
        return []
    rows: list[str] = []
    total_rows = 2 * n - 1
    for r in range(total_rows):
        level = r if r < n else total_rows - 1 - r
        outer = " " * (n - 1 - level)
        if level == 0:
            rows.append(outer + "*" + outer)
        else:
            inner = " " * (2 * level - 1)
            rows.append(outer + "*" + inner + "*" + outer)
    return rows


def solve_create_alphabet_diamond(n: int) -> list[str]:
    """Return a hollow alphabet diamond using the first ``n`` letters ``A..Z``.

    Raises:
        ValueError("n must be at most 26.") if ``n > 26``.
    """
    pass


if __name__ == "__main__":
    for row in example_hollow_star_diamond(4):
        print(repr(row))
