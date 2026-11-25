"""
Activity 053: List Slicing & Rotation
Difficulty: 53 / 132

Context:
    Circular buffers, turn-order queues, and shift registers all rotate lists
    cyclically. Slicing plus modulo arithmetic (`k % len(items)`) turns a tricky
    index-shifting problem into a crisp 3-line solution.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Rotate Left by 1
===============================================================================
Problem:
    Return a NEW list rotated LEFT by 1 position (the first element wraps around
    to the end). Return `[]` if `items` is empty. Do NOT mutate `items`.

Step-by-Step Explanation:
    1. Guard `if not items: return []` (and for 1-element lists, `items[1:] + items[:1]`
       also safely produces a shallow copy `[items[0]]`).
    2. `items[1:]` takes everything from index 1 to the end; `items[:1]` takes a
       1-element slice with the first item.
    3. Concatenating `items[1:] + items[:1]` builds a brand-new list without
       touching the original.

Edge Cases:
    - `[1, 2, 3, 4]` -> `[2, 3, 4, 1]`
    - `[99]`         -> `[99]`
    - `[]`           -> `[]`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Rotate Right by `k` Positions
===============================================================================
Problem:
    Implement `solve_rotate_right(items: list[Any], k: int) -> list[Any]`.
    Return a NEW list rotated RIGHT by `k` positions—moving the last `k` items
    to the front—without mutating `items`.
      - Handle `k == 0`, `k == len(items)`, and `k > len(items)` (wrap around!).
      - Handle negative `k` cleanly too (rotating right by `-1` is the same as
        rotating left by `1`, which `k % len(items)` handles naturally!).
      - Return `[]` if `items` is empty.

Examples:
    - `([1, 2, 3, 4, 5], 2)` -> `[4, 5, 1, 2, 3]`
    - `([1, 2, 3, 4, 5], 7)` -> `[4, 5, 1, 2, 3]`  (`7 % 5 == 2`)
    - `([1, 2, 3], 0)`       -> `[1, 2, 3]`        (must still be a NEW list!)
    - `([1, 2, 3], 3)`       -> `[1, 2, 3]`
    - `([1, 2, 3, 4], -1)`   -> `[2, 3, 4, 1]`
    - `([], 5)`              -> `[]`

Edge-Case Hints:
    - Check `if not items: return []` BEFORE computing `k % len(items)` to avoid
      `ZeroDivisionError`!
    - WATCH OUT for `shift = k % len(items) == 0`: in Python, `items[-0:]` is
      `items[0:]` (the whole list!), so `items[-0:] + items[:-0]` would be
      `items + []`—wait: `items[:-0]` is `items[:0]` which IS `[]`! Even clearer:
      compute `split = len(items) - shift`, then `items[split:] + items[:split]`!
      Check `shift = 0`: `split = n`, `items[n:] + items[:n] == [] + copy(items)`!
"""

from __future__ import annotations

from typing import Any


def example_rotate_left(items: list[Any]) -> list[Any]:
    """Return a new list rotated left by 1 position without mutating `items`."""
    if not items:
        return []
    return items[1:] + items[:1]


def solve_rotate_right(items: list[Any], k: int) -> list[Any]:
    """Return a new list rotated right by `k` positions (handles `k > len`)."""
    pass


if __name__ == "__main__":
    nums = [10, 20, 30, 40]
    print("Original    :", nums)
    print("Rotated left:", example_rotate_left(nums))
