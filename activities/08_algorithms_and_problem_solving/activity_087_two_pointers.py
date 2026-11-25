"""
Activity 087 — Two Pointers on Sorted Sequences
Difficulty: 87 / 132

Context:
    When data is ALREADY sorted, a pair of index pointers (`left`/`right`
    moving inward, or `i`/`j` advancing across two sorted lists) replaces
    slow $O(n^2)$ nested loops with blazing-fast $O(n)$ single passes!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Implement `example_sorted_two_sum(sorted_nums, target)` that finds two
    distinct indices `(left, right)` with `left < right` such that
    `sorted_nums[left] + sorted_nums[right] == target`, returning `(left, right)`
    or `None` if no such pair exists.

Step-by-Step Explanation:
    1. Place `left = 0` at the smallest number and `right = len(sorted_nums) - 1`
       at the largest number.
    2. While `left < right`:
       - Compute `total = sorted_nums[left] + sorted_nums[right]`.
       - If `total == target`: return `(left, right)`.
       - If `total < target`: sum is too small -> advance `left += 1` to get a
         larger value.
       - If `total > target`: sum is too big -> retreat `right -= 1` to get a
         smaller value.
    3. Every iteration eliminates one index, guaranteeing O(n) time and O(1)
       extra space!

Edge Cases:
    - Fewer than 2 items (`[]` or `[5]`) -> `None`
    - Negative numbers `[-4, -1, 3, 7]` with target `2` -> `(1, 2)` (`-1 + 3`)
    - Duplicates `[3, 3]` with target `6` -> `(0, 1)`

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem:
    Implement `solve_merge_sorted_lists(list_a, list_b)` using TWO POINTERS
    (`i` for `list_a`, `j` for `list_b`) to merge two already-sorted ascending
    lists into a NEW sorted list in $O(n + m)$ time — WITHOUT calling `sorted()`
    and WITHOUT mutating `list_a` or `list_b`!

Rules:
    1. Compare `list_a[i]` and `list_b[j]`: append the smaller one to `merged`
       and increment its pointer (if tied, append `list_a[i]` first).
    2. Once either pointer hits the end of its list, append all remaining
       elements from the other list (`merged.extend(list_a[i:])`, etc.).
    3. Return `merged`. Both input lists must remain completely unchanged.

Examples:
    solve_merge_sorted_lists([1, 3, 5], [2, 3, 6, 8]) -> [1, 2, 3, 3, 5, 6, 8]
    solve_merge_sorted_lists([], [1, 4])              -> [1, 4]
    solve_merge_sorted_lists([-5, 0], [-3, 2])        -> [-5, -3, 0, 2]
    solve_merge_sorted_lists([], [])                  -> []
"""

from __future__ import annotations


def example_sorted_two_sum(
    sorted_nums: list[int],
    target: int,
) -> tuple[int, int] | None:
    """Return ``(left, right)`` indices summing to ``target``, or ``None``."""
    left = 0
    right = len(sorted_nums) - 1

    while left < right:
        total = sorted_nums[left] + sorted_nums[right]
        if total == target:
            return (left, right)
        if total < target:
            left += 1
        else:
            right -= 1

    return None


def solve_merge_sorted_lists(
    list_a: list[int],
    list_b: list[int],
) -> list[int]:
    """Merge two ascending sorted lists in O(n + m) without mutating inputs."""
    pass


if __name__ == "__main__":
    nums = [-4, -1, 2, 5, 9, 11]
    print("Two-sum for 7:", example_sorted_two_sum(nums, 7))
    print("Two-sum for 99:", example_sorted_two_sum(nums, 99))
