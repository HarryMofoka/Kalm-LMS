"""
Activity 062: Character Frequency Map
Difficulty: 62 / 132

Context:
    Frequency histograms power spell-checkers, cipher-breaking tools, text
    classifiers, and countless exam questions. Learning the clean
    `counts[ch] = counts.get(ch, 0) + 1` idiom eliminates verbose `if/else`
    boilerplate and `KeyError` crashes.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Character Frequency Dictionary
===============================================================================
Problem:
    Given a string `text`, return a dictionary mapping each character present
    in `text` to the number of times it appears (case-sensitive).

Step-by-Step Explanation:
    1. Start with an empty dictionary `counts: dict[str, int] = {}`.
    2. For each `ch` in `text`, run `counts[ch] = counts.get(ch, 0) + 1`.
       `counts.get(ch, 0)` safely returns `0` the first time `ch` is seen,
       preventing a `KeyError`.
    3. Empty string returns `{}`.

Edge Cases:
    - `"banana"` -> `{"b": 1, "a": 3, "n": 2}`
    - `"AaA"`    -> `{"A": 2, "a": 1}`
    - `""`       -> `{}`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Full 26-Letter `'a'..'z'` Case-Insensitive Map
===============================================================================
Problem:
    Implement `solve_alphabet_frequency(text: str) -> dict[str, int]`.
    Return a dictionary containing ALL 26 lowercase English letters `'a'` through
    `'z'` as keys, mapped to how many times each letter appears in `text`
    (ignoring letter case).
      - Every letter from `'a'` to `'z'` MUST exist as a key—with value `0` if
        it does not appear in `text`!
      - Ignore digits, spaces, punctuation, and any non-ASCII-letter characters.

Examples:
    - `"Abba! 123"` -> `{"a": 2, "b": 2, "c": 0, "d": 0, ..., "z": 0}` (26 keys)
    - `""`          -> `{"a": 0, "b": 0, ..., "z": 0}`                 (26 keys)
    - `"The quick brown fox jumps over the lazy dog"` -> every letter >= 1

Edge-Case Hints:
    - Pre-initialize the 26 keys cleanly using `string.ascii_lowercase`:
      `counts = {letter: 0 for letter in string.ascii_lowercase}`.
    - Then loop over `text.lower()`: only increment `if ch in counts: counts[ch] += 1`!
      Because `counts` already holds exact `'a'..'z'`, `if ch in counts:` both
      filters out digits/punctuation AND avoids `KeyError` in one line!
"""

from __future__ import annotations


def example_char_frequency(text: str) -> dict[str, int]:
    """Return a case-sensitive `{char: count}` frequency map for `text`."""
    counts: dict[str, int] = {}
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1
    return counts


def solve_alphabet_frequency(text: str) -> dict[str, int]:
    """Return a full 26-letter `'a'..'z'` case-insensitive frequency dictionary."""
    pass


if __name__ == "__main__":
    print(example_char_frequency("banana"))
    print(example_char_frequency("AaBbA"))
