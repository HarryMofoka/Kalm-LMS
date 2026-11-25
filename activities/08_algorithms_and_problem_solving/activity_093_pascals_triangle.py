"""
Activity 093 — Pascal's Triangle & Combinations
Difficulty: 93 / 132

Context:
    Pascal's triangle is a classic exam favorite because every row builds
    directly from the row above it: the first and last numbers are always `1`,
    and every interior number is the sum of the two numbers directly above it!

        Row 0:          1
        Row 1:        1   1
        Row 2:      1   2   1
        Row 3:    1   3   3   1
        Row 4:  1   4   6   4   1

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Implement `example_pascal_row(row_index)` that returns the 0-indexed row
    `row_index` of Pascal's triangle (or `[]` if `row_index < 0`).

Step-by-Step Explanation:
    1. Guard: if `row_index < 0`, return `[]`.
    2. Start with `row = [1]` (row 0).
    3. Repeat `row_index` times:
       - Build the interior elements by summing adjacent pairs of `row`:
         `[row[i] + row[i + 1] for i in range(len(row) - 1)]`
       - Wrap with `[1] + ... + [1]`.
    4. Trace:
       - `row_index = 0` -> `[1]`
       - `row_index = 1` -> `[1, 1]`
       - `row_index = 4` -> `[1, 4, 6, 4, 1]`

Edge Cases:
    - `row_index < 0` -> `[]`
    - `row_index == 0` -> `[1]`

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem:
    Implement `solve_pascal_triangle(n)` that returns the first `n` rows of
    Pascal's triangle as a 2D list `list[list[int]]`.

Rules:
    1. If `n <= 0`: return `[]`.
    2. If `n == 1`: return `[[1]]`.
    3. For each subsequent row, start and end with `1`, and compute each
       interior entry as `prev[i] + prev[i + 1]`.

Examples:
    solve_pascal_triangle(0) -> []
    solve_pascal_triangle(1) -> [[1]]
    solve_pascal_triangle(4) -> [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
    ]
    solve_pascal_triangle(5) -> [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
    ]
"""

from __future__ import annotations


def example_pascal_row(row_index: int) -> list[int]:
    """Return the 0-indexed row ``row_index`` of Pascal's triangle."""
    if row_index < 0:
        return []
    row = [1]
    for _ in range(row_index):
        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]
    return row


def solve_pascal_triangle(n: int) -> list[list[int]]:
    """Return the first ``n`` rows of Pascal's triangle (``[]`` if ``n <= 0``)."""
    pass


if __name__ == "__main__":
    for idx in range(6):
        print(f"Row {idx}: {example_pascal_row(idx)}")
