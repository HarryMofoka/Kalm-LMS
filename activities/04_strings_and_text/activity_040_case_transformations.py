"""
Activity 040: Case Transformations
Difficulty: 40 / 132

Context:
    Formatting names, titles, and obfuscated codes requires careful control over
    letter casing. Built-in methods like `.title()` have surprising quirks
    (e.g., `"don't".title()` becomes `"Don'T"`!), so knowing how to inspect and
    transform characters manually is a huge exam advantage.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Safe Word Capitalization
===============================================================================
Problem:
    Given a string `text`, capitalize the first character of each whitespace-
    separated word and lowercase the remaining characters of each word. Join the
    resulting words with a single space `" "`.

Step-by-Step Explanation:
    1. Call `text.split()` to extract clean words (this trims leading/trailing
       whitespace and collapses multiple spaces).
    2. For each word, transform it with `word[0].upper() + word[1:].lower()`.
       Unlike `.title()`, this turns `"don't"` into `"Don't"` instead of `"Don'T"`.
    3. Join the transformed words with `" ".join(...)`.

Edge Cases:
    - `"  don't   STOP believing  "` -> `"Don't Stop Believing"`
    - `"a"`                          -> `"A"`
    - `"   "`                        -> `""`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Conditional Swap-Case & Reverse
===============================================================================
Problem:
    Implement `solve_smart_swap_case(text: str) -> str`.
    Transform `text` in two steps:
      1. Swap the case of every letter in `text` (uppercase becomes lowercase,
         lowercase becomes uppercase; non-letters stay unchanged).
      2. Inspect `text`: if it contains ANY character that is NEITHER a letter
         (`ch.isalpha()`) NOR a space (`ch == " "`), reverse the entire swapped
         string! Otherwise, keep the swapped string in its original order.

Examples:
    - `"Hello World"` -> `"hELLO wORLD"`   (only letters & spaces -> no reverse)
    - `"Hi 2026!"`    -> `"!6202 Ih"`      (contains digits & '!' -> reversed)
    - `"PyThOn3"`     -> `"3NoHtYp"`       (contains '3' -> reversed)
    - `"abc"`         -> `"ABC"`
    - `"   "`         -> `"   "`           (only spaces -> no reverse)
    - `""`            -> `""`

Edge-Case Hints:
    - Check for non-letter/non-space characters with:
      `any(not (ch.isalpha() or ch == " ") for ch in text)`.
    - Tabs (`"\\t"`) or punctuation (`"-"`, `"!"`, `"."`) are NOT spaces (`" "`)
      and NOT letters, so they trigger the reversal.
"""

from __future__ import annotations


def example_capitalize_words(text: str) -> str:
    """Capitalize the first character of each word and lowercase the rest."""
    words = text.split()
    formatted = [word[0].upper() + word[1:].lower() for word in words]
    return " ".join(formatted)


def solve_smart_swap_case(text: str) -> str:
    """Swap letter cases; reverse the result if any non-letter/non-space char exists."""
    pass


if __name__ == "__main__":
    for sample in ["hello world", "  don't   PANIC  ", "PYTHON 101"]:
        print(f"{sample!r:22} -> {example_capitalize_words(sample)!r}")
