"""
Activity 071: Hash-Map Two-Sum & Disjoint Pairs
Difficulty: 71 / 132

Context:
    Two-Sum is arguably the single most famous hash-map problem in computer
    science. Instead of checking all $O(n^2)$ pairs with nested loops, remember
    seen values in a dict so you can check `target - num` in $O(1)$ time—then
    upgrade the dict to store index queues so you can pair up ALL disjoint matches!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Single Two-Sum Index Pair
===============================================================================
Problem:
    Given a list of integers `numbers` and an integer `target`, return a tuple
    `(i, j)` with `i < j` such that `numbers[i] + numbers[j] == target` (the
    first valid pair encountered while scanning left-to-right). Return `None`
    if no such pair exists.

Step-by-Step Explanation:
    1. Keep `seen: dict[int, int] = {}` mapping each previously visited value
       to its earliest index.
    2. For each `j, num` in `enumerate(numbers)`:
         - Compute `complement = target - num`.
         - If `complement in seen`, immediately return `(seen[complement], j)`.
         - Otherwise, store `seen.setdefault(num, j)` (keeping the earliest index).
    3. Why check `complement in seen` BEFORE inserting `num`? So an element
       NEVER pairs with itself (e.g., `numbers = [3]`, `target = 6` returns `None`)!

Edge Cases:
    - `([2, 7, 11, 15], 9)` -> `(0, 1)`
    - `([3, 3], 6)`         -> `(0, 1)`
    - `([3, 2, 4], 6)`      -> `(1, 2)`
    - `([1, 2, 3], 10)`     -> `None`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — All Disjoint Index Pairs Summing to Target
===============================================================================
Problem:
    Implement `solve_all_disjoint_pairs(numbers: list[int], target: int) -> list[tuple[int, int]]`.
    Find ALL **disjoint** index pairs `(i, j)` (`i < j`) such that
    `numbers[i] + numbers[j] == target`, where EVERY index may be used in AT MOST
    ONE pair!

    Follow this exact deterministic single-pass matching rule:
      1. Scan `numbers` left-to-right (`for j, num in enumerate(numbers):`).
      2. Maintain `waiting: dict[int, list[int]]` mapping each currently unmatched
         value to a FIFO list of its available earlier indices.
      3. Compute `need = target - num`.
         - If `waiting.get(need)` is non-empty: pop the EARLIEST available index
           `i = waiting[need].pop(0)` and append `(i, j)` to `pairs`!
         - Otherwise: append `j` to `waiting.setdefault(num, [])`.
      4. Return `pairs`.

Examples:
    - `([2, 7, 11, 15, 7, 2], 9)` -> `[(0, 1), (4, 5)]`
    - `([3, 3, 3, 3], 6)`         -> `[(0, 1), (2, 3)]`
    - `([3, 3, 3], 6)`            -> `[(0, 1)]`         (index 2 left unpaired!)
    - `([1, 5, 1, 5], 6)`         -> `[(0, 1), (2, 3)]`
    - `([1, 1, 5, 5], 6)`         -> `[(0, 2), (1, 3)]` (FIFO pops index 0, then 1!)
    - `([1, 2, 3], 10)`           -> `[]`
    - `([], 5)`                   -> `[]`

Edge-Case Hints:
    - Notice how `waiting[need]` being a LIST of indices naturally handles
      multiple identical values (like `[1, 1, 5, 5]` and `[3, 3, 3, 3]`) without
      overwriting earlier indices or reusing a consumed index!
"""

from __future__ import annotations


def example_two_sum(numbers: list[int], target: int) -> tuple[int, int] | None:
    """Return `(i, j)` (`i < j`) with `numbers[i] + numbers[j] == target`, or None."""
    seen: dict[int, int] = {}
    for j, num in enumerate(numbers):
        complement = target - num
        if complement in seen:
            return (seen[complement], j)
        seen.setdefault(num, j)
    return None


def solve_all_disjoint_pairs(
    numbers: list[int],
    target: int,
) -> list[tuple[int, int]]:
    """Return all disjoint `(i, j)` index pairs (`i < j`) summing to `target`."""
    pass


if __name__ == "__main__":
    print("Two-sum [2, 7, 11, 15], 9 ->", example_two_sum([2, 7, 11, 15], 9))
    print("Two-sum [3, 2, 4], 6      ->", example_two_sum([3, 2, 4], 6))
