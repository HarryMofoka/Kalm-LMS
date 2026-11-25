"""
Activity 081 — Higher-Order Functions (`map` / `group_by`)
Difficulty: 81 / 132

Context:
    In Python, functions are first-class values: you can pass a function as an
    argument into another function! A function that accepts (or returns) another
    function is called a *higher-order function*. Passing behavior via `key_fn`
    or `transform_fn` eliminates repetitive loops across your codebase.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Implement `example_apply_transform(items, transform_fn)` that applies
    `transform_fn(item)` to every element of `items` and returns a new list of
    results. If `transform_fn` is not callable, raise
    `TypeError("transform_fn must be callable.")`.

Step-by-Step Explanation:
    1. Validate `if not callable(transform_fn): raise TypeError(...)`.
    2. Build and return `[transform_fn(item) for item in items]`.
    3. Never mutate `items`. Works with built-in functions (`str.upper`, `abs`),
       `def` functions, or `lambda` expressions!

Edge Cases:
    - Empty list `[]` -> `[]` (still validates `callable(transform_fn)` first!)
    - Non-callable `transform_fn` (like `42` or `None`) -> `TypeError`.

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem:
    Implement `solve_group_by(items, key_fn)` that groups elements from `items`
    into a dictionary keyed by `key_fn(item)`.

Rules:
    1. First, validate `callable(key_fn)`. If not callable, raise
       `TypeError("key_fn must be callable.")`.
    2. For each `item` in `items`, compute `group_key = key_fn(item)` and
       append `item` to `groups[group_key]`.
    3. Preserve BOTH the order in which keys are first seen AND the relative
       order of items within each group.
    4. Do NOT mutate `items`. Empty `items` -> `{}`.

Examples:
    solve_group_by(["ant", "bear", "cat", "dog", "elephant"], len)
        -> {3: ["ant", "cat", "dog"], 4: ["bear"], 8: ["elephant"]}

    solve_group_by([1, 2, 3, 4, 5], lambda n: "even" if n % 2 == 0 else "odd")
        -> {"odd": [1, 3, 5], "even": [2, 4]}

    solve_group_by([], len)
        -> {}

    solve_group_by([1, 2], "not_a_func")
        -> raises TypeError("key_fn must be callable.")
"""

from __future__ import annotations

from typing import Any, Callable


def example_apply_transform(
    items: list[Any],
    transform_fn: Callable[[Any], Any],
) -> list[Any]:
    """Apply ``transform_fn`` to every item in ``items`` and return a new list."""
    if not callable(transform_fn):
        raise TypeError("transform_fn must be callable.")
    return [transform_fn(item) for item in items]


def solve_group_by(
    items: list[Any],
    key_fn: Callable[[Any], Any],
) -> dict[Any, list[Any]]:
    """Group ``items`` into a dictionary mapping ``key_fn(item)`` to lists.

    Raises:
        TypeError("key_fn must be callable.") if ``key_fn`` is not callable.
    """
    pass


if __name__ == "__main__":
    print("Squares:", example_apply_transform([1, 2, 3, 4], lambda x: x * x))
    print("Upper:", example_apply_transform(["hi", "python"], str.upper))
