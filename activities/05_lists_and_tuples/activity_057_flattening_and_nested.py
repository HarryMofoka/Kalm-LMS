"""
Activity 057: Flattening & Nested Lists
Difficulty: 57 / 132

Context:
    Spreadsheets, gradebooks, and game boards live inside 2D nested lists
    (lists of lists). Knowing how to traverse rows AND columns without mixing
    up outer vs. inner indices is essential for matrix questions.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Flatten a 1-Level 2D List
===============================================================================
Problem:
    Given a list of lists `nested`, return a single flat 1D list containing all
    elements in row-by-row, left-to-right order.

Step-by-Step Explanation:
    1. Create an empty `flat` list.
    2. Use a nested loop: outer loop iterates over each `sublist` in `nested`,
       inner loop iterates over each `item` in `sublist` and appends it.
    3. Empty inner lists (`[]`) naturally contribute zero items and never crash.

Edge Cases:
    - `[[1, 2], [], [3, 4, 5]]` -> `[1, 2, 3, 4, 5]`
    - `[[], []]`                -> `[]`
    - `[]`                      -> `[]`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Row Sums & Column Sums of a Matrix
===============================================================================
Problem:
    Implement `solve_row_and_col_sums(matrix: list[list[int | float]]) -> tuple[list[int | float], list[int | float]]`.
    Given a rectangular 2D matrix (every row has the same number of columns):
      - Compute `row_sums`: a list where `row_sums[r]` is the sum of row `r`.
      - Compute `col_sums`: a list where `col_sums[c]` is the sum of column `c`.
      - Return `(row_sums, col_sums)`.
      - If `matrix` is empty (`[]`) or its rows are empty (`[[]]`, `[[], []]`),
        return `([], [])`.

Examples:
    - `[[1, 2, 3], [4, 5, 6]]`           -> `([6, 15], [5, 7, 9])`
    - `[[10]]`                           -> `([10], [10])`
    - `[[-1, 2], [3, -4], [5, 6]]`       -> `([1, -1, 11], [7, 4])`
    - `[]`                               -> `([], [])`
    - `[[]]`                             -> `([], [])`

Edge-Case Hints:
    - Check `if not matrix or not matrix[0]: return ([], [])` before reading
      `num_cols = len(matrix[0])`.
    - Remember: `num_rows = len(matrix)` and `num_cols = len(matrix[0])` can be
      different for non-square matrices! For column `c`, sum `matrix[r][c]` for
      `r in range(num_rows)`.
"""

from __future__ import annotations

from typing import Any


def example_flatten_2d(nested: list[list[Any]]) -> list[Any]:
    """Flatten a 1-level 2D list into a single 1D list preserving order."""
    flat: list[Any] = []
    for sublist in nested:
        for item in sublist:
            flat.append(item)
    return flat


def solve_row_and_col_sums(
    matrix: list[list[int | float]],
) -> tuple[list[int | float], list[int | float]]:
    """Return `(row_sums, col_sums)` for a rectangular matrix, or `([], [])` if empty."""
    pass


if __name__ == "__main__":
    grid = [[1, 2], [], [3, 4, 5]]
    print("Nested   :", grid)
    print("Flattened:", example_flatten_2d(grid))
