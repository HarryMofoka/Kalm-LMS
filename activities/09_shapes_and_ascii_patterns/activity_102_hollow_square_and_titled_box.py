"""
Activity 102 — Hollow Square & Titled ASCII Box  [Unlocks Checkpoint 17!]
Difficulty: 102 / 132

Context:
    Hollow shapes introduce the **Border Rule**: top row (`r == 0`) and bottom
    row (`r == height - 1`) are solid walls; every middle row has a left wall,
    hollow interior spaces, and a right wall. Always check tiny degenerate
    sizes (`n == 1` and `n == 2`) so `n - 2` never becomes negative!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Implement `example_bordered_box(width, height)` drawing a hollow ASCII box
    using `+` corners, `-` horizontal borders, and `|` vertical borders
    (`[]` if `width < 2` or `height < 2`).

Draw -> Index -> Rule (width = 5, height = 4):
    Draw:
        +---+
        |   |
        |   |
        +---+
    Index:
        - `r == 0` or `r == height - 1` -> `"+" + "-" * (width - 2) + "+"`
        - interior rows (`0 < r < height - 1`) -> `"|" + " " * (width - 2) + "|"`
    Rule:
        Guard `width < 2 or height < 2 -> []`, then build top, `height - 2`
        middle rows, and bottom!

Edge Cases:
    - `width = 2, height = 2` -> `["++", "++"]`
    - `width = 1, height = 4` -> `[]` (too narrow for left + right walls!)

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem A — `solve_create_hollow_square(n)`:
    Return a hollow square of side `n` drawn with `'*'` (constant width `n`):
    - `n <= 0` -> `[]`
    - `n == 1` -> `["*"]`
    - `n == 2` -> `["**", "**"]`
    - `n >= 3`:
      - Top & bottom rows (`r == 0` or `r == n - 1`): `"*" * n`
      - Interior rows: `"*" + " " * (n - 2) + "*"`

Problem B — `solve_titled_box(title, width)`:
    Return a 3-row framed ASCII title box using `+`, `-`, `|`:
    - Let `inner_width = max(width - 2, len(title) + 2)`.
      (That way, if `width` is large enough, every row has exact width `width`;
      and if `title` is too long for `width`, the box gracefully widens to fit
      `title` with 1 space on each side!)
    - Top row:    `"+" + "-" * inner_width + "+"`
    - Middle row: `"|" + title.center(inner_width) + "|"`
    - Bottom row: `"+" + "-" * inner_width + "+"`

Examples:
    solve_create_hollow_square(4) -> [
        "****",
        "*  *",
        "*  *",
        "****",
    ]
    solve_create_hollow_square(1) -> ["*"]

    solve_titled_box("HI", 8) -> [
        "+------+",
        "|  HI  |",
        "+------+",
    ]
    solve_titled_box("HELLO", 4) -> [
        "+-------+",
        "| HELLO |",
        "+-------+",
    ]
"""

from __future__ import annotations


def example_bordered_box(width: int, height: int) -> list[str]:
    """Return a hollow ``width x height`` ASCII box using ``+``, ``-``, ``|``."""
    if width < 2 or height < 2:
        return []
    horizontal = "+" + "-" * (width - 2) + "+"
    middle = "|" + " " * (width - 2) + "|"
    return [horizontal] + [middle] * (height - 2) + [horizontal]


def solve_create_hollow_square(n: int) -> list[str]:
    """Return a hollow square of side ``n`` drawn with ``*``."""
    pass


def solve_titled_box(title: str, width: int) -> list[str]:
    """Return a 3-row titled ASCII box using ``+``, ``-``, ``|``."""
    pass


if __name__ == "__main__":
    print("\n".join(example_bordered_box(6, 4)))
