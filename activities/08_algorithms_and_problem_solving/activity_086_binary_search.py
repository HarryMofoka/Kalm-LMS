"""
Activity 086 — Binary Search on Sorted Lists
Difficulty: 86 / 132

Context:
    Searching a 1,000,000-element sorted list linearly can take 1,000,000
    checks. Binary search halves the search range every step — finishing in at
    most 20 checks! Mastering exact boundary updates (`left`, `right`, `mid`)
    prevents infinite loops and off-by-one bugs forever.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Implement iterative `example_binary_search(sorted_nums, target)` that
    returns the index of `target` in an ascending sorted list, or `-1` if not
    found.

Step-by-Step Explanation:
    1. Maintain an INCLUSIVE search interval `[left, right]` starting at
       `left = 0`, `right = len(sorted_nums) - 1`.
    2. While `left <= right`:
       - Compute `mid = (left + right) // 2`.
       - If `sorted_nums[mid] == target`: return `mid`.
       - If `sorted_nums[mid] < target`: target must be strictly to the right,
         so set `left = mid + 1`.
       - Else: target must be strictly to the left, so set `right = mid - 1`.
    3. If the loop exits, `left > right` (interval empty) -> return `-1`.

Edge Cases:
    - Empty list `[]` -> `right = -1`, loop never executes, returns `-1`.
    - Single-element list `[9]` searching `9` -> `mid = 0` -> returns `0`.
    - Target smaller than smallest or larger than largest -> `-1`.

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem:
    Implement `solve_lower_bound(sorted_nums, target)` using iterative binary
    search (do NOT use the `bisect` module — write the binary search yourself!).

    Return the **leftmost insertion index** `i` (`0 <= i <= len(sorted_nums)`)
    where `target` could be inserted so the list remains sorted in ascending
    order. Equivalently: the smallest index `i` such that `sorted_nums[i] >= target`
    (or `len(sorted_nums)` if all elements are `< target`).

Step-by-Step Hint (Half-Open Interval `[left, right)`):
    - Start with `left = 0`, `right = len(sorted_nums)` (notice: `right` is
      EXCLUSIVE, allowing `len(sorted_nums)` as a valid answer!).
    - Loop `while left < right:`
      - `mid = (left + right) // 2`
      - If `sorted_nums[mid] < target`: `left = mid + 1`
      - Else (`sorted_nums[mid] >= target`): `right = mid` (keep `mid` as a
        candidate!)
    - When `left == right`, return `left`!

Examples:
    solve_lower_bound([1, 3, 5, 7], 5)        -> 2
    solve_lower_bound([1, 3, 5, 7], 4)        -> 2
    solve_lower_bound([1, 2, 2, 2, 5], 2)     -> 1   (LEFTMOST duplicate!)
    solve_lower_bound([1, 3, 5], 0)           -> 0
    solve_lower_bound([1, 3, 5], 10)          -> 3
    solve_lower_bound([], 42)                 -> 0
"""

from __future__ import annotations


def example_binary_search(sorted_nums: list[int], target: int) -> int:
    """Return an index of ``target`` in ascending ``sorted_nums``, or ``-1``."""
    left = 0
    right = len(sorted_nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_nums[mid] == target:
            return mid
        if sorted_nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def solve_lower_bound(sorted_nums: list[int], target: int) -> int:
    """Return the leftmost index where ``target`` can be inserted in order."""
    pass


if __name__ == "__main__":
    data = [2, 5, 8, 12, 16, 23, 38, 56]
    print("Search 16:", example_binary_search(data, 16))
    print("Search 20:", example_binary_search(data, 20))
