"""
Activity 028: `while` Loop Countdown & the Collatz Conjecture
Difficulty: 28 / 132 (Rank 3 - Loop Apprentice)

Context:
Use a `for` loop when you know in advance how many iterations you need. Use a
`while` loop when you keep repeating *until a condition becomes False*! One of
mathematics' most famous unsolved mysteries — the Collatz Conjecture (3n + 1
problem) — is the ultimate playground for `while` loops!

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
Write `example_halving_steps(n)` that counts how many times a positive integer
`n` must be integer-halved (`n //= 2`) until `n` reaches `1`. Raise `ValueError`
if `n < 1`.

Step-by-step walkthrough:
1. Guard clause: `if n < 1: raise ValueError("n must be >= 1")`.
   Why is this guard CRITICAL? If `n` were `0` or `-1`, `0 // 2` stays `0`
   forever! Always verify your `while` loop makes progress toward termination!
2. Initialize `steps = 0`.
3. Loop `while n > 1:`:
       `n //= 2`
       `steps += 1`
4. Return `steps`.
   Trace `n = 8`: `8 -> 4` (1) `-> 2` (2) `-> 1` (3) -> returns `3`.
   Trace `n = 7`: `7 -> 3` (1) `-> 1` (2) -> returns `2`.

Edge cases:
- `n = 1` -> `0` steps (already at `1`!).
- `n = 0` or `n = -5` -> raises `ValueError`.

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
The **Collatz Conjecture** takes any positive integer `n` and repeatedly applies:
- If `n` is **even**: `n = n // 2`
- If `n` is **odd**:  `n = 3 * n + 1`
until `n` reaches `1`! (Nobody has ever found a starting integer that fails to
reach `1`, yet no mathematician has ever proved it for all integers!)

Write `solve_collatz_steps(n)` that returns the exact number of steps required
for `n` to reach `1`.

Rules:
- Guard clause: if `n < 1`, `raise ValueError("n must be a positive integer")`.
- If `n == 1`, return `0` (already at 1, zero steps taken).
- Use integer division `// 2` (NOT `/ 2`) so `n` stays an exact integer!

Examples:
- `solve_collatz_steps(1)` -> `0`
- `solve_collatz_steps(2)` -> `1`     # 2 -> 1
- `solve_collatz_steps(6)` -> `8`     # 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
- `solve_collatz_steps(27)` -> `111`  # famous wild trajectory peaking at 9232!
- `solve_collatz_steps(0)` -> raises `ValueError`

Hints:
- Loop `while n != 1:` (or `while n > 1:`), update `n` based on `n % 2 == 0`,
  and increment `steps += 1` on every iteration.
"""

from __future__ import annotations


def example_halving_steps(n: int) -> int:
    """Return how many integer halvings (n //= 2) are needed to reduce n to 1."""
    if n < 1:
        raise ValueError(f"n must be >= 1, got {n}")
    steps = 0
    while n > 1:
        n //= 2
        steps += 1
    return steps


def solve_collatz_steps(n: int) -> int:
    """Return the number of Collatz steps needed for n >= 1 to reach 1."""
    pass


if __name__ == "__main__":
    for start in (1, 7, 8, 100):
        print(f"halving_steps({start}) -> {example_halving_steps(start)}")
