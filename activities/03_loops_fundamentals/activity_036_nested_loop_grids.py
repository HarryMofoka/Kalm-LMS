"""
Activity 036: Nested Loop Basics (2D Grids & Pair Scans)  [Unlocks Checkpoint 06!]
Difficulty: 36 / 132 (Rank 4 - Iteration Specialist)

Context:
Putting one loop INSIDE another unlocks two superpowers you will use on
practically every exam and coding interview:
1. **2D Grids** (game boards, image pixels, spreadsheets, multiplication tables):
   an outer loop walks rows `r` while an inner loop walks columns `c`.
2. **All Unordered Pairs** (collision detection, Two-Sum counts, round-robin
   tournaments): an outer loop chooses `i` while the inner loop starts at
   `j = i + 1` so every pair `(i, j)` with `i < j` is visited ONCE and no item
   is ever paired with itself!

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
Write `example_multiplication_row(n, size)` that returns a list of the first
`size` positive multiples of `n`: `[n * 1, n * 2, ..., n * size]`.
Return `[]` if `size <= 0`.

Step-by-step walkthrough:
1. Guard / natural empty behavior: `range(1, size + 1)` is empty if `size <= 0`.
2. Initialize `row = []`.
3. Loop `for col in range(1, size + 1):` and append `n * col`.
4. Return `row`.
   Notice how a full `size x size` multiplication table is simply building one
   `row` for each `r` in `range(1, size + 1)`!

Edge cases:
- `example_multiplication_row(3, 5)` -> `[3, 6, 9, 12, 15]`.
- `example_multiplication_row(5, 0)` -> `[]`.
- `example_multiplication_row(0, 4)` -> `[0, 0, 0, 0]`.

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
Write `solve_grid_and_pair_sums(size, target_sum)` that uses nested loops to
compute TWO results returned as a 2-tuple `(grid, pair_count)`:
1. `grid`: a `size x size` multiplication table (list of `size` lists), where
   for each row `r` in `1..size` and each column `c` in `1..size`, the entry is
   `r * c`.
   (If `size <= 0`, `grid` is `[]`.)
2. `pair_count`: the number of unordered pairs `(i, j)` of integers such that:
       `1 <= i < j <= size`   AND   `i + j == target_sum`.
   (Notice strict `i < j`! So `(2, 2)` does NOT count, and `(1, 4)` and `(4, 1)`
   are the SAME unordered pair and must only be counted ONCE!)
   (If `size <= 0`, `pair_count` is `0`.)

Example Walkthrough (`size = 4, target_sum = 5`):
- `grid`:
      [
          [1, 2, 3, 4],
          [2, 4, 6, 8],
          [3, 6, 9, 12],
          [4, 8, 12, 16],
      ]
- Pairs `(i, j)` with `1 <= i < j <= 4`:
      (1,2)=3, (1,3)=4, (1,4)=5 [MATCH!], (2,3)=5 [MATCH!], (2,4)=6, (3,4)=7
  -> `pair_count = 2`!
- Return `(grid, 2)`.

Examples:
- `solve_grid_and_pair_sums(3, 4)`
  -> `([[1, 2, 3], [2, 4, 6], [3, 6, 9]], 1)`  # only (1, 3); (2, 2) excluded!
- `solve_grid_and_pair_sums(1, 2)` -> `([[1]], 0)`
- `solve_grid_and_pair_sums(0, 5)` -> `([], 0)`
- `solve_grid_and_pair_sums(-2, 3)` -> `([], 0)`

Hints:
- For `grid`: create a fresh `row = []` INSIDE the outer loop for each `r` in
  `range(1, size + 1)`, fill it in the inner loop `for c in range(1, size + 1)`,
  then append `row` to `grid`!
- For `pair_count`:
      `for i in range(1, size + 1):`
          `for j in range(i + 1, size + 1):`
              `if i + j == target_sum:`
                  `pair_count += 1`
- Completing this activity finishes **Module 03** and unlocks **Checkpoint 06**!
"""

from __future__ import annotations


def example_multiplication_row(n: int, size: int) -> list[int]:
    """Return [n*1, n*2, ..., n*size] (or [] if size <= 0)."""
    row: list[int] = []
    for col in range(1, size + 1):
        row.append(n * col)
    return row


def solve_grid_and_pair_sums(
    size: int, target_sum: int
) -> tuple[list[list[int]], int]:
    """Return (size x size multiplication grid, count of pairs 1<=i<j<=size with i+j==target_sum)."""
    pass


if __name__ == "__main__":
    for r in range(1, 5):
        print(f"Row {r}:", example_multiplication_row(r, 4))
