"""
Activity 090 — Sliding Window (Variable Size)  [Unlocks Checkpoint 15!]
Difficulty: 90 / 132

Context:
    Many substring and subarray problems ask for the "longest contiguous slice
    satisfying condition X". Checking every `(start, end)` slice takes $O(n^2)$
    or $O(n^3)$. A **variable-size sliding window** `[left, right]` expands
    `right` one step at a time and shrinks `left` only when the window breaks
    its rule — solving the whole problem in $O(n)$!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Implement `example_longest_identical_run(text)` that returns the length of
    the longest contiguous streak of the exact same character.

Step-by-Step Explanation:
    1. If `text` is empty, return `0`.
    2. Track `best = 1` and `current = 1`.
    3. For each index `i` from `1` to `len(text) - 1`:
       - If `text[i] == text[i - 1]`: extend the streak (`current += 1`).
       - Else: start a fresh streak (`current = 1`).
       - Update `best = max(best, current)`.
    4. Return `best`.

Edge Cases:
    - `""` -> `0`
    - `"a"` -> `1`
    - `"aaabbccccd"` -> `4` (`"cccc"`)
    - Case-sensitive: `"aAAa"` -> `2` (`"AA"`)

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem:
    Implement `solve_longest_unique_substring(text)` returning the LENGTH of
    the longest contiguous substring of `text` that contains NO repeating
    characters!

Step-by-Step Sliding Window Hint:
    1. Keep `last_seen: dict[str, int] = {}` (mapping each character to its
       most recent index), `left = 0`, and `best = 0`.
    2. For `right, ch in enumerate(text)`:
       - If `ch in last_seen and last_seen[ch] >= left`:
         jump `left = last_seen[ch] + 1` (shrink window past the duplicate!).
       - Update `last_seen[ch] = right`.
       - Update `best = max(best, right - left + 1)`.
    3. Return `best`.

Examples:
    solve_longest_unique_substring("abcabcbb") -> 3  ("abc")
    solve_longest_unique_substring("bbbbb")    -> 1  ("b")
    solve_longest_unique_substring("pwwkew")   -> 3  ("wke")
    solve_longest_unique_substring("dvdf")     -> 3  ("vdf")
    solve_longest_unique_substring("")         -> 0

Edge-Case Hints:
    - Watch out for `"abba"`! When `right = 3` sees `'a'`, `last_seen['a']` is
      `0`, which is `< left` (already `2`). Checking `last_seen[ch] >= left`
      prevents `left` from accidentally moving BACKWARDS!
"""

from __future__ import annotations


def example_longest_identical_run(text: str) -> int:
    """Return the length of the longest contiguous run of identical characters."""
    if not text:
        return 0

    best = 1
    current = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            current += 1
            if current > best:
                best = current
        else:
            current = 1
    return best


def solve_longest_unique_substring(text: str) -> int:
    """Return the length of the longest substring with all unique characters."""
    pass


if __name__ == "__main__":
    for sample in ["aaabbccccd", "abcd", "x", ""]:
        print(f"{sample!r:14} -> {example_longest_identical_run(sample)}")
