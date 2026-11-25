"""
Activity 108 — Number Spiral Strings
Difficulty: 108 / 132

Context:
    Finale of Module 09! Combine your Four Shrinking Walls spiral algorithm
    from Module 08 (Activity 094) with clean ASCII row formatting to produce
    both compact exam-style spiral strings AND neatly column-aligned spirals
    with zero trailing spaces!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Implement `example_format_number_grid(grid, aligned=False)` that formats a
    2D list of positive integers into a list of row strings:
      - If `aligned=False` (compact mode): concatenate `str(val)` with no
        separator (`[1, 2, 3]` -> `"123"`).
      - If `aligned=True` (neat column mode): find the digit width of the
        largest number in `grid`, right-align every cell to that width using
        `f"{val:>{col_width}}"`, and join cells with a single `" "` (NO
        trailing spaces!).

Draw -> Index -> Rule (for 4x4 spiral, max value = 16 -> col_width = 2):
    Compact (`aligned=False`):
        "1234"
        "1213145"
        "1116156"
        "10987"
    Aligned (`aligned=True`):
        " 1  2  3  4"
        "12 13 14  5"
        "11 16 15  6"
        "10  9  8  7"
    Rule:
        - Empty `grid` or `[[]]` -> `[]`.
        - `col_width = max(len(str(val)) for row in grid for val in row)`
        - Each aligned row: `" ".join(f"{val:>{col_width}}" for val in row)`.

Edge Cases:
    - `[]` -> `[]`
    - `[[1]]` -> `["1"]` (both compact and aligned!)

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem A — `solve_create_number_spiral(n)`:
    Build the `n x n` clockwise spiral of `1..n^2` and return it as a list of
    compact row strings (numbers in each row concatenated with `""`).
    - If `n <= 0`: return `[]`.

Problem B — `solve_create_spiral_string(n, aligned=False)`:
    Return the `n x n` clockwise spiral of `1..n^2` as a SINGLE string with
    rows joined by `"\\n"` (`""` if `n <= 0`):
    - When `aligned=False` (default): join `solve_create_number_spiral(n)`
      with `"\\n"`.
    - When `aligned=True`: right-align every number to `len(str(n * n))`
      separated by a single space (NO trailing spaces), joined by `"\\n"`.

Examples:
    solve_create_number_spiral(3) -> ["123", "894", "765"]
    solve_create_number_spiral(0) -> []

    solve_create_spiral_string(3) -> "123\\n894\\n765"
    solve_create_spiral_string(4, aligned=True) -> (
        " 1  2  3  4\\n"
        "12 13 14  5\\n"
        "11 16 15  6\\n"
        "10  9  8  7"
    )
    solve_create_spiral_string(0) -> ""
"""

from __future__ import annotations


def example_format_number_grid(
    grid: list[list[int]],
    aligned: bool = False,
) -> list[str]:
    """Format a 2D integer grid as compact or right-aligned row strings."""
    if not grid or not grid[0]:
        return []
    if not aligned:
        return ["".join(str(val) for val in row) for row in grid]

    col_width = max(len(str(val)) for row in grid for val in row)
    return [
        " ".join(f"{val:>{col_width}}" for val in row)
        for row in grid
    ]


def solve_create_number_spiral(n: int) -> list[str]:
    """Return the ``n x n`` clockwise spiral ``1..n^2`` as compact row strings."""
    pass


def solve_create_spiral_string(n: int, aligned: bool = False) -> str:
    """Return the ``n x n`` clockwise spiral as one newline-joined string."""
    pass


if __name__ == "__main__":
    sample_spiral = [
        [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7],
    ]
    print("Compact:")
    print("\n".join(example_format_number_grid(sample_spiral, aligned=False)))
    print("\nAligned:")
    print("\n".join(example_format_number_grid(sample_spiral, aligned=True)))
