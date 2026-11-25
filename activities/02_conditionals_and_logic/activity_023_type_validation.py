"""
Activity 023: Type Checking & Raising `TypeError` (The `bool` Trap!)
Difficulty: 23 / 132 (Rank 3 - Logic Architect)

Context:
Python is dynamically typed: nothing stops a caller from passing `"42"`, `None`,
or `True` into a function expecting an integer! Defensive functions fail fast
and loudly with a descriptive `TypeError` rather than silently producing garbage
results. And watch out for Python's most famous exam gotcha: `bool` is a
SUBCLASS of `int`, so `isinstance(True, int)` evaluates to `True`!

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
Write `example_validate_str_length(text)` that validates `text` is a `str`
(raising `TypeError` if not) and returns its character length `len(text)`.

Step-by-step walkthrough:
1. Use `isinstance(text, str)` to check whether `text` is a string.
2. If `not isinstance(text, str)`:
       `raise TypeError(f"Expected str, got {type(text).__name__}")`
3. Otherwise return `len(text)`.

Why `isinstance` instead of `type(x) == ...`?
In Python, `isinstance()` is the standard idiomatic way to check types — EXCEPT
when you need to explicitly exclude a subclass like `bool` when validating `int`!

Edge cases:
- `example_validate_str_length("hello")` -> `5`.
- `example_validate_str_length("")` -> `0` (empty string IS still a valid `str`!).
- `example_validate_str_length(123)` -> raises `TypeError`.
- `example_validate_str_length(None)` -> raises `TypeError`.

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
Write `solve_validate_positive_int(value)` that strictly validates `value` is a
genuine positive integer (and NOT a `bool`, `float`, `str`, or `None`!).

Rules (check in this exact order!):
1. If `isinstance(value, bool)` OR `not isinstance(value, int)`:
       `raise TypeError(...)`
   (Remember: in Python, `isinstance(True, int)` is `True` and `True == 1`!
   You MUST reject `True` and `False` with `TypeError`!)
2. If `value <= 0`:
       `raise ValueError(...)`
3. Otherwise return `value` unchanged!

Examples:
- `solve_validate_positive_int(7)` -> `7`
- `solve_validate_positive_int(1)` -> `1`
- `solve_validate_positive_int(True)` -> raises `TypeError`!
- `solve_validate_positive_int(False)` -> raises `TypeError`!
- `solve_validate_positive_int(3.0)` -> raises `TypeError`!
- `solve_validate_positive_int("5")` -> raises `TypeError`!
- `solve_validate_positive_int(0)` -> raises `ValueError`!
- `solve_validate_positive_int(-10)` -> raises `ValueError`!

Hints:
- Check `isinstance(value, bool)` FIRST (or combine `if isinstance(value, bool) or not isinstance(value, int):`) before testing `value <= 0`. Otherwise `False <= 0` would raise `ValueError` instead of `TypeError`!
"""

from __future__ import annotations


def example_validate_str_length(text: object) -> int:
    """Validate that text is a str (else raise TypeError) and return len(text)."""
    if not isinstance(text, str):
        raise TypeError(f"Expected a str, got {type(text).__name__}")
    return len(text)


def solve_validate_positive_int(value: object) -> int:
    """Return value if it is a positive int (not bool); else raise TypeError or ValueError."""
    pass


if __name__ == "__main__":
    print("Length of 'Python':", example_validate_str_length("Python"))
    try:
        example_validate_str_length(42)
    except TypeError as exc:
        print("Caught expected error:", exc)
