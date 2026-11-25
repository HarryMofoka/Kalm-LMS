"""
Activity 096 — Dynamic Programming Intro  [Unlocks Checkpoint 16!]
Difficulty: 96 / 132

Context:
    Dynamic Programming (DP) sounds intimidating, yet it is simply:
    **"Store the answers to smaller subproblems in a table so you never compute
    the same subproblem twice."**
    You start with a tiny 1D table (Climbing Stairs) and level up directly into
    a classic 2D DP table (Longest Common Subsequence — used in `git diff` and
    DNA sequence alignment!).

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Implement `example_climb_stairs(n)`: you are climbing a staircase of `n`
    steps, taking either `1` or `2` steps at a time. Return the number of
    distinct ways to reach the top (`0` if `n <= 0`).

Step-by-Step Explanation:
    1. To land on step `i`, you MUST have jumped from step `i - 1` (1 step) or
       step `i - 2` (2 steps).
    2. Recurrence: `dp[i] = dp[i - 1] + dp[i - 2]`!
    3. Base cases: `dp[1] = 1`, `dp[2] = 2`.
    4. Filling the table bottom-up takes O(n) time (whereas naive recursion
       takes exponential $O(2^n)$ time!).

Edge Cases:
    - `n <= 0` -> `0`
    - `n == 1` -> `1`
    - `n == 2` -> `2`
    - `n == 5` -> `8`

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem:
    Implement `solve_longest_common_subsequence(str1, str2)` returning the
    **length** of the longest common subsequence (LCS) of `str1` and `str2`
    using a 2D bottom-up DP table!

    (Remember: a *subsequence* keeps relative order, but characters do NOT need
    to be contiguous. For `"ABCDGH"` and `"AEDFHR"`, `"ADH"` has length `3`.)

Step-by-Step 2D DP Table Blueprint:
    1. Let `m = len(str1)`, `n = len(str2)`.
    2. Allocate `dp = [[0] * (n + 1) for _ in range(m + 1)]`.
       Meaning: `dp[i][j]` = LCS length of `str1[:i]` and `str2[:j]`.
       Row `0` and column `0` are all `0` (empty prefix matches 0 characters).
    3. For `i` in `range(1, m + 1)`:
         For `j` in `range(1, n + 1)`:
           - If `str1[i - 1] == str2[j - 1]`:
             Both strings end with the same character -> extend the diagonal!
             `dp[i][j] = dp[i - 1][j - 1] + 1`
           - Else:
             Skip one character from either `str1` or `str2`, taking the max:
             `dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])`
    4. Return `dp[m][n]`.

Examples:
    solve_longest_common_subsequence("ABCDGH", "AEDFHR")  -> 3  ("ADH")
    solve_longest_common_subsequence("AGGTAB", "GXTXAYB") -> 4  ("GTAB")
    solve_longest_common_subsequence("abc", "def")        -> 0
    solve_longest_common_subsequence("", "python")        -> 0
    solve_longest_common_subsequence("python", "python")  -> 6
"""

from __future__ import annotations


def example_climb_stairs(n: int) -> int:
    """Return the number of distinct ways to climb ``n`` stairs (1 or 2 steps)."""
    if n <= 0:
        return 0
    if n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for step in range(3, n + 1):
        dp[step] = dp[step - 1] + dp[step - 2]
    return dp[n]


def solve_longest_common_subsequence(str1: str, str2: str) -> int:
    """Return the length of the longest common subsequence of ``str1`` and ``str2``."""
    pass


if __name__ == "__main__":
    for steps in range(0, 8):
        print(f"n={steps} -> {example_climb_stairs(steps)} ways")
