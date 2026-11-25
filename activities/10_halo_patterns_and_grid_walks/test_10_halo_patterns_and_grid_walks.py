"""Unit tests for Module 10: Halo Patterns & Grid Walks (Activities 109-120).

Run from ExamPrep/:
    python -m unittest activities/10_halo_patterns_and_grid_walks/test_10_halo_patterns_and_grid_walks.py -v
"""
from __future__ import annotations

import importlib
import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

_PKG = "activities.10_halo_patterns_and_grid_walks"

_m109 = importlib.import_module(f"{_PKG}.activity_109_grid_indexing_and_format_row")
_m110 = importlib.import_module(f"{_PKG}.activity_110_square_and_rectangle_halo")
_m111 = importlib.import_module(f"{_PKG}.activity_111_thick_border_and_double_halo")
_m112 = importlib.import_module(f"{_PKG}.activity_112_triangle_border_halos")
_m113 = importlib.import_module(f"{_PKG}.activity_113_diamond_manhattan_halo")
_m114 = importlib.import_module(f"{_PKG}.activity_114_clockwise_legs_walk")
_m115 = importlib.import_module(f"{_PKG}.activity_115_ccw_and_custom_start_walks")
_m116 = importlib.import_module(f"{_PKG}.activity_116_triangle_and_diamond_walks")
_m117 = importlib.import_module(f"{_PKG}.activity_117_modulo_wrap_and_single_runner")
_m118 = importlib.import_module(f"{_PKG}.activity_118_ragged_triangle_runner_and_tail")
_m119 = importlib.import_module(f"{_PKG}.activity_119_multi_runner_race_and_collision")
_m120 = importlib.import_module(f"{_PKG}.activity_120_spiral_inward_walker")

example_coordinate_grid = _m109.example_coordinate_grid
format_row = _m109.format_row
solve_render_grid = _m109.solve_render_grid

is_square_border = _m110.is_square_border
example_square_halo_lines = _m110.example_square_halo_lines
is_rectangle_border = _m110.is_rectangle_border
solve_rectangle_halo_lines = _m110.solve_rectangle_halo_lines

example_thick_border_square = _m111.example_thick_border_square
solve_double_halo_square = _m111.solve_double_halo_square

example_left_triangle_halo = _m112.example_left_triangle_halo
solve_right_triangle_halo = _m112.solve_right_triangle_halo

example_filled_diamond = _m113.example_filled_diamond
solve_diamond_halo = _m113.solve_diamond_halo

example_square_walk = _m114.example_square_walk
solve_rectangle_walk = _m114.solve_rectangle_walk

example_square_walk_ccw = _m115.example_square_walk_ccw
solve_rectangle_walk_from = _m115.solve_rectangle_walk_from

example_triangle_walk = _m116.example_triangle_walk
solve_diamond_walk = _m116.solve_diamond_walk

example_square_runner_lines = _m117.example_square_runner_lines
solve_rectangle_runner_lines = _m117.solve_rectangle_runner_lines

example_triangle_runner_lines = _m118.example_triangle_runner_lines
solve_triangle_runner_tail = _m118.solve_triangle_runner_tail

example_simulate_two_runners = _m119.example_simulate_two_runners
solve_first_collision = _m119.solve_first_collision

example_peel_outer_ring = _m120.example_peel_outer_ring
solve_spiral_walk = _m120.solve_spiral_walk


