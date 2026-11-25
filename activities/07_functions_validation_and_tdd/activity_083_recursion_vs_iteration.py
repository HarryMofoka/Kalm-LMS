"""
Activity 083 — Recursion vs Iteration (Explicit Stack)
Difficulty: 83 / 132

Context:
    Python limits call-stack depth to ~1000 frames (`sys.getrecursionlimit()`).
    Recursion shines on clean tree/nested structures of modest depth, while an
    **explicit stack** (a plain Python `list` using `.append()` and `.pop()`)
    solves the exact same nested problems iteratively — without ever risking
    `RecursionError` even on 5,000-level deep structures!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Implement `example_flatten_recursive(nested)` that takes an arbitrarily
    deeply nested list and returns a single flat list preserving left-to-right
    order, without mutating `nested`.

Step-by-Step Explanation:
    1. Start with `flat: list = []`.
    2. Loop over each `item` in `nested`:
       - If `isinstance(item, list)`: recursively flatten `item` and `.extend()`
         onto `flat`.
       - Otherwise: `.append(item)` directly.
    3. Return `flat`.

Edge Cases:
    - `[]` -> `[]`
    - `[[], [[], []]]` -> `[]`
    - `[1, [2, [3, 4]], 5]` -> `[1, 2, 3, 4, 5]`
    - Non-list containers (like strings `"hi"` or tuples `(1, 2)`) are kept as
      atomic elements because we check `isinstance(item, list)`.

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem:
    Implement `solve_nested_sum_iterative(structure)` that computes the total
    sum of all numbers (`int` or `float`) stored anywhere inside an arbitrarily
    nested list structure — using an **explicit stack** (NO recursion!).

Rules:
    1. Use a `while stack:` loop (do NOT call `solve_nested_sum_iterative`
       recursively, because tests will pass a 1,500-level deeply nested list!).
    2. If an popped item is a `list`, push its elements onto `stack`.
    3. If a popped item is an `int` or `float` (and NOT a `bool`), add it to
       `total`.
    4. Do NOT mutate `structure` or any sublists inside it!
    5. Empty structures like `[]` or `[[], [[]]]` return `0`.

Examples:
    solve_nested_sum_iterative([1, [2, [3, 4]], 5])     -> 15
    solve_nested_sum_iterative([[], [[10], [-2, 0.5]]]) -> 8.5
    solve_nested_sum_iterative([[], [[]]])              -> 0

Edge-Case Hints:
    - Initialize `stack = [structure]` (or `list(structure)` — a shallow copy so
      popping from `stack` never mutates `structure`!).
    - Because addition is commutative, order of popping doesn't even change the
      total!
"""

from __future__ import annotations

from typing import Any


def example_flatten_recursive(nested: list[Any]) -> list[Any]:
    """Recursively flatten arbitrarily nested lists without mutating input."""
    flat: list[Any] = []
    for item in nested:
        if isinstance(item, list):
            flat.extend(example_flatten_recursive(item))
        else:
            flat.append(item)
    return flat


def solve_nested_sum_iterative(structure: list[Any]) -> int | float:
    """Iteratively sum all numbers in arbitrarily nested lists using a stack."""
    pass


if __name__ == "__main__":
    tree = [1, [2, [3, 4], []], 5, [[6]]]
    print("Original:", tree)
    print("Flattened:", example_flatten_recursive(tree))
