"""
Activity 038: Character Counting & Case Sensitivity
Difficulty: 38 / 132

Context:
    Text analytics, password validators, and DNA sequence scanners all count how
    often specific characters appear. Knowing when comparisons should be
    case-sensitive vs. case-insensitive prevents subtle exam bugs.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Exact Character Counter
===============================================================================
Problem:
    Given a string `text` and a single-character string `target`, count how many
    times `target` appears in `text` (case-sensitive). If `target` does not have
    length 1, return `0`.

Step-by-Step Explanation:
    1. Validate that `len(target) == 1`; otherwise return `0`.
    2. Initialize `count = 0` and iterate character by character through `text`.
    3. Increment `count` only on exact equality (`ch == target`), so `'a'` and
       `'A'` are treated as distinct characters.

Edge Cases:
    - `("Banana", "a")` -> `3` (does not match `'A'`)
    - `("Banana", "B")` -> `1`
    - `("hello", "")`   -> `0`
    - `("", "a")`       -> `0`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Case-Insensitive Vowel Counter
===============================================================================
Problem:
    Implement `solve_count_vowels(text: str) -> int`.
    Count the total number of English vowels (`a`, `e`, `i`, `o`, `u`) in `text`,
    ignoring letter case (so both `'a'` and `'A'` count, while `'y'` does NOT).

Examples:
    - `"Hello World"` -> `3`  (`e`, `o`, `o`)
    - `"AEIOUaeiou"`  -> `10`
    - `"Rhythm"`      -> `0`
    - `"PyThOn 3.12"` -> `1`  (`O`)
    - `""`            -> `0`

Edge-Case Hints:
    - Checking `ch.lower() in "aeiou"` (or `ch in "aeiouAEIOU"`) handles both
      cases cleanly in one expression without mutating `text`.
    - Digits, spaces, and punctuation are not vowels and should simply be skipped.
"""

from __future__ import annotations


def example_count_char(text: str, target: str) -> int:
    """Count case-sensitive occurrences of single character `target` in `text`."""
    if len(target) != 1:
        return 0

    count = 0
    for ch in text:
        if ch == target:
            count += 1
    return count


def solve_count_vowels(text: str) -> int:
    """Return the count of English vowels (a, e, i, o, u) in `text`, ignoring case."""
    pass


if __name__ == "__main__":
    print("Count 'a' in 'Banana':", example_count_char("Banana", "a"))
    print("Count 'B' in 'Banana':", example_count_char("Banana", "B"))
    print("Count 'b' in 'Banana':", example_count_char("Banana", "b"))
