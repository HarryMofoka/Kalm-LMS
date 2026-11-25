# Module 09 — Shapes and ASCII Patterns (Activities 097–108)

> **Difficulty Range:** `97 / 132` → `108 / 132`  
> **Checkpoints Unlocked:**
> - Complete **Activity 102** to unlock **Checkpoint 17**!

## Overview

ASCII shape questions are one of the highest-yield, most predictable parts of Python programming exams — AND the easiest place to lose points to a single stray trailing space or off-by-one row formula!

Every single activity in this module teaches the **Draw → Index → Rule** method:

1. **Draw** a small example (`n = 3` or `n = 5`) on paper with spaces made visible (`·`).
2. **Index** every row `r` (and column `c`) in a tiny table counting leading spaces, symbols, inner spaces, and trailing padding.
3. **Rule** — write the exact closed-form formula from the table (`pad = n - i`, `stars = 2 * i - 1`, `dist = min(r, c, size - 1 - r, size - 1 - c)`), then code it in 5 clean lines!

## Learning Goals

- Apply **Draw → Index → Rule** systematically so you never guess loop bounds.
- Distinguish **unpadded variable-width shapes** (no trailing spaces, e.g., left triangles) from **constant-width centered shapes** (exact symmetric left & right padding, e.g., pyramids, diamonds, hourglasses).
- Master border rules (`r == 0`, `r == n - 1`, `c == 0`, `c == n - 1`), diagonal rules (`r == c`, `r + c == n - 1`), vertical mirroring (`top + top[-2::-1]`), distance-to-edge rules, and spiral string formatting.

## Activity Ladder

| Activity | File | Worked Example ("I Do") | Your Turn ("You Do") | Difficulty |
| :---: | :--- | :--- | :--- | :---: |
| **097** | [activity_097_solid_squares_and_rectangles.py](activity_097_solid_squares_and_rectangles.py) | `example_solid_square` (`n x n` solid square) | `solve_solid_rectangle` (`width x height` solid rectangle) | `97 / 132` |
| **098** | [activity_098_left_triangles.py](activity_098_left_triangles.py) | `example_left_star_triangle` (left `*` triangle) | `solve_create_number_triangle` (`['1', '22', '333']`) | `98 / 132` |
| **099** | [activity_099_inverted_and_right_triangles.py](activity_099_inverted_and_right_triangles.py) | `example_inverted_left_triangle` (inverted left triangle) | `solve_right_aligned_triangle` (right-aligned width `n`) | `99 / 132` |
| **100** | [activity_100_centered_star_pyramid.py](activity_100_centered_star_pyramid.py) | `example_pyramid_row` (single width `2n - 1` row) | `solve_create_pyramid` (centered `*` pyramid, width `2n - 1`) | `100 / 132` |
| **101** | [activity_101_centered_number_pyramid.py](activity_101_centered_number_pyramid.py) | `example_counting_pyramid` (`1..i` centered pyramid) | `solve_create_number_pyramid` (`['  1  ', ' 2 2 ', '3 3 3']`) | `101 / 132` |
| **102** | [activity_102_hollow_square_and_titled_box.py](activity_102_hollow_square_and_titled_box.py) | `example_bordered_box` (`+`, `-`, `|` hollow box) | `solve_create_hollow_square` & `solve_titled_box` **[Checkpoint 17!]** | `102 / 132` |
| **103** | [activity_103_symmetric_diamond.py](activity_103_symmetric_diamond.py) | `example_mirror_rows` (mirror top half cleanly) | `solve_create_diamond` (odd `n` centered `*` diamond) | `103 / 132` |
| **104** | [activity_104_symmetric_hourglass.py](activity_104_symmetric_hourglass.py) | `example_inverted_pyramid` (inverted `*` pyramid) | `solve_create_hourglass` (odd `n` centered `*` hourglass) | `104 / 132` |
| **105** | [activity_105_checkerboard_and_x_cross.py](activity_105_checkerboard_and_x_cross.py) | `example_checkerboard` (`(r + c) % 2` grid) | `solve_x_cross` (`r == c` or `r + c == n - 1`) | `105 / 132` |
| **106** | [activity_106_hollow_and_alphabet_diamond.py](activity_106_hollow_and_alphabet_diamond.py) | `example_hollow_star_diamond` (hollow `*` diamond) | `solve_create_alphabet_diamond` (`['  A  ', ' B B ', 'C   C', ...]`) | `106 / 132` |
| **107** | [activity_107_concentric_number_rings.py](activity_107_concentric_number_rings.py) | `example_edge_distance_grid` (`min(r, c, ...)` distances) | `solve_concentric_rings` (border `n` shrinking inward to `1`) | `107 / 132` |
| **108** | [activity_108_number_spiral_strings.py](activity_108_number_spiral_strings.py) | `example_format_number_grid` (compact & aligned formatting) | `solve_create_number_spiral` & `solve_create_spiral_string` | `108 / 132` |

## How to Run the Tests

From the `ExamPrep` root directory:

```bash
python -m unittest activities/09_shapes_and_ascii_patterns/test_09_shapes_and_ascii_patterns.py -v
```

Or with `pytest`:

```bash
pytest activities/09_shapes_and_ascii_patterns/test_09_shapes_and_ascii_patterns.py -v
```

Run just the worked examples (should all pass out of the box):

```bash
python -m unittest activities.09_shapes_and_ascii_patterns.test_09_shapes_and_ascii_patterns.TestWorkedExamples -v
```

Run a single activity test while working on it (e.g., Activity 100):

```bash
pytest activities/09_shapes_and_ascii_patterns/test_09_shapes_and_ascii_patterns.py -k test_activity_100 -v
```
