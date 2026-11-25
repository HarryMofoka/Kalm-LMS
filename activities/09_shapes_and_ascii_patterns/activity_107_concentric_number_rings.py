"""
Activity 107 — Concentric Number Rings Square
Difficulty: 107 / 132

Context:
    Concentric-ring problems stump students who try to simulate rings layer by
    layer with four loops — yet there is a jaw-dropping ONE-LINE geometry
    formula! Every cell `(r, c)` has a distance to each of the 4 edges of the
    grid; the **smallest** of those 4 distances tells you WHICH ring it lives
    on!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Implement `example_edge_distance_grid(n)` returning an `n x n` 2D integer
    grid where cell `(r, c)` equals its distance to the nearest border of the
    grid (`[]` when `n <= 0`).

Draw -> Index -> Rule (for n = 5):
    Distances from `(r, c)` to the four edges:
      - Top edge:    `r`
      - Left edge:   `c`
      - Bottom edge: `(n - 1) - r`
      - Right edge:  `(n - 1) - c`
    Nearest edge distance:
      `dist = min(r, c, n - 1 - r, n - 1 - c)`

    Result for n = 5:
        [0, 0, 0, 0, 0]
        [0, 1, 1, 1, 0]
        [0, 1, 2, 1, 0]
        [0, 1, 1, 1, 0]
        [0, 0, 0, 0, 0]

Edge Cases:
    - `n <= 0` -> `[]`
    - `n == 1` -> `[[0]]`

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem:
    Implement `solve_concentric_rings(n)` returning a `(2n - 1) x (2n - 1)`
    square as a list of strings where the outermost ring is `n`, the next ring
    inward is `n - 1`, and so on down to `1` at the very center!

Draw -> Index -> Rule (for n = 3 -> size = 2 * 3 - 1 = 5):
    Draw:
        33333
        32223
        32123
        32223
        33333
    Index:
        - `size = 2 * n - 1`
        - For cell `(r, c)`: `dist = min(r, c, size - 1 - r, size - 1 - c)`
        - Outer ring has `dist = 0` -> digit `n - 0 = 3`
        - Middle ring has `dist = 1` -> digit `n - 1 = 2`
        - Center cell has `dist = 2` -> digit `n - 2 = 1`
    Rule:
        - If `n <= 0`: return `[]`.
        - If `n > 9`: raise `ValueError("n must be between 1 and 9.")`
          (so every cell is a single digit and every row has exact width `2n - 1`!).
        - Cell `(r, c)` character = `str(n - min(r, c, size - 1 - r, size - 1 - c))`.

Examples:
    solve_concentric_rings(0) -> []
    solve_concentric_rings(1) -> ["1"]
    solve_concentric_rings(2) -> [
        "222",
        "212",
        "222",
    ]
    solve_concentric_rings(3) -> [
        "33333",
        "32223",
        "32123",
        "32223",
        "33333",
    ]
    solve_concentric_rings(10) -> raises ValueError("n must be between 1 and 9.")
"""

from __future__ import annotations


def example_edge_distance_grid(n: int) -> list[list[int]]:
    """Return an ``n x n`` grid of each cell's distance to the nearest edge."""
    if n <= 0:
        return []
    return [
        [min(r, c, n - 1 - r, n - 1 - c) for c in range(n)]
        for r in range(n)
    ]


def solve_concentric_rings(n: int) -> list[str]:
    """Return a ``(2n - 1) x (2n - 1)`` concentric number rings square.

    Raises:
        ValueError("n must be between 1 and 9.") if ``n > 9``.
    """
    pass


if __name__ == "__main__":
    for row in example_edge_distance_grid(5):
        print(row)
