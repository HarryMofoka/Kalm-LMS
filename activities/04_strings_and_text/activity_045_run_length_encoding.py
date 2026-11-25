"""
Activity 045: Run-Length Encoding & Decoding
Difficulty: 45 / 132

Context:
    Run-Length Encoding (RLE) is one of the oldest data compression schemes—used
    in fax machines, bitmap graphics, and classic coding exams. It replaces runs
    of consecutive identical characters with `<character><count>`.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — RLE Compression
===============================================================================
Problem:
    Compress a string `text` by replacing each maximal run of consecutive
    identical characters with the character followed by its run length.
    Example: `"aaabbc"` -> `"a3b2c1"`. Return `""` for an empty string.

Step-by-Step Explanation:
    1. Handle empty input early: `if not text: return ""`.
    2. Track `current_char = text[0]` and `run_length = 1`.
    3. Iterate through `text[1:]`:
         - If `ch == current_char`, increment `run_length`.
         - Otherwise, flush `f"{current_char}{run_length}"` to a list, reset
           `current_char = ch`, and reset `run_length = 1`.
    4. CRITICAL STEP: After the loop ends, flush the FINAL run! Forgetting the
       last run is the #1 bug in RLE implementations.

Edge Cases:
    - `"aaabbc"`     -> `"a3b2c1"`
    - `"aabaa"`      -> `"a2b1a2"` (non-adjacent `'a'` runs stay separate!)
    - `"a" * 12`     -> `"a12"`    (multi-digit run count!)
    - `"x"`          -> `"x1"`
    - `""`           -> `""`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — RLE Decompression
===============================================================================
Problem:
    Implement `solve_rle_decompress(encoded: str) -> str`.
    Decompress an RLE-encoded string back to its original text.
    You may assume `encoded` is valid RLE where each run consists of ONE
    non-digit character followed by ONE OR MORE ASCII digits (`'0'`–`'9'`).

Examples:
    - `"a3b2c1"`   -> `"aaabbc"`
    - `"a12b2"`    -> `"aaaaaaaaaaaabb"`  (WATCH OUT: multi-digit count `12`!)
    - `"a2b1a2"`   -> `"aabaa"`
    - `" 3!2"`     -> `"   !!"`           (spaces and punctuation can repeat too)
    - `"x1"`       -> `"x"`
    - `""`         -> `""`

Edge-Case Hints:
    - Do NOT assume counts are always 1 digit (`encoded[i + 1]`)! That fails on
      `"a12b2"` or `"z100"`.
    - Use a `while i < len(encoded):` loop:
        1. Read `ch = encoded[i]`, advance `i += 1`.
        2. Read all consecutive digits into `num_start = i; while i < n and encoded[i].isdigit(): i += 1`.
        3. Convert `int(encoded[num_start:i])` and append `ch * count`.
"""

from __future__ import annotations


def example_rle_compress(text: str) -> str:
    """Compress `text` using Run-Length Encoding (`"aaabbc"` -> `"a3b2c1"`)."""
    if not text:
        return ""

    parts: list[str] = []
    current_char = text[0]
    run_length = 1

    for ch in text[1:]:
        if ch == current_char:
            run_length += 1
        else:
            parts.append(f"{current_char}{run_length}")
            current_char = ch
            run_length = 1

    # Flush the final run that was active when the loop ended.
    parts.append(f"{current_char}{run_length}")
    return "".join(parts)


def solve_rle_decompress(encoded: str) -> str:
    """Decompress a Run-Length Encoded string (`"a3b2c1"` -> `"aaabbc"`)."""
    pass


if __name__ == "__main__":
    for sample in ["aaabbc", "aabaa", "x", "a" * 12, ""]:
        print(f"{sample!r:16} -> {example_rle_compress(sample)!r}")
