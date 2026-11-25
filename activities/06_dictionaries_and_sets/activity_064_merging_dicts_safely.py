"""
Activity 064: Merging Dictionaries Safely
Difficulty: 64 / 132

Context:
    Configuration loaders merge defaults with user overrides, while analytics
    aggregators combine daily count maps by summing overlapping keys. In both
    cases, mutating the caller's input dictionaries causes nasty side-effect bugs!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Non-Mutating Override Merge
===============================================================================
Problem:
    Return a NEW dictionary containing all entries from `base` and `updates`.
    When a key appears in both, the value from `updates` wins. Neither `base`
    nor `updates` may be mutated.

Step-by-Step Explanation:
    1. Start with a shallow copy of `base`: `merged = dict(base)`.
    2. Call `merged.update(updates)` (or equivalently `{**base, **updates}` /
       `base | updates` on Python 3.9+).
    3. Both input dictionaries stay completely unchanged!

Edge Cases:
    - `({"a": 1, "b": 2}, {"b": 99, "c": 3})` -> `{"a": 1, "b": 99, "c": 3}`
    - `({}, {"x": 10})`                       -> `{"x": 10}`
    - `({}, {})`                              -> `{}`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Sum-Merge Dictionaries Without Mutating Inputs
===============================================================================
Problem:
    Implement `solve_sum_merge_dicts(first: dict[str, int | float], second: dict[str, int | float]) -> dict[str, int | float]`.
    Return a NEW dictionary combining `first` and `second` such that:
      - Keys present in ONLY `first` or ONLY `second` keep their value.
      - Keys present in BOTH `first` and `second` have their values SUMMED
        (`first[k] + second[k]`).
      - Keep a key even if its summed value equals `0`!
      - Do NOT mutate `first` or `second`.

Examples:
    - `({"a": 2, "b": 3}, {"b": 4, "c": 5})` -> `{"a": 2, "b": 7, "c": 5}`
    - `({"x": 10}, {"x": -10})`              -> `{"x": 0}`
    - `({"a": 1}, {})`                       -> `{"a": 1}`
    - `({}, {"b": 2})`                       -> `{"b": 2}`
    - `({}, {})`                             -> `{}`

Edge-Case Hints:
    - Copy `merged = dict(first)` first, then loop `for key, val in second.items():`
      and set `merged[key] = merged.get(key, 0) + val`!
    - Remember: `merged = first` does NOT copy—it creates an alias that mutates
      `first`! Always copy with `dict(first)` or `first.copy()`.
"""

from __future__ import annotations

from typing import Any


def example_override_merge(
    base: dict[Any, Any],
    updates: dict[Any, Any],
) -> dict[Any, Any]:
    """Merge `base` and `updates` (updates win) into a new dict without mutating inputs."""
    merged = dict(base)
    merged.update(updates)
    return merged


def solve_sum_merge_dicts(
    first: dict[str, int | float],
    second: dict[str, int | float],
) -> dict[str, int | float]:
    """Merge two numeric dicts by summing overlapping keys without mutating inputs."""
    pass


if __name__ == "__main__":
    defaults = {"theme": "light", "font_size": 12}
    prefs = {"theme": "dark", "tab_width": 4}
    print("Merged  :", example_override_merge(defaults, prefs))
    print("Defaults:", defaults)
