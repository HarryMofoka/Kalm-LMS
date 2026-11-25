"""
Activity 085 — Linear Search & Sentinel Scanning
Difficulty: 85 / 132

Context:
    You are scanning server event logs to find when a specific error code
    occurred. Python's built-in `list.index()` stops at the first match and
    crashes with `ValueError` when the target is missing! Writing your own
    linear scan with `enumerate()` and a sentinel (`-1`) gives you full control.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Implement `example_first_and_last_index(items, target)` that makes a SINGLE
    pass over `items` and returns `(first_index, last_index)` of `target`, or
    `(-1, -1)` if `target` does not appear.

Step-by-Step Explanation:
    1. Initialize sentinel values `first = -1` and `last = -1`.
    2. Loop with `for index, value in enumerate(items):`
       - When `value == target`:
         - If `first == -1`, record `first = index` (only set once!).
         - Always update `last = index` (tracks the latest match seen).
    3. Return `(first, last)`.
    4. Time complexity: O(n) single pass; space complexity: O(1).

Edge Cases:
    - Target absent -> `(-1, -1)`
    - Empty list `[]` -> `(-1, -1)`
    - Single match at index 3 -> `(3, 3)`
    - All elements match `[7, 7, 7]` -> `(0, 2)`

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem:
    Implement `solve_find_all_indices(items, target)` that returns a list of
    ALL indices (in ascending order) where `items[i] == target`.

Rules:
    1. Return an empty list `[]` if `target` is not present or `items` is empty.
    2. Do NOT mutate `items`.
    3. Single O(n) pass using `enumerate()`.

Examples:
    solve_find_all_indices([4, 2, 4, 9, 4], 4)     -> [0, 2, 4]
    solve_find_all_indices(["a", "b", "c"], "z")   -> []
    solve_find_all_indices([], 10)                 -> []
    solve_find_all_indices([5], 5)                 -> [0]
"""

from __future__ import annotations

from typing import Any


def example_first_and_last_index(items: list[Any], target: Any) -> tuple[int, int]:
    """Return ``(first_idx, last_idx)`` of ``target`` in ``items``, or ``(-1, -1)``."""
    first = -1
    last = -1
    for index, value in enumerate(items):
        if value == target:
            if first == -1:
                first = index
            last = index
    return (first, last)


def solve_find_all_indices(items: list[Any], target: Any) -> list[int]:
    """Return all ascending indices where ``items[i] == target``."""
    pass


if __name__ == "__main__":
    logs = ["OK", "ERR", "OK", "WARN", "ERR", "OK"]
    print("First & last 'ERR':", example_first_and_last_index(logs, "ERR"))
    print("First & last 'FATAL':", example_first_and_last_index(logs, "FATAL"))
