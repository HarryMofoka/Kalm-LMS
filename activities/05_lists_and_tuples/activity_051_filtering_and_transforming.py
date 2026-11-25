"""
Activity 051: Filtering & Transforming Lists
Difficulty: 51 / 132

Context:
    Data pipelines constantly clean bad measurements and scale valid ones into
    a standard range (like normalizing exam percentages `0..100` into `0.0..1.0`
    for machine learning or grading systems)—all without corrupting the original
    raw dataset.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Square All Numbers (Non-Mutating)
===============================================================================
Problem:
    Return a NEW list containing the square (`x * x`) of every number in
    `numbers`. Do NOT modify `numbers` in place.

Step-by-Step Explanation:
    1. Build a brand-new list via a list comprehension `[x * x for x in numbers]`
       (or start with `result = []` and `.append(x * x)`).
    2. Returning a new list guarantees the caller's original list stays intact!
    3. Empty input returns `[]`.

Edge Cases:
    - `[1, -2, 0, 5]` -> `[1, 4, 0, 25]`
    - `[]`            -> `[]`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Filter & Normalize Exam Scores
===============================================================================
Problem:
    Implement `solve_normalize_scores(scores: list[int | float]) -> list[float]`.
    Given a list of raw numeric scores:
      1. Filter out invalid readings—keep ONLY scores in the inclusive range
         `0 <= score <= 100`.
      2. Normalize each valid score to the `[0.0, 1.0]` scale by dividing by
         `100` and rounding to 2 decimal places: `round(score / 100, 2)`.
      3. Preserve the original order of valid scores and do NOT mutate `scores`.

Examples:
    - `[-5, 0, 50, 87, 100, 120]` -> `[0.0, 0.5, 0.87, 1.0]`
    - `[33.3, 66.7, -1, 101]`     -> `[0.33, 0.67]`
    - `[-10, 150, 200]`           -> `[]`
    - `[]`                        -> `[]`

Edge-Case Hints:
    - Both boundary scores `0` and `100` are VALID (inclusive `<=`, not `<`).
    - Make sure `0` becomes `0.0` (a float, which `0 / 100` produces naturally).
    - Never mutate `scores` (e.g., do not call `scores.remove(...)` while looping!).
"""

from __future__ import annotations


def example_square_all(numbers: list[int | float]) -> list[int | float]:
    """Return a new list containing the square of each number in `numbers`."""
    return [num * num for num in numbers]


def solve_normalize_scores(scores: list[int | float]) -> list[float]:
    """Keep scores in [0, 100], divide by 100, round to 2 decimals, without mutating."""
    pass


if __name__ == "__main__":
    original = [1, -3, 0, 4]
    print("Original:", original)
    print("Squared :", example_square_all(original))
    print("Intact? :", original)
