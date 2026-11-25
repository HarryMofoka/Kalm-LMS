"""
Activity 126: Utility & Solver Classes (ProblemSolver Style!)
Difficulty: 126 / 132

In coding interviews and practical exams (just like `ProblemSolver` in
Code Pairing!), algorithms are frequently grouped inside a **Solver / Analyzer
class** — often paired with stateful telemetry like a call counter or cache.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — ExampleTextAnalyzer
===============================================================================
Problem:
    Build `ExampleTextAnalyzer` with a stateful `self.calls` counter that
    increments by 1 every time ANY analysis method is invoked:
      - `word_count(text) -> int`: number of whitespace-separated words.
      - `char_frequency(text) -> dict[str, int]`: lowercase counts of non-space chars.
      - `is_palindrome(text) -> bool`: True if alphanumeric characters read the
        same forward and backward (case-insensitive).

Step-by-Step Breakdown:
    1. `__init__` starts `self.calls = 0`.
    2. Each public method starts with `self.calls += 1` so the analyzer tracks
       usage across all methods uniformly.

===============================================================================
PART 2: YOUR TURN ("YOU DO") — MiniProblemSolver
===============================================================================
Problem:
    Implement `MiniProblemSolver` — aligned directly with `ProblemSolver`!
      - `__init__(self) -> None`
        * Initializes `self.call_count = 0`.
      - `sum_even_positives(self, numbers: list[int]) -> int`
        * Increments `self.call_count` by 1.
        * Returns the sum of all STRICTLY POSITIVE (`> 0`) even integers in
          `numbers` (negative even numbers and `0` are ignored; empty list -> `0`).
      - `remove_duplicates_preserve_order(self, items: list) -> list`
        * Increments `self.call_count` by 1.
        * Returns a NEW list containing each unique element once, in the exact
          order it FIRST appeared (does NOT mutate `items`!).
      - `longest_word(self, sentence: str) -> str`
        * Increments `self.call_count` by 1.
        * Splits `sentence` on whitespace, strips non-alphanumeric characters
          from each token, and returns the longest cleaned word.
        * Tie-breaker: if multiple words share the maximum length, return the
          **LAST** one!
        * Returns `""` for an empty or punctuation-only sentence.

    Examples:
        solver = MiniProblemSolver()
        solver.sum_even_positives([-4, 0, 2, 3, 6])                -> 8
        solver.remove_duplicates_preserve_order([3, 1, 3, 2, 1])   -> [3, 1, 2]
        solver.longest_word("Cat, dog! Fox?")                      -> "Fox"
        solver.call_count                                          -> 3

    Edge-case hints:
        - Check `longest_word` tie-breaker carefully: `len(cleaned) >= len(best)`
          picks the LAST word on a tie (whereas `>` would pick the first!).
        - Use a `seen = set()` for O(n) duplicate removal while preserving order.
"""
from __future__ import annotations


class ExampleTextAnalyzer:
    """A utility text analyzer tracking how many times its methods are called."""

    def __init__(self) -> None:
        self.calls = 0

    def word_count(self, text: str) -> int:
        """Return the count of whitespace-separated words."""
        self.calls += 1
        return len(text.split())

    def char_frequency(self, text: str) -> dict[str, int]:
        """Return lowercase frequency dictionary of non-whitespace characters."""
        self.calls += 1
        counts: dict[str, int] = {}
        for ch in text.lower():
            if not ch.isspace():
                counts[ch] = counts.get(ch, 0) + 1
        return counts

    def is_palindrome(self, text: str) -> bool:
        """Return True if text is a palindrome ignoring case and punctuation."""
        self.calls += 1
        cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
        return cleaned == cleaned[::-1]


class MiniProblemSolver:
    """A solver class tracking `call_count` across three exam-style algorithms."""

    def __init__(self) -> None:
        """Initialize call_count to 0."""
        pass

    def sum_even_positives(self, numbers: list[int]) -> int:
        """Increment call_count and sum all strictly positive even integers."""
        pass

    def remove_duplicates_preserve_order(self, items: list) -> list:
        """Increment call_count and return deduplicated list in first-seen order."""
        pass

    def longest_word(self, sentence: str) -> str:
        """Increment call_count and return longest alphanumeric word (last on tie)."""
        pass


if __name__ == "__main__":
    analyzer = ExampleTextAnalyzer()
    print("Words:", analyzer.word_count("Hello Python OOP world"))
    print("Palindrome?", analyzer.is_palindrome("A man, a plan, a canal: Panama!"))
    print("Total calls:", analyzer.calls)
