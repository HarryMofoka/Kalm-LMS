"""
Activity 031: FizzBuzz & Clean String-Building Variations
Difficulty: 31 / 132 (Rank 4 - Iteration Specialist)

Context:
FizzBuzz is the most famous coding interview warm-up in history — and when
interviewers want to see whether you write maintainable code, they immediately
add a third rule ("now add 'Bazz' for multiples of 7!"). If you wrote nested
`if/elif` branches for every combination, 3 rules explode into 8 branches and 4
rules into 16! Instead, building up an output string piece-by-piece handles
ANY number of rules with just ONE `if` per rule!

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
Write `example_fizzbuzz(n)` that returns a list of strings for `1` through `n`:
- Divisible by BOTH 3 and 5 -> `"FizzBuzz"`
- Divisible by 3 only       -> `"Fizz"`
- Divisible by 5 only       -> `"Buzz"`
- Otherwise                 -> `str(i)`
Return `[]` if `n <= 0`.

Step-by-step walkthrough:
1. Loop `for i in range(1, n + 1):`.
2. Start each number with an empty string `label = ""`.
3. `if i % 3 == 0: label += "Fizz"`
4. `if i % 5 == 0: label += "Buzz"` (NOT `elif`! Multiples of 15 trigger BOTH!)
5. Append `label or str(i)` — in Python, an empty string `""` is falsy, so if
   neither rule matched, `label or str(i)` evaluates cleanly to `str(i)`!

Edge cases:
- `n = 15` ends with `"FizzBuzz"`.
- `n <= 0` returns `[]`.

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
Write `solve_fizzbuzzbazz(n, fizz=3, buzz=5, bazz=7)` that extends FizzBuzz to
THREE customizable divisors (`fizz`, `buzz`, and `bazz`, all positive integers):
- If `i` is divisible by `fizz`, append `"Fizz"` to the item's label.
- If `i` is divisible by `buzz`, append `"Buzz"` to the item's label.
- If `i` is divisible by `bazz`, append `"Bazz"` to the item's label.
- If none of the three divide `i`, use `str(i)`.

Return the list of `n` strings for `i = 1..n` (or `[]` if `n <= 0`).

Rules:
- Keep the exact order: `"Fizz"` before `"Buzz"` before `"Bazz"`.
  (So with defaults `3, 5, 7`: `21 -> "FizzBazz"`, `35 -> "BuzzBazz"`,
  `105 -> "FizzBuzzBazz"`!)
- Must work with custom divisor arguments too, such as
  `solve_fizzbuzzbazz(12, fizz=2, buzz=3, bazz=4)`!

Examples:
- `solve_fizzbuzzbazz(7)` -> `["1", "2", "Fizz", "4", "Buzz", "Fizz", "Bazz"]`
- `solve_fizzbuzzbazz(0)` -> `[]`
- `solve_fizzbuzzbazz(6, fizz=2, buzz=3, bazz=4)`
  -> `["1", "Fizz", "Buzz", "FizzBazz", "5", "FizzBuzz"]`

Hints:
- Notice how effortless this becomes with the string-building pattern from the
  worked example: just three independent `if` statements!
"""

from __future__ import annotations


def example_fizzbuzz(n: int) -> list[str]:
    """Return classic FizzBuzz strings for 1..n (or [] if n <= 0)."""
    result: list[str] = []
    for i in range(1, n + 1):
        label = ""
        if i % 3 == 0:
            label += "Fizz"
        if i % 5 == 0:
            label += "Buzz"
        # Empty string is falsy, so `label or str(i)` falls back to the number.
        result.append(label or str(i))
    return result


def solve_fizzbuzzbazz(
    n: int, fizz: int = 3, buzz: int = 5, bazz: int = 7
) -> list[str]:
    """Return customizable Fizz/Buzz/Bazz labels for 1..n (or [] if n <= 0)."""
    pass


if __name__ == "__main__":
    print("FizzBuzz(15):", example_fizzbuzz(15))
