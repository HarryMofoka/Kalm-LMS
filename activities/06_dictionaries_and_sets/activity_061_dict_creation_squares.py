"""
Activity 061: Dictionary Creation & Squares Map
Difficulty: 61 / 132

Context:
    Lookup tables are the bread and butter of fast Python code: precomputing a
    mapping from keys to values lets you answer lookups in $O(1)$ time. Here we
    warm up with a classic Python exam favorite—`generate_squared_dict`—making
    sure positive, zero, AND negative inputs all behave cleanly.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Positive Squares Map (`1..n`)
===============================================================================
Problem:
    Given an integer `n`, return a dictionary mapping each integer `k` from `1`
    to `n` (inclusive) to `k * k`. If `n <= 0`, return an empty dictionary `{}`.

Step-by-Step Explanation:
    1. If `n <= 0`, `range(1, n + 1)` is already empty, so the dict
       comprehension `{k: k * k for k in range(1, n + 1)}` naturally returns `{}`.
    2. `range(1, n + 1)` includes `n` because Python's `range` stop bound is
       exclusive.

Edge Cases:
    - `4`  -> `{1: 1, 2: 4, 3: 9, 4: 16}`
    - `1`  -> `{1: 1}`
    - `0`  -> `{}`
    - `-3` -> `{}`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — `generate_squared_dict` (Positive, Zero & Negative)
===============================================================================
Problem:
    Implement `solve_generate_squared_dict(n: int) -> dict[int, int]`.
    Generate a dictionary mapping every integer from `n` towards `0` (excluding
    `0`) to its square:
      - If `n > 0`: keys `1, 2, ..., n`   (e.g., `3`  -> `{1: 1, 2: 4, 3: 9}`)
      - If `n == 0`: empty dictionary `{}`
      - If `n < 0`: keys `n, n + 1, ..., -1` (e.g., `-3` -> `{-3: 9, -2: 4, -1: 1}`)

Examples:
    - `3`  -> `{1: 1, 2: 4, 3: 9}`
    - `1`  -> `{1: 1}`
    - `0`  -> `{}`
    - `-1` -> `{-1: 1}`
    - `-3` -> `{-3: 9, -2: 4, -1: 1}`

Edge-Case Hints:
    - For `n < 0`, `range(n, 0)` counts UP from `n` to `-1` (e.g., `range(-3, 0)`
      yields `-3, -2, -1`).
    - Remember Python operator precedence: `-3 ** 2` evaluates to `-9`, whereas
      `k * k` or `(-3) ** 2` evaluates to `+9`! Inside a loop, `k * k` (or
      `k ** 2` on a variable `k`) always yields a positive square for negative `k`.
"""

from __future__ import annotations


def example_squares_map(n: int) -> dict[int, int]:
    """Return `{1: 1, 2: 4, ..., n: n*n}` for `n > 0`, or `{}` if `n <= 0`."""
    return {k: k * k for k in range(1, n + 1)}


def solve_generate_squared_dict(n: int) -> dict[int, int]:
    """Generate squared dict for positive (`1..n`), zero (`{}`), or negative (`n..-1`) `n`."""
    pass


if __name__ == "__main__":
    for val in [4, 1, 0, -2]:
        print(f"n={val:2} -> {example_squares_map(val)}")
