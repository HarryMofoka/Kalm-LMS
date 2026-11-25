"""
Activity 014: Two-Way `if / else` Branching
Difficulty: 14 / 132 (Rank 2 - Decision Maker)

Context:
Forks in the road appear everywhere in code: member vs. guest pricing, dark mode
vs. light mode, pass vs. fail. A two-way `if / else` guarantees that EXACTLY
one of two paths executes for every possible input.

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
A science museum charges `$10` for minors (under 18) and `$18` for adults
(18 and older). Write `example_ticket_price(age)` returning the integer ticket
price.

Step-by-step walkthrough:
1. Check the boundary carefully: "under 18" means strictly `< 18` (so a
   17-year-old pays `$10`, while an 18-year-old pays `$18`!).
2. If `age < 18`, return `10`.
3. Otherwise (`else`), return `18`.

Edge cases:
- Boundary value `age = 17` -> `10`.
- Boundary value `age = 18` -> `18` (off-by-one bugs almost always happen right
  on the boundary!).
- `age = 0` (infant) -> `10`.

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
In an arcade pinball bonus round, your final bonus depends on whether your
`score` is even or odd! Write `solve_bonus_points(score)` that applies:
- If `score` is **even** (`score % 2 == 0`): double the score and add 10
      `score * 2 + 10`
- If `score` is **odd**: triple the score and subtract 5
      `score * 3 - 5`

Rules:
- Works for positive, zero, AND negative integer scores!
  (Note: in Python, `0 % 2 == 0` so `0` is even; `-4 % 2 == 0` so `-4` is even;
  `-3 % 2 == 1` so `-3` is odd!)
- Return the resulting integer.

Examples:
- `solve_bonus_points(10)` -> `30`   # even: 10 * 2 + 10
- `solve_bonus_points(7)` -> `16`    # odd:  7 * 3 - 5
- `solve_bonus_points(0)` -> `10`    # even: 0 * 2 + 10
- `solve_bonus_points(1)` -> `-2`    # odd:  1 * 3 - 5
- `solve_bonus_points(-3)` -> `-14`  # odd:  -3 * 3 - 5

Hints:
- Always test parity with `score % 2 == 0` rather than `score % 2 == 1` (even
  though Python handles negatives cleanly, `== 0` is crystal clear across all
  languages!).
"""

from __future__ import annotations


def example_ticket_price(age: int) -> int:
    """Return 10 for minors (age < 18) and 18 for adults (age >= 18)."""
    if age < 18:
        return 10
    else:
        return 18


def solve_bonus_points(score: int) -> int:
    """Return score*2 + 10 if score is even, or score*3 - 5 if score is odd."""
    pass


if __name__ == "__main__":
    print("Age 12 ticket:", example_ticket_price(12))
    print("Age 18 ticket:", example_ticket_price(18))
