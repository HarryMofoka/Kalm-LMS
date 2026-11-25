"""
Activity 049: Manual Length & Sum Without Built-ins
Difficulty: 49 / 132

Context:
    Introductory Python exams frequently ban `len()`, `sum()`, `min()`, and
    `max()` on specific questions to verify that you understand the underlying
    accumulator loop pattern. Mastering manual accumulators makes every later
    list algorithm effortless.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Manual List Length
===============================================================================
Problem:
    Count how many elements are in `items` WITHOUT calling `len()`.

Step-by-Step Explanation:
    1. Start an integer counter `count = 0`.
    2. Loop over each element with `for _ in items:` (using `_` signals we don't
       need the element's value—only the fact that it exists).
    3. Add `1` to `count` on every iteration and return `count`.

Edge Cases:
    - `[]`             -> `0`
    - `[None, False]`  -> `2` (falsy items still count!)
    - `[10, 20, 30]`   -> `3`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Sum Positive Even Numbers Without `sum()`
===============================================================================
Problem:
    Implement `solve_sum_positive_evens(numbers: list[int]) -> int`.
    Return the sum of all numbers in `numbers` that are BOTH:
      - strictly positive (`num > 0`), AND
      - even (`num % 2 == 0`).
    Accumulate the total manually using a loop (do NOT use `sum()`).
    Return `0` if `numbers` is empty or contains no positive even integers.

Examples:
    - `[1, 2, 3, 4, -6, 0, 8]` -> `14`  (`2 + 4 + 8`; `-6` and `0` are NOT positive!)
    - `[-4, -2, 0, 1, 3]`      -> `0`
    - `[2, 2, 10]`             -> `14`
    - `[]`                     -> `0`

Edge-Case Hints:
    - Zero (`0`) is even (`0 % 2 == 0`), but NOT strictly positive (`0 > 0` is
      False). Adding `0` wouldn't change a sum, yet writing `num > 0 and num % 2 == 0`
      keeps your condition semantically accurate for future problems (like counting!).
    - Negative even numbers like `-4` satisfy `num % 2 == 0`, so do NOT forget
      the `num > 0` check!
"""

from __future__ import annotations

from typing import Any


def example_manual_length(items: list[Any]) -> int:
    """Return the number of items in `items` without calling `len()`."""
    count = 0
    for _ in items:
        count += 1
    return count


def solve_sum_positive_evens(numbers: list[int]) -> int:
    """Return the sum of all strictly positive even integers in `numbers` manually."""
    pass


if __name__ == "__main__":
    for sample in [[10, 20, 30], [None, False], []]:
        print(f"{sample!r:18} -> length = {example_manual_length(sample)}")
