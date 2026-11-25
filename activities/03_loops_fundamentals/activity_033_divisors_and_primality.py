"""
Activity 033: Divisors & `sqrt(n)` Primality Testing
Difficulty: 33 / 132 (Rank 4 - Iteration Specialist)

Context:
Prime numbers are the atoms of arithmetic — and the backbone of HTTPS internet
encryption (RSA)! Checking whether a number `n` is prime by testing every
divisor up to `n - 1` works for small numbers, but slows to a crawl on large
inputs. One neat mathematical insight cuts the work from `n` steps down to
`sqrt(n)` steps!

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
Write `example_divisors(n)` that returns a sorted list of all positive divisors
of `n` (integers `d >= 1` where `n % d == 0`). Return `[]` if `n <= 0`.

Step-by-step walkthrough:
1. Guard clause: `if n <= 0: return []`.
2. Notice divisors come in pairs `(d, n // d)`!
   For `n = 36`: `(1, 36)`, `(2, 18)`, `(3, 12)`, `(4, 9)`, `(6, 6)`.
   Every pair has at least one member `<= sqrt(n)`!
3. Loop `d` starting at `1` while `d * d <= n` (using `d * d <= n` avoids any
   floating-point `math.sqrt` rounding issues!):
   - If `n % d == 0`:
     * record `d` in `small`
     * if `d != n // d`, record `n // d` in `large` (avoid duplicating `6` for `36`!)
4. Combine `small + large[::-1]` so the result is already in ascending order!

Edge cases:
- `n = 1` -> `[1]` (don't duplicate `1`!).
- `n = 36` -> `[1, 2, 3, 4, 6, 9, 12, 18, 36]` (perfect square: `6` appears once!).
- `n = 7` -> `[1, 7]` (prime!).
- `n <= 0` -> `[]`.

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
Write `solve_is_prime(n)` that returns `True` if `n` is a prime number and
`False` otherwise, using an efficient `sqrt(n)` loop (`d * d <= n`).

Definition:
A prime number is an integer `>= 2` whose ONLY positive divisors are `1` and
itself.

Rules:
- `n <= 1` (including `0`, `1`, and all negative integers) -> `False`!
  (`1` is NOT prime!)
- `n == 2` -> `True` (the ONLY even prime!).
- Any other even number (`n % 2 == 0`) -> `False`.
- Test odd candidate divisors `d = 3, 5, 7, ...` while `d * d <= n`:
  if `n % d == 0`, return `False` immediately!
- If the loop finishes with no divisor found, return `True`!

Examples:
- `solve_is_prime(1)` -> `False`
- `solve_is_prime(2)` -> `True`
- `solve_is_prime(9)` -> `False`       # 3 * 3 == 9 (watch `<=`, not `<`!)
- `solve_is_prime(13)` -> `True`
- `solve_is_prime(104729)` -> `True`    # 10,000th prime — instant with sqrt(n)!
- `solve_is_prime(-7)` -> `False`

Hints:
- CRITICAL BUG WATCH: write `while d * d <= n:` (LESS THAN OR EQUAL!), NOT
  `d * d < n`! If you wrote `<`, then perfect squares of primes like `9`, `25`,
  and `49` would falsely return `True`!
"""

from __future__ import annotations


def example_divisors(n: int) -> list[int]:
    """Return all positive divisors of n in ascending order (or [] if n <= 0)."""
    if n <= 0:
        return []
    small: list[int] = []
    large: list[int] = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            small.append(d)
            paired = n // d
            # Avoid adding the square root twice when n is a perfect square.
            if paired != d:
                large.append(paired)
        d += 1
    return small + large[::-1]


def solve_is_prime(n: int) -> bool:
    """Return True if integer n is prime using a sqrt(n) loop, else False."""
    pass


if __name__ == "__main__":
    print("Divisors of 36:", example_divisors(36))
    print("Divisors of 13:", example_divisors(13))
    print("Divisors of 1: ", example_divisors(1))
