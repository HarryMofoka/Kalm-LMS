# Module 02: Conditionals, Logic & Validation

Welcome to **Module 02** of the ExamPrep Python Track! Now that you can calculate and format values, it is time to teach your programs how to make decisions, handle tricky edge cases gracefully, calculate progressive tiered brackets, and defend themselves against invalid types and bad data with `TypeError` and `ValueError`.

Every activity follows the **I Do / You Do** pattern:
1. Read the **Worked Example (`example_*`)** and study why each condition is ordered the way it is.
2. Implement the sibling **Your Turn (`solve_*`)** function right below it.
3. Run the unit tests to verify both normal paths and subtle boundary cases!

## Learning Goals

- Write crisp boolean expressions using comparison operators (`<`, `<=`, `>`, `>=`, `==`, `!=`) and logical operators (`and`, `or`, `not`).
- Choose between two-way `if/else`, mutually exclusive `if/elif/else` chains, and clean early-return guard clauses.
- Compute bounded values and order statistics (clamping, median of three) using pure comparisons.
- Translate multi-rule real-world specifications (leap years, triangle geometry, game rule tables, marginal tax brackets) without missing boundary conditions.
- Validate inputs defensively by raising `TypeError` (including catching Python's `bool`-is-an-`int` trap!) and `ValueError`.

## Activities Roadmap

| Activity # | File | Worked Example (`example_*`) | Your Turn (`solve_*`) | Difficulty |
| :---: | :--- | :--- | :--- | :--- |
| **013** | `activity_013_booleans_and_comparisons.py` | `example_is_positive` — Positive number check | `solve_is_even_and_positive` — Positive even integer check | 13 / 132 (Rank 2) |
| **014** | `activity_014_if_else_branching.py` | `example_ticket_price` — Minor vs adult admission | `solve_bonus_points` — Even/odd arcade score bonus | 14 / 132 (Rank 2) |
| **015** | `activity_015_elif_chains.py` | `example_letter_grade` — Numeric score to A–F grade | `solve_bmi_category` — BMI health category classifier | 15 / 132 (Rank 2) |
| **016** | `activity_016_logical_operators.py` | `example_can_ride_coaster` — Theme park safety rules | `solve_movie_discount` — Cinema discount eligibility | 16 / 132 (Rank 2) |
| **017** | `activity_017_clamping_and_median.py` | `example_clamp` — Clamp value without `min`/`max` | `solve_median_of_three` — Median of 3 without builtins | 17 / 132 (Rank 2) |
| **018** | `activity_018_guard_clauses.py` | `example_safe_divide` — Zero-safe division guard | `solve_safe_percent_change` — Zero-safe percentage change | 18 / 132 (Rank 2) |
| **019** | `activity_019_leap_year_calendar.py` | `example_is_leap_year` — Gregorian leap-year rule | `solve_days_in_month` — Exact days in `(year, month)` | 19 / 132 (Rank 3) |
| **020** | `activity_020_triangle_geometry.py` | `example_is_valid_triangle` — Strict triangle inequality | `solve_classify_triangle` — Equilateral/isosceles/scalene/invalid | 20 / 132 (Rank 3) |
| **021** | `activity_021_game_rules_matrix.py` | `example_rps_winner` — Rock-Paper-Scissors referee | `solve_rpsls_winner` — Rock-Paper-Scissors-Lizard-Spock | 21 / 132 (Rank 3) |
| **022** | `activity_022_tiered_pricing.py` | `example_parking_fee` — Progressive parking fee tiers | `solve_progressive_tax` — Marginal income tax brackets | 22 / 132 (Rank 3) |
| **023** | `activity_023_type_validation.py` | `example_validate_str_length` — String check with `TypeError` | `solve_validate_positive_int` — Positive `int` rejecting `bool` | 23 / 132 (Rank 3) |
| **024** | `activity_024_value_validation.py` | `example_validate_age` — Range-checked age validator | `solve_validate_date` — Full `(year, month, day)` validator | 24 / 132 (Rank 3) |

> **Checkpoint 03 Unlock:** Completing **Activity 018** unlocks **Checkpoint 03**!
>
> **Checkpoint 04 Unlock:** Completing **Activity 024** unlocks **Checkpoint 04**!

## How to Run Tests

From the `ExamPrep/` root folder:

```bash
# Run all tests (worked examples + your activities)
python -m unittest activities/02_conditionals_and_logic/test_02_conditionals_and_logic.py -v

# Run only the worked examples (should all pass right away)
python -m unittest activities.02_conditionals_and_logic.test_02_conditionals_and_logic.TestWorkedExamples -v

# Run only your own activity solutions
python -m unittest activities.02_conditionals_and_logic.test_02_conditionals_and_logic.TestYourActivities -v

# Run a single activity test (e.g., Activity 013)
python -m unittest activities.02_conditionals_and_logic.test_02_conditionals_and_logic.TestYourActivities.test_activity_013 -v
```

You can also run any activity file directly to see its worked example output:

```bash
python activities/02_conditionals_and_logic/activity_013_booleans_and_comparisons.py
```
