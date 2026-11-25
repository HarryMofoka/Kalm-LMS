# Module 08 — Algorithms and Problem Solving (Activities 085–096)

> **Difficulty Range:** `85 / 132` → `96 / 132`  
> **Checkpoints Unlocked:**
> - Complete **Activity 090** to unlock **Checkpoint 15**!
> - Complete **Activity 096** to unlock **Checkpoint 16**!

## Overview

Now that your Python foundations, validation contracts, and helper decomposition are sharp, it is time to master the **classic algorithmic patterns** that appear again and again in technical exams and real software systems.

Every activity walks you gently from a simpler sibling algorithm ("I Do") to a classic exam problem ("You Do") — covering linear scans, binary search, two pointers, stacks, sliding windows, Kadane's algorithm, sorting from scratch, Pascal's triangle, spiral matrices, merge sort with inversion counting, and 2D dynamic programming.

## Learning Goals

- Scan sequences cleanly using **linear search** and sentinel values (`-1`).
- Implement iterative **binary search** and lower-bound insertion points in $O(\log n)$ time.
- Solve sorted-sequence problems in linear time with **two pointers**.
- Model LIFO state with **stacks** (undo buffers, backspaces, nested brackets).
- Track dynamic subarrays and substrings using **sliding windows** and **Kadane's algorithm**.
- Build classic sorting algorithms from scratch (selection sort, insertion sort, merge sort) without mutating inputs.
- Construct 2D structures (**Pascal's triangle**, **clockwise spiral matrices**) and solve overlapping subproblems with **bottom-up DP** (**climbing stairs**, **longest common subsequence**).

## Activity Ladder

| Activity | File | Worked Example ("I Do") | Your Turn ("You Do") | Difficulty |
| :---: | :--- | :--- | :--- | :---: |
| **085** | [activity_085_linear_search_sentinels.py](activity_085_linear_search_sentinels.py) | `example_first_and_last_index` (first & last match sentinel) | `solve_find_all_indices` (all matching indices) | `85 / 132` |
| **086** | [activity_086_binary_search.py](activity_086_binary_search.py) | `example_binary_search` (index or `-1`) | `solve_lower_bound` (leftmost insertion index) | `86 / 132` |
| **087** | [activity_087_two_pointers.py](activity_087_two_pointers.py) | `example_sorted_two_sum` (two-pointer pair sum) | `solve_merge_sorted_lists` (two-pointer immutable merge) | `87 / 132` |
| **088** | [activity_088_stacks_and_undo.py](activity_088_stacks_and_undo.py) | `example_reverse_with_stack` (LIFO sequence reversal) | `solve_apply_backspaces` (editor `#` backspace simulator) | `88 / 132` |
| **089** | [activity_089_bracket_matching.py](activity_089_bracket_matching.py) | `example_valid_parens_only` (single `()` stack check) | `solve_valid_brackets` (nested `()[]{}` validation) | `89 / 132` |
| **090** | [activity_090_sliding_window.py](activity_090_sliding_window.py) | `example_longest_identical_run` (longest identical streak) | `solve_longest_unique_substring` (variable sliding window) **[Checkpoint 15!]** | `90 / 132` |
| **091** | [activity_091_kadanes_algorithm.py](activity_091_kadanes_algorithm.py) | `example_max_stock_profit` (single buy/sell max profit) | `solve_max_subarray_sum` (Kadane's algorithm + all-negatives) | `91 / 132` |
| **092** | [activity_092_selection_and_insertion_sort.py](activity_092_selection_and_insertion_sort.py) | `example_selection_sort` (selection sort returning new list) | `solve_insertion_sort_with_swaps` (`(sorted_list, swaps_count)`) | `92 / 132` |
| **093** | [activity_093_pascals_triangle.py](activity_093_pascals_triangle.py) | `example_pascal_row` (single 0-indexed Pascal row) | `solve_pascal_triangle` (first `n` rows of Pascal's triangle) | `93 / 132` |
| **094** | [activity_094_spiral_matrix.py](activity_094_spiral_matrix.py) | `example_read_spiral` (read matrix clockwise) | `solve_spiral_matrix` (build `n x n` spiral `1..n^2`) | `94 / 132` |
| **095** | [activity_095_merge_sort_and_inversions.py](activity_095_merge_sort_and_inversions.py) | `example_merge_sort` ($O(n \log n)$ merge sort) | `solve_count_inversions` ($O(n \log n)$ inversion count) | `95 / 132` |
| **096** | [activity_096_dynamic_programming_intro.py](activity_096_dynamic_programming_intro.py) | `example_climb_stairs` (1D bottom-up DP) | `solve_longest_common_subsequence` (2D DP table) **[Checkpoint 16!]** | `96 / 132` |

## How to Run the Tests

From the `ExamPrep` root directory:

```bash
python -m unittest activities/08_algorithms_and_problem_solving/test_08_algorithms_and_problem_solving.py -v
```

Or with `pytest`:

```bash
pytest activities/08_algorithms_and_problem_solving/test_08_algorithms_and_problem_solving.py -v
```

Run just the worked examples (should all pass out of the box):

```bash
python -m unittest activities.08_algorithms_and_problem_solving.test_08_algorithms_and_problem_solving.TestWorkedExamples -v
```

Run a single activity test while working on it (e.g., Activity 086):

```bash
pytest activities/08_algorithms_and_problem_solving/test_08_algorithms_and_problem_solving.py -k test_activity_086 -v
```
