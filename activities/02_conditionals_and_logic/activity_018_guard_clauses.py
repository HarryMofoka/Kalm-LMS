"""
Activity 018: Guard Clauses & Early Returns  [Unlocks Checkpoint 03!]
Difficulty: 18 / 132 (Rank 2 - Decision Maker)

Context:
Deeply nested `if` blocks ("arrow code" indented 5 levels right!) are painful
to read and easy to break. Professional Python engineers use **guard clauses**:
handle invalid or special cases right at the top of the function with an early
`return`, leaving the main "happy path" clean, flat, and unindented!

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
Write `example_safe_divide(numerator, denominator)` that returns
`round(numerator / denominator, 4)` when `denominator != 0`, or returns `None`
if `denominator == 0` (preventing a `ZeroDivisionError` crash!).

Step-by-step walkthrough:
1. Place the guard clause right at the top:
       `if denominator == 0:`
           `return None`
2. Now that the dangerous case has exited early, the rest of the function runs
   at top-level indentation — no `else` wrapper needed!
       `return round(numerator / denominator, 4)`

Edge cases:
- `example_safe_divide(10, 0)` -> `None` (no crash!).
- `example_safe_divide(0, 5)` -> `0.0` (0 divided by 5 IS completely valid!).
- `example_safe_divide(1, 3)` -> `0.3333`.

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
A stock-tracker dashboard computes percentage change between yesterday's value
(`old_value`) and today's value (`new_value`), but if `old_value` is `0`,
percentage change is undefined! Write `solve_safe_percent_change(old_value,
new_value)`:
- Guard clause: if `old_value == 0`, return `None`.
- Otherwise compute:
      `change = ((new_value - old_value) / abs(old_value)) * 100`
  and return `round(change, 2)`.

Why `abs(old_value)` in the denominator?
Suppose a company's profit goes from `-$100` to `-$50`. That is an *improvement*
(positive `+50.0%` change), whereas dividing by raw `-100` would misleadingly
produce `-50.0%`! Using `abs(old_value)` keeps increases positive and decreases
negative even for negative starting values.

Rules:
- Return `None` when `old_value == 0` (even if `new_value == 0`).
- Return a float rounded to 2 decimals otherwise.

Examples:
- `solve_safe_percent_change(100, 125)` -> `25.0`
- `solve_safe_percent_change(200, 150)` -> `-25.0`
- `solve_safe_percent_change(0, 50)` -> `None`
- `solve_safe_percent_change(-100, -50)` -> `50.0`
- `solve_safe_percent_change(80, 80)` -> `0.0`

Hints:
- Check `if old_value == 0: return None` as your very first line!
- Completing this activity unlocks **Checkpoint 03**!
"""

from __future__ import annotations


def example_safe_divide(numerator: float, denominator: float) -> float | None:
    """Return numerator / denominator rounded to 4 decimals, or None on division by zero."""
    # Guard clause: exit early when division is undefined.
    if denominator == 0:
        return None
    return round(numerator / denominator, 4)


def solve_safe_percent_change(old_value: float, new_value: float) -> float | None:
    """Return percentage change from old_value to new_value (2 decimals), or None if old_value == 0."""
    pass


if __name__ == "__main__":
    print("10 / 4 ->", example_safe_divide(10, 4))
    print("10 / 0 ->", example_safe_divide(10, 0))
    print("0 / 5  ->", example_safe_divide(0, 5))
