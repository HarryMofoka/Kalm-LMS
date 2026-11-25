"""
Activity 043: Palindrome Detection
Difficulty: 43 / 132

Context:
    Palindromes ("racecar", "A man, a plan, a canal: Panama!") are one of the
    most frequently tested string questions in university exams and coding
    interviews—especially the version that asks you to ignore noise characters.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Simple Exact Palindrome
===============================================================================
Problem:
    Return `True` if `text` reads identically left-to-right and right-to-left
    (exact character and case match), otherwise return `False`.

Step-by-Step Explanation:
    1. `text[::-1]` creates the reversed string in $O(n)$ time.
    2. Compare `text == text[::-1]`.
    3. Empty strings and 1-character strings read the same backwards, so they
       are palindromes (`True`).

Edge Cases:
    - `"racecar"` -> `True`
    - `"Racecar"` -> `False` (case-sensitive!)
    - `"a"`       -> `True`
    - `""`        -> `True`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Phrase Palindrome (Ignore Case, Spaces & Punctuation)
===============================================================================
Problem:
    Implement `solve_is_phrase_palindrome(text: str) -> bool`.
    Return `True` if `text` is a palindrome after:
      1. Keeping ONLY alphanumeric characters (`ch.isalnum()` — letters & digits),
      2. Ignoring letter case (convert kept characters to lowercase).
    Return `False` otherwise.

Examples:
    - `"A man, a plan, a canal: Panama!"` -> `True`
    - `"Was it a car or a cat I saw?"`    -> `True`
    - `"No 'x' in Nixon"`                 -> `True`
    - `"12321"`                           -> `True`
    - `"race a car"`                      -> `False`
    - `"0P"`                              -> `False`
    - `"   !!!"`                          -> `True` (cleaned text is `""`)

Edge-Case Hints:
    - Digits matter! `"1a2"` is NOT a palindrome (`"1a2" != "2a1"`), whereas
      `"1a1"` IS a palindrome. That's why `ch.isalnum()` is preferred over
      `ch.isalpha()`.
    - Build the cleaned lowercase string first, then compare it to its reverse
      (or use two pointers from both ends!).
"""

from __future__ import annotations


def example_is_simple_palindrome(text: str) -> bool:
    """Return True if `text` is an exact, case-sensitive palindrome."""
    return text == text[::-1]


def solve_is_phrase_palindrome(text: str) -> bool:
    """Return True if `text` is a palindrome ignoring case, spaces, and punctuation."""
    pass


if __name__ == "__main__":
    for sample in ["racecar", "Racecar", "abba", "python", ""]:
        print(f"{sample!r:10} -> {example_is_simple_palindrome(sample)}")
