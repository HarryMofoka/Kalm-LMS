"""
Activity 052: Deduplication Preserving Order
Difficulty: 52 / 132

Context:
    A classic exam trap: someone tries `list(set(items))` to remove duplicates
    and loses the original element order! Another common task—especially in
    event streams and sensor logs—is collapsing only CONSECUTIVE repeats while
    keeping later reappearances.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Unique Elements Preserving Order
===============================================================================
Problem:
    Return a NEW list containing each distinct element of `items` at most once,
    preserving the order of FIRST appearance. Do NOT mutate `items`.

Step-by-Step Explanation:
    1. Keep a `seen` set for $O(1)$ membership checks and a `result` list to
       preserve exact insertion order.
    2. For each `item` in `items`: if `item not in seen`, add `item` to `seen`
       AND append `item` to `result`.
    3. This runs in $O(n)$ time (much faster than checking `if item not in result`,
       which is $O(n^2)$!) and never alters the input list.

Edge Cases:
    - `[3, 1, 2, 1, 3, 4]` -> `[3, 1, 2, 4]`
    - `["b", "a", "b"]`    -> `["b", "a"]`
    - `[]`                 -> `[]`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Remove Consecutive Duplicates (Run Dedup)
===============================================================================
Problem:
    Implement `solve_remove_consecutive_dups(items: list[Any]) -> list[Any]`.
    Return a NEW list where any run of consecutive equal elements is collapsed
    to a single element. Non-adjacent duplicates MUST be preserved!
    Do NOT mutate `items`.

Examples:
    - `[1, 1, 2, 2, 2, 3, 1, 1]` -> `[1, 2, 3, 1]`
    - `["a", "a", "b", "a"]`     -> `["a", "b", "a"]`
    - `[None, None, 1, 1, None]` -> `[None, 1, None]`
    - `[5]`                      -> `[5]`
    - `[]`                       -> `[]`

Edge-Case Hints:
    - WATCH OUT for initializing `prev = None`! If the list starts with `None`
      (like `[None, None, 1]`), comparing `item != prev` would accidentally drop
      the very first `None`!
    - Instead, check `if not result or item != result[-1]: result.append(item)`!
      That handles `None`, booleans, strings, and empty lists cleanly!
"""

from __future__ import annotations

from typing import Any


def example_unique_preserve_order(items: list[Any]) -> list[Any]:
    """Return a new list with duplicates removed, preserving first-seen order."""
    seen: set[Any] = set()
    result: list[Any] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def solve_remove_consecutive_dups(items: list[Any]) -> list[Any]:
    """Return a new list with only consecutive duplicate elements collapsed."""
    pass


if __name__ == "__main__":
    data = [3, 1, 2, 1, 3, 4, 2]
    print("Input :", data)
    print("Unique:", example_unique_preserve_order(data))
