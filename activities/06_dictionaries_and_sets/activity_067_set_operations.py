"""
Activity 067: Set Operations
Difficulty: 67 / 132

Context:
    Comparing two rosters, finding tags unique to one article, or syncing two
    folders takes messy nested loops with lists—and a single expressive operator
    (`&`, `|`, `-`, `^`) with Python sets!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Common Elements in Two Lists
===============================================================================
Problem:
    Given two lists `first` and `second` of comparable items, return a SORTED
    list of the unique elements that appear in BOTH lists.

Step-by-Step Explanation:
    1. Convert both lists to sets and take their intersection:
       `common = set(first) & set(second)`.
    2. Sort the result into a list with `sorted(common)` so the output order is
       deterministic (remember: sets have NO guaranteed ordering!).
    3. Duplicates inside either list are automatically deduplicated.

Edge Cases:
    - `([3, 1, 2, 2], [2, 3, 4])` -> `[2, 3]`
    - `([1, 2], [3, 4])`          -> `[]`
    - `([], [1, 2])`              -> `[]`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Sorted Symmetric Difference (Unique to Each)
===============================================================================
Problem:
    Implement `solve_symmetric_difference_sorted(first: list[Any], second: list[Any]) -> list[Any]`.
    Return a SORTED list of all unique elements that appear in EITHER `first`
    OR `second`, but NOT in BOTH (their symmetric difference).

Examples:
    - `([1, 2, 2, 3], [2, 3, 4, 4])` -> `[1, 4]`
    - `(["a", "b"], ["b", "c"])`     -> `["a", "c"]`
    - `([1, 2], [1, 2])`             -> `[]`
    - `([], [3, 1, 2])`              -> `[1, 2, 3]`
    - `([], [])`                     -> `[]`

Edge-Case Hints:
    - Python's symmetric difference operator is `^` (or `.symmetric_difference()`):
      `set(first) ^ set(second)` equals `(set(first) - set(second)) | (set(second) - set(first))`.
    - Wrap the set in `sorted(...)` to return a sorted `list`!
"""

from __future__ import annotations

from typing import Any


def example_common_elements(first: list[Any], second: list[Any]) -> list[Any]:
    """Return a sorted list of unique elements present in both `first` and `second`."""
    return sorted(set(first) & set(second))


def solve_symmetric_difference_sorted(first: list[Any], second: list[Any]) -> list[Any]:
    """Return a sorted list of unique elements present in `first` or `second`, not both."""
    pass


if __name__ == "__main__":
    a = [3, 1, 2, 2, 5]
    b = [2, 3, 4, 5]
    print("Common elements:", example_common_elements(a, b))
