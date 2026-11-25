"""
Activity 047: Substring Scanning & Masking
Difficulty: 47 / 132

Context:
    Security-conscious backends constantly scan text for patterns and redact
    personally identifiable information (PII) like credit card numbers and email
    addresses before writing to logs or receipts.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Manual Non-Overlapping Substring Counter
===============================================================================
Problem:
    Count how many NON-OVERLAPPING times `pattern` occurs inside `text`, without
    using `str.count()`. Return `0` if `pattern` is empty.

Step-by-Step Explanation:
    1. Guard `if not pattern: return 0` (avoiding infinite loops when stepping by
       `len(pattern) == 0`!).
    2. Use an index `i = 0` and loop while `i <= len(text) - len(pattern)`:
         - If slice `text[i : i + len(pattern)] == pattern`, we found a match!
           Increment `count` and jump `i += len(pattern)` so matches never overlap.
         - Otherwise, advance `i += 1`.
    3. Example: `("aaaa", "aa")` finds index `0` (`"aa"`), jumps to `2` (`"aa"`),
       returning `2` (NOT `3`, which would be overlapping).

Edge Cases:
    - `("aaaa", "aa")`  -> `2`
    - `("ababab", "ab") -> `3`
    - `("hello", "")`   -> `0`
    - `("hi", "hello")` -> `0`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Mask Emails & Card Numbers Keeping Last 4
===============================================================================
Problem:
    Implement `solve_mask_sensitive(value: str) -> str`.
    Mask sensitive email addresses or card/account numbers while keeping the
    last 4 identifying characters/digits visible:

    Case A — Email address (contains `"@"`):
      - Split once on the first `"@"` into `local` and `domain`.
      - Keep `domain` completely visible.
      - For `local`:
          * If `len(local) > 4`: replace all characters before the last 4 with
            `"*"`, keeping `local[-4:]` visible.
          * If `len(local) <= 4`: mask EVERY character of `local` with `"*"`
            so short usernames are never leaked in full!
      - Return `f"{masked_local}@{domain}"`.

    Case B — Card / Account / Phone number (does NOT contain `"@"`):
      - Count all digits (`ch.isdigit()`) in `value`.
      - Keep the LAST 4 digits visible (if there are 4 or fewer digits total,
        leave all digits unchanged).
      - Replace every EARLIER digit with `"*"`.
      - Preserve all non-digit formatting characters (hyphens, spaces, etc.) in
        their exact positions!

Examples:
    - `"4111-2222-3333-4444"`     -> `"****-****-****-4444"`
    - `"1234 5678 9012 3456"`     -> `"**** **** **** 3456"`
    - `"9876543210"`              -> `"******3210"`
    - `"1234"`                    -> `"1234"`
    - `"student2026@uni.edu"`     -> `"*******2026@uni.edu"`
    - `"alice.smith@example.com"` -> `"*******mith@example.com"`
    - `"amy@uni.edu"`             -> `"***@uni.edu"`
    - `""`                        -> `""`

Edge-Case Hints:
    - For Case B, first count `total_digits = sum(1 for ch in value if ch.isdigit())`,
      then `to_mask = max(0, total_digits - 4)`. Walk left-to-right: each time
      you see a digit while `to_mask > 0`, output `"*"` and decrement `to_mask`;
      otherwise keep the character as-is!
"""

from __future__ import annotations


def example_count_substring(text: str, pattern: str) -> int:
    """Count non-overlapping occurrences of `pattern` in `text` manually."""
    if not pattern:
        return 0

    count = 0
    i = 0
    step = len(pattern)
    limit = len(text) - step

    while i <= limit:
        if text[i : i + step] == pattern:
            count += 1
            i += step  # Jump past this match to avoid overlaps.
        else:
            i += 1
    return count


def solve_mask_sensitive(value: str) -> str:
    """Mask an email address or card/account number, keeping the last 4 visible."""
    pass


if __name__ == "__main__":
    print("Non-overlapping 'aa' in 'aaaa':", example_count_substring("aaaa", "aa"))
    print("Non-overlapping 'aba' in 'ababa':", example_count_substring("ababa", "aba"))
