"""
Activity 078 — Safe Validation Pipelines & Error Reporting  [Unlocks Checkpoint 13!]
Difficulty: 78 / 132

Context:
    Nothing frustrates a user more than submitting a registration form, fixing
    one error, resubmitting, and seeing a brand-new error three times in a row.
    Instead of raising an exception on the very first problem, safe validation
    pipelines accumulate a structured list of ALL errors and return a clear
    `(is_valid, errors)` report.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Implement `example_collect_password_errors(password)` that returns a list
    of ALL failed policy messages in order:
      - If `password` is not a `str`: return `["Password must be a string."]`
        immediately (we cannot inspect string rules on a non-string).
      - Otherwise check ALL four independent rules (no `elif`!):
        1. `len(password) < 8`            -> `"Must be at least 8 characters."`
        2. No uppercase letter            -> `"Must contain an uppercase letter."`
        3. No digit                       -> `"Must contain a digit."`
        4. Contains any whitespace        -> `"Must not contain spaces."`

Step-by-Step Explanation:
    1. Start with `errors: list[str] = []`.
    2. Use independent `if` statements — NOT `if/elif` — so multiple failures
       are all reported in a single pass.
    3. An empty `errors` list means the password passed every rule!

Edge Cases:
    - `12345` -> `["Password must be a string."]`
    - `"abc"` -> 3 errors (too short, no uppercase, no digit)
    - `"Secret99"` -> `[]` (valid!)

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem:
    Implement `solve_validate_profile(profile)` that validates a user profile
    dictionary and returns `(is_valid, errors)` where `is_valid` is a `bool`
    and `errors` is a `list[str]`.

Rules:
    - First, if `not isinstance(profile, dict)`:
      return `(False, ["Profile must be a dictionary."])`.
    - Otherwise check ALL THREE fields in this exact order (using independent
      checks so multiple problems are all collected):
      1. `"username"`:
         Must be present in `profile`, be a `str`, and have
         `len(username.strip()) >= 3`.
         Otherwise append `"Invalid username."`.
      2. `"age"`:
         Must be present in `profile`, be an `int` (and NOT a `bool`!), and
         satisfy `13 <= age <= 120`.
         Otherwise append `"Invalid age."`.
      3. `"email"`:
         Must be present in `profile`, be a `str`, contain NO spaces, contain
         EXACTLY ONE `"@"`, have a non-empty local part before `"@"`, and have
         a domain part after `"@"` that contains `"."` (and does not start or
         end with `"."`).
         Otherwise append `"Invalid email."`.
    - Return `(len(errors) == 0, errors)`.

Examples:
    solve_validate_profile({"username": "ada", "age": 28, "email": "ada@example.com"})
        -> (True, [])

    solve_validate_profile({"username": "  ", "age": True, "email": "bad"})
        -> (False, ["Invalid username.", "Invalid age.", "Invalid email."])

    solve_validate_profile("not a dict")
        -> (False, ["Profile must be a dictionary."])
"""

from __future__ import annotations


def example_collect_password_errors(password: str) -> list[str]:
    """Return a list of all password policy violations (empty list if valid)."""
    if not isinstance(password, str):
        return ["Password must be a string."]

    errors: list[str] = []
    if len(password) < 8:
        errors.append("Must be at least 8 characters.")
    if not any(ch.isupper() for ch in password):
        errors.append("Must contain an uppercase letter.")
    if not any(ch.isdigit() for ch in password):
        errors.append("Must contain a digit.")
    if any(ch.isspace() for ch in password):
        errors.append("Must not contain spaces.")
    return errors


def solve_validate_profile(profile: dict) -> tuple[bool, list[str]]:
    """Validate a user profile dictionary and return ``(is_valid, errors)``."""
    pass


if __name__ == "__main__":
    for candidate in ["Secret99", "weak", "No Digits!", 12345]:
        print(f"{candidate!r:14} -> {example_collect_password_errors(candidate)}")  # type: ignore[arg-type]
