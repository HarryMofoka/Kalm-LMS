"""
Activity 055: Running / Prefix Sums
Difficulty: 55 / 132

Context:
    Financial dashboards track cumulative revenue day by day, and high-speed
    query engines answer thousands of "what was the total from day L to day R?"
    questions in $O(1)$ time each by precomputing a prefix-sum array once.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Prefix Sum List
===============================================================================
Problem:
    Given a list of numbers, return a new list `prefix` of the same length where
    `prefix[i]` equals `numbers[0] + numbers[1] + ... + numbers[i]`.

Step-by-Step Explanation:
    1. Track `running = 0` and an empty `result` list.
    2. For each `num` in `numbers`: add `running += num` and append `running`.
    3. Total time complexity is $O(n)$ (much faster than recomputing
       `sum(numbers[:i + 1])` at every index, which is $O(n^2)$!).

Edge Cases:
    - `[3, 1, 4, 1]`   -> `[3, 4, 8, 9]`
    - `[5, -2, 3, -6]` -> `[5, 3, 6, 0]`
    - `[]`             -> `[]`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Range Sum Queries Using Prefix Sums
===============================================================================
Problem:
    Implement `solve_range_sum_queries(numbers: list[int | float], queries: list[tuple[int, int]]) -> list[int | float]`.
    Given `numbers` and a list of inclusive index range queries `(left, right)`
    (guaranteed `0 <= left <= right < len(numbers)`), return a list containing
    the sum of `numbers[left : right + 1]` for each query—computed using prefix
    sums so each query takes $O(1)$ time!

Examples:
    - `numbers = [2, 4, 1, 7, 3]`, `queries = [(0, 2), (1, 3), (2, 4), (4, 4)]`
      -> `[7, 12, 11, 3]`
    - `numbers = [5, -3, 2, -1]`, `queries = [(0, 3), (1, 2)]`
      -> `[3, -1]`
    - `numbers = [10, 20]`, `queries = []`
      -> `[]`

Edge-Case Hints:
    - PRO TIP: Build a padded prefix array of length `len(numbers) + 1` starting
      with `prefix = [0]`, where `prefix[i + 1] = prefix[i] + numbers[i]`.
    - Then EVERY inclusive range `(left, right)` has the exact formula:
      `prefix[right + 1] - prefix[left]`—with NO special `if left == 0:` branch
      needed!
"""

from __future__ import annotations


def example_prefix_sums(numbers: list[int | float]) -> list[int | float]:
    """Return the running (prefix) sums of `numbers` in O(n) time."""
    result: list[int | float] = []
    running: int | float = 0
    for num in numbers:
        running += num
        result.append(running)
    return result


def solve_range_sum_queries(
    numbers: list[int | float],
    queries: list[tuple[int, int]],
) -> list[int | float]:
    """Answer inclusive `(left, right)` range sum queries using prefix sums."""
    pass


if __name__ == "__main__":
    daily_sales = [3, 1, 4, 1, 5]
    print("Sales      :", daily_sales)
    print("Prefix sums:", example_prefix_sums(daily_sales))
