"""
Activity 041: Word Splitting & Joining
Difficulty: 41 / 132

Context:
    Countless coding problems ask you to manipulate sentences word by word—
    reversing words, pig-latinizing them, or censoring specific tokens. The
    split -> transform -> join pipeline is one of Python's cleanest idioms.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Clean Word Splitting
===============================================================================
Problem:
    Given a string `text`, return a list of all whitespace-separated words.
    Leading/trailing spaces and consecutive spaces/tabs/newlines must NOT create
    empty strings in the result.

Step-by-Step Explanation:
    1. Calling `text.split()` WITH NO ARGUMENTS splits on any run of whitespace
       and automatically drops leading/trailing whitespace.
    2. Contrast with `text.split(" ")`: `"  a  b ".split(" ")` produces
       `['', '', 'a', '', 'b', '']`—a classic exam bug!
    3. For empty or whitespace-only input, `text.split()` naturally returns `[]`.

Edge Cases:
    - `"  Hello   world\\tfrom\\nPython  "` -> `["Hello", "world", "from", "Python"]`
    - `"   "`                              -> `[]`
    - `""`                                 -> `[]`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Reverse Each Word Preserving Word Order
===============================================================================
Problem:
    Implement `solve_reverse_each_word(text: str) -> str`.
    Split `text` into words (ignoring extra leading, trailing, and repeated
    whitespace), reverse the characters of EACH individual word while keeping
    the words in their ORIGINAL left-to-right order, and join them with a single
    space `" "`.

Examples:
    - `"Hello World"`          -> `"olleH dlroW"`
    - `"  Python   is  fun! "` -> `"nohtyP si !nuf"`
    - `"racecar level"`        -> `"racecar level"`
    - `"single"`               -> `"elgnis"`
    - `"   "`                  -> `""`
    - `""`                     -> `""`

Edge-Case Hints:
    - Do NOT reverse the whole sentence (`text[::-1]` reverses word order too!).
    - Instead, split into words first, reverse each word with `word[::-1]`, and
      join with `" ".join(...)`.
"""

from __future__ import annotations


def example_split_words(text: str) -> list[str]:
    """Split `text` into non-empty words across any run of whitespace."""
    return text.split()


def solve_reverse_each_word(text: str) -> str:
    """Reverse each word in `text` individually while keeping word order intact."""
    pass


if __name__ == "__main__":
    sample = "  Python   exam\tprep\nrocks  "
    print(f"{sample!r} -> {example_split_words(sample)}")
