"""
Activity 065: Inverting & Filtering Dictionaries
Difficulty: 65 / 132

Context:
    When you flip a dictionary (`value -> key`), naive `{v: k for k, v in d.items()}`
    SILENTLY OVERWRITES keys whenever two keys share the same value! Real-world
    code (like grouping students by letter grade) collects equal-value keys into
    a list so zero data is lost.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Filter Entries Above Threshold
===============================================================================
Problem:
    Given a dictionary `scores` mapping names to numbers and a numeric
    `threshold`, return a NEW dictionary keeping only entries where
    `value > threshold` (strictly greater). Do NOT mutate `scores`.

Step-by-Step Explanation:
    1. Use a dict comprehension with an `if` filter:
       `{k: v for k, v in scores.items() if v > threshold}`.
    2. Preserves the original key insertion order and leaves `scores` intact.
    3. Entries equal to `threshold` are excluded because the rule is strictly `>`.

Edge Cases:
    - `({"ada": 95, "bo": 70, "cal": 85}, 70)` -> `{"ada": 95, "cal": 85}`
    - `({"a": 1, "b": 2}, 10)`                 -> `{}`
    - `({}, 0)`                                -> `{}`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Invert Dictionary Grouping Duplicate Values
===============================================================================
Problem:
    Implement `solve_invert_dict_grouped(mapping: dict[str, Any]) -> dict[Any, list[str]]`.
    Invert `mapping` so that each unique value becomes a key in the returned
    dictionary, mapped to a list of ALL original keys that had that value—
    preserving the order in which those keys appeared in `mapping`!
    Do NOT mutate `mapping`.

Examples:
    - `{"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}`
      -> `{1: ["a", "c"], 2: ["b", "e"], 3: ["d"]}`
    - `{"ada": "A", "bob": "B", "cal": "A"}`
      -> `{"A": ["ada", "cal"], "B": ["bob"]}`
    - `{"only": 42}`
      -> `{42: ["only"]}`
    - `{}`
      -> `{}`

Edge-Case Hints:
    - Use `inverted.setdefault(value, []).append(key)` (or `if value not in inverted: inverted[value] = []` followed by `.append(key)`).
    - Because Python 3.7+ preserves dictionary insertion order, iterating
      `for key, value in mapping.items():` guarantees both key order inside each
      list AND first-seen value order in the resulting dict!
"""

from __future__ import annotations

from typing import Any


def example_filter_above_threshold(
    scores: dict[str, int | float],
    threshold: int | float,
) -> dict[str, int | float]:
    """Return a new dict keeping only entries with `value > threshold`."""
    return {name: score for name, score in scores.items() if score > threshold}


def solve_invert_dict_grouped(mapping: dict[str, Any]) -> dict[Any, list[str]]:
    """Invert `mapping`, grouping keys that share equal values into lists."""
    pass


if __name__ == "__main__":
    grades = {"ada": 95, "bo": 70, "cal": 85, "dee": 60}
    print("Above 70:", example_filter_above_threshold(grades, 70))
