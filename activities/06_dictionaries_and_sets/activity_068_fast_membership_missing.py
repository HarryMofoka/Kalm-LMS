"""
Activity 068: Fast Membership & Missing Numbers
Difficulty: 68 / 132

Context:
    Checking `x in a_list` scans linearly ($O(n)$), which turns an outer loop
    into a sluggish $O(n^2)$ algorithm. Checking `x in a_set` runs in $O(1)$
    average time—letting you find missing IDs or duplicate records across
    millions of entries effortlessly.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Find Missing Number in `1..n`
===============================================================================
Problem:
    Given a list `numbers` of integers from `1..n` and the upper bound `n`,
    return the smallest missing integer in `1..n`, or `None` if every integer
    from `1` through `n` is present.

Step-by-Step Explanation:
    1. Convert `numbers` to a set `present = set(numbers)` once in $O(n)$ time.
    2. Loop `for candidate in range(1, n + 1):` and check `if candidate not in present:`
       ($O(1)$ per lookup!).
    3. Return the first missing `candidate`, or `None` if all are present.

Edge Cases:
    - `([3, 1, 4], 4)`       -> `2`
    - `([1, 2, 3], 3)`       -> `None`
    - `([], 1)`              -> `1`
    - `([], 0)`              -> `None`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Find All Duplicates Preserving First-Dup Order
===============================================================================
Problem:
    Implement `solve_find_duplicates_in_order(items: list[Any]) -> list[Any]`.
    Return a list of every item that appears MORE THAN ONCE in `items`:
      - Include each duplicate item AT MOST ONCE in the returned list.
      - Preserve **first-duplicate order**: order items by the index where they
        are seen for the SECOND time (the moment they first become a duplicate)!
      - Return `[]` if there are no duplicates. Do NOT mutate `items`.

Walkthrough Example:
    Consider `items = ["a", "b", "c", "b", "a", "b"]`:
      - idx 0: `"a"` -> first time seen (`seen = {"a"}`)
      - idx 1: `"b"` -> first time seen (`seen = {"a", "b"}`)
      - idx 2: `"c"` -> first time seen (`seen = {"a", "b", "c"}`)
      - idx 3: `"b"` -> SECOND time seen -> record `"b"` first! (`result = ["b"]`)
      - idx 4: `"a"` -> SECOND time seen -> record `"a"` next! (`result = ["b", "a"]`)
      - idx 5: `"b"` -> already recorded as duplicate -> skip!
    Final answer: `["b", "a"]`.

Examples:
    - `["a", "b", "c", "b", "a", "b"]` -> `["b", "a"]`
    - `[1, 2, 3, 2, 1, 4, 4, 2]`       -> `[2, 1, 4]`
    - `[1, 2, 3, 4]`                   -> `[]`
    - `[5, 5, 5, 5]`                   -> `[5]`
    - `[]`                             -> `[]`

Edge-Case Hints:
    - Maintain TWO sets—`seen` and `recorded`—plus your `result` list:
        * If `item in seen` and `item not in recorded`:
            add `item` to `recorded` and append `item` to `result`!
        * Else:
            add `item` to `seen`.
    - Total runtime is $O(n)$!
"""

from __future__ import annotations

from typing import Any


def example_find_missing_number(numbers: list[int], n: int) -> int | None:
    """Return the smallest missing integer in `1..n` using O(1) set membership."""
    present = set(numbers)
    for candidate in range(1, n + 1):
        if candidate not in present:
            return candidate
    return None


def solve_find_duplicates_in_order(items: list[Any]) -> list[Any]:
    """Return all duplicate elements once each, ordered by their first duplicate occurrence."""
    pass


if __name__ == "__main__":
    print("Missing in [3, 1, 4] (n=4):", example_find_missing_number([3, 1, 4], 4))
    print("Missing in [1, 2, 3] (n=3):", example_find_missing_number([1, 2, 3], 3))
