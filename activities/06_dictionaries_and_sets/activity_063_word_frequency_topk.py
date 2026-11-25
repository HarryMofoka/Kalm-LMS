"""
Activity 063: Word Frequency & Top-K
Difficulty: 63 / 132

Context:
    Search engines, tag clouds, and spam filters count word frequencies across
    documents and rank the top terms—breaking ties predictably so results never
    depend on accidental input ordering.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Cleaned Word Counts Dictionary
===============================================================================
Problem:
    Given a string `text`, return a dictionary mapping each normalized word to
    its frequency count:
      1. Split `text` on whitespace.
      2. Clean each token by keeping only alphanumeric characters (`ch.isalnum()`)
         and converting to lowercase. Ignore tokens that become empty.
      3. Count each cleaned word into a dictionary.

Step-by-Step Explanation:
    1. For each raw token from `text.split()`, compute
       `cleaned = "".join(ch.lower() for ch in token if ch.isalnum())`.
    2. If `cleaned` is non-empty, increment `counts[cleaned] = counts.get(cleaned, 0) + 1`.
    3. Empty or punctuation-only strings return `{}`.

Edge Cases:
    - `"The cat, and the hat!"` -> `{"the": 2, "cat": 1, "and": 1, "hat": 1}`
    - `"!!! ---"`               -> `{}`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Most Frequent Word (Alphabetical Tie-Break)
===============================================================================
Problem:
    Implement `solve_most_frequent_word(text: str) -> str`.
    Using the exact same word normalization (split on whitespace, keep only
    alphanumeric characters, lowercase, ignore empty tokens):
      - Return the single word with the HIGHEST frequency in `text`.
      - If two or more words tie for the highest frequency, return the
        **alphabetically smallest** word (e.g., `"apple"` beats `"banana"`).
      - Return `""` if `text` contains no valid words.

Examples:
    - `"red blue red green blue"`         -> `"blue"`  (tie at 2: `"blue" < "red"`)
    - `"Cat, dog, cat! Dog? Bat."`        -> `"cat"`   (tie at 2: `"cat" < "dog"`)
    - `"One two two three three three"`   -> `"three"`
    - `"Hello!"`                          -> `"hello"`
    - `"!!!   ---"`                       -> `""`
    - `""`                                -> `""`

Edge-Case Hints:
    - Once you have `counts: dict[str, int]`, how do you pick highest count AND
      lowest word alphabetically?
      * Option A (loop): update `best_word` if `count > best_count or (count == best_count and word < best_word)`.
      * Option B (`min` with tuple key): `min(counts.items(), key=lambda pair: (-pair[1], pair[0]))[0]`!
        Negating the count turns "maximize count, minimize word" into a single
        `min(...)` call!
"""

from __future__ import annotations


def example_word_counts(text: str) -> dict[str, int]:
    """Return lowercase alphanumeric-cleaned word frequencies from `text`."""
    counts: dict[str, int] = {}
    for token in text.split():
        cleaned = "".join(ch.lower() for ch in token if ch.isalnum())
        if cleaned:
            counts[cleaned] = counts.get(cleaned, 0) + 1
    return counts


def solve_most_frequent_word(text: str) -> str:
    """Return the most frequent normalized word in `text` (alphabetical tie-break)."""
    pass


if __name__ == "__main__":
    sample = "The cat, the hat, and the cat!"
    print(f"{sample!r} -> {example_word_counts(sample)}")
