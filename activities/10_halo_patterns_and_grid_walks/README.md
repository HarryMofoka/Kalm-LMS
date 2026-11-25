# Module 10: Halo Patterns & Grid Walks (Activities 109–120)

Master 2D grid coordinates, border predicates, perimeter walks, modulo wrap-around runners, multi-runner collisions, and full inward spiral sweeps!

This module is the crown-jewel progression that takes you from basic `(row, col)` indexing all the way through — and **beyond** — the **Halo Patterns Workshop**, using the 5-step planning routine on every problem:

> **DRAW → INDEX → RULE → TEST → CODE**
>
> 1. **DRAW**: Sketch a tiny example (`3x3`, `4x3`, `5`-tall triangle, radius-`2` diamond).
> 2. **INDEX**: Write `(row, col)` on every cell. Rows increase downward; columns increase rightward.
> 3. **RULE / LEGS TABLE**: Express the outline as one crisp boolean predicate, or list each walk leg with its start, end, and corner ownership so no cell is ever visited twice.
> 4. **TEST**: Verify exact formatting (one space between cells, **zero trailing spaces**), perimeter length formulas, and uniqueness.
> 5. **CODE**: Translate the rule or legs table cleanly into Python.

## Learning Goals

- Build and format 2D grids with exact spacing and **zero trailing spaces**.
- Write rock-solid border predicates for squares, rectangles (including thin `4x1`, `1x3`, `1x1` shapes), thick frames, concentric double halos, left/right triangles, and Manhattan diamonds.
- Construct duplicate-free perimeter walks (clockwise, counter-clockwise, custom start cell, triangular, diamond, and inward spiral sweeps).
- Use Python's modulo operator (`%`) — including negative wrap-around — to animate single runners, glowing tails, and multi-runner collision detectors.

## Activities

| Activity | File | Worked Example ("I Do") | Your Turn ("You Do") | Difficulty |
|---|---|---|---|---|
| 109 | `activity_109_grid_indexing_and_format_row.py` | Coordinate label grid `"(r,c)"` | `format_row` & render 2D char grid (zero trailing spaces) | 109 / 132 |
| 110 | `activity_110_square_and_rectangle_halo.py` | `is_square_border` + `example_square_halo_lines` | `is_rectangle_border` + `solve_rectangle_halo_lines` (thin shapes!) | 110 / 132 |
| 111 | `activity_111_thick_border_and_double_halo.py` | Thick border square frame (thickness `k`) | Concentric double-halo square (`#` outer, `+` inner) | 111 / 132 |
| 112 | `activity_112_triangle_border_halos.py` | Left-aligned right triangle halo | Right-aligned mirrored triangle halo (zero trailing spaces) | 112 / 132 |
| 113 | `activity_113_diamond_manhattan_halo.py` | Filled Manhattan-distance diamond | Hollow diamond halo (`abs(r - mid) + abs(c - mid) == radius`) | 113 / 132 |
| 114 | `activity_114_clockwise_legs_walk.py` | Square clockwise walk (legs table) | Rectangle clockwise walk (`4x1`, `1x3`, `1x1`, zero duplicates) | 114 / 132 |
| 115 | `activity_115_ccw_and_custom_start_walks.py` | Counter-clockwise square walk from `(0, 0)` | Clockwise rectangle walk starting at ANY border cell | 115 / 132 |
| 116 | `activity_116_triangle_and_diamond_walks.py` | Right-triangle clockwise walk (`3h - 3` cells) | Diamond halo clockwise walk (`4 * radius` cells) | 116 / 132 |
| 117 | `activity_117_modulo_wrap_and_single_runner.py` | Square halo runner (returns formatted lines) | Rectangle runner with positive CW & negative CCW `steps` | 117 / 132 |
| 118 | `activity_118_ragged_triangle_runner_and_tail.py` | Ragged-grid triangle runner | Triangle runner with 3-cell glowing tail (`@`, `*`, `.`) | 118 / 132 |
| 119 | `activity_119_multi_runner_race_and_collision.py` | Simulate two runners at tick `t` | Find first collision step & cell on a rectangle halo | 119 / 132 |
| 120 | `activity_120_spiral_inward_walker.py` | Peel one clockwise outer ring `(top..bottom, left..right)` | Full inward spiral coordinate walk of an `m x n` grid | 120 / 132 |

## Checkpoints Unlocked

- **Checkpoint 18** — Unlocked upon completing **Activity 114** (mastery of border predicates & duplicate-free clockwise walks on squares and rectangles, including thin shapes).
- **Checkpoint 19** — Unlocked upon completing **Activity 120** (mastery of triangle/diamond walks, modulo runners, tails, collision detection, and full spiral-inward sweeps).

## Running Tests

From the `ExamPrep/` directory, run:

```bash
python -m unittest activities/10_halo_patterns_and_grid_walks/test_10_halo_patterns_and_grid_walks.py -v
```

Or run only the worked examples or only your activities:

```bash
python -m unittest activities.10_halo_patterns_and_grid_walks.test_10_halo_patterns_and_grid_walks.TestWorkedExamples -v
python -m unittest activities.10_halo_patterns_and_grid_walks.test_10_halo_patterns_and_grid_walks.TestYourActivities -v
```
