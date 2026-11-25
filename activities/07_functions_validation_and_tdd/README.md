# Module 07 — Functions, Validation, and TDD (Activities 073–084)

> **Difficulty Range:** `73 / 132` → `84 / 132`  
> **Checkpoints Unlocked:**
> - Complete **Activity 078** to unlock **Checkpoint 13**!
> - Complete **Activity 084** to unlock **Checkpoint 14**!

## Overview

In exams and real engineering codebases, writing logic that "sort of works on the happy path" is never enough. Tests inspect **return values** (not printed output), verify **exact `TypeError` messages**, check that you **never mutate inputs**, pass edge cases like `bool` where an `int` is expected, and combine functions as building blocks.

This module builds a gentle, progressive ladder from pure functions and helper decomposition all the way to custom sort keys, higher-order functions, recursion vs. iteration, and property-based invariant checkers.

## Learning Goals

- Separate **pure computation** (returning values) from **side effects** (`print`).
- Decompose non-trivial tasks into small, testable helper functions.
- Design ergonomic APIs with **default arguments** and **keyword flags**.
- Enforce strict **input validation contracts** (including catching Python's `isinstance(True, int)` trap!).
- Guarantee **immutability** by returning new collections rather than mutating caller arguments.
- Build safe validation pipelines that collect **all** errors instead of stopping at the first.
- Master `key=` functions for multi-criteria sorting, higher-order callables, gentle recursion, explicit stacks, and property-based invariant verification.

## Activity Ladder

| Activity | File | Worked Example ("I Do") | Your Turn ("You Do") | Difficulty |
| :---: | :--- | :--- | :--- | :---: |
| **073** | [activity_073_pure_return_vs_print.py](activity_073_pure_return_vs_print.py) | `example_format_row` (pure string formatting vs printing wrapper) | `solve_build_banner_lines` (pure framed banner line list) | `73 / 132` |
| **074** | [activity_074_helper_decomposition.py](activity_074_helper_decomposition.py) | `example_vowel_density` (with `_is_vowel` helper) | `solve_word_length_stats` (using `clean_word` helper) | `74 / 132` |
| **075** | [activity_075_default_args_and_flags.py](activity_075_default_args_and_flags.py) | `example_greet_customer` (default title & excitement flag) | `solve_format_currency` (symbol, decimals, sign flags) | `75 / 132` |
| **076** | [activity_076_strict_input_validation.py](activity_076_strict_input_validation.py) | `example_count_vowels_strict` (exact `TypeError` contract) | `solve_merge_dicts` & `solve_is_prime` (rejecting `bool`!) | `76 / 132` |
| **077** | [activity_077_list_validation_and_immutability.py](activity_077_list_validation_and_immutability.py) | `example_validate_int_list` (validate ints + sorted copy) | `solve_sorted_strings_copy` (validate strings + sorted copy) | `77 / 132` |
| **078** | [activity_078_safe_validation_pipelines.py](activity_078_safe_validation_pipelines.py) | `example_collect_password_errors` (collect all violations) | `solve_validate_profile` → `(is_valid, errors)` **[Checkpoint 13!]** | `78 / 132` |
| **079** | [activity_079_custom_sort_keys.py](activity_079_custom_sort_keys.py) | `example_sort_by_second` (sort tuples by 2nd element) | `solve_sort_words_by_length` (sort by `(len(w), w)`, immutable) | `79 / 132` |
| **080** | [activity_080_multi_criteria_leaderboards.py](activity_080_multi_criteria_leaderboards.py) | `example_rank_students` (score desc, name asc) | `solve_rank_teams` (points desc, goal_diff desc, name asc) | `80 / 132` |
| **081** | [activity_081_higher_order_functions.py](activity_081_higher_order_functions.py) | `example_apply_transform` (custom `map` with callable check) | `solve_group_by` (group items by `key_fn`) | `81 / 132` |
| **082** | [activity_082_recursion_intro.py](activity_082_recursion_intro.py) | `example_recursive_sum` (recursive list sum) | `solve_is_palindrome_recursive` & `solve_fast_pow` | `82 / 132` |
| **083** | [activity_083_recursion_vs_iteration.py](activity_083_recursion_vs_iteration.py) | `example_flatten_recursive` (recursive arbitrary list flatten) | `solve_nested_sum_iterative` (explicit stack nested sum) | `83 / 132` |
| **084** | [activity_084_property_invariants_and_tdd.py](activity_084_property_invariants_and_tdd.py) | `example_verify_sort_invariants` (sort oracle checker) | `solve_verify_walk_invariants` (2D perimeter walk oracle) **[Checkpoint 14!]** | `84 / 132` |

## How to Run the Tests

From the `ExamPrep` root directory:

```bash
python -m unittest activities/07_functions_validation_and_tdd/test_07_functions_validation_and_tdd.py -v
```

Or with `pytest`:

```bash
pytest activities/07_functions_validation_and_tdd/test_07_functions_validation_and_tdd.py -v
```

Run just the worked examples (should all pass out of the box):

```bash
python -m unittest activities.07_functions_validation_and_tdd.test_07_functions_validation_and_tdd.TestWorkedExamples -v
```

Run a single activity test while working on it (e.g., Activity 073):

```bash
pytest activities/07_functions_validation_and_tdd/test_07_functions_validation_and_tdd.py -k test_activity_073 -v
```
