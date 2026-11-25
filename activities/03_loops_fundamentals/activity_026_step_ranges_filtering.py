"""
Activity 026: Step Ranges & Loop Filtering
Difficulty: 26 / 132 (Rank 3 - Loop Apprentice)

Context:
Loops get even more expressive when you combine `range(start, stop, step)` with
`if` filters inside the loop body! Today's exercise introduces one of the most
famous warm-up puzzles in computer science (Project Euler Problem #1).

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
Write `example_even_numbers(n)` that returns a list of all positive even
numbers up to `n` inclusive (`[2, 4, 6, ...]`). Return `[]` if `n < 2`.

Step-by-step walkthrough:
1. Notice `range()` accepts a third argument: `step`!
       `range(2, n + 1, 2)`
   starts at `2`, jumps by `+2` each time (`2, 4, 6, ...`), and stops before
   exceeding `n`.
2. Append each value into `evens` (or iterate directly).
3. When `n < 2` (like `1`, `0`, or `-5`), `range(2, n + 1, 2)` is empty so we
   cleanly return `[]`.

Edge cases:
- `n = 10` -> `[2, 4, 6, 8, 10]` (10 IS included because of `n + 1`!).
- `n = 9` -> `[2, 4, 6, 8]`.
- `n = 1` -> `[]`.

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
Write `solve_sum_multiples_3_or_5(limit)` that returns the sum of all positive
integers **strictly below** `limit` that are multiples of `3` OR `5`.

Watch the classic trap!
Numbers like `15`, `30`, and `45` are divisible by BOTH `3` AND `5`. They must
be added to the total **ONLY ONCE** — never double-counted!

Rules:
- Strictly below `limit` means iterate `for num in range(1, limit):` (NOT
  `limit + 1`!).
- Include `num` if `num % 3 == 0 or num % 5 == 0`.
- If `limit <= 3`, return `0`.

Examples:
- `solve_sum_multiples_3_or_5(10)` -> `23`    # 3 + 5 + 6 + 9
- `solve_sum_multiples_3_or_5(16)` -> `60`    # 3+5+6+9+10+12+15 (15 counted once!)
- `solve_sum_multiples_3_or_5(20)` -> `78`    # 60 + 18
- `solve_sum_multiples_3_or_5(3)` -> `0`      # strictly below 3 -> none
- `solve_sum_multiples_3_or_5(0)` -> `0`
- `solve_sum_multiples_3_or_5(1000)` -> `233168`

Hints:
- A single `if num % 3 == 0 or num % 5 == 0:` automatically adds multiples of
  15 exactly once!
"""

from __future__ import annotations


def example_even_numbers(n: int) -> list[int]:
    """Return all positive even integers <= n using a stepped range."""
    evens: list[int] = []
    # Step of 2 visits 2, 4, 6, ... without even needing a modulo check!
    for num in range(2, n + 1, 2):
        evens.append(num)
    return evens


def solve_sum_multiples_3_or_5(limit: int) -> int:
    """Return the sum of positive integers strictly below limit divisible by 3 or 5."""
    pass


if __name__ == "__main__":
    print("Evens up to 10 ->", example_even_numbers(10))
    print("Evens up to 9  ->", example_even_numbers(9))
    print("Evens up to 1  ->", example_even_numbers(1))
