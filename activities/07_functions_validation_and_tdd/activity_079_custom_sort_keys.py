"""
Activity 079 — Custom Sort Keys with `key=`
Difficulty: 79 / 132

Context:
    Default Python sorting compares items directly (alphabetically for strings,
    numerically for numbers, element-by-element for tuples). Real applications
    almost always need a custom ordering — like sorting tuples by their second
    value or sorting words shortest-first — without rewriting a sorting algorithm.
    Python's `sorted(iterable, key=...)` does this cleanly in one line!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Implement `example_sort_by_second(pairs)` that takes a list of
    `(label, value)` tuples and returns a NEW list sorted by `value` ascending,
    breaking ties by `label` ascending — without mutating `pairs`.

Step-by-Step Explanation:
    1. Pass `key=lambda item: (item[1], item[0])` to `sorted(pairs, ...)`.
    2. Returning a *tuple* from the key function handles primary AND secondary
       tie-breaking automatically!
    3. `sorted()` always allocates and returns a new list, preserving `pairs`.

Edge Cases:
    - Empty list `[]` -> `[]`
    - Tied values `[("beta", 2), ("alpha", 2)]` -> `[("alpha", 2), ("beta", 2)]`
    - Original list remains completely unchanged.

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem:
    Implement `solve_sort_words_by_length(words)` (a classic exam question!):
    Sort a list of strings by LENGTH ascending first, and break ties
    lexicographically (alphabetically) ascending.

Rules:
    1. Validate first: if `words` is not a `list` OR contains any element that
       is not a `str`, raise `TypeError("Input must be a list of strings.")`.
    2. Return a NEW list sorted by `(len(word), word)`.
    3. Do NOT mutate `words`.

Examples:
    solve_sort_words_by_length(["banana", "fig", "apple", "bat", "ant"])
        -> ["ant", "bat", "fig", "apple", "banana"]

    solve_sort_words_by_length(["b", "a", ""])
        -> ["", "a", "b"]

    solve_sort_words_by_length(("a", "b"))
        -> raises TypeError("Input must be a list of strings.")

Edge-Case Hints:
    - Uppercase letters sort before lowercase letters in standard Python
      lexicographical order (`"Apple" < "apple"`), which matches `(len(w), w)`.
"""

from __future__ import annotations


def example_sort_by_second(
    pairs: list[tuple[str, int]],
) -> list[tuple[str, int]]:
    """Return a new list of (label, value) tuples sorted by value, then label."""
    return sorted(pairs, key=lambda item: (item[1], item[0]))


def solve_sort_words_by_length(words: list[str]) -> list[str]:
    """Validate and return a new list of strings sorted by (len(w), w).

    Raises:
        TypeError("Input must be a list of strings.") if ``words`` is invalid.
    """
    pass


if __name__ == "__main__":
    scores = [("charlie", 10), ("alice", 5), ("bob", 10), ("dana", 2)]
    print("Original:", scores)
    print("Sorted by 2nd item:", example_sort_by_second(scores))
