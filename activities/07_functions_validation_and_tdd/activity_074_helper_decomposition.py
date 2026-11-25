"""
Activity 074 — Helper Decomposition
Difficulty: 74 / 132

Context:
    You are building a readability analyzer for an online newspaper editor.
    Cramming character checking, cleaning, and statistics into one giant loop
    makes bugs hard to spot. Breaking a problem into small, single-purpose
    helpers makes each piece trivial to read, test, and reuse.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Compute the *vowel density* of a sentence: the fraction of alphabetic
    characters that are vowels (`a, e, i, o, u`, case-insensitive), rounded to
    4 decimal places. If there are no alphabetic characters, return `0.0`.

Step-by-Step Explanation:
    1. Extract a focused helper `_is_vowel(ch: str) -> bool` that checks if a
       single character is in `"aeiouAEIOU"` (and has length 1).
    2. In `example_vowel_density(sentence)`:
       - Keep only alphabetic characters (`letters = [ch for ch in sentence if ch.isalpha()]`).
       - Guard against division by zero: if `not letters`, return `0.0`.
       - Count vowels using our helper: `vowel_count = sum(1 for ch in letters if _is_vowel(ch))`.
       - Return `round(vowel_count / len(letters), 4)`.

Edge Cases:
    - Empty string `""` -> `0.0`
    - Digits/punctuation only `"12345!!!"` -> `0.0`
    - All vowels `"AEIOU"` -> `1.0`
    - Mixed case `"Hello, World!"` -> 3 vowels (`e, o, o`) / 10 letters = `0.3`

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem:
    Decompose word-length analysis into TWO functions:
      1. Helper `clean_word(raw: str) -> str`:
         Keep only alphabetic characters (`ch.isalpha()`) and convert them to
         lowercase. Example: `"Python3!"` -> `"python"`, `"---"` -> `""`.
      2. Main function `solve_word_length_stats(text: str) -> dict[str, int | float]`:
         Split `text` on whitespace (`text.split()`), clean each raw token
         using `clean_word`, discard any tokens that become empty `""`, and
         return a dictionary with keys:
           - `"count"`: number of cleaned non-empty words (`int`)
           - `"shortest"`: length of the shortest cleaned word (`int`)
           - `"longest"`: length of the longest cleaned word (`int`)
           - `"average"`: mean length rounded to 2 decimal places (`float`)

Rules & Edge Cases:
    - If `text` has NO valid words after cleaning (e.g., `""`, `"   "`, or
      `"123 !!!"`), return:
      `{"count": 0, "shortest": 0, "longest": 0, "average": 0.0}`
    - Ensure `"average"` is a `float` rounded to 2 decimal places (`round(..., 2)`).

Examples:
    solve_word_length_stats("Hi, Python! 2026 rocks.")
        cleaned words -> ["hi", "python", "rocks"] (lengths 2, 6, 5)
        -> {"count": 3, "shortest": 2, "longest": 6, "average": 4.33}

    solve_word_length_stats("42 ???")
        -> {"count": 0, "shortest": 0, "longest": 0, "average": 0.0}
"""

from __future__ import annotations


def _is_vowel(ch: str) -> bool:
    """Helper: return True if ``ch`` is a single English vowel (a, e, i, o, u)."""
    return len(ch) == 1 and ch.lower() in "aeiou"


def example_vowel_density(sentence: str) -> float:
    """Return the fraction of alphabetic characters that are vowels (4 decimals)."""
    letters = [ch for ch in sentence if ch.isalpha()]
    if not letters:
        return 0.0
    vowel_count = sum(1 for ch in letters if _is_vowel(ch))
    return round(vowel_count / len(letters), 4)


def clean_word(raw: str) -> str:
    """Helper: strip non-alphabetic characters from ``raw`` and lowercase it."""
    pass


def solve_word_length_stats(text: str) -> dict[str, int | float]:
    """Return word length statistics after cleaning punctuation and digits.

    Returns a dict with keys ``"count"``, ``"shortest"``, ``"longest"``, and
    ``"average"`` (rounded to 2 decimal places).
    """
    pass


if __name__ == "__main__":
    sample = "Hello, World! 2026"
    print(f"Sentence: {sample!r}")
    print("Vowel density:", example_vowel_density(sample))
