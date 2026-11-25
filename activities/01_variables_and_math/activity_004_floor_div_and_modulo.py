"""
Activity 004: Integer Division `//` and Remainder `%`
Difficulty: 4 / 132 (Rank 1 - Absolute Beginner)

Context:
Whenever you split a bulk quantity into whole units plus leftovers — coins into
dollars and cents, eggs into cartons, or video timestamps into hours and minutes
— Python's dynamic duo `//` (floor division) and `%` (modulo/remainder) do the
heavy lifting cleanly without decimals.

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
Write `example_minutes_to_hours(total_minutes)` that converts a non-negative
number of minutes into `(hours, remaining_minutes)`.

Step-by-step walkthrough:
1. Each hour contains 60 minutes. How many FULL hours fit into `total_minutes`?
       `hours = total_minutes // 60`
   For example, `135 // 60` is `2`.
2. How many minutes are left over after removing those full hours?
       `remaining_minutes = total_minutes % 60`
   For example, `135 % 60` is `15`.
3. Notice the mathematical invariant: `hours * 60 + remaining_minutes == total_minutes`.
4. Return `(hours, remaining_minutes)`.

Edge cases:
- `0` minutes -> `(0, 0)`.
- `60` minutes -> `(1, 0)` (exact multiple leaves 0 remainder).
- `59` minutes -> `(0, 59)` (less than one full hour).

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
A spacecraft mission timer counts elapsed mission time in raw seconds. Write
`solve_seconds_to_dhms(total_seconds)` that converts a non-negative integer
`total_seconds` into a 4-tuple:
    `(days, hours, minutes, seconds)`

Useful time constants:
- 1 minute = `60` seconds
- 1 hour   = `3600` seconds (`60 * 60`)
- 1 day    = `86400` seconds (`24 * 3600`)

Rules:
- Use integer division `//` and remainder `%`.
- `hours` must be in `0..23`, `minutes` in `0..59`, and `seconds` in `0..59`.

Examples:
- `solve_seconds_to_dhms(0)` -> `(0, 0, 0, 0)`
- `solve_seconds_to_dhms(3661)` -> `(0, 1, 1, 1)`
- `solve_seconds_to_dhms(90061)` -> `(1, 1, 1, 1)`
- `solve_seconds_to_dhms(172800)` -> `(2, 0, 0, 0)`

Hints:
- Peel off the largest unit first and keep updating a `remaining` variable:
  `days = total_seconds // 86400`, then `remaining = total_seconds % 86400`,
  then extract `hours` from `remaining`, and so on!
"""

from __future__ import annotations


def example_minutes_to_hours(total_minutes: int) -> tuple[int, int]:
    """Convert non-negative total_minutes into (hours, remaining_minutes)."""
    # `//` gives the whole number of 60-minute blocks; `%` gives the leftover.
    hours = total_minutes // 60
    remaining_minutes = total_minutes % 60
    return (hours, remaining_minutes)


def solve_seconds_to_dhms(total_seconds: int) -> tuple[int, int, int, int]:
    """Convert non-negative total_seconds into (days, hours, minutes, seconds)."""
    pass


if __name__ == "__main__":
    print("135 mins ->", example_minutes_to_hours(135))
    print("60 mins  ->", example_minutes_to_hours(60))
    print("0 mins   ->", example_minutes_to_hours(0))
