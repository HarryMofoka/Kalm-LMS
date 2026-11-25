"""
Activity 032: Fibonacci Sequence & Simultaneous Tuple Updates
Difficulty: 32 / 132 (Rank 4 - Iteration Specialist)

Context:
Sunflowers, pinecones, nautilus shells, and agile sprint-point scales all use
the Fibonacci sequence: `0, 1, 1, 2, 3, 5, 8, 13, 21, ...` where each term is
the sum of the previous two! In Python, simultaneous tuple assignment
`a, b = b, a + b` lets you advance two interdependent variables at once
without needing a temporary variable!

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
Write `example_first_n_fibonacci(n)` that returns a list containing the first
`n` Fibonacci numbers starting with `0, 1, 1, 2, 3, ...`.
Return `[]` if `n <= 0`.

Step-by-step walkthrough:
1. Initialize `seq = []`, and the two sliding state variables `a, b = 0, 1`.
2. Repeat `n` times (`for _ in range(n):`):
   - `seq.append(a)`
   - `a, b = b, a + b`
   Why is `a, b = b, a + b` so clean? Python evaluates the ENTIRE right-hand
   side `(b, a + b)` BEFORE updating `a` and `b`! (If you wrote `a = b` and
   then `b = a + b` on separate lines, `a` would already have been overwritten!)
3. Trace `n = 5`:
   - iter 1: append `0`, `(a, b)` becomes `(1, 1)`
   - iter 2: append `1`, `(a, b)` becomes `(1, 2)`
   - iter 3: append `1`, `(a, b)` becomes `(2, 3)`
   - iter 4: append `2`, `(a, b)` becomes `(3, 5)`
   - iter 5: append `3`, `(a, b)` becomes `(5, 8)`
   Result: `[0, 1, 1, 2, 3]`!

Edge cases:
- `n <= 0` -> `[]`.
- `n == 1` -> `[0]`.
- `n == 2` -> `[0, 1]`.

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
Instead of generating a fixed COUNT of terms, generate Fibonacci numbers up to
a maximum VALUE! Write `solve_fibonacci_up_to(limit)` that returns a list of
all Fibonacci numbers (starting from `0, 1, 1, 2, ...`) that are **less than
or equal to** `limit`.

Rules:
- If `limit < 0`, return `[]` (no Fibonacci number is negative!).
- `limit` is INCLUSIVE: if `limit` itself is a Fibonacci number (like `13`),
  include it!
- Watch `limit == 1`: the Fibonacci sequence contains TWO `1`s (`0, 1, 1, 2, ...`),
  so `solve_fibonacci_up_to(1)` MUST return `[0, 1, 1]`!

Examples:
- `solve_fibonacci_up_to(-5)` -> `[]`
- `solve_fibonacci_up_to(0)` -> `[0]`
- `solve_fibonacci_up_to(1)` -> `[0, 1, 1]`
- `solve_fibonacci_up_to(10)` -> `[0, 1, 1, 2, 3, 5, 8]`
- `solve_fibonacci_up_to(13)` -> `[0, 1, 1, 2, 3, 5, 8, 13]`

Hints:
- Use `a, b = 0, 1` and loop `while a <= limit:`: append `a`, then advance
  `a, b = b, a + b`! Trace `limit = 0` and `limit = 1` by hand — it works
  automatically!
"""

from __future__ import annotations


def example_first_n_fibonacci(n: int) -> list[int]:
    """Return the first n Fibonacci numbers starting with 0, 1, 1, 2, ..."""
    seq: list[int] = []
    a, b = 0, 1
    for _ in range(max(0, n)):
        seq.append(a)
        # Tuple assignment evaluates both expressions before binding a and b.
        a, b = b, a + b
    return seq


def solve_fibonacci_up_to(limit: int) -> list[int]:
    """Return all Fibonacci numbers (0, 1, 1, 2, ...) less than or equal to limit."""
    pass


if __name__ == "__main__":
    print("First 10 Fibonacci:", example_first_n_fibonacci(10))
    print("First 1 Fibonacci: ", example_first_n_fibonacci(1))
    print("First 0 Fibonacci: ", example_first_n_fibonacci(0))
