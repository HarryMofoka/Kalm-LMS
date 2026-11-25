"""
Activity 095 — Merge Sort & Counting Inversions
Difficulty: 95 / 132

Context:
    How "out of order" is a playlist or ranked list? An **inversion** is any
    pair of indices `(i, j)` with `i < j` and `values[i] > values[j]`.
    Checking all pairs takes O(n^2) time (too slow for 10,000 items!). By
    piggybacking a single line onto **Merge Sort**, you can count all
    inversions in blazing-fast O(n log n) time!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Implement `example_merge_sort(values)` using divide-and-conquer merge sort,
    returning a NEW sorted list without mutating `values`.

Step-by-Step Explanation:
    1. Base case: a list of length `<= 1` is already sorted — return `list(values)`.
    2. Divide: split at `mid = len(values) // 2` into `left` and `right` halves
       and recursively sort both.
    3. Conquer (merge): use two pointers `i` and `j` (just like Activity 087!):
       - If `left[i] <= right[j]`: append `left[i]`, `i += 1`.
       - Else: append `right[j]`, `j += 1`.
       - Append whichever tail remains.
    4. Total time: O(n log n) in all cases!

Edge Cases:
    - `[]`, `[7]`, negative values, duplicates, already sorted, reverse sorted.

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem:
    Implement `solve_count_inversions(values)` returning the number of
    inversions — pairs `(i, j)` with `i < j` and `values[i] > values[j]` — in
    O(n log n) time WITHOUT mutating `values`!

The Magic One-Line Insight:
    When merging two already-sorted halves `left` and `right`:
      - If `left[i] <= right[j]`: NO inversion! (`left[i]` belongs before `right[j]`).
      - If `right[j] < left[i]`: because `left` is sorted ascending, `right[j]`
        is strictly smaller than `left[i]` AND EVERY REMAINING ELEMENT
        `left[i+1], left[i+2], ..., left[-1]`!
        That adds **`len(left) - i`** inversions in ONE step!

    Total inversions = `left_inversions + right_inversions + split_inversions`.

Examples:
    solve_count_inversions([])               -> 0
    solve_count_inversions([1, 2, 3, 4])     -> 0
    solve_count_inversions([4, 3, 2, 1])     -> 6   (n * (n - 1) // 2)
    solve_count_inversions([2, 4, 1, 3, 5])  -> 3   ((2,1), (4,1), (4,3))
    solve_count_inversions([2, 2, 2])        -> 0   (strict `>` only!)
"""

from __future__ import annotations


def example_merge_sort(values: list[int]) -> list[int]:
    """Return a new ascending sorted copy of ``values`` via O(n log n) merge sort."""
    if len(values) <= 1:
        return list(values)

    mid = len(values) // 2
    left = example_merge_sort(values[:mid])
    right = example_merge_sort(values[mid:])

    merged: list[int] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def solve_count_inversions(values: list[int]) -> int:
    """Return the number of pairs ``(i, j)`` with ``i < j`` and ``values[i] > values[j]``."""
    pass


if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    print("Original:", data)
    print("Merge sorted:", example_merge_sort(data))
