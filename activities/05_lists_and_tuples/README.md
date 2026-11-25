# Module 05: Lists & Tuples (Activities 049–060)

Build rock-solid mastery over Python's ordered sequences—from manual traversals without built-ins and non-mutating transformations to rotations, chunking, prefix sums, sliding windows, 2D matrices, coordinate tuples, and aliasing-free grid navigation.

## Learning Goals

- Accumulate lengths, sums, and extremes manually without relying on `len()`, `sum()`, `min()`, or `max()`.
- Transform, filter, deduplicate, rotate, and chunk lists cleanly without mutating caller inputs.
- Apply $O(n)$ algorithmic patterns—prefix sums and sliding windows—that show up constantly in timed exams.
- Work confidently with tuples, 2D nested lists, matrices (transpose & diagonals), Manhattan distances, and 4-directional grid neighbors.
- Avoid the notorious `[[0] * cols] * rows` shallow-reference aliasing trap.

## Activities Roadmap

| Activity | File | Worked Example ("I Do") | Your Turn ("You Do") | Difficulty |
| :---: | :--- | :--- | :--- | :---: |
| **049** | `activity_049_manual_length_and_sum.py` | Manual length without `len()` | Sum positive even numbers without `sum()` | `49 / 132` |
| **050** | `activity_050_finding_extremes.py` | Find minimum without `min()` | Find `(min, max)` tuple in one pass (`None` if empty) | `50 / 132` |
| **051** | `activity_051_filtering_and_transforming.py` | Squares of a list | Filter & normalize scores in `[0, 100]` | `51 / 132` |
| **052** | `activity_052_deduplication.py` | Unique elements preserving order | Remove consecutive duplicates (run dedup) | `52 / 132` |
| **053** | `activity_053_slicing_and_rotation.py` | Rotate list left by 1 | Rotate right by `k` (`k > len`, new list) | `53 / 132` |
| **054** | `activity_054_chunking_and_pairing.py` | Pair two lists into tuples | Split list into fixed-size chunks | `54 / 132` |
| **055** | `activity_055_prefix_sums.py` | Build running prefix sums | Range sum queries using prefix sums | `55 / 132` |
| **056** | `activity_056_sliding_window.py` | Max sum of `k` consecutive items | Moving average of window `k` | `56 / 132` |
| **057** | `activity_057_flattening_and_nested.py` | Flatten 1-level 2D list | Row sums & column sums of a matrix | `57 / 132` |
| **058** | `activity_058_matrix_transpose_diagonals.py` | Transpose rectangular matrix | Main & anti-diagonal sums of square matrix | `58 / 132` |
| **059** | `activity_059_coordinate_tuples.py` | Nearest `(x, y)` point to origin | Total Manhattan distance across waypoints | `59 / 132` |
| **060** | `activity_060_grid_creation_neighbors.py` | Build 2D grid without aliasing bug | Count 4-directional live neighbors of `(r, c)` | `60 / 132` |

## Checkpoints

> **Checkpoint 09 Unlocked after Activity 054!**
> Once Activities 049–054 pass, you have mastered core 1D list/tuple manipulation, non-mutating transforms, rotation, and chunking.

> **Checkpoint 10 Unlocked after Activity 060!**
> Once Activities 055–060 pass, you can tackle prefix sums, sliding windows, 2D matrices, coordinates, and grid-neighbor problems with confidence!

## How to Run Tests

From inside the `ExamPrep/` directory:

```bash
# Run all tests in Module 05 with unittest
python -m unittest activities/05_lists_and_tuples/test_05_lists_and_tuples.py -v

# Run ONLY the worked examples (should all PASS right away)
python -m unittest activities.05_lists_and_tuples.test_05_lists_and_tuples.TestWorkedExamples -v

# Run ONLY your activities (starts red -> turn them green!)
python -m unittest activities.05_lists_and_tuples.test_05_lists_and_tuples.TestYourActivities -v

# Or using pytest
pytest activities/05_lists_and_tuples/test_05_lists_and_tuples.py -v
```
