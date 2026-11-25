"""
Activity 058: Matrix Transpose & Diagonal Sums
Difficulty: 58 / 132

Context:
    Image rotation, linear algebra libraries, and board games like Tic-Tac-Toe
    all inspect matrices along transposed axes and diagonals. Mastering index
    relationships like `(r, c) <-> (c, r)` and `(i, i)` vs. `(i, n - 1 - i)`
    unlocks an entire family of exam problems.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Transpose a Rectangular Matrix
===============================================================================
Problem:
    Given an `R x C` rectangular matrix, return its `C x R` transpose where
    `result[c][r] == matrix[r][c]`. Return `[]` if `matrix` is empty (`[]`) or
    has empty rows (`[[]]`). Do NOT mutate `matrix`.

Step-by-Step Explanation:
    1. Guard `if not matrix or not matrix[0]: return []`.
    2. Let `rows = len(matrix)` and `cols = len(matrix[0])`.
    3. For each column index `c` in `range(cols)`, build a new row
       `[matrix[r][c] for r in range(rows)]`.
    4. Notice an `R x C` matrix becomes a `C x R` matrix (e.g., `2 x 3` -> `3 x 2`).

Edge Cases:
    - `[[1, 2, 3], [4, 5, 6]]` -> `[[1, 4], [2, 5], [3, 6]]`
    - `[[1, 2, 3]]`            -> `[[1], [2], [3]]`
    - `[]`                     -> `[]`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Main & Anti-Diagonal Sums of a Square Matrix
===============================================================================
Problem:
    Implement `solve_diagonal_sums(matrix: list[list[int | float]]) -> tuple[int | float, int | float]`.
    Given an `n x n` square matrix, return `(main_diag_sum, anti_diag_sum)`:
      - `main_diag_sum`: sum of elements on the main (top-left to bottom-right)
        diagonal, where `row == col`: `matrix[i][i]`.
      - `anti_diag_sum`: sum of elements on the anti- (top-right to bottom-left)
        diagonal, where `row + col == n - 1`: `matrix[i][n - 1 - i]`.
      - For an empty matrix `[]`, return `(0, 0)`.
      - Note: When `n` is odd, the center cell `matrix[n // 2][n // 2]` lies on
        BOTH diagonals and SHOULD be included in BOTH sums!

Examples:
    - `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]` -> `(15, 15)` (`1+5+9=15`, `3+5+7=15`)
    - `[[2, 10], [3, 5]]`                 -> `(7, 13)`  (`2+5=7`, `10+3=13`)
    - `[[42]]`                            -> `(42, 42)`
    - `[]`                                -> `(0, 0)`

Edge-Case Hints:
    - You only need ONE loop `for i in range(n):` — no nested loop required!
      Inside it, accumulate `main_sum += matrix[i][i]` and
      `anti_sum += matrix[i][n - 1 - i]` in $O(n)$ time!
"""

from __future__ import annotations

from typing import Any


def example_transpose(matrix: list[list[Any]]) -> list[list[Any]]:
    """Return the transpose of a rectangular 2D matrix without mutating input."""
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    return [[matrix[r][c] for r in range(rows)] for c in range(cols)]


def solve_diagonal_sums(
    matrix: list[list[int | float]],
) -> tuple[int | float, int | float]:
    """Return `(main_diag_sum, anti_diag_sum)` of an `n x n` square matrix."""
    pass


if __name__ == "__main__":
    mat = [[1, 2, 3], [4, 5, 6]]
    print("Original  :", mat)
    print("Transposed:", example_transpose(mat))
