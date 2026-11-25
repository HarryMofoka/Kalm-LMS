"""
Activity 039: Filtering Characters
Difficulty: 39 / 132

Context:
    User input is messy: phone numbers have dashes, license plates have spaces,
    and usernames contain stray symbols. Because Python strings are immutable,
    filtering characters means building a new string from the characters you keep.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Remove English Vowels
===============================================================================
Problem:
    Given a string `text`, return a new string with all English vowels
    (`a, e, i, o, u`, both lowercase and uppercase) removed. Preserve all other
    characters (consonants, spaces, digits, punctuation) in their original order.

Step-by-Step Explanation:
    1. Define a constant string (or set) of vowels: `"aeiouAEIOU"`.
    2. Collect kept characters in a list (or generator expression) and join them
       once with `"".join(...)`.
    3. Why `"".join(...)` instead of `result += ch` inside a loop? Repeated string
       concatenation copies the string over and over ($O(n^2)$), whereas joining
       a list runs in linear $O(n)$ time.

Edge Cases:
    - `"Hello, World!"` -> `"Hll, Wrld!"`
    - `"AEIOU"`         -> `""`
    - `"123!@#"`        -> `"123!@#"`
    - `""`              -> `""`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Keep Only Alphanumeric Characters
===============================================================================
Problem:
    Implement `solve_keep_alphanumeric(text: str) -> str`.
    Return a new string keeping ONLY letters and digits (`ch.isalnum()`) from
    `text`, preserving their exact original order and case. Strip out all spaces,
    punctuation, underscores, and symbols.

Examples:
    - `"Hello, World! 2026"` -> `"HelloWorld2026"`
    - `"user_name-01@mail"`  -> `"username01mail"`
    - `"!!!   ---"`          -> `""`
    - `"Python3"`            -> `"Python3"`
    - `""`                   -> `""`

Edge-Case Hints:
    - Remember that `"_".isalnum()` is `False` (underscores are NOT alphanumeric).
    - Do not lowercase or uppercase the kept characters; keep original case intact.
"""

from __future__ import annotations


def example_remove_vowels(text: str) -> str:
    """Return a copy of `text` with all English vowels removed."""
    vowels = set("aeiouAEIOU")
    kept = [ch for ch in text if ch not in vowels]
    return "".join(kept)


def solve_keep_alphanumeric(text: str) -> str:
    """Return a copy of `text` containing only alphanumeric characters."""
    pass


if __name__ == "__main__":
    for sample in ["Hello, World!", "AEIOUaeiou", "Exam Prep 2026"]:
        print(f"{sample!r:18} -> {example_remove_vowels(sample)!r}")
