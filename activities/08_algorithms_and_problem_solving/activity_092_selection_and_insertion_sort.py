"""
Activity 092 — Selection Sort & Insertion Sort from Scratch
Difficulty: 92 / 132

Context:
    Understanding how simple $O(n^2)$ sorts move elements gives you deep
    intuition for sorting invariants, stability, and swap counts — and prepares
    you directly for counting inversions in Activity 095!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Implement `example_selection_sort(values)` from scratch (no `.sort()` or
    `sorted()`), returning a NEW ascending list without mutating `values`.

Step-by-Step Explanation:
    1. Copy `result = list(values)` so the caller's list is untouched.
    2. For each slot `i` from `0` to `len(result) - 1`:
       - Assume `min_idx = i`.
       - Scan `j` from `i + 1` to `len(result) - 1` to find the smallest value.
       - Swap `result[i], result[min_idx] = result[min_idx], result[i]`.
    3. Loop invariant: after step `i`, `result[:i + 1]` holds the `i + 1`
       smallest items in final sorted order.

Edge Cases:
    - `[]` -> `[]`
    - `[42]` -> `[42]`
    - Duplicates `[3, 1, 3, 2, 1]` -> `[1, 1, 2, 3, 3]`

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem:
    Implement `solve_insertion_sort_with_swaps(values)` from scratch (no
    `sorted()` or `.sort()`):
      - Sort a COPY of `values` in ascending order using **insertion sort**.
      - Count every adjacent swap performed while bubbling `result[j]` leftward
        into its sorted position (`while j > 0 and result[j - 1] > result[j]:`).
      - Return `(sorted_list, swaps_count)`.
      - Do NOT mutate `values`!

Step-by-Step Insertion Sort Hint:
    - `result = list(values)`
    - `swaps = 0`
    - For `i` in `range(1, len(result))`:
      - `j = i`
      - `while j > 0 and result[j - 1] > result[j]:`
        - swap `result[j - 1]` and `result[j]`
        - `swaps += 1`
        - `j -= 1`
    - Return `(result, swaps)`.

Fun Fact:
    The exact number of adjacent swaps insertion sort performs ALWAYS equals
    the number of **inversions** in the input array (Activity 095)!

Examples:
    solve_insertion_sort_with_swaps([3, 2, 1])       -> ([1, 2, 3], 3)
    solve_insertion_sort_with_swaps([1, 2, 3])       -> ([1, 2, 3], 0)
    solve_insertion_sort_with_swaps([2, 4, 1, 3, 5]) -> ([1, 2, 3, 4, 5], 3)
    solve_insertion_sort_with_swaps([])              -> ([], 0)
"""

from __future__ import annotations


def example_selection_sort(values: list[int]) -> list[int]:
    """Return a new ascending sorted list using selection sort (no mutation)."""
    result = list(values)
    n = len(result)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if result[j] < result[min_idx]:
                min_idx = j
        result[i], result[min_idx] = result[min_idx], result[i]
    return result


def solve_insertion_sort_with_swaps(values: list[int]) -> tuple[list[int], int]:
    """Sort a copy of ``values`` via insertion sort; return ``(sorted_list, swaps)``."""
    pass


if __name__ == "__main__":
    raw = [64, 25, 12, 22, 11]
    print("Original:", raw)
    print("Selection sorted:", example_selection_sort(raw))
