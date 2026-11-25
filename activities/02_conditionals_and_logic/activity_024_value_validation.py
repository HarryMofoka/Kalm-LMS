"""
Activity 024: Raising `ValueError` & Multi-Rule Validation  [Unlocks Checkpoint 04!]
Difficulty: 24 / 132 (Rank 3 - Logic Architect)

Context:
`TypeError` says "you gave me the wrong KIND of object" (like a string instead
of an int). `ValueError` says "the type is right, but the VALUE makes no sense"
(like an age of `-5`, or February 30!). Knowing when to raise `TypeError` vs.
`ValueError` is a hallmark of clean Python API design.

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
Write `example_validate_age(age)` that:
1. Raises `TypeError` if `age` is a `bool` or not an `int`.
2. Raises `ValueError` if `age < 0` or `age > 130`.
3. Returns `age` if valid.

Step-by-step walkthrough:
1. Type guard first:
       `if isinstance(age, bool) or not isinstance(age, int):`
           `raise TypeError("age must be an integer")`
2. Value-range guard second:
       `if age < 0 or age > 130:`
           `raise ValueError("age must be between 0 and 130 inclusive")`
3. Return `age`.

Edge cases:
- `0` and `130` are both valid inclusive bounds -> return `0` and `130`.
- `-1` and `131` -> raise `ValueError`.
- `True` or `25.5` or `"25"` -> raise `TypeError`.

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
Combine everything from Module 02 (type guards, value guards, and Gregorian
leap-year calendar logic!) to write a rock-solid calendar validator:
    `solve_validate_date(year, month, day)`

Validation Rules (in order!):
1. Type check: if ANY of `year`, `month`, or `day` is a `bool` or not an `int`
   -> `raise TypeError(...)`.
2. Year range: `year` must satisfy `1 <= year <= 9999`
   -> otherwise `raise ValueError(...)`.
3. Month range: `month` must satisfy `1 <= month <= 12`
   -> otherwise `raise ValueError(...)`.
4. Day range: `day` must satisfy `1 <= day <= max_days`, where `max_days` is
   the true number of days in `(year, month)` accounting for Gregorian leap
   years (Feb has 29 days in leap years like 2024 and 2000, and 28 in non-leap
   years like 2023 and 1900!) -> otherwise `raise ValueError(...)`.
5. If every rule passes, return the tuple `(year, month, day)`.

Examples:
- `solve_validate_date(2024, 2, 29)` -> `(2024, 2, 29)`
- `solve_validate_date(2025, 12, 31)` -> `(2025, 12, 31)`
- `solve_validate_date(2023, 2, 29)` -> raises `ValueError` (2023 is not leap!)
- `solve_validate_date(1900, 2, 29)` -> raises `ValueError` (1900 is not leap!)
- `solve_validate_date(2024, 4, 31)` -> raises `ValueError` (April has 30 days!)
- `solve_validate_date(2024, True, 1)` -> raises `TypeError` (`bool` rejected!)

Hints:
- You can check all three types concisely with a quick loop:
      `for part in (year, month, day):`
          `if isinstance(part, bool) or not isinstance(part, int):`
              `raise TypeError("year, month, and day must be integers")`
- Completing this activity finishes **Module 02** and unlocks **Checkpoint 04**!
"""

from __future__ import annotations


def example_validate_age(age: int) -> int:
    """Validate that age is an int (not bool) in 0..130, returning age if valid."""
    if isinstance(age, bool) or not isinstance(age, int):
        raise TypeError(f"age must be an int, got {type(age).__name__}")
    if age < 0 or age > 130:
        raise ValueError(f"age must be between 0 and 130, got {age}")
    return age


def solve_validate_date(
    year: int, month: int, day: int
) -> tuple[int, int, int]:
    """Validate (year, month, day) as a real Gregorian date; raise TypeError or ValueError."""
    pass


if __name__ == "__main__":
    print("Valid age 25 ->", example_validate_age(25))
    try:
        example_validate_age(-3)
    except ValueError as exc:
        print("Caught expected error:", exc)
