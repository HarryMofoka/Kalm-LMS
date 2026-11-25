"""
Activity 077 — List-of-Strings Validation & Immutability
Difficulty: 77 / 132

Context:
    Validating a container is only half the battle — you also have to validate
    the *elements inside* the container! And once you process the container,
    callers expect their original list to stay untouched (never calling
    `.sort()` directly on an input parameter).

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Implement `example_validate_int_list(values)` that:
      1. Raises `TypeError("Input must be a list of integers.")` if `values` is
         not a `list` OR if any element is not a strict `int` (reject `bool`!).
      2. Returns a NEW list containing the integers sorted ascending.
      3. Never mutates `values`.

Step-by-Step Explanation:
    1. Check `isinstance(values, list)` first. If `values` is a tuple, string,
       or `None`, short-circuiting `or` avoids iterating over a non-iterable!
    2. Check every element with `isinstance(item, int) and not isinstance(item, bool)`.
    3. Use `sorted(values)` — unlike `values.sort()`, `sorted()` always creates
       and returns a fresh list object!

Edge Cases:
    - Empty list `[]` -> returns a NEW `[]` (`result is not original`!).
    - Tuple `(1, 2)` -> `TypeError` (must be a `list`, not a tuple).
    - `[1, True, 3]` -> `TypeError` (`bool` is rejected!).

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem:
    Implement `solve_sorted_strings_copy(words, reverse=False)` that validates
    a list of strings and returns a NEW sorted copy without mutating `words`.

Rules:
    1. If `words` is not a `list`, OR if any element inside `words` is not a
       `str`, raise `TypeError("Input must be a list of strings.")`.
    2. Return a NEW list sorted lexicographically (ascending by default, or
       descending when `reverse=True`).
    3. Do NOT mutate `words`, and always return a distinct list object even
       when `words` is empty or already sorted (`result is not words`).

Examples:
    data = ["pear", "apple", "banana"]
    solve_sorted_strings_copy(data)                -> ["apple", "banana", "pear"]
    solve_sorted_strings_copy(data, reverse=True)  -> ["pear", "banana", "apple"]
    # `data` is still ["pear", "apple", "banana"]!

    solve_sorted_strings_copy("hello")             -> raises TypeError("Input must be a list of strings.")
    solve_sorted_strings_copy(["ok", 99])          -> raises TypeError("Input must be a list of strings.")
"""

from __future__ import annotations


def example_validate_int_list(values: list[int]) -> list[int]:
    """Validate a list of strict ints and return a new ascending sorted copy."""
    if not isinstance(values, list) or not all(
        isinstance(item, int) and not isinstance(item, bool)
        for item in values
    ):
        raise TypeError("Input must be a list of integers.")
    return sorted(values)


def solve_sorted_strings_copy(
    words: list[str],
    reverse: bool = False,
) -> list[str]:
    """Validate a list of strings and return a new sorted copy.

    Raises:
        TypeError("Input must be a list of strings.") if ``words`` is not a list
        or contains any non-string element.
    """
    pass


if __name__ == "__main__":
    nums = [5, 2, 9, 1]
    result = example_validate_int_list(nums)
    print("Original:", nums)
    print("Sorted copy:", result)
    print("Distinct list objects?", result is not nums)
