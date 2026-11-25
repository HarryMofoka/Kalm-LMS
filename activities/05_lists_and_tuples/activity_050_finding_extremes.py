"""
Activity 050: Finding Extremes Without Built-ins
Difficulty: 50 / 132

Context:
    Initializing `smallest = 0` or `largest = 0` is one of the most infamous
    exam mistakes: the moment your list contains only positive numbers (like
    `[5, 8, 12]`) or only negative numbers (`[-10, -3, -25]`), starting at `0`
    gives the wrong answer! Always seed extremes from `numbers[0]`.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Find Minimum Manually
===============================================================================
Problem:
    Find and return the smallest number in `numbers` WITHOUT calling `min()` or
    `sorted()`. Return `None` if `numbers` is empty.

Step-by-Step Explanation:
    1. Guard against an empty list FIRST: `if not numbers: return None`.
    2. Seed `smallest = numbers[0]`—a real element from the list.
    3. Loop through `numbers[1:]`: whenever `value < smallest`, update
       `smallest = value`.
    4. Works identically for positive numbers, negative numbers, floats, and
       1-element lists!

Edge Cases:
    - `[7, 2, 9, -4, 5]` -> `-4`
    - `[10, 20, 30]`     -> `10`  (would break if seeded at `0`!)
    - `[42]`             -> `42`
    - `[]`               -> `None`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Single-Pass `(min, max)` Tuple
===============================================================================
Problem:
    Implement `solve_find_min_max(numbers: list[int | float]) -> tuple[int | float, int | float] | None`.
    Find BOTH the minimum and maximum values in `numbers` in a SINGLE pass
    without using `min()`, `max()`, or `sorted()`.
    Return `(minimum, maximum)` as a 2-tuple, or `None` if `numbers` is empty.

Examples:
    - `[7, 2, 9, -4, 5]`  -> `(-4, 9)`
    - `[-10, -3, -25]`    -> `(-25, -3)`
    - `[42]`              -> `(42, 42)`
    - `[1.5, 1.5, 1.5]`   -> `(1.5, 1.5)`
    - `[]`                -> `None`

Edge-Case Hints:
    - Seed BOTH `minimum = numbers[0]` and `maximum = numbers[0]` after checking
      `if not numbers: return None`.
    - Inside the loop over `numbers[1:]`, update `minimum` if `val < minimum`
      and `maximum` if `val > maximum`.
"""

from __future__ import annotations


def example_find_min(numbers: list[int | float]) -> int | float | None:
    """Return the minimum value in `numbers` without `min()`, or None if empty."""
    if not numbers:
        return None

    smallest = numbers[0]
    for value in numbers[1:]:
        if value < smallest:
            smallest = value
    return smallest


def solve_find_min_max(
    numbers: list[int | float],
) -> tuple[int | float, int | float] | None:
    """Return `(minimum, maximum)` in one pass without builtins, or None if empty."""
    pass


if __name__ == "__main__":
    for sample in [[7, 2, 9, -4, 5], [10, 20, 30], [42], []]:
        print(f"{sample!r:20} -> min = {example_find_min(sample)}")
