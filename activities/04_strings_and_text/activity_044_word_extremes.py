"""
Activity 044: Longest & Shortest Word with Tie-Breaking
Difficulty: 44 / 132

Context:
    Finding an extreme value (shortest or longest word) is easy—until two words
    have the exact same length! Exams love testing whether you understand strict
    (`<` / `>`) vs. non-strict (`<=` / `>=`) tie-breaking, plus punctuation noise.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Shortest Word (First Tie Wins)
===============================================================================
Problem:
    Given a string `text`, return the shortest whitespace-separated word.
    If multiple words tie for shortest length, return the FIRST one encountered.
    If `text` has no words, return `""`.

Step-by-Step Explanation:
    1. Split `text` into `words = text.split()`. If `words` is empty, return `""`.
    2. Start with `shortest = words[0]`.
    3. Loop through `words[1:]`: update `shortest = word` ONLY when
       `len(word) < len(shortest)`. Using strict `<` guarantees the FIRST tied
       word is preserved!

Edge Cases:
    - `"cat dog ox an"` -> `"ox"` (ties with `"an"`, first tie wins)
    - `"hello"`         -> `"hello"`
    - `"   "`           -> `""`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Longest Word Ignoring Punctuation (Last Tie Wins)
===============================================================================
Problem:
    Implement `solve_longest_word(text: str) -> str`.
    Find the longest word in `text` while ignoring punctuation, with LAST tie
    winning:
      1. Split `text` on whitespace into tokens.
      2. Clean each token by keeping only alphanumeric characters
         (`"".join(ch for ch in token if ch.isalnum())`). Ignore tokens that
         become empty after cleaning (e.g., `"---"` or `"!!!"`).
      3. Return the cleaned word with the maximum length (preserving its original
         case). If two or more cleaned words tie for the longest length, return
         the LAST one encountered!
      4. If no valid words exist, return `""`.

Examples:
    - `"The quick, brown fox!"` -> `"brown"`  (`"quick"` and `"brown"` both len 5; last wins)
    - `"Hello, world!!!"`       -> `"world"`  (punctuation stripped before measuring!)
    - `"cat dog bat"`           -> `"bat"`
    - `"one!!! two"`            -> `"two"`    (`"one"` and `"two"` both len 3)
    - `"!!! ... ???"`           -> `""`
    - `""`                      -> `""`

Edge-Case Hints:
    - Why does `"one!!!"` have length 3 instead of 6? Because you must clean
      punctuation from each token BEFORE comparing lengths.
    - Use `>=` (`len(word) >= len(longest)`) so later equal-length words replace
      earlier ones—making the LAST tie win!
"""

from __future__ import annotations


def example_shortest_word(text: str) -> str:
    """Return the shortest whitespace-separated word in `text` (first tie wins)."""
    words = text.split()
    if not words:
        return ""

    shortest = words[0]
    for word in words[1:]:
        # Strict '<' keeps the first word when lengths are equal.
        if len(word) < len(shortest):
            shortest = word
    return shortest


def solve_longest_word(text: str) -> str:
    """Return the longest punctuation-cleaned word in `text` (last tie wins)."""
    pass


if __name__ == "__main__":
    for sample in ["The quick brown fox", "cat dog ox an", "   "]:
        print(f"{sample!r:24} -> {example_shortest_word(sample)!r}")
