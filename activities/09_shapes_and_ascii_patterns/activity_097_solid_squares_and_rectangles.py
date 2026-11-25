"""
Activity 097 — Solid Square & Rectangle Rows
Difficulty: 97 / 132

Context:
    Welcome to ASCII Pattern Engineering! Every shape in this module is built
    as a **list of row strings** (pure return — no `print()` inside the
    function) using the **Draw -> Index -> Rule** workflow.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Implement `example_solid_square(n, char="*")` returning an `n x n` solid
    square as a list of `n` strings (`[]` when `n <= 0`).

Draw -> Index -> Rule (for n = 3):
    Draw:
        ***
        ***
        ***
    Index:
        row r = 0 -> 3 stars -> "***"
        row r = 1 -> 3 stars -> "***"
        row r = 2 -> 3 stars -> "***"
    Rule:
        - Total rows = `n`
        - Every row is `char * n` (exact width `n`, zero trailing spaces)
        - Guard: if `n <= 0`, return `[]`.

Edge Cases:
    - `n <= 0` -> `[]`
    - `n == 1` -> `["*"]`
    - Custom character: `example_solid_square(2, "#")` -> `["##", "##"]`

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem:
    Implement `solve_solid_rectangle(width, height, char="*")` returning a
    `width x height` solid rectangle as a list of `height` strings, each of
    length `width` (no trailing spaces!).

Draw -> Index -> Rule Hint (width = 5, height = 3):
    Draw:
        *****
        *****
        *****
    Index:
        - Number of rows = `height` (3) — careful not to swap `width` & `height`!
        - Length of each row = `width` (5)
    Rule:
        - If `width <= 0 or height <= 0`: return `[]`.
        - Return `[char * width for _ in range(height)]`.

Examples:
    solve_solid_rectangle(5, 3)      -> ["*****", "*****", "*****"]
    solve_solid_rectangle(4, 2, "#") -> ["####", "####"]
    solve_solid_rectangle(1, 3)      -> ["*", "*", "*"]
    solve_solid_rectangle(0, 3)      -> []
    solve_solid_rectangle(4, -1)     -> []
"""

from __future__ import annotations


def example_solid_square(n: int, char: str = "*") -> list[str]:
    """Return an ``n x n`` solid square as a list of ``n`` row strings."""
    if n <= 0:
        return []
    return [char * n for _ in range(n)]


def solve_solid_rectangle(
    width: int,
    height: int,
    char: str = "*",
) -> list[str]:
    """Return a ``width x height`` solid rectangle as a list of row strings."""
    pass


if __name__ == "__main__":
    print("\n".join(example_solid_square(4)))
