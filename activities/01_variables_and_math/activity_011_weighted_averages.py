"""
Activity 011: Weighted Averages & Grade Algebra
Difficulty: 11 / 132 (Rank 2 - Foundations Builder)

Context:
Almost every university syllabus weighs assignments, midterms, and final exams
differently — and the night before finals, every student asks the exact same
question: "What score do I need on the final to hit my target grade?" Let's
automate that calculation!

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
Write `example_weighted_score(homework, midterm, final)` that computes a
student's overall course percentage rounded to 2 decimal places using:
- Homework weight: 20% (`0.20`)
- Midterm weight:  30% (`0.30`)
- Final weight:    50% (`0.50`)

Step-by-step walkthrough:
1. Multiply each score by its decimal weight (note `0.20 + 0.30 + 0.50 == 1.0`):
       `overall = homework * 0.20 + midterm * 0.30 + final * 0.50`
2. Return `round(overall, 2)`.

Edge cases:
- If all three scores are equal (e.g., all `85`), the weighted average is `85.0`.
- Extra-credit scores over `100` (e.g., `105`) are handled naturally.

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
Write `solve_required_final_score(current_avg, current_weight, target_grade)`
to calculate the exact score a student needs on their final exam to achieve
`target_grade`, rounded to 2 decimal places.

Parameters:
- `current_avg`: student's average across all coursework so far (e.g., `82.0`).
- `current_weight`: decimal fraction of the total grade already completed
  (strictly between `0` and `1`, e.g., `0.60` means 60% of the course is done,
  leaving `1 - 0.60 = 0.40` for the final exam).
- `target_grade`: desired final course grade (e.g., `90.0`).

Derivation:
    current_avg * current_weight + required_final * (1 - current_weight) = target_grade
Solve for `required_final`:
    final_weight = 1 - current_weight
    required_final = (target_grade - current_avg * current_weight) / final_weight

Rules:
- Return `round(required_final, 2)`.
- Do NOT clamp the result to `0..100`! If the student needs `110.0` (impossible
  without extra credit) or `-30.0` (already guaranteed the target!), return that
  exact mathematical result rounded to 2 decimals.

Examples:
- `solve_required_final_score(80.0, 0.6, 85.0)` -> `92.5`
- `solve_required_final_score(90.0, 0.7, 90.0)` -> `90.0`
- `solve_required_final_score(70.0, 0.5, 90.0)` -> `110.0`
- `solve_required_final_score(95.0, 0.8, 70.0)` -> `-30.0`

Hints:
- Double-check your answer by plugging it back into:
  `current_avg * current_weight + answer * (1 - current_weight)` -> should equal
  `target_grade`!
"""

from __future__ import annotations


def example_weighted_score(homework: float, midterm: float, final: float) -> float:
    """Return weighted course grade (20% HW, 30% midterm, 50% final), rounded to 2 decimals."""
    overall = homework * 0.20 + midterm * 0.30 + final * 0.50
    return round(overall, 2)


def solve_required_final_score(
    current_avg: float, current_weight: float, target_grade: float
) -> float:
    """Return the final exam score needed to hit target_grade, rounded to 2 decimals."""
    pass


if __name__ == "__main__":
    print("HW=90, Mid=80, Final=85 ->", example_weighted_score(90, 80, 85))
    print("All 100s                ->", example_weighted_score(100, 100, 100))
