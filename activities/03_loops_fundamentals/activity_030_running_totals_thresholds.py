"""
Activity 030: Running Totals, Thresholds & Infinite-Loop Guards  [Unlocks Checkpoint 05!]
Difficulty: 30 / 132 (Rank 3 - Loop Apprentice)

Context:
Financial simulations — saving for a laptop, paying off a credit card, or
modeling battery drain — step forward one day or one month at a time until a
running total crosses a threshold. The biggest danger in threshold `while` loops
is an **infinite loop** when the goal can never be reached, so guarding against
non-progress upfront is essential!

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
Write `example_days_to_goal(daily_saving, goal)` that returns how many days of
saving `daily_saving` dollars per day are needed for your running total to reach
or exceed `goal`.
- If `goal <= 0`, return `0` immediately (goal already met!).
- If `daily_saving <= 0`, raise `ValueError` (you would loop forever and never
  reach a positive goal!).

Step-by-step walkthrough:
1. Check `if goal <= 0: return 0` FIRST (even if `daily_saving` is 0, a goal of
   0 is already reached!).
2. Check `if daily_saving <= 0: raise ValueError(...)` so the loop is
   mathematically guaranteed to terminate.
3. Run `while saved < goal:`:
       `saved += daily_saving`
       `days += 1`
4. Return `days`.

Edge cases:
- `example_days_to_goal(25, 100)` -> `4` (hits 100 exactly).
- `example_days_to_goal(30, 100)` -> `4` (30, 60, 90, 120 >= 100).
- `example_days_to_goal(10, 0)` -> `0`.
- `example_days_to_goal(0, 100)` -> raises `ValueError`.

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
You are building a credit-card payoff simulator! Write:
    `solve_months_to_payoff(balance, monthly_rate, monthly_payment)`

Each month, TWO things happen in this exact order:
1. Interest is added to the remaining balance:
       `balance += balance * monthly_rate`
2. Your fixed payment is subtracted:
       `balance -= monthly_payment`
3. Increment `months += 1`.

Repeat until `balance <= 0`, then return `months`!

CRITICAL Guards (check in this order!):
1. If `balance <= 0`: return `0` (already paid off!).
2. If `monthly_payment <= 0` OR `monthly_payment <= balance * monthly_rate`:
   `raise ValueError("monthly_payment must exceed the monthly interest to pay off the balance")`
   Think about why: if the first month's interest is `$20` and you only pay
   `$20` (or `$15`), your balance stays flat or GROWS every month forever!

Examples:
- `solve_months_to_payoff(100.0, 0.0, 30.0)` -> `4`    # 70, 40, 10, -20
- `solve_months_to_payoff(100.0, 0.10, 60.0)` -> `2`   # m1: 110-60=50; m2: 55-60=-5
- `solve_months_to_payoff(0.0, 0.05, 50.0)` -> `0`     # already $0!
- `solve_months_to_payoff(1000.0, 0.02, 20.0)` -> raises `ValueError` (interest == payment!)
- `solve_months_to_payoff(1000.0, 0.02, 15.0)` -> raises `ValueError` (balance grows!)

Hints:
- Note that if `monthly_payment > balance * monthly_rate` in month 1, the
  balance shrinks after month 1, so month 2's interest is even smaller — which
  guarantees termination!
- Completing this activity unlocks **Checkpoint 05**!
"""

from __future__ import annotations


def example_days_to_goal(daily_saving: float, goal: float) -> int:
    """Return number of days saving daily_saving per day to reach >= goal."""
    if goal <= 0:
        return 0
    if daily_saving <= 0:
        raise ValueError("daily_saving must be positive when goal > 0")

    saved = 0.0
    days = 0
    while saved < goal:
        saved += daily_saving
        days += 1
    return days


def solve_months_to_payoff(
    balance: float, monthly_rate: float, monthly_payment: float
) -> int:
    """Simulate monthly interest + payment until balance <= 0; raise ValueError if unwinnable."""
    pass


if __name__ == "__main__":
    print("$30/day to reach $100 ->", example_days_to_goal(30, 100), "days")
    print("$25/day to reach $100 ->", example_days_to_goal(25, 100), "days")
