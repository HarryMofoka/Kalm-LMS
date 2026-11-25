"""
Activity 027: Accumulating a Product (Power & Factorial)
Difficulty: 27 / 132 (Rank 3 - Loop Apprentice)

Context:
When you accumulate a SUM, you initialize `total = 0` (because `0` is the
additive identity: `0 + x == x`). When you accumulate a PRODUCT, starting at
`0` is a classic disaster because `0 * anything == 0`! Product accumulators
ALWAYS start at `1` (the multiplicative identity: `1 * x == x`).

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
Write `example_integer_power(base, exponent)` that computes `base ** exponent`
for non-negative integer `exponent` using a loop (without using `**` or
`pow()`). Raise `ValueError` if `exponent < 0`.

Step-by-step walkthrough:
1. Guard clause: if `exponent < 0`, raise `ValueError("exponent must be >= 0")`.
2. Initialize `result = 1` (NOT `0`!).
3. Repeat `exponent` times (`for _ in range(exponent):`):
       `result *= base`
   Notice `_` is Python's convention for a loop variable whose value we don't
   need inside the loop body!
4. When `exponent == 0`, the loop runs 0 times and returns `1` — matching the
   mathematical rule that `base ** 0 == 1`!

Edge cases:
- `example_integer_power(2, 5)` -> `32`.
- `example_integer_power(7, 0)` -> `1`.
- `example_integer_power(-3, 3)` -> `-27`.
- `example_integer_power(2, -1)` -> raises `ValueError`.

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
Write `solve_factorial(n)` that computes `n!` (n factorial) iteratively using
a loop — **WITHOUT** calling `math.factorial`.

Definition:
- `0! = 1`
- `n! = 1 * 2 * 3 * ... * n` for `n >= 1`
- For `n < 0`, factorial is undefined -> `raise ValueError(...)`!

Rules:
- Guard clause: `if n < 0: raise ValueError("n must be non-negative")`.
- Initialize `product = 1` and multiply by every integer from `1` (or `2`) up
  to `n` inclusive.
- Return the exact integer (Python integers have arbitrary precision, so even
  `20!` computes without overflow!).

Examples:
- `solve_factorial(0)` -> `1`
- `solve_factorial(1)` -> `1`
- `solve_factorial(5)` -> `120`     # 1 * 2 * 3 * 4 * 5
- `solve_factorial(10)` -> `3628800`
- `solve_factorial(-1)` -> raises `ValueError`

Hints:
- Starting `product = 1` and looping `for factor in range(2, n + 1):` cleanly
  handles `n = 0` and `n = 1` with zero extra `if` checks!
"""

from __future__ import annotations


def example_integer_power(base: int, exponent: int) -> int:
    """Compute base ** exponent for exponent >= 0 via a multiplicative loop."""
    if exponent < 0:
        raise ValueError(f"exponent must be non-negative, got {exponent}")
    result = 1
    # Multiply by base `exponent` times; 0 iterations naturally yields 1.
    for _ in range(exponent):
        result *= base
    return result


def solve_factorial(n: int) -> int:
    """Compute n! iteratively using a loop; raise ValueError if n < 0."""
    pass


if __name__ == "__main__":
    print("2^5  ->", example_integer_power(2, 5))
    print("9^0  ->", example_integer_power(9, 0))
    print("-3^3 ->", example_integer_power(-3, 3))
