"""
Activity 029: Digit Loops with `while`
Difficulty: 29 / 132 (Rank 3 - Loop Apprentice)

Context:
Back in Activity 007, we extracted digits from a fixed 3-digit number. What if
an integer could have 1 digit, 7 digits, or 50 digits? Combine `% 10` and `// 10`
inside a `while` loop to peel digits off ANY integer of ANY length!

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
Write `example_count_digits(n)` that returns how many base-10 digits the integer
`n` has (ignoring any negative sign), using a `while` loop and NO `str()`!

Step-by-step walkthrough:
1. Handle the sneaky special case `n == 0`:
   If you just ran `while n > 0:`, then `0` would execute 0 iterations and
   wrongly say `0` has zero digits! In reality, `0` has `1` digit!
       `if n == 0: return 1`
2. Strip the minus sign for negative integers: `remaining = abs(n)`.
3. Loop `while remaining > 0:`:
       `remaining //= 10`
       `count += 1`
   Each `//= 10` chops off one digit until nothing is left (`remaining == 0`).
4. Return `count`.

Edge cases:
- `0` -> `1` (the #1 most forgotten edge case in digit loops!).
- `-905` -> `3` (negative sign is NOT a digit!).
- `100000` -> `6`.

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
Write `solve_digit_stats(n)` using a `while` loop with `% 10` and `// 10`
(NO `str()` conversion!) to compute TWO statistics about the digits of `n`,
returned as a 2-tuple:
    `(digit_sum, even_digit_count)`

Where:
- `digit_sum`: the sum of all digits in `abs(n)`.
- `even_digit_count`: how many digits in `abs(n)` are even (`0, 2, 4, 6, 8`).

Rules:
- Ignore any minus sign (`abs(n)`).
- Special case `n == 0`: `0` has one digit (`0`), whose sum is `0`, and `0` IS
  an even digit (`0 % 2 == 0`), so `solve_digit_stats(0)` MUST return `(0, 1)`!

Examples:
- `solve_digit_stats(4823)` -> `(17, 3)`   # 4+8+2+3=17; even digits: 4, 8, 2
- `solve_digit_stats(-205)` -> `(7, 2)`    # 2+0+5=7; even digits: 2, 0
- `solve_digit_stats(0)` -> `(0, 1)`       # digit 0 is even!
- `solve_digit_stats(13579)` -> `(25, 0)`  # all odd digits
- `solve_digit_stats(8)` -> `(8, 1)`

Hints:
- Handle `if n == 0: return (0, 1)` cleanly at the top!
- Inside `while remaining > 0:`:
  `digit = remaining % 10`, update `digit_sum`, check `if digit % 2 == 0`, then
  chop the digit with `remaining //= 10`!
"""

from __future__ import annotations


def example_count_digits(n: int) -> int:
    """Return the number of decimal digits in integer n using a while loop."""
    if n == 0:
        return 1
    remaining = abs(n)
    count = 0
    while remaining > 0:
        remaining //= 10
        count += 1
    return count


def solve_digit_stats(n: int) -> tuple[int, int]:
    """Return (digit_sum, even_digit_count) for integer n using a while loop."""
    pass


if __name__ == "__main__":
    for sample in (0, 7, 4823, -90500):
        print(f"count_digits({sample}) -> {example_count_digits(sample)}")
