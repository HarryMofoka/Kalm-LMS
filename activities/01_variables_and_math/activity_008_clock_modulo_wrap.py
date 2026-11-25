"""
Activity 008: Clock Wrap-Around with Modulo
Difficulty: 8 / 132 (Rank 2 - Foundations Builder)

Context:
Time, compass headings (0-359°), musical scales, and circular game boards all
wrap around when you pass the end! Python's modulo operator `%` is a superpower
here because Python uses *mathematical floor modulo*, meaning even negative
offsets wrap cleanly into `0 .. modulus - 1`!

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
Write `example_clock_hours(start_hour, hours_added)` for a 24-hour clock
(`0` through `23`). Given `start_hour` and an integer `hours_added` (which can
be positive, zero, or even negative!), return the resulting hour on the 24-hour
clock.

Step-by-step walkthrough:
1. Add the offset: `raw_hour = start_hour + hours_added`.
2. Wrap into the range `0..23` with `% 24`:
       `return raw_hour % 24`
3. Why does this work for negative `hours_added` too?
   Suppose `start_hour = 2` and `hours_added = -5`. Then `raw_hour = -3`.
   In Python, `-3 % 24 == 21` (9 PM the previous night!), because
   `-3 = (-1) * 24 + 21` with remainder in `0..23`.

Edge cases:
- `example_clock_hours(23, 2)` -> `1` (wraps past midnight).
- `example_clock_hours(10, 48)` -> `10` (full multiples of 24 land on the same hour).
- `example_clock_hours(1, -3)` -> `22` (wraps backward past midnight).

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
An international flight scheduler tracks departures on a 24-hour clock
(`start_hour` in `0..23`, `start_minute` in `0..59`) and adds `added_minutes`
(an integer representing flight duration or schedule shift — may be `0`,
positive, or negative!). Write `solve_clock_with_rollover(start_hour,
start_minute, added_minutes)` that returns a 3-tuple:
    `(days_rolled, new_hour, new_minute)`

Where:
- `days_rolled`: how many calendar days forward (positive) or backward
  (negative) the clock rolled over (`0` if still on the same day).
- `new_hour`: resulting hour in `0..23`.
- `new_minute`: resulting minute in `0..59`.

Rules:
- 1 day = `24 * 60 = 1440` minutes.
- Convert the starting time into minutes since midnight:
      `total_minutes = start_hour * 60 + start_minute + added_minutes`
- Then use `// 1440` and `% 1440`, followed by `// 60` and `% 60`!

Examples:
- `solve_clock_with_rollover(8, 15, 45)` -> `(0, 9, 0)`
- `solve_clock_with_rollover(22, 30, 120)` -> `(1, 0, 30)`
- `solve_clock_with_rollover(23, 59, 1)` -> `(1, 0, 0)`
- `solve_clock_with_rollover(10, 0, 2880)` -> `(2, 10, 0)`
- `solve_clock_with_rollover(1, 0, -90)` -> `(-1, 23, 30)`

Hints:
- Because Python's `//` floors toward negative infinity and `%` always keeps
  the remainder non-negative for a positive divisor (`1440`), ONE single set of
  `//` and `%` statements handles positive, zero, AND negative `added_minutes`
  without a single `if` statement!
"""

from __future__ import annotations


def example_clock_hours(start_hour: int, hours_added: int) -> int:
    """Return the hour (0..23) on a 24-hour clock after adding hours_added."""
    # Python's modulo keeps results in 0..23 even when hours_added is negative.
    return (start_hour + hours_added) % 24


def solve_clock_with_rollover(
    start_hour: int, start_minute: int, added_minutes: int
) -> tuple[int, int, int]:
    """Return (days_rolled, new_hour, new_minute) on a 24-hour clock."""
    pass


if __name__ == "__main__":
    print("22:00 + 5h ->", example_clock_hours(22, 5))
    print("02:00 - 5h ->", example_clock_hours(2, -5))
