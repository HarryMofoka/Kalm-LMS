"""
Activity 105 — Checkerboard & Diagonal X-Cross Patterns
Difficulty: 105 / 132

Context:
    Not every pattern is built from `" " * pad + "*" * stars`. Grid patterns
    are even cleaner when you write a **2D Cell Rule `f(r, c)`** that decides
    what character belongs at row `r`, column `c`!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Implement `example_checkerboard(n, dark="#", light=".")` returning an
    `n x n` alternating checkerboard where top-left `(0, 0)` is `dark`.

Draw -> Index -> Rule (for n = 4):
    Draw:
        #.#.
        .#.#
        #.#.
        .#.#
    Index `(r, c)` parity `r + c`:
        (0,0)->0 (even: #), (0,1)->1 (odd: .), (0,2)->2 (even: #) ...
        (1,0)->1 (odd: .),  (1,1)->2 (even: #), (1,2)->3 (odd: .) ...
    Rule:
        Cell `(r, c)` is `dark` if `(r + c) % 2 == 0` else `light`!

Edge Cases:
    - `n <= 0` -> `[]`
    - `n == 1` -> `["#"]`

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem:
    Implement `solve_x_cross(n, mark="X", fill=" ")` returning an `n x n`
    X-cross pattern of constant width `n` (works for BOTH odd and even `n`!).

Draw -> Index -> Rule (for n = 5, fill shown as `·`):
    Draw:
        X···X   (r = 0: marks at c = 0, 4)
        ·X·X·   (r = 1: marks at c = 1, 3)
        ··X··   (r = 2: marks at c = 2)
        ·X·X·   (r = 3: marks at c = 1, 3)
        X···X   (r = 4: marks at c = 0, 4)
    Index:
        - Main diagonal (top-left to bottom-right): `r == c`
        - Anti-diagonal (top-right to bottom-left): `r + c == n - 1`
    Rule:
        - If `n <= 0`: return `[]`.
        - For each row `r` in `range(n)`:
          join `mark` if `r == c or r + c == n - 1` else `fill` for `c` in `range(n)`.

Examples:
    solve_x_cross(5) -> [
        "X   X",
        " X X ",
        "  X  ",
        " X X ",
        "X   X",
    ]
    solve_x_cross(4) -> [
        "X  X",
        " XX ",
        " XX ",
        "X  X",
    ]
    solve_x_cross(1) -> ["X"]
    solve_x_cross(0) -> []
"""

from __future__ import annotations


def example_checkerboard(
    n: int,
    dark: str = "#",
    light: str = ".",
) -> list[str]:
    """Return an ``n x n`` checkerboard where ``(r + c) % 2 == 0`` is ``dark``."""
    if n <= 0:
        return []
    return [
        "".join(dark if (r + c) % 2 == 0 else light for c in range(n))
        for r in range(n)
    ]


def solve_x_cross(
    n: int,
    mark: str = "X",
    fill: str = " ",
) -> list[str]:
    """Return an ``n x n`` X-cross pattern where ``r == c`` or ``r + c == n - 1``."""
    pass


if __name__ == "__main__":
    print("\n".join(example_checkerboard(5)))
