# Module 01: Variables, Math & Formatting

Welcome to **Module 01** of the ExamPrep Python Track! This module takes you from your very first f-string and arithmetic expressions all the way to modulo wrap-around, ceiling division tricks, weighted averages, and crisp column-aligned receipt formatting.

Every activity follows the **I Do / You Do** pattern:
1. Study the fully commented **Worked Example (`example_*`)** in the file and run the file directly to see it in action.
2. Implement the sibling **Your Turn (`solve_*`)** function right below it.
3. Run the unit tests to confirm your solution passes every normal case and edge case!

## Learning Goals

- Build readable dynamic strings using Python f-strings and format specifiers (`<`, `>`, `.2f`).
- Master core numeric operators: `+`, `-`, `*`, `/`, integer floor division `//`, remainder `%`, and exponentiation `**`.
- Extract digits and wrap values around modular cycles (like 24-hour clocks) without string hacks.
- Compute ceiling division (`(n + k - 1) // k`) without importing `math.ceil`.
- Translate multi-step real-world formulas (tips, taxes, Euclidean distance, compound interest, weighted grades) into clean, bug-free functions.

## Activities Roadmap

| Activity # | File | Worked Example (`example_*`) | Your Turn (`solve_*`) | Difficulty |
| :---: | :--- | :--- | :--- | :--- |
| **001** | `activity_001_fstring_greeting.py` | `example_welcome_banner` — Language welcome message | `solve_gamer_badge` — Formatted RPG player badge | 1 / 132 (Rank 1) |
| **002** | `activity_002_basic_arithmetic.py` | `example_rectangle_metrics` — Rectangle perimeter & area | `solve_trapezoid_and_triangle` — Triangle & trapezoid areas | 2 / 132 (Rank 1) |
| **003** | `activity_003_unit_conversion.py` | `example_celsius_to_fahrenheit` — Temperature conversion | `solve_trip_speed_conversion` — Kilometers to miles & mph | 3 / 132 (Rank 1) |
| **004** | `activity_004_floor_div_and_modulo.py` | `example_minutes_to_hours` — Minutes to `(hrs, mins)` | `solve_seconds_to_dhms` — Seconds to `(d, h, m, s)` | 4 / 132 (Rank 1) |
| **005** | `activity_005_rounding_and_percentages.py` | `example_discounted_price` — Store discount calculator | `solve_bill_split` — Restaurant tax, tip & per-diner split | 5 / 132 (Rank 1) |
| **006** | `activity_006_powers_and_distance.py` | `example_hypotenuse` — Right-triangle hypotenuse | `solve_euclidean_distance` — 2D coordinate distance | 6 / 132 (Rank 1) |
| **007** | `activity_007_digit_extraction.py` | `example_last_two_digits` — Tens & ones digit extractor | `solve_three_digit_ops` — 3-digit sum & arithmetic reverse | 7 / 132 (Rank 2) |
| **008** | `activity_008_clock_modulo_wrap.py` | `example_clock_hours` — 24-hour clock hour wrap | `solve_clock_with_rollover` — 24-hour minute addition + day rollover | 8 / 132 (Rank 2) |
| **009** | `activity_009_interest_and_rates.py` | `example_simple_interest` — Simple interest & total | `solve_compound_interest` — Periodic compound interest | 9 / 132 (Rank 2) |
| **010** | `activity_010_ceiling_division.py` | `example_boxes_needed` — Packing boxes without `math.ceil` | `solve_bus_seating` — Buses needed & leftover empty seats | 10 / 132 (Rank 2) |
| **011** | `activity_011_weighted_averages.py` | `example_weighted_score` — Weighted course average | `solve_required_final_score` — Required score on final exam | 11 / 132 (Rank 2) |
| **012** | `activity_012_formatted_receipts.py` | `example_price_line` — Aligned single receipt line | `solve_mini_receipt` — Multi-line aligned cafe receipt | 12 / 132 (Rank 2) |

> **Checkpoint 01 Unlock:** Completing **Activity 006** unlocks **Checkpoint 01**!
>
> **Checkpoint 02 Unlock:** Completing **Activity 012** unlocks **Checkpoint 02**!

## How to Run Tests

From the `ExamPrep/` root folder:

```bash
# Run all tests (worked examples + your activities)
python -m unittest activities/01_variables_and_math/test_01_variables_and_math.py -v

# Run only the worked examples (should all pass right away)
python -m unittest activities.01_variables_and_math.test_01_variables_and_math.TestWorkedExamples -v

# Run only your own activity solutions
python -m unittest activities.01_variables_and_math.test_01_variables_and_math.TestYourActivities -v

# Run a single activity test (e.g., Activity 001)
python -m unittest activities.01_variables_and_math.test_01_variables_and_math.TestYourActivities.test_activity_001 -v
```

You can also run any activity file directly to see its worked example output:

```bash
python activities/01_variables_and_math/activity_001_fstring_greeting.py
```
