"""
Activity 069: Anagram Checking with Frequency Dicts
Difficulty: 69 / 132

Context:
    Sorting two strings to test whether they are anagrams takes O(n log n)
    time. Comparing character frequency dictionaries solves it in O(n) time—
    and the exact same frequency-counting trick unlocks palindrome permutations!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — `is_anagram` Ignoring Case & Spaces
===============================================================================
Problem:
    Return `True` if `first` and `second` are anagrams of each other when
    ignoring letter case and spaces (`" "`), otherwise `False`.

Step-by-Step Explanation:
    1. Build a helper frequency counter that ignores whitespace (`not ch.isspace()`)
       and lowercases every kept character.
    2. In Python, two dictionaries compare equal (`counts_a == counts_b`) iff
       they have the exact same keys with the exact same values—regardless of
       key insertion order!
    3. Total runtime is $O(n + m)$.

Edge Cases:
    - `("Listen", "Silent")`          -> `True`
    - `("Astronomer", "Moon starer")` -> `True`
    - `("hello", "helloo")`           -> `False`
    - `("", "   ")`                   -> `True`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Can String Permute Into a Palindrome?
===============================================================================
Problem:
    Implement `solve_can_form_palindrome(text: str) -> bool`.
    Return `True` if the characters of `text` (ignoring whitespace and letter
    case) can be rearranged into ANY palindrome, otherwise return `False`.

Key Insight:
    In any palindrome, characters on the left mirror characters on the right, so
    almost every character must appear an EVEN number of times—except at most
    ONE character, which can sit right in the middle with an ODD count!
    Therefore: a string can permute into a palindrome iff AT MOST ONE distinct
    character has an odd frequency (`odd_count <= 1`)!

Examples:
    - `"civic"`      -> `True`  (`c:2, i:2, v:1` -> 1 odd count)
    - `"ivicc"`      -> `True`  (rearranges to `"civic"`)
    - `"Tact Coa"`   -> `True`  (ignores space & case -> `"taco cat"`, 1 odd: `'o'`)
    - `"aabbcc"`     -> `True`  (0 odd counts)
    - `"hello"`      -> `False` (`h:1, e:1, o:1` -> 3 odd counts)
    - `"ab"`         -> `False` (2 odd counts)
    - `"   "`        -> `True`  (0 odd counts)
    - `""`           -> `True`

Edge-Case Hints:
    - Do NOT generate all `n!` permutations (that explodes instantly for strings
      longer than 10 characters!). Count frequencies in one $O(n)$ dict pass and
      count how many values satisfy `count % 2 == 1`.
"""

from __future__ import annotations


def example_is_anagram(first: str, second: str) -> bool:
    """Return True if `first` and `second` are anagrams ignoring case and spaces."""
    counts_first: dict[str, int] = {}
    for ch in first.lower():
        if not ch.isspace():
            counts_first[ch] = counts_first.get(ch, 0) + 1

    counts_second: dict[str, int] = {}
    for ch in second.lower():
        if not ch.isspace():
            counts_second[ch] = counts_second.get(ch, 0) + 1

    return counts_first == counts_second


def solve_can_form_palindrome(text: str) -> bool:
    """Return True if non-space chars of `text` (case-insensitive) can form a palindrome."""
    pass


if __name__ == "__main__":
    pairs = [
        ("Listen", "Silent"),
        ("Astronomer", "Moon starer"),
        ("Python", "Typhoon"),
    ]
    for a, b in pairs:
        print(f"{a!r} vs {b!r} -> {example_is_anagram(a, b)}")