class TestWorkedExamples(unittest.TestCase):
    """Tests for the 12 worked examples ('I Do') — all should PASS out of the box."""

    def test_example_109(self) -> None:
        self.assertEqual(
            example_coordinate_grid(2, 3),
            [["(0,0)", "(0,1)", "(0,2)"], ["(1,0)", "(1,1)", "(1,2)"]],
        )
        self.assertEqual(example_coordinate_grid(1, 1), [["(0,0)"]])
        self.assertEqual(example_coordinate_grid(0, 3), [])
        self.assertEqual(example_coordinate_grid(3, -1), [])

    def test_example_110(self) -> None:
        self.assertTrue(is_square_border(0, 3, 4))
        self.assertTrue(is_square_border(3, 0, 4))
        self.assertFalse(is_square_border(1, 2, 4))
        self.assertFalse(is_square_border(-1, 0, 4))
        self.assertFalse(is_square_border(0, 0, 0))
        self.assertEqual(
            example_square_halo_lines(4),
            ["# # # #", "#     #", "#     #", "# # # #"],
        )
        self.assertEqual(example_square_halo_lines(1), ["#"])
        self.assertEqual(example_square_halo_lines(2), ["# #", "# #"])
        self.assertEqual(example_square_halo_lines(0), [])

    def test_example_111(self) -> None:
        self.assertEqual(
            example_thick_border_square(6, 2),
            [
                "# # # # # #",
                "# # # # # #",
                "# #     # #",
                "# #     # #",
                "# # # # # #",
                "# # # # # #",
            ],
        )
        self.assertEqual(
            example_thick_border_square(4, 1),
            ["# # # #", "#     #", "#     #", "# # # #"],
        )
        self.assertEqual(
            example_thick_border_square(3, 5),
            ["# # #", "# # #", "# # #"],
        )
        self.assertEqual(example_thick_border_square(0, 2), [])
        self.assertEqual(example_thick_border_square(2, 0), ["", ""])

    def test_example_112(self) -> None:
        self.assertEqual(
            example_left_triangle_halo(5),
            ["#", "# #", "#   #", "#     #", "# # # # #"],
        )
        self.assertEqual(example_left_triangle_halo(1), ["#"])
        self.assertEqual(example_left_triangle_halo(2), ["#", "# #"])
        self.assertEqual(example_left_triangle_halo(0), [])

    def test_example_113(self) -> None:
        self.assertEqual(
            example_filled_diamond(2),
            ["    #", "  # # #", "# # # # #", "  # # #", "    #"],
        )
        self.assertEqual(example_filled_diamond(0), ["#"])
        self.assertEqual(example_filled_diamond(-1), [])
        for line in example_filled_diamond(3):
            self.assertEqual(line, line.rstrip(" "))

    def test_example_114(self) -> None:
        self.assertEqual(
            example_square_walk(3),
            [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0)],
        )
        self.assertEqual(example_square_walk(1), [(0, 0)])
        self.assertEqual(example_square_walk(0), [])
        for size in range(2, 8):
            path = example_square_walk(size)
            self.assertEqual(len(path), 4 * size - 4)
            self.assertEqual(len(path), len(set(path)))

    def test_example_115(self) -> None:
        self.assertEqual(
            example_square_walk_ccw(3),
            [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (0, 1)],
        )
        self.assertEqual(example_square_walk_ccw(1), [(0, 0)])
        self.assertEqual(example_square_walk_ccw(0), [])
        cw = example_square_walk(5)
        ccw = example_square_walk_ccw(5)
        self.assertEqual(ccw[0], cw[0])
        self.assertEqual(ccw[1:], list(reversed(cw[1:])))

    def test_example_116(self) -> None:
        self.assertEqual(
            example_triangle_walk(4),
            [
                (0, 0), (1, 1), (2, 2), (3, 3),
                (3, 2), (3, 1), (3, 0),
                (2, 0), (1, 0),
            ],
        )
        self.assertEqual(example_triangle_walk(1), [(0, 0)])
        self.assertEqual(example_triangle_walk(2), [(0, 0), (1, 1), (1, 0)])
        self.assertEqual(example_triangle_walk(0), [])
        for h in range(2, 9):
            path = example_triangle_walk(h)
            self.assertEqual(len(path), 3 * h - 3)
            self.assertEqual(len(path), len(set(path)))

    def test_example_117(self) -> None:
        self.assertEqual(
            example_square_runner_lines(3, 5),
            ["o o o", "o   o", "o @ o"],
        )
        self.assertEqual(
            example_square_runner_lines(3, 8),
            example_square_runner_lines(3, 0),
        )
        self.assertEqual(example_square_runner_lines(1, 99), ["@"])
        self.assertEqual(example_square_runner_lines(0, 3), [])

    def test_example_118(self) -> None:
        self.assertEqual(
            example_triangle_runner_lines(5, 6),
            ["o", "o o", "o   o", "o     o", "o o @ o o"],
        )
        self.assertEqual(
            example_triangle_runner_lines(5, 12),
            example_triangle_runner_lines(5, 0),
        )
        self.assertEqual(example_triangle_runner_lines(1, 5), ["@"])
        self.assertEqual(example_triangle_runner_lines(0, 2), [])

    def test_example_119(self) -> None:
        self.assertEqual(
            example_simulate_two_runners(4, 3, 0, 1, 4, -1, 0),
            {"pos_a": (0, 0), "pos_b": (1, 3), "collided": False},
        )
        self.assertEqual(
            example_simulate_two_runners(4, 3, 0, 1, 4, -1, 2),
            {"pos_a": (0, 2), "pos_b": (0, 2), "collided": True},
        )
        with self.assertRaises(ValueError):
            example_simulate_two_runners(0, 3, 0, 1, 1, 1, 0)

    def test_example_120(self) -> None:
        self.assertEqual(
            example_peel_outer_ring(0, 2, 0, 3),
            [
                (0, 0), (0, 1), (0, 2), (0, 3),
                (1, 3), (2, 3),
                (2, 2), (2, 1), (2, 0),
                (1, 0),
            ],
        )
        self.assertEqual(example_peel_outer_ring(1, 1, 1, 2), [(1, 1), (1, 2)])
        self.assertEqual(example_peel_outer_ring(1, 3, 2, 2), [(1, 2), (2, 2), (3, 2)])
        self.assertEqual(example_peel_outer_ring(2, 2, 2, 2), [(2, 2)])
        self.assertEqual(example_peel_outer_ring(3, 2, 0, 1), [])


