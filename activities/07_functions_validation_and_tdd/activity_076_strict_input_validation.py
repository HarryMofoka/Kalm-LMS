"""
Activity 076 — Strict Input Validation Contracts
Difficulty: 76 / 132

Context:
    Programming assessments love testing *defensive contracts*: not only must
    your function reject bad types, the test suite often checks the EXACT
    `TypeError` message — and tries to trick you with `True` / `False`, because
    in Python `bool` is a subclass of `int` (`isinstance(True, int) == True`)!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Implement `example_count_vowels_strict(text)` that counts English vowels
    (`a, e, i, o, u`, case-insensitive) and enforces:
      - Raises `TypeError("Input must be a string.")` if `text` is not a `str`.

Step-by-Step Explanation:
    1. Validate inputs at the very top of the function (guard clause pattern).
    2. Match the required exception class (`TypeError`) and EXACT message
       character-for-character (including punctuation and capitalization).
    3. Once validated, perform the clean business logic.

Edge Cases:
    - `None`, `123`, `["a"]` -> `TypeError("Input must be a string.")`
    - `""` -> `0`
    - `"AEIOUaeiou"` -> `10`

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem A — `solve_merge_dicts(dict1, dict2)`:
    Merge two dictionaries into a NEW dictionary.
    - Validation: if either `dict1` or `dict2` is not a `dict`, raise
      `TypeError("Both inputs must be dictionaries.")`.
    - Behavior: if a key appears in both dictionaries, sum their values (`+`);
      otherwise copy the key/value into the merged dictionary.
    - Immutability: NEVER modify `dict1` or `dict2`.

Problem B — `solve_is_prime(n)`:
    Determine whether an integer `n` is a prime number.
    - Validation: if `n` is a `bool` OR not an `int`, raise
      `TypeError("Input must be an integer.")`.
      (CRITICAL: `solve_is_prime(True)` and `solve_is_prime(False)` MUST raise
      `TypeError`!)
    - Behavior: integers `< 2` are NOT prime (`False`). Check divisors up to
      `int(n ** 0.5)` (or `divisor * divisor <= n`) for speed.

Examples:
    solve_merge_dicts({"a": 2, "b": 3}, {"b": 4, "c": 5}) -> {"a": 2, "b": 7, "c": 5}
    solve_merge_dicts({"a": 1}, "not a dict")             -> raises TypeError("Both inputs must be dictionaries.")

    solve_is_prime(2)      -> True
    solve_is_prime(17)     -> True
    solve_is_prime(1)      -> False
    solve_is_prime(-7)     -> False
    solve_is_prime(True)   -> raises TypeError("Input must be an integer.")
    solve_is_prime(3.0)    -> raises TypeError("Input must be an integer.")
"""

from __future__ import annotations


def example_count_vowels_strict(text: str) -> int:
    """Count vowels in ``text``, enforcing an exact TypeError contract."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    vowels = set("aeiou")
    return sum(1 for ch in text.lower() if ch in vowels)


def solve_merge_dicts(dict1: dict, dict2: dict) -> dict:
    """Return a new merged dictionary summing values for overlapping keys.

    Raises:
        TypeError("Both inputs must be dictionaries.") if either input is not a dict.
    """
    pass


def solve_is_prime(n: int) -> bool:
    """Return True if ``n`` is a prime integer, False otherwise.

    Raises:
        TypeError("Input must be an integer.") if ``n`` is a bool or not an int.
    """
    pass


if __name__ == "__main__":
    print("Vowels in 'Programming':", example_count_vowels_strict("Programming"))
    try:
        example_count_vowels_strict(42)  # type: ignore[arg-type]
    except TypeError as exc:
        print("Caught expected TypeError:", exc)
