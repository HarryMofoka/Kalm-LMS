"""
Activity 034: Prime Sieve & Primes in a Range
Difficulty: 34 / 132 (Rank 4 - Iteration Specialist)

Context:
Over 2,200 years ago, the Greek mathematician Eratosthenes invented a blazingly
fast way to find EVERY prime up to `n` without dividing a single number! You
start with a boolean array assuming every number `2..n` is prime, then cross
out multiples of `2`, then multiples of `3`, then multiples of `5`, and so on.
Whatever survives uncrossed is prime!

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
Write `example_count_primes_up_to(n)` that returns how many prime numbers exist
in the inclusive range `2..n` (returning `0` if `n < 2`), using the Sieve of
Eratosthenes.

Step-by-step walkthrough:
1. Guard clause: `if n < 2: return 0`.
2. Create a boolean list `is_prime = [True] * (n + 1)` and mark `0` and `1`
   as non-prime: `is_prime[0] = False`, `is_prime[1] = False`.
3. Loop `p = 2` while `p * p <= n`:
   - If `is_prime[p]` is still `True`, then `p` is prime!
   - Cross out all multiples of `p` starting from `p * p` in steps of `p`:
         `for multiple in range(p * p, n + 1, p):`
             `is_prime[multiple] = False`
     (Why start at `p * p`? Any smaller multiple `k * p` with `k < p` was
     ALREADY crossed out when we processed a smaller prime factor of `k`!)
4. Count how many `True` entries remain (`sum(is_prime)` works because `True`
   counts as `1` and `False` counts as `0`!).

Edge cases:
- `n < 2` (like `1`, `0`, `-10`) -> `0`.
- `n = 2` -> `1` (`2` itself).
- `n = 10` -> `4` (`2, 3, 5, 7`).
- `n = 100` -> `25`.

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
Write `solve_primes_in_range(low, high)` that returns a sorted list of ALL
prime numbers `p` satisfying `low <= p <= high` (both endpoints inclusive!).

Rules:
- If `high < 2` or `low > high`, return `[]`.
- `low` may be negative, `0`, or `1` — never include numbers `< 2`!
- `low` and `high` are BOTH inclusive (so `(2, 2)` returns `[2]`, and
  `(11, 13)` returns `[11, 13]`).
- Must be fast enough to handle ranges up to e.g. `10_000` cleanly (either run
  the Sieve up to `high` and collect primes `>= max(2, low)`, or check each
  candidate with a `sqrt(n)` primality helper!).

Examples:
- `solve_primes_in_range(10, 30)` -> `[11, 13, 17, 19, 23, 29]`
- `solve_primes_in_range(1, 10)` -> `[2, 3, 5, 7]`
- `solve_primes_in_range(-5, 5)` -> `[2, 3, 5]`
- `solve_primes_in_range(14, 16)` -> `[]`
- `solve_primes_in_range(20, 10)` -> `[]`
- `solve_primes_in_range(2, 2)` -> `[2]`

Hints:
- If you run the Sieve of Eratosthenes up to `high`, then collecting the result
  is simply `[num for num in range(max(2, low), high + 1) if is_prime[num]]`!
"""

from __future__ import annotations


def example_count_primes_up_to(n: int) -> int:
    """Return the count of prime numbers <= n using the Sieve of Eratosthenes."""
    if n < 2:
        return 0
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False

    p = 2
    while p * p <= n:
        if is_prime[p]:
            # Cross off multiples of p starting at p*p.
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
        p += 1

    return sum(is_prime)


def solve_primes_in_range(low: int, high: int) -> list[int]:
    """Return a sorted list of all prime numbers p with low <= p <= high."""
    pass


if __name__ == "__main__":
    print("Primes <= 10: ", example_count_primes_up_to(10))
    print("Primes <= 100:", example_count_primes_up_to(100))
