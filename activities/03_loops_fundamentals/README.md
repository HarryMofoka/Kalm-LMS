# Module 03: Loops Fundamentals

Welcome to **Module 03** of the ExamPrep Python Track! Loops turn Python from a pocket calculator into a true problem-solving engine. Across these 12 activities you will master counting `for` loops, step ranges, additive & multiplicative accumulators, condition-driven `while` loops, infinite-loop guards, classic number-theory algorithms (Collatz, Fibonacci, Sieve of Eratosthenes, Euclidean GCD), and nested 2D loops.

Every activity follows the **I Do / You Do** pattern:
1. Study the **Worked Example (`example_*`)** and trace how loop state changes on every iteration.
2. Implement the sibling **Your Turn (`solve_*`)** function right below it.
3. Run the unit tests to verify normal inputs, boundary values, and error guards!

## Learning Goals

- Build counting, summing, and multiplying accumulators with `for` loops and `range(start, stop, step)`.
- Write safe `while` loops for unknown iteration counts (Collatz steps, digit peeling, financial payoff simulations) — including guards that prevent infinite loops!
- Apply clean loop design patterns (string building for FizzBuzzBazz, tuple state updates for Fibonacci and GCD).
- Optimize primality testing with the `sqrt(n)` loop bound (`d * d <= n`) and generate primes over intervals.
- Structure nested loops cleanly for 2D grids and unordered `(i, j)` pair scans (`i < j`).

## Activities Roadmap

| Activity # | File | Worked Example (`example_*`) | Your Turn (`solve_*`) | Difficulty |
| :---: | :--- | :--- | :--- | :--- |
| **025** | `activity_025_for_loop_counting.py` | `example_count_up` — Count `1..n` into a list | `solve_sum_to_n` — Sum `1..n` without `sum()` | 25 / 132 (Rank 3) |
| **026** | `activity_026_step_ranges_filtering.py` | `example_even_numbers` — Evens up to `n` via step range | `solve_sum_multiples_3_or_5` — Sum multiples of 3 or 5 below `limit` | 26 / 132 (Rank 3) |
| **027** | `activity_027_product_accumulator.py` | `example_integer_power` — Integer power via loop | `solve_factorial` — Iterative `n!` with `ValueError` guard | 27 / 132 (Rank 3) |
| **028** | `activity_028_while_countdown_collatz.py` | `example_halving_steps` — Halving count down to `1` | `solve_collatz_steps` — Collatz conjecture step counter | 28 / 132 (Rank 3) |
| **029** | `activity_029_while_digit_loops.py` | `example_count_digits` — Digit count via `while` loop | `solve_digit_stats` — Sum of digits & even-digit count | 29 / 132 (Rank 3) |
| **030** | `activity_030_running_totals_thresholds.py` | `example_days_to_goal` — Days to reach savings target | `solve_months_to_payoff` — Loan payoff months with interest | 30 / 132 (Rank 3) |
| **031** | `activity_031_fizzbuzz_variations.py` | `example_fizzbuzz` — Classic FizzBuzz list | `solve_fizzbuzzbazz` — Customizable FizzBuzzBazz list | 31 / 132 (Rank 4) |
| **032** | `activity_032_fibonacci_sequence.py` | `example_first_n_fibonacci` — First `n` Fibonacci numbers | `solve_fibonacci_up_to` — Fibonacci numbers `<= limit` | 32 / 132 (Rank 4) |
| **033** | `activity_033_divisors_and_primality.py` | `example_divisors` — Sorted list of positive divisors | `solve_is_prime` — Fast `sqrt(n)` primality test | 33 / 132 (Rank 4) |
| **034** | `activity_034_primes_in_range.py` | `example_count_primes_up_to` — Prime count via Sieve | `solve_primes_in_range` — All primes in `[low, high]` | 34 / 132 (Rank 4) |
| **035** | `activity_035_number_theory_loops.py` | `example_gcd` — Euclidean GCD `while` loop | `solve_lcm_and_fraction` — LCM & simplified fraction tuple | 35 / 132 (Rank 4) |
| **036** | `activity_036_nested_loop_grids.py` | `example_multiplication_row` — Single multiplication row | `solve_grid_and_pair_sums` — Full `n×n` grid & target pair count | 36 / 132 (Rank 4) |

> **Checkpoint 05 Unlock:** Completing **Activity 030** unlocks **Checkpoint 05**!
>
> **Checkpoint 06 Unlock:** Completing **Activity 036** unlocks **Checkpoint 06**!

## How to Run Tests

From the `ExamPrep/` root folder:

```bash
# Run all tests (worked examples + your activities)
python -m unittest activities/03_loops_fundamentals/test_03_loops_fundamentals.py -v

# Run only the worked examples (should all pass right away)
python -m unittest activities.03_loops_fundamentals.test_03_loops_fundamentals.TestWorkedExamples -v

# Run only your own activity solutions
python -m unittest activities.03_loops_fundamentals.test_03_loops_fundamentals.TestYourActivities -v

# Run a single activity test (e.g., Activity 025)
python -m unittest activities.03_loops_fundamentals.test_03_loops_fundamentals.TestYourActivities.test_activity_025 -v
```

You can also run any activity file directly to see its worked example output:

```bash
python activities/03_loops_fundamentals/activity_025_for_loop_counting.py
```
