"""
Activity 035: Number Theory Loops (Euclidean GCD, LCM & Fractions)
Difficulty: 35 / 132 (Rank 4 - Iteration Specialist)

Context:
Euclid's algorithm for Greatest Common Divisor (GCD) — written around 300 BCE —
is one of the oldest and most elegant algorithms still running inside modern
computers! It powers fraction simplification, cryptography, audio-resampling
ratios, and scheduling intervals (via Least Common Multiple, LCM).

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
Write `example_gcd(a, b)` that computes the Greatest Common Divisor of two
integers `a` and `b` using the iterative Euclidean `while` loop — without
calling `math.gcd`.

Key Mathematical Fact:
    gcd(a, b) == gcd(b, a % b),  and  gcd(a, 0) == |a|.

Step-by-step walkthrough:
1. Take absolute values so negative inputs produce a non-negative GCD:
       `x, y = abs(a), abs(b)`
2. Loop `while y != 0:`:
       `x, y = y, x % y`
   Because `0 <= x % y < y`, `y` strictly decreases on EVERY step and MUST hit
   `0` in just a handful of steps (logarithmic time!).
3. Return `x`.
   Trace `example_gcd(48, 18)`:
   - `(48, 18)` -> `(18, 12)` -> `(12, 6)` -> `(6, 0)` -> returns `6`!

Edge cases:
- `example_gcd(0, 7)` -> `7`; `example_gcd(7, 0)` -> `7`; `example_gcd(0, 0)` -> `0`.
- Negative numbers: `example_gcd(-12, 18)` -> `6`.
- Coprime numbers: `example_gcd(13, 20)` -> `1`.

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
A recipe-scaling and music-rhythm toolkit needs BOTH the Least Common Multiple
(LCM) AND the fully simplified ratio of two positive integers `a` and `b`.
Write `solve_lcm_and_fraction(a, b)` (without using `math.gcd`, `math.lcm`, or
`fractions.Fraction`) that returns:
    `(lcm, (simplified_a, simplified_b))`

Formulas (once you compute `g = gcd(a, b)` with a `while` loop):
- `lcm = (a // g) * b`   (exact integer!)
- `simplified_a = a // g`
- `simplified_b = b // g`

Rules:
- Guard clause: if `a <= 0` or `b <= 0`, `raise ValueError("a and b must be positive integers")`.
- Use integer floor division `//` so every value in the returned structure is an
  exact `int` (never a float!).
- Return `(lcm, (simplified_a, simplified_b))`.

Examples:
- `solve_lcm_and_fraction(12, 18)` -> `(36, (2, 3))`  # gcd=6, lcm=36, 12/18=2/3
- `solve_lcm_and_fraction(7, 5)` -> `(35, (7, 5))`    # already simplified (gcd=1)
- `solve_lcm_and_fraction(10, 10)` -> `(10, (1, 1))`
- `solve_lcm_and_fraction(4, 20)` -> `(20, (1, 5))`
- `solve_lcm_and_fraction(0, 5)` -> raises `ValueError`
- `solve_lcm_and_fraction(-4, 6)` -> raises `ValueError`

Hints:
- Writing `(a // g) * b` instead of `(a * b) // g` avoids an unnecessarily huge
  intermediate product while guaranteeing an exact integer!
"""

from __future__ import annotations


def example_gcd(a: int, b: int) -> int:
    """Compute greatest common divisor of a and b using Euclid's while loop."""
    x, y = abs(a), abs(b)
    while y != 0:
        x, y = y, x % y
    return x


def solve_lcm_and_fraction(a: int, b: int) -> tuple[int, tuple[int, int]]:
    """Return (lcm, (a // gcd, b // gcd)) for positive ints a, b; raise ValueError if <= 0."""
    pass


if __name__ == "__main__":
    print("gcd(48, 18) ->", example_gcd(48, 18))
    print("gcd(13, 20) ->", example_gcd(13, 20))
    print("gcd(-12, 8) ->", example_gcd(-12, 8))
