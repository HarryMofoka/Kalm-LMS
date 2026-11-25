"""
Activity 025: Counting & Accumulating with a `for` Loop
Difficulty: 25 / 132 (Rank 3 - Loop Apprentice)

Context:
`for i in range(...)` is the workhorse of Python! Remember the #1 rule of
`range(start, stop)`: `start` is INCLUSIVE, while `stop` is EXCLUSIVE! So to
count from `1` through `n` inclusive, you write `range(1, n + 1)`.

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
Write `example_count_up(n)` that uses a `for` loop to return a list of integers
from `1` up to `n` inclusive (`[1, 2, ..., n]`). If `n <= 0`, return `[]`.

Step-by-step walkthrough:
1. Initialize an empty list accumulator BEFORE the loop: `numbers = []`.
2. Loop `for current in range(1, n + 1):`
   - Inside the loop, append `current` to `numbers`.
   - Notice: if `n <= 0`, `range(1, n + 1)` is automatically empty, so the loop
     runs 0 times and returns `[]` cleanly!
3. Return `numbers` AFTER the loop finishes (watch indentation — putting
   `return` INSIDE the loop would exit on the very first iteration!).

Edge cases:
- `n = 5` -> `[1, 2, 3, 4, 5]`.
- `n = 1` -> `[1]`.
- `n = 0` or `n = -3` -> `[]`.

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
Write `solve_sum_to_n(n)` that computes the sum `1 + 2 + ... + n` using a
`for` loop and an integer accumulator — **WITHOUT** calling Python's built-in
`sum()`.

Rules:
- Initialize `total = 0` before the loop.
- Add each number from `1` through `n` inclusive using `total += current`.
- If `n <= 0`, return `0`.

Examples:
- `solve_sum_to_n(5)` -> `15`    # 1 + 2 + 3 + 4 + 5
- `solve_sum_to_n(1)` -> `1`
- `solve_sum_to_n(0)` -> `0`
- `solve_sum_to_n(-4)` -> `0`
- `solve_sum_to_n(100)` -> `5050`

Hints:
- Because `range(1, n + 1)` produces zero iterations whenever `n <= 0`, starting
  with `total = 0` handles `0` and negative `n` automatically!
"""

from __future__ import annotations


def example_count_up(n: int) -> list[int]:
    """Return [1, 2, ..., n] built with a for loop (or [] if n <= 0)."""
    numbers: list[int] = []
    # range(1, n + 1) starts at 1 and stops right after n.
    for current in range(1, n + 1):
        numbers.append(current)
    return numbers


def solve_sum_to_n(n: int) -> int:
    """Return 1 + 2 + ... + n using a for loop accumulator (0 if n <= 0)."""
    pass


if __name__ == "__main__":
    print("count_up(5)  ->", example_count_up(5))
    print("count_up(0)  ->", example_count_up(0))
    print("count_up(-2) ->", example_count_up(-2))
