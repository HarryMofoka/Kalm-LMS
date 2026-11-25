"""
Activity 082 — Recursion: Gentle Intro
Difficulty: 82 / 132

Context:
    Recursion feels intimidating until you remember its TWO sacred rules:
      1. **Base case:** a trivially small input that stops immediately.
      2. **Recursive step:** shrink the problem strictly closer to the base case
         and combine the sub-answer.
    Without rule 1, you get infinite recursion (`RecursionError`); without rule 2,
    you never reach the base case!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Implement `example_recursive_sum(numbers)` that sums a list of numbers
    using recursion (no `sum()` or loops).

Step-by-Step Explanation:
    1. Base case: an empty list has sum `0`.
       `if not numbers: return 0`
    2. Recursive step: peel off the first element and add the recursive sum of
       the remaining tail:
       `return numbers[0] + example_recursive_sum(numbers[1:])`
    3. Trace on `[4, 7, 2]`:
       `4 + sum([7, 2])` -> `4 + (7 + sum([2]))` -> `4 + (7 + (2 + 0))` = `13`.

Edge Cases:
    - `[]` -> `0`
    - `[-5]` -> `-5`
    - Floats `[1.5, 2.5]` -> `4.0`

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem A — `solve_is_palindrome_recursive(text)`:
    Check recursively whether `text` reads the same forwards and backwards,
    ignoring case and non-alphanumeric characters (spaces, punctuation).
    - Hint: clean `text` once into lowercase alphanumeric characters
      (`cleaned = "".join(ch.lower() for ch in text if ch.isalnum())`), then
      run a recursive helper comparing `s[0] == s[-1]` and recursing on `s[1:-1]`
      (or using `left`/`right` indices).
    - Base case: length `<= 1` -> `True`!

Problem B — `solve_fast_pow(base, exp)`:
    Compute `base ** exp` recursively using **exponentiation by squaring** in
    O(log exp) recursive calls!
    - Validation: if `exp < 0`, raise `ValueError("Exponent must be non-negative.")`.
    - Base case: `exp == 0` -> `1`.
    - Even `exp`: compute `half = solve_fast_pow(base, exp // 2)` ONCE and
      return `half * half`.
    - Odd `exp`: return `base * solve_fast_pow(base, exp - 1)`.

Examples:
    solve_is_palindrome_recursive("A man, a plan, a canal: Panama!") -> True
    solve_is_palindrome_recursive("racecar")                         -> True
    solve_is_palindrome_recursive("Python")                          -> False
    solve_is_palindrome_recursive("")                                -> True

    solve_fast_pow(2, 10)  -> 1024
    solve_fast_pow(5, 0)   -> 1
    solve_fast_pow(-3, 3)  -> -27
    solve_fast_pow(2, -1)  -> raises ValueError("Exponent must be non-negative.")
"""

from __future__ import annotations


def example_recursive_sum(numbers: list[int | float]) -> int | float:
    """Return the sum of ``numbers`` recursively (empty list -> 0)."""
    if not numbers:
        return 0
    return numbers[0] + example_recursive_sum(numbers[1:])


def solve_is_palindrome_recursive(text: str) -> bool:
    """Return True if ``text`` is an alphanumeric palindrome (case-insensitive)."""
    pass


def solve_fast_pow(base: int | float, exp: int) -> int | float:
    """Compute ``base ** exp`` recursively via exponentiation by squaring.

    Raises:
        ValueError("Exponent must be non-negative.") if ``exp < 0``.
    """
    pass


if __name__ == "__main__":
    print("Recursive sum of [4, 7, 2]:", example_recursive_sum([4, 7, 2]))
    print("Recursive sum of []:", example_recursive_sum([]))
