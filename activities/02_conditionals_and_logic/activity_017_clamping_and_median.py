"""
Activity 017: Clamping & Median of Three Without Builtins
Difficulty: 17 / 132 (Rank 2 - Decision Maker)

Context:
In game development (keeping a player inside screen bounds, volume sliders from
0 to 100) and sorting algorithms (choosing a "median-of-three" pivot in
Quicksort), you need pure comparison logic that works with zero helper lists
and handles equal values (ties) without breaking!

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
Write `example_clamp(value, low, high)` that restricts `value` to stay within
the inclusive range `[low, high]` — WITHOUT using Python's `min()` or `max()`.
(Assume `low <= high`.)

Step-by-step walkthrough:
1. If `value < low`, it fell below the floor -> return `low`.
2. Else if `value > high`, it went above the ceiling -> return `high`.
3. Otherwise it is already inside `[low, high]` -> return `value`.

Edge cases:
- `value == low` or `value == high` returns `value` unchanged.
- `low == high` always returns that single allowed value.
- Works seamlessly for negative numbers and floats!

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
Three weather sensors measure the same room temperature, and one of them might
glitch high or low. Taking the **median** (middle value when ordered from
smallest to largest) discards any single-sensor outlier!

Write `solve_median_of_three(a, b, c)` returning the middle value of three
numbers **WITHOUT** using `sorted()`, `min()`, `max()`, or lists!

Rules:
- Must handle ALL 6 possible orderings of distinct numbers (`a<b<c`, `a<c<b`,
  `b<a<c`, `b<c<a`, `c<a<b`, `c<b<a`).
- Must ALSO handle **duplicate values (ties)** properly!
  * `(5, 5, 2)` ordered is `[2, 5, 5]` -> median is `5`!
  * `(2, 5, 2)` ordered is `[2, 2, 5]` -> median is `2`!
  * `(7, 7, 7)` ordered is `[7, 7, 7]` -> median is `7`!
- Works with ints, floats, and negative numbers.

Examples:
- `solve_median_of_three(3, 1, 2)` -> `2`
- `solve_median_of_three(10, 5, 20)` -> `10`
- `solve_median_of_three(5, 5, 2)` -> `5`
- `solve_median_of_three(-1, -5, -3)` -> `-3`
- `solve_median_of_three(4, 4, 4)` -> `4`

Hints:
- When is `a` the median? Whenever `b <= a <= c` OR `c <= a <= b`!
  Notice Python supports chained comparisons like `b <= a <= c`!
- Using `<=` (not `<`) is the secret that makes duplicate values work cleanly!
- Check if `a` is the median; elif check if `b` is the median; else `c` MUST be
  the median!
"""

from __future__ import annotations


def example_clamp(value: float, low: float, high: float) -> float:
    """Restrict value to the inclusive interval [low, high] without min/max."""
    if value < low:
        return low
    elif value > high:
        return high
    else:
        return value


def solve_median_of_three(a: float, b: float, c: float) -> float:
    """Return the median of three numbers using comparisons only (no sorted/min/max)."""
    pass


if __name__ == "__main__":
    print("clamp(150, 0, 100) ->", example_clamp(150, 0, 100))
    print("clamp(-5, 0, 100)  ->", example_clamp(-5, 0, 100))
    print("clamp(42, 0, 100)  ->", example_clamp(42, 0, 100))
