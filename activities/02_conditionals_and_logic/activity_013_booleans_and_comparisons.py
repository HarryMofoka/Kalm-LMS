"""
Activity 013: Simple Comparisons & Booleans
Difficulty: 13 / 132 (Rank 2 - Decision Maker)

Context:
Every `if` statement in Python is powered by a boolean value: `True` or `False`.
One of the cleanest habits you can build early is recognizing that a comparison
expression like `number > 0` ALREADY evaluates to `True` or `False` — you don't
have to wrap it in `if number > 0: return True else: return False`!

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
Write `example_is_positive(number)` that returns `True` if `number` is strictly
greater than `0`, and `False` otherwise.

Step-by-step walkthrough:
1. Evaluate the comparison `number > 0`.
   - If `number` is `5`, `5 > 0` evaluates directly to `True`.
   - If `number` is `0`, `0 > 0` evaluates directly to `False` (0 is neither
     positive nor negative!).
   - If `number` is `-3.5`, `-3.5 > 0` evaluates directly to `False`.
2. Return `number > 0` directly. It is shorter, clearer, and 100% Pythonic!

Edge cases:
- `0` -> `False` (strictly greater than zero means `>`, not `>=`).
- Negative floats like `-0.001` -> `False`.
- Tiny positive floats like `0.001` -> `True`.

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
A telemetry sensor only accepts packets whose ID is BOTH strictly positive AND
an even integer. Write `solve_is_even_and_positive(number)` that returns `True`
if `number` is strictly greater than `0` AND evenly divisible by `2`, and
`False` otherwise.

Rules:
- Strictly positive means `number > 0` (so `0` is NOT positive -> `False`).
- Even means `number % 2 == 0`.
- Negative even numbers like `-4` must return `False`!
- Positive odd numbers like `7` must return `False`!

Examples:
- `solve_is_even_and_positive(4)` -> `True`
- `solve_is_even_and_positive(0)` -> `False`
- `solve_is_even_and_positive(-6)` -> `False`
- `solve_is_even_and_positive(9)` -> `False`
- `solve_is_even_and_positive(2)` -> `True`

Hints:
- Combine both comparisons with `and`: `return number > 0 and number % 2 == 0`.
- Remember: return an actual boolean (`True` or `False`), never `None` or an int.
"""

from __future__ import annotations


def example_is_positive(number: float) -> bool:
    """Return True if number is strictly greater than 0, else False."""
    # Comparison expressions already produce a bool — return directly!
    return number > 0


def solve_is_even_and_positive(number: int) -> bool:
    """Return True if number is strictly positive and even, else False."""
    pass


if __name__ == "__main__":
    print("Is 10 positive?", example_is_positive(10))
    print("Is 0 positive? ", example_is_positive(0))
    print("Is -4 positive?", example_is_positive(-4))
