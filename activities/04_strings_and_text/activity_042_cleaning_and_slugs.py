"""
Activity 042: Cleaning & Formatting Slugs  [Unlocks Checkpoint 07!]
Difficulty: 42 / 132

Context:
    Blog engines, e-commerce sites, and documentation platforms turn messy human
    titles like `"  Python 3.12: Tips & Tricks!  "` into clean, URL-friendly
    slugs like `"python-312-tips-tricks"`. Building a slugifier combines
    normalization, filtering, splitting, and joining in one real-world task!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Trim & Collapse Whitespace
===============================================================================
Problem:
    Given a messy string `text`, remove leading and trailing whitespace and
    collapse every internal run of spaces, tabs, or newlines into a single space.

Step-by-Step Explanation:
    1. `text.split()` strips outer whitespace and splits on every whitespace run.
    2. `" ".join(...)` stitches the tokens back together with exactly one space
       between adjacent words.
    3. Empty or whitespace-only strings return `""`.

Edge Cases:
    - `"   hello   \\t  world  \\n"` -> `"hello world"`
    - `"already clean"`              -> `"already clean"`
    - `"   "`                        -> `""`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — URL Slug Generator
===============================================================================
Problem:
    Implement `solve_slugify(text: str) -> str`.
    Convert any title string `text` into a clean URL slug by following these
    exact four steps:
      1. Lowercase the entire string.
      2. Treat hyphens (`"-"`) and underscores (`"_"`) as word separators by
         replacing both with spaces (`" "`).
      3. Remove every remaining character that is NOT alphanumeric (`ch.isalnum()`)
         and NOT whitespace (`ch.isspace()`).
      4. Split on whitespace (collapsing all runs and trimming ends) and join
         the resulting words with `"-"`.

Examples:
    - `"Hello, World!"`              -> `"hello-world"`
    - `"  Learn   Python 101!  "`    -> `"learn-python-101"`
    - `"Don't Panic!"`               -> `"dont-panic"`
    - `"snake_case--and---kebab"`    -> `"snake-case-and-kebab"`
    - `"C++ & Python: A Guide"`      -> `"c-python-a-guide"`
    - `"!!! --- ___"`                -> `""`
    - `""`                           -> `""`

Edge-Case Hints:
    - Notice step 2 + step 4 guarantees you will NEVER have leading hyphens,
      trailing hyphens, or double hyphens (`"--"`) in the output!
    - Punctuation like apostrophes (`'`) or `+` gets dropped in step 3, not
      turned into hyphens (`"Don't"` -> `"dont"`).
"""

from __future__ import annotations


def example_clean_spaces(text: str) -> str:
    """Trim outer whitespace and collapse internal whitespace runs to one space."""
    return " ".join(text.split())


def solve_slugify(text: str) -> str:
    """Convert `text` into a lowercase, hyphen-separated URL slug."""
    pass


if __name__ == "__main__":
    for sample in ["  Hello   World  ", "a\tb\n\nc", "   "]:
        print(f"{sample!r:22} -> {example_clean_spaces(sample)!r}")
