"""
Activity 084 — Property-Based Invariants & TDD  [Unlocks Checkpoint 14!]
Difficulty: 84 / 132

Context:
    How do professional engineers test complex algorithms like sorting or 2D
    perimeter walks across hundreds of inputs without hand-typing every output?
    By checking **invariants** — mathematical properties that MUST hold for
    EVERY valid output! Writing an invariant verifier sharpens your edge-case
    instincts like nothing else.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Implement `example_verify_sort_invariants(original, result)` that checks
    whether `result` is a valid ascending sort of `original` and returns
    `(is_valid, violations)`.

Step-by-Step Explanation:
    A broken sort could return `[1, 2, 3]` for `[5, 5, 5]` (sorted, right
    length, WRONG elements!) or drop duplicates. So we check ALL THREE
    fundamental sort invariants:
      1. Same length: `len(result) == len(original)` -> else `"Length mismatch."`
      2. Same multiset of elements: `Counter(result) == Counter(original)` ->
         else `"Elements changed."`
      3. Non-decreasing order: `all(result[i] <= result[i + 1] for i in range(len(result) - 1))`
         -> else `"Not sorted in non-decreasing order."`
    Return `(len(violations) == 0, violations)`.

Edge Cases:
    - Both empty `[], []` -> `(True, [])`
    - Duplicates `[3, 1, 3]` vs `[1, 3, 3]` -> `(True, [])`
    - Duplicates dropped `[3, 1, 3]` vs `[1, 3]` -> fails BOTH length & elements!

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem:
    Implement `solve_verify_walk_invariants(path, expected_len)` to verify a
    closed 2D perimeter walk (like a clockwise `square_walk` or `rectangle_walk`
    around a grid border), where each cell is a `(row, col)` tuple of ints.

Check these 5 invariants in EXACT order and collect every violation message:
    1. **Expected length:**
       `len(path) == expected_len`
       -> else append `"Length mismatch."`
    2. **No duplicates:**
       Every coordinate in `path` is unique (`len(set(path)) == len(path)`).
       -> else append `"Duplicate coordinates found."`
    3. **Origin start (only checked when `expected_len > 0` and `len(path) > 0`):**
       `path[0] == (0, 0)`
       -> else append `"Walk must start at (0, 0)."`
    4. **Adjacent steps (checked for all consecutive pairs `(path[i], path[i+1])`):**
       Every consecutive pair has Manhattan distance 1:
       `abs(r1 - r2) + abs(c1 - c2) == 1`.
       -> else append `"Non-adjacent step found."` (append at most ONCE even if
          multiple steps jump!)
    5. **Closed loop (only checked when `len(path) > 1`):**
       The last cell `path[-1]` is also adjacent (Manhattan distance 1) to the
       first cell `path[0]`.
       -> else append `"Walk does not form a closed loop."`

Return:
    `(len(violations) == 0, violations)`

Examples:
    # Valid 2x2 square clockwise walk (length 4):
    solve_verify_walk_invariants([(0, 0), (0, 1), (1, 1), (1, 0)], 4)
        -> (True, [])

    # Valid empty walk (length 0) and 1x1 walk (length 1):
    solve_verify_walk_invariants([], 0)        -> (True, [])
    solve_verify_walk_invariants([(0, 0)], 1)  -> (True, [])

    # Diagonal jump and wrong start:
    solve_verify_walk_invariants([(0, 1), (1, 2)], 2)
        -> (False, [
            "Walk must start at (0, 0).",
            "Non-adjacent step found.",
            "Walk does not form a closed loop.",
        ])
"""

from __future__ import annotations

from collections import Counter


def example_verify_sort_invariants(
    original: list,
    result: list,
) -> tuple[bool, list[str]]:
    """Verify the three fundamental invariants of an ascending sort."""
    violations: list[str] = []

    if len(result) != len(original):
        violations.append("Length mismatch.")

    if Counter(result) != Counter(original):
        violations.append("Elements changed.")

    if any(result[i] > result[i + 1] for i in range(len(result) - 1)):
        violations.append("Not sorted in non-decreasing order.")

    return (len(violations) == 0, violations)


def solve_verify_walk_invariants(
    path: list[tuple[int, int]],
    expected_len: int,
) -> tuple[bool, list[str]]:
    """Verify closed 2D perimeter walk invariants and return ``(is_valid, violations)``."""
    pass


if __name__ == "__main__":
    orig = [3, 1, 2, 1]
    print("Good sort:", example_verify_sort_invariants(orig, [1, 1, 2, 3]))
    print("Bad sort:", example_verify_sort_invariants(orig, [1, 2, 3]))
