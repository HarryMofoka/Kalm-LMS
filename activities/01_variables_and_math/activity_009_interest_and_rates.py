"""
Activity 009: Financial Math & Compound Interest
Difficulty: 9 / 132 (Rank 2 - Foundations Builder)

Context:
Albert Einstein allegedly called compound interest "the eighth wonder of the
world." Whether you are modeling savings accounts, student loans, or investment
growth, converting clean textbook formulas into bug-free Python expressions
with clear variable names is an essential real-world skill.

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
Write `example_simple_interest(principal, annual_rate, years)` where
`annual_rate` is a decimal (for example, `0.05` means 5% per year). Return
`(interest, total)` rounded to 2 decimal places.

Formula:
    interest = principal * annual_rate * years
    total = principal + interest

Step-by-step walkthrough:
1. Compute `interest = principal * annual_rate * years`.
2. Compute `total = principal + interest` BEFORE rounding so you never suffer
   from rounding drift.
3. Return `(round(interest, 2), round(total, 2))`.

Edge cases:
- `0` years or `0.0` annual rate yields `(0.0, round(principal, 2))`.
- Fractional years (like `0.5` for 6 months) work automatically.

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
A fintech savings app lets users compare accounts that compound interest
annually, quarterly, or monthly. Write:
    `solve_compound_interest(principal, annual_rate, compounds_per_year, years)`

Formula:
    A = P * (1 + r / n) ** (n * t)
Where:
- `P` = `principal` (starting balance)
- `r` = `annual_rate` as a decimal (e.g., `0.06` for 6%)
- `n` = `compounds_per_year` (positive integer, e.g., `12` for monthly)
- `t` = `years` (non-negative float)

Return a 2-tuple `(final_amount, interest_earned)` where:
- `final_amount = round(A, 2)`
- `interest_earned = round(A - principal, 2)`

Rules:
- Notice the order in the tuple: `(final_amount, interest_earned)`.
- Use parentheses around `(n * t)` in the exponent! `base ** n * t` without
  parentheses would raise to `n` and then multiply the whole result by `t`!

Examples:
- `solve_compound_interest(1000.0, 0.05, 1, 2)` -> `(1102.5, 102.5)`
- `solve_compound_interest(1000.0, 0.12, 12, 1)` -> `(1126.83, 126.83)`
- `solve_compound_interest(500.0, 0.0, 4, 5)` -> `(500.0, 0.0)`
- `solve_compound_interest(2000.0, 0.08, 4, 0)` -> `(2000.0, 0.0)`

Hints:
- Remember operator precedence: `**` binds tighter than `*` and `/`, so write
  `(1 + annual_rate / compounds_per_year) ** (compounds_per_year * years)`.
"""

from __future__ import annotations


def example_simple_interest(
    principal: float, annual_rate: float, years: float
) -> tuple[float, float]:
    """Return (interest, total) for simple interest, rounded to 2 decimals."""
    interest = principal * annual_rate * years
    total = principal + interest
    return (round(interest, 2), round(total, 2))


def solve_compound_interest(
    principal: float, annual_rate: float, compounds_per_year: int, years: float
) -> tuple[float, float]:
    """Return (final_amount, interest_earned) for compound interest, rounded to 2 decimals."""
    pass


if __name__ == "__main__":
    print("$1000 at 5% for 3 yrs:", example_simple_interest(1000.0, 0.05, 3))
    print("$2500 at 3.5% for 0.5 yrs:", example_simple_interest(2500.0, 0.035, 0.5))
