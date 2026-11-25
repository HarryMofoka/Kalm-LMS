"""
Activity 007: Digit Extraction with `% 10` and `// 10`
Difficulty: 7 / 132 (Rank 2 - Foundations Builder)

Context:
Credit-card checksums (Luhn algorithm), ISBN book validators, and digital
odometers all peel individual decimal digits off an integer using pure math.
Understanding `% 10` (grab the rightmost digit) and `// 10` (chop off the
rightmost digit) is a foundational trick that appears on nearly every Python
exam!

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
Write `example_last_two_digits(number)` that takes a non-negative integer and
returns a tuple `(tens_digit, ones_digit)` using ONLY integer arithmetic
(`//` and `%`).

Step-by-step walkthrough:
1. `ones_digit = number % 10`
   Dividing any integer by 10 leaves its last (ones-place) digit as the
   remainder. For `482`, `482 % 10` is `2`.
2. `tens_digit = (number // 10) % 10`
   First, `number // 10` shifts all digits one place to the right (`482 // 10`
   becomes `48`). Next, `% 10` grabs the new rightmost digit (`48 % 10` is `8`).
3. Return `(tens_digit, ones_digit)`.

Edge cases:
- Single-digit number like `7`: `7 // 10` is `0`, so `(0, 7)`.
- `0` -> `(0, 0)`.
- Large numbers like `98765`: `(98765 // 10) % 10 == 6`, `98765 % 10 == 5`,
  so `(6, 5)`.

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
A retro arcade vault uses 3-digit PIN codes (integers from `100` to `999`).
Write `solve_three_digit_ops(number)` that extracts the hundreds, tens, and
ones digits using ONLY `//` and `%` (no `str()`!), and returns a 2-tuple:
    `(digit_sum, reversed_number)`

Where:
- `digit_sum = hundreds + tens + ones`
- `reversed_number = ones * 100 + tens * 10 + hundreds`

Rules:
- Assume `number` is a 3-digit integer (`100 <= number <= 999`).
- Notice how arithmetic reversal naturally drops leading zeros! For example,
  reversing `500` gives `0 * 100 + 0 * 10 + 5 = 5`.
- Return `(digit_sum, reversed_number)` as two integers.

Examples:
- `solve_three_digit_ops(374)` -> `(14, 473)`   # 3+7+4 = 14, reversed = 473
- `solve_three_digit_ops(500)` -> `(5, 5)`      # 5+0+0 = 5, reversed = 5
- `solve_three_digit_ops(101)` -> `(2, 101)`    # palindrome!
- `solve_three_digit_ops(999)` -> `(27, 999)`

Hints:
- For a 3-digit number:
  * `hundreds = number // 100`
  * `tens = (number // 10) % 10`
  * `ones = number % 10`
"""

from __future__ import annotations


def example_last_two_digits(number: int) -> tuple[int, int]:
    """Return (tens_digit, ones_digit) of a non-negative integer using // and %."""
    # `% 10` isolates the last digit; `// 10` drops the last digit.
    ones_digit = number % 10
    tens_digit = (number // 10) % 10
    return (tens_digit, ones_digit)


def solve_three_digit_ops(number: int) -> tuple[int, int]:
    """Return (digit_sum, reversed_number) for a 3-digit integer (100..999)."""
    pass


if __name__ == "__main__":
    print("482 ->", example_last_two_digits(482))
    print("7   ->", example_last_two_digits(7))
    print("100 ->", example_last_two_digits(100))
