"""
Activity 019: Leap Year & Calendar Rules
Difficulty: 19 / 132 (Rank 3 - Logic Architect)

Context:
Every four years we add February 29 — EXCEPT on century years like 1900,
EXCEPT EXCEPT on every 400th year like 2000! Calendar bugs have crashed stock
exchanges, satellite software, and billing systems (remember the 2012 Azure
leap-day outage!). Mastering nested/compound divisibility rules makes you
immune to date bugs.

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
Write `example_is_leap_year(year)` that returns `True` if `year` is a Gregorian
leap year and `False` otherwise.

Gregorian Leap-Year Rule:
A year is a leap year if:
- It is divisible by `400` (`year % 400 == 0`), OR
- It is divisible by `4` (`year % 4 == 0`) AND NOT divisible by `100`
  (`year % 100 != 0`).

Step-by-step walkthrough:
1. Check `year % 400 == 0`: catches `2000`, `2400` -> `True`.
2. Check `(year % 4 == 0 and year % 100 != 0)`: catches `2024`, `2028` -> `True`,
   while rejecting `1900` and `2100` (divisible by 100, not by 400!) -> `False`.
3. Combine with `or` and return the boolean directly.

Edge cases:
- `2024` -> `True` (regular leap year).
- `2023` -> `False` (non-leap year).
- `1900` -> `False` (century trap! Divisible by 4 and 100, NOT 400).
- `2000` -> `True` (400-year exception!).

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
Write `solve_days_in_month(year, month)` that returns the exact number of days
in the given `month` (`1` = January .. `12` = December) of `year`.

Rules:
- Guard clause: if `month < 1` or `month > 12`, return `0`.
- 31-day months: `1, 3, 5, 7, 8, 10, 12` (Jan, Mar, May, Jul, Aug, Oct, Dec).
- 30-day months: `4, 6, 9, 11` (Apr, Jun, Sep, Nov).
- February (`month == 2`): `29` if `year` is a leap year, otherwise `28`!

Examples:
- `solve_days_in_month(2024, 2)` -> `29`
- `solve_days_in_month(2023, 2)` -> `28`
- `solve_days_in_month(1900, 2)` -> `28`
- `solve_days_in_month(2000, 2)` -> `29`
- `solve_days_in_month(2025, 4)` -> `30`
- `solve_days_in_month(2025, 8)` -> `31`
- `solve_days_in_month(2025, 13)` -> `0`

Hints:
- You can use the `in` operator with tuples like `if month in (4, 6, 9, 11): return 30`!
- For February, apply the exact Gregorian leap-year rule (or call `example_is_leap_year(year)`).
"""

from __future__ import annotations


def example_is_leap_year(year: int) -> bool:
    """Return True if year is a Gregorian leap year, else False."""
    # Divisible by 400 OR (divisible by 4 and NOT a non-400 century year).
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def solve_days_in_month(year: int, month: int) -> int:
    """Return number of days in (year, month), or 0 if month is outside 1..12."""
    pass


if __name__ == "__main__":
    for y in (1900, 2000, 2023, 2024):
        print(f"{y} leap year? -> {example_is_leap_year(y)}")
