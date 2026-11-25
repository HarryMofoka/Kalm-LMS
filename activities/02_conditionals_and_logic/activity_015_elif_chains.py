"""
Activity 015: Chained `if / elif / else` Ranges
Difficulty: 15 / 132 (Rank 2 - Decision Maker)

Context:
Real-world categories rarely come in just two buckets — think letter grades
(A/B/C/D/F), hurricane categories (1–5), or BMI ranges. When you chain
`if / elif / else` in strict ascending or descending order, each branch only
needs ONE threshold check because previous branches already eliminated everything
earlier!

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
Write `example_letter_grade(score)` converting a numeric exam percentage into a
letter grade:
- `90` and above -> `"A"`
- `80` to `< 90` -> `"B"`
- `70` to `< 80` -> `"C"`
- `60` to `< 70` -> `"D"`
- below `60`     -> `"F"`

Step-by-step walkthrough:
1. Check thresholds strictly from highest down to lowest:
   - `if score >= 90:` -> `"A"`
   - `elif score >= 80:` -> `"B"` (we only reach here if `score < 90`!)
   - `elif score >= 70:` -> `"C"`
   - `elif score >= 60:` -> `"D"`
   - `else:` -> `"F"`
2. Why does order matter? If you checked `score >= 60` FIRST, then a score of
   `95` would match `>= 60` and wrongly receive a `"D"`!

Edge cases:
- Exact boundaries: `90 -> "A"`, `89.9 -> "B"`, `80 -> "B"`, `60 -> "D"`, `59.9 -> "F"`.
- Extra credit like `105` -> `"A"`.

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
A fitness clinic app computes Body Mass Index (BMI) and assigns a standard
health category. Write `solve_bmi_category(weight_kg, height_m)` where:
    `bmi = weight_kg / (height_m ** 2)`

Return one of these exact strings based on `bmi`:
- `bmi < 18.5`          -> `"Underweight"`
- `18.5 <= bmi < 25.0`  -> `"Normal"`
- `25.0 <= bmi < 30.0`  -> `"Overweight"`
- `bmi >= 30.0`         -> `"Obese"`

Rules:
- Assume `weight_kg > 0` and `height_m > 0`.
- Watch exact capitalization of the returned strings:
  `"Underweight"`, `"Normal"`, `"Overweight"`, `"Obese"`.
- Check the exact boundary values:
  * `bmi == 18.5` is `"Normal"` (NOT `"Underweight"`).
  * `bmi == 25.0` is `"Overweight"` (NOT `"Normal"`).
  * `bmi == 30.0` is `"Obese"` (NOT `"Overweight"`).

Examples:
- `solve_bmi_category(50, 1.75)` -> `"Underweight"`  (BMI ~ 16.33)
- `solve_bmi_category(70, 1.75)` -> `"Normal"`       (BMI ~ 22.86)
- `solve_bmi_category(85, 1.75)` -> `"Overweight"`   (BMI ~ 27.76)
- `solve_bmi_category(100, 1.75)` -> `"Obese"`       (BMI ~ 32.65)
- `solve_bmi_category(100, 2.0)` -> `"Overweight"`   (BMI == 25.0 exact boundary!)

Hints:
- If you check thresholds in ascending order (`< 18.5`, `< 25.0`, `< 30.0`,
  `else`), each `elif` needs only a single `<` comparison!
"""

from __future__ import annotations


def example_letter_grade(score: float) -> str:
    """Convert numeric score to letter grade ('A', 'B', 'C', 'D', or 'F')."""
    # Checking from highest threshold down ensures each elif implicitly excludes higher ranges.
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def solve_bmi_category(weight_kg: float, height_m: float) -> str:
    """Compute BMI and return 'Underweight', 'Normal', 'Overweight', or 'Obese'."""
    pass


if __name__ == "__main__":
    print("92 ->", example_letter_grade(92))
    print("80 ->", example_letter_grade(80))
    print("59.5 ->", example_letter_grade(59.5))
