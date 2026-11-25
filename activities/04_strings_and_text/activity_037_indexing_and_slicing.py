"""
Activity 037: Indexing & Slicing Basics
Difficulty: 37 / 132

Context:
    Every text parser, log inspector, and command-line tool starts with pulling
    exact pieces out of a string. Python's positive/negative indices and slice
    syntax `text[start:stop:step]` let you extract characters cleanly without
    mutating the original string.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — First & Last Characters
===============================================================================
Problem:
    Given a string `text`, return a 2-tuple `(first_char, last_char)` containing
    its first and last characters. If `text` is empty, return `("", "")`.

Step-by-Step Explanation:
    1. Guard against the empty string FIRST: indexing `""[0]` raises IndexError!
    2. Use `text[0]` for the first character and `text[-1]` for the last character.
    3. Notice that a 1-character string like `"X"` works automatically because
       both `text[0]` and `text[-1]` refer to `"X"`, returning `("X", "X")`.

Edge Cases:
    - `""`      -> `("", "")`
    - `"A"`     -> `("A", "A")`
    - `"hello"` -> `("h", "o")`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Reverse String & Extract Middle Slice
===============================================================================
Problem:
    Implement `solve_reverse_and_middle(text: str) -> tuple[str, str]`.
    Given a string `text`, return a 2-tuple `(reversed_text, middle_slice)`:
      - `reversed_text`: `text` reversed using slicing (`text[::-1]`).
      - `middle_slice`:
          * If `text` is empty, `""`.
          * If `len(text)` is odd, the single exact middle character.
          * If `len(text)` is even (and non-empty), the 2 middle characters.

Examples:
    - `"hello"`  (len 5, odd)  -> `("olleh", "l")`
    - `"python"` (len 6, even) -> `("nohtyp", "th")`
    - `"code"`   (len 4, even) -> `("edoc", "od")`
    - `"a"`      (len 1, odd)  -> `("a", "a")`
    - `""`       (len 0)       -> `("", "")`

Edge-Case Hints:
    - Check `if not text:` first so integer division never slices an empty string.
    - Let `mid = len(text) // 2`. For odd length, `text[mid]` is the center;
      for even length, `text[mid - 1 : mid + 1]` grabs the exact middle pair!
"""

from __future__ import annotations


def example_first_and_last(text: str) -> tuple[str, str]:
    """Return `(first_char, last_char)` of `text`, or `("", "")` if empty."""
    # Always guard against empty strings before indexing [0] or [-1].
    if not text:
        return ("", "")
    return (text[0], text[-1])


def solve_reverse_and_middle(text: str) -> tuple[str, str]:
    """Return `(reversed_text, middle_slice)` for `text`.

    - `reversed_text` is `text` backwards.
    - `middle_slice` is `""` if empty, the single center character if `len(text)`
      is odd, or the two center characters if `len(text)` is even.
    """
    pass


if __name__ == "__main__":
    samples = ["python", "X", "", "Exam Prep!"]
    for sample in samples:
        print(f"{sample!r:12} -> {example_first_and_last(sample)}")
