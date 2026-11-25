"""
Activity 094 — Spiral Matrix Traversal & Construction
Difficulty: 94 / 132

Context:
    Spiral matrix questions look scary until you discover the **Four Shrinking
    Walls** pattern: maintain four integer boundaries `top`, `bottom`, `left`,
    `right`. Walk one edge, immediately shrink that wall inward by 1, and guard
    the bottom & left legs so thin strips never get double-visited!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Implement `example_read_spiral(matrix)` that reads any rectangular `m x n`
    2D list in clockwise spiral order starting at `(0, 0)` and returns a flat
    list of values.

Step-by-Step Explanation:
    1. Guard empty inputs: if `not matrix or not matrix[0]`, return `[]`.
    2. Set `top, bottom = 0, len(matrix) - 1` and `left, right = 0, len(matrix[0]) - 1`.
    3. While `top <= bottom and left <= right`:
       - Walk TOP row left->right (`col` in `range(left, right + 1)`), then `top += 1`.
       - Walk RIGHT col top->bottom (`row` in `range(top, bottom + 1)`), then `right -= 1`.
       - If `top <= bottom`: walk BOTTOM row right->left, then `bottom -= 1`.
       - If `left <= right`: walk LEFT col bottom->top, then `left += 1`.
    4. Notice the two `if` guards! Without them, a `1 x 4` or `4 x 1` matrix
       would walk back over cells it already visited!

Edge Cases:
    - `[]` or `[[]]` -> `[]`
    - `1 x 4` single row `[[1, 2, 3, 4]]` -> `[1, 2, 3, 4]`
    - `3 x 1` single col `[[1], [2], [3]]` -> `[1, 2, 3]`

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem:
    Implement `solve_spiral_matrix(n)` that BUILDS an `n x n` 2D matrix filled
    with `1, 2, ..., n^2` in clockwise spiral order!

Rules:
    1. If `n <= 0`: return `[]`.
    2. Pre-allocate `matrix = [[0] * n for _ in range(n)]` (NEVER use
       `[[0] * n] * n`, which aliases all rows to the same list!).
    3. Use the EXACT same Four Shrinking Walls loop as `example_read_spiral`,
       writing `current` (starting at `1` and incrementing by `1`) into each
       cell instead of reading it!

Examples:
    solve_spiral_matrix(0) -> []
    solve_spiral_matrix(1) -> [[1]]
    solve_spiral_matrix(3) -> [
        [1, 2, 3],
        [8, 9, 4],
        [7, 6, 5],
    ]
    solve_spiral_matrix(4) -> [
        [ 1,  2,  3,  4],
        [12, 13, 14,  5],
        [11, 16, 15,  6],
        [10,  9,  8,  7],
    ]
"""

from __future__ import annotations


def example_read_spiral(matrix: list[list[int]]) -> list[int]:
    """Return all elements of a 2D matrix traversed in clockwise spiral order."""
    if not matrix or not matrix[0]:
        return []

    result: list[int] = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result


def solve_spiral_matrix(n: int) -> list[list[int]]:
    """Return an ``n x n`` matrix filled with ``1..n^2`` in clockwise spiral order."""
    pass


if __name__ == "__main__":
    sample = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    print("Clockwise spiral read:", example_read_spiral(sample))