class TestYourActivities(unittest.TestCase):
    """Tests for your 12 student activities ('You Do') — make every single one green!"""

    def test_activity_109(self) -> None:
        self.assertEqual(format_row(["#", " ", "#"]), "#   #")
        self.assertEqual(format_row([" ", " ", "#"]), "    #")
        self.assertEqual(format_row(["#", " ", " "]), "#")
        self.assertEqual(format_row([" ", " "]), "")
        self.assertEqual(format_row([]), "")

        self.assertEqual(
            solve_render_grid([["#", "#"], ["#", " "]]),
            "# #\n#",
        )
        self.assertEqual(
            solve_render_grid([[" ", "#"], ["#", "#"]]),
            "  #\n# #",
        )
        # Ragged grid support and zero trailing spaces
        rendered = solve_render_grid([["#"], ["#", "#"], ["#", " ", "#"]])
        self.assertEqual(rendered, "#\n# #\n#   #")
        for line in rendered.splitlines():
            self.assertEqual(line, line.rstrip(" "))
        self.assertEqual(solve_render_grid([]), "")

    def test_activity_110(self) -> None:
        self.assertTrue(is_rectangle_border(0, 0, 6, 3))
        self.assertTrue(is_rectangle_border(2, 5, 6, 3))
        self.assertTrue(is_rectangle_border(1, 5, 6, 3))
        self.assertFalse(is_rectangle_border(1, 2, 6, 3))
        self.assertFalse(is_rectangle_border(3, 0, 6, 3))
        self.assertFalse(is_rectangle_border(0, 6, 6, 3))
        self.assertFalse(is_rectangle_border(0, 0, 0, 3))

        self.assertEqual(
            solve_rectangle_halo_lines(6, 3),
            ["# # # # # #", "#         #", "# # # # # #"],
        )
        self.assertEqual(solve_rectangle_halo_lines(4, 1), ["# # # #"])
        self.assertEqual(solve_rectangle_halo_lines(1, 3), ["#", "#", "#"])
        self.assertEqual(solve_rectangle_halo_lines(1, 1), ["#"])
        self.assertEqual(solve_rectangle_halo_lines(0, 4), [])
        self.assertEqual(solve_rectangle_halo_lines(4, -2), [])

    def test_activity_111(self) -> None:
        self.assertEqual(solve_double_halo_square(0), [])
        self.assertEqual(solve_double_halo_square(1), ["#"])
        self.assertEqual(solve_double_halo_square(2), ["# #", "# #"])
        self.assertEqual(
            solve_double_halo_square(3),
            ["# # #", "# + #", "# # #"],
        )
        self.assertEqual(
            solve_double_halo_square(4),
            ["# # # #", "# + + #", "# + + #", "# # # #"],
        )
        self.assertEqual(
            solve_double_halo_square(5),
            [
                "# # # # #",
                "# + + + #",
                "# +   + #",
                "# + + + #",
                "# # # # #",
            ],
        )
        for line in solve_double_halo_square(6):
            self.assertEqual(line, line.rstrip(" "))

    def test_activity_112(self) -> None:
        self.assertEqual(solve_right_triangle_halo(0), [])
        self.assertEqual(solve_right_triangle_halo(1), ["#"])
        self.assertEqual(solve_right_triangle_halo(2), ["  #", "# #"])
        self.assertEqual(
            solve_right_triangle_halo(5),
            [
                "        #",
                "      # #",
                "    #   #",
                "  #     #",
                "# # # # #",
            ],
        )
        for line in solve_right_triangle_halo(6):
            self.assertEqual(line, line.rstrip(" "))

    def test_activity_113(self) -> None:
        self.assertEqual(solve_diamond_halo(-1), [])
        self.assertEqual(solve_diamond_halo(0), ["#"])
        self.assertEqual(solve_diamond_halo(1), ["  #", "#   #", "  #"])
        self.assertEqual(
            solve_diamond_halo(2),
            [
                "    #",
                "  #   #",
                "#       #",
                "  #   #",
                "    #",
            ],
        )
        for line in solve_diamond_halo(4):
            self.assertEqual(line, line.rstrip(" "))

    def test_activity_114(self) -> None:
        self.assertEqual(
            solve_rectangle_walk(4, 3),
            [
                (0, 0), (0, 1), (0, 2), (0, 3),
                (1, 3), (2, 3),
                (2, 2), (2, 1), (2, 0),
                (1, 0),
            ],
        )
        # Thin shapes — zero duplicates!
        self.assertEqual(solve_rectangle_walk(4, 1), [(0, 0), (0, 1), (0, 2), (0, 3)])
        self.assertEqual(solve_rectangle_walk(1, 3), [(0, 0), (1, 0), (2, 0)])
        self.assertEqual(solve_rectangle_walk(1, 1), [(0, 0)])
        self.assertEqual(solve_rectangle_walk(0, 3), [])
        self.assertEqual(solve_rectangle_walk(3, 0), [])

        for w in range(2, 7):
            for h in range(2, 6):
                path = solve_rectangle_walk(w, h)
                self.assertEqual(len(path), 2 * w + 2 * h - 4)
                self.assertEqual(len(path), len(set(path)))

    def test_activity_115(self) -> None:
        self.assertEqual(
            solve_rectangle_walk_from(4, 3, (2, 3)),
            [
                (2, 3), (2, 2), (2, 1), (2, 0),
                (1, 0), (0, 0), (0, 1), (0, 2),
                (0, 3), (1, 3),
            ],
        )
        self.assertEqual(
            solve_rectangle_walk_from(4, 1, (0, 2)),
            [(0, 2), (0, 3), (0, 0), (0, 1)],
        )
        self.assertEqual(solve_rectangle_walk_from(1, 1, (0, 0)), [(0, 0)])
        with self.assertRaises(ValueError):
            solve_rectangle_walk_from(4, 3, (1, 1))
        with self.assertRaises(ValueError):
            solve_rectangle_walk_from(4, 3, (5, 0))
        with self.assertRaises(ValueError):
            solve_rectangle_walk_from(0, 3, (0, 0))

    def test_activity_116(self) -> None:
        self.assertEqual(solve_diamond_walk(-1), [])
        self.assertEqual(solve_diamond_walk(0), [(0, 0)])
        self.assertEqual(solve_diamond_walk(1), [(0, 1), (1, 2), (2, 1), (1, 0)])
        self.assertEqual(
            solve_diamond_walk(2),
            [
                (0, 2), (1, 3),
                (2, 4), (3, 3),
                (4, 2), (3, 1),
                (2, 0), (1, 1),
            ],
        )
        for radius in range(1, 8):
            path = solve_diamond_walk(radius)
            self.assertEqual(len(path), 4 * radius)
            self.assertEqual(len(path), len(set(path)))
            for r, c in path:
                self.assertEqual(abs(r - radius) + abs(c - radius), radius)

    def test_activity_117(self) -> None:
        self.assertEqual(
            solve_rectangle_runner_lines(6, 4, 9),
            [
                "o o o o o o",
                "o         o",
                "o         o",
                "o o o o @ o",
            ],
        )
        # Wrap forward after a full lap (16 cells)
        self.assertEqual(
            solve_rectangle_runner_lines(6, 4, 16),
            solve_rectangle_runner_lines(6, 4, 0),
        )
        # Negative steps (counter-clockwise)
        self.assertEqual(
            solve_rectangle_runner_lines(4, 3, -1),
            ["o o o o", "@     o", "o o o o"],
        )
        self.assertEqual(
            solve_rectangle_runner_lines(4, 3, -11),
            solve_rectangle_runner_lines(4, 3, -1),
        )
        # Thin shapes & empty
        self.assertEqual(solve_rectangle_runner_lines(4, 1, -1), ["o o o @"])
        self.assertEqual(solve_rectangle_runner_lines(1, 3, 2), ["o", "o", "@"])
        self.assertEqual(solve_rectangle_runner_lines(1, 1, -5), ["@"])
        self.assertEqual(solve_rectangle_runner_lines(0, 4, 2), [])

    def test_activity_118(self) -> None:
        self.assertEqual(
            solve_triangle_runner_tail(5, 6),
            [
                "o",
                "o o",
                "o   o",
                "o     o",
                "o o @ * .",
            ],
        )
        # Wrapping across apex (0, 0)
        self.assertEqual(
            solve_triangle_runner_tail(2, 0),
            ["@", "* ."],
        )
        # Tiny 1-cell triangle — head '@' takes priority!
        self.assertEqual(solve_triangle_runner_tail(1, 0), ["@"])
        # Negative steps wrap smoothly
        self.assertEqual(
            solve_triangle_runner_tail(5, -6),
            solve_triangle_runner_tail(5, 6),
        )
        self.assertEqual(solve_triangle_runner_tail(0, 3), [])
        for line in solve_triangle_runner_tail(5, 1):
            self.assertEqual(line, line.rstrip(" "))

    def test_activity_119(self) -> None:
        # Opposite directions meeting at t=2 on (0, 2)
        self.assertEqual(
            solve_first_collision(4, 3, 0, 1, 4, -1, 10),
            {"collided": True, "step": 2, "cell": (0, 2)},
        )
        # Already starting on the same cell (mod 10)
        self.assertEqual(
            solve_first_collision(4, 3, 0, 2, 10, -1, 5),
            {"collided": True, "step": 0, "cell": (0, 0)},
        )
        # Faster runner catches slower runner moving in same direction
        self.assertEqual(
            solve_first_collision(4, 3, 0, 2, 3, 1, 10),
            {"collided": True, "step": 3, "cell": (2, 2)},
        )
        # Opposite parity on even perimeter -> never collide on an integer tick
        self.assertEqual(
            solve_first_collision(4, 3, 0, 1, 1, -1, 25),
            {"collided": False, "step": None, "cell": None},
        )
        # Thin 1x1 shape always collides at t=0
        self.assertEqual(
            solve_first_collision(1, 1, 0, 3, 0, -2, 5),
            {"collided": True, "step": 0, "cell": (0, 0)},
        )
        with self.assertRaises(ValueError):
            solve_first_collision(0, 3, 0, 1, 1, 1, 5)
        with self.assertRaises(ValueError):
            solve_first_collision(4, 3, 0, 1, 1, 1, -1)

    def test_activity_120(self) -> None:
        self.assertEqual(
            solve_spiral_walk(3, 3),
            [
                (0, 0), (0, 1), (0, 2),
                (1, 2), (2, 2), (2, 1),
                (2, 0), (1, 0), (1, 1),
            ],
        )
        self.assertEqual(
            solve_spiral_walk(3, 4),
            [
                (0, 0), (0, 1), (0, 2), (0, 3),
                (1, 3), (2, 3), (2, 2), (2, 1),
                (2, 0), (1, 0), (1, 1), (1, 2),
            ],
        )
        self.assertEqual(
            solve_spiral_walk(4, 3),
            [
                (0, 0), (0, 1), (0, 2),
                (1, 2), (2, 2), (3, 2),
                (3, 1), (3, 0), (2, 0),
                (1, 0), (1, 1), (2, 1),
            ],
        )
        self.assertEqual(solve_spiral_walk(1, 4), [(0, 0), (0, 1), (0, 2), (0, 3)])
        self.assertEqual(solve_spiral_walk(4, 1), [(0, 0), (1, 0), (2, 0), (3, 0)])
        self.assertEqual(solve_spiral_walk(1, 1), [(0, 0)])
        self.assertEqual(solve_spiral_walk(0, 5), [])
        self.assertEqual(solve_spiral_walk(5, -1), [])

        for r in range(1, 7):
            for c in range(1, 7):
                path = solve_spiral_walk(r, c)
                self.assertEqual(len(path), r * c)
                self.assertEqual(len(path), len(set(path)))


if __name__ == "__main__":
    unittest.main()
