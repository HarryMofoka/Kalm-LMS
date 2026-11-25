"""
Activity 056: Sliding Window Basics
Difficulty: 56 / 132

Context:
    Stock tickers compute 5-day moving averages, network monitors spot peak
    traffic bursts over 10-second windows, and exam problems love testing the
    fixed-size sliding window technique: slide forward by subtracting the
    leaving element and adding the entering element!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Maximum Sum of `k` Consecutive Elements
===============================================================================
Problem:
    Given a list `numbers` and window size `k`, return the maximum sum of any
    `k` consecutive elements. Return `None` if `k <= 0` or `k > len(numbers)`.

Step-by-Step Explanation:
    1. Validate window bounds: `if k <= 0 or k > len(numbers): return None`.
    2. Compute the sum of the first window: `window_sum = sum(numbers[:k])` and
       initialize `best = window_sum`.
    3. Slide the window one step at a time for `i` from `k` to `len(numbers) - 1`:
         - Add the newly entering element `numbers[i]`.
         - Subtract the element leaving the left edge `numbers[i - k]`.
         - Update `best = max(best, window_sum)`.
    4. Total time is $O(n)$ even when `k` is huge!

Edge Cases:
    - `([2, 1, 5, 1, 3, 2], 3)` -> `9` (`5 + 1 + 3`)
    - `([-5, -2, -8, -1], 2)`   -> `-7` (`-5 + -2`)
    - `([1, 2], 3)`             -> `None`
    - `([1, 2], 0)`             -> `None`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Moving Average of Window `k`
===============================================================================
Problem:
    Implement `solve_moving_average(numbers: list[int | float], k: int) -> list[float]`.
    Return a list containing the average of every contiguous window of length `k`
    in `numbers`, each rounded to 2 decimal places (`round(window_sum / k, 2)`).
    If `k <= 0` or `k > len(numbers)`, return `[]`.

Examples:
    - `([2, 4, 6, 8, 10], 3)` -> `[4.0, 6.0, 8.0]`
    - `([1, 2, 3, 4], 2)`     -> `[1.5, 2.5, 3.5]`
    - `([1, 2, 4], 3)`        -> `[2.33]`
    - `([10, -10, 10], 2)`    -> `[0.0, 0.0]`
    - `([5, 10], 5)`          -> `[]`
    - `([5, 10], 0)`          -> `[]`

Edge-Case Hints:
    - There are exactly `len(numbers) - k + 1` valid windows when `1 <= k <= len(numbers)`.
    - Keep `window_sum` as the exact sum (do NOT carry rounded averages forward!)
      and only round when appending `round(window_sum / k, 2)` to your output list.
"""

from __future__ import annotations


def example_max_window_sum(numbers: list[int | float], k: int) -> int | float | None:
    """Return the maximum sum of any `k` consecutive elements, or None if invalid."""
    if k <= 0 or k > len(numbers):
        return None

    window_sum = sum(numbers[:k])
    best = window_sum

    for i in range(k, len(numbers)):
        # Slide window right by 1: add entering element, drop leaving element.
        window_sum += numbers[i] - numbers[i - k]
        if window_sum > best:
            best = window_sum
    return best


def solve_moving_average(numbers: list[int | float], k: int) -> list[float]:
    """Return the window-`k` moving averages of `numbers`, rounded to 2 decimals."""
    pass


if __name__ == "__main__":
    data = [2, 1, 5, 1, 3, 2]
    print("Max sum of 3 consecutive:", example_max_window_sum(data, 3))
