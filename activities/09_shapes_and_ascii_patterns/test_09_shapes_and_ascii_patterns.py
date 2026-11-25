"""Unit tests for Module 09: Shapes and ASCII Patterns (Activities 097-108)."""

from __future__ import annotations

import importlib
import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

_PKG = "activities.09_shapes_and_ascii_patterns"

_m097 = importlib.import_module(f"{_PKG}.activity_097_solid_squares_and_rectangles")
_m098 = importlib.import_module(f"{_PKG}.activity_098_left_triangles")
_m099 = importlib.import_module(f"{_PKG}.activity_099_inverted_and_right_triangles")
_m100 = importlib.import_module(f"{_PKG}.activity_100_centered_star_pyramid")
_m101 = importlib.import_module(f"{_PKG}.activity_101_centered_number_pyramid")
_m102 = importlib.import_module(f"{_PKG}.activity_102_hollow_square_and_titled_box")
_m103 = importlib.import_module(f"{_PKG}.activity_103_symmetric_diamond")
_m104 = importlib.import_module(f"{_PKG}.activity_104_symmetric_hourglass")
_m105 = importlib.import_module(f"{_PKG}.activity_105_checkerboard_and_x_cross")
_m106 = importlib.import_module(f"{_PKG}.activity_106_hollow_and_alphabet_diamond")
_m107 = importlib.import_module(f"{_PKG}.activity_107_concentric_number_rings")
_m108 = importlib.import_module(f"{_PKG}.activity_108_number_spiral_strings")

example_solid_square = _m097.example_solid_square
solve_solid_rectangle = _m097.solve_solid_rectangle

example_left_star_triangle = _m098.example_left_star_triangle
solve_create_number_triangle = _m098.solve_create_number_triangle

example_inverted_left_triangle = _m099.example_inverted_left_triangle
solve_right_aligned_triangle = _m099.solve_right_aligned_triangle

example_pyramid_row = _m100.example_pyramid_row
solve_create_pyramid = _m100.solve_create_pyramid

example_counting_pyramid = _m101.example_counting_pyramid
solve_create_number_pyramid = _m101.solve_create_number_pyramid

example_bordered_box = _m102.example_bordered_box
solve_create_hollow_square = _m102.solve_create_hollow_square
solve_titled_box = _m102.solve_titled_box

example_mirror_rows = _m103.example_mirror_rows
solve_create_diamond = _m103.solve_create_diamond

example_inverted_pyramid = _m104.example_inverted_pyramid
solve_create_hourglass = _m104.solve_create_hourglass

example_checkerboard = _m105.example_checkerboard
solve_x_cross = _m105.solve_x_cross

example_hollow_star_diamond = _m106.example_hollow_star_diamond
solve_create_alphabet_diamond = _m106.solve_create_alphabet_diamond

example_edge_distance_grid = _m107.example_edge_distance_grid
solve_concentric_rings = _m107.solve_concentric_rings

example_format_number_grid = _m108.example_format_number_grid
solve_create_number_spiral = _m108.solve_create_number_spiral
solve_create_spiral_string = _m108.solve_create_spiral_string


class TestWorkedExamples(unittest.TestCase):
    """Verify all 12 worked examples ('I Do') pass completely."""

    def test_example_097(self) -> None:
        self.assertEqual(example_solid_square(3), ["***", "***", "***"])
        self.assertEqual(example_solid_square(2, "#"), ["##", "##"])
        self.assertEqual(example_solid_square(1), ["*"])
        self.assertEqual(example_solid_square(0), [])

    def test_example_098(self) -> None:
        self.assertEqual(example_left_star_triangle(4), ["*", "**", "***", "****"])
        self.assertEqual(example_left_star_triangle(1), ["*"])
        self.assertEqual(example_left_star_triangle(0), [])

    def test_example_099(self) -> None:
        self.assertEqual(example_inverted_left_triangle(4), ["****", "***", "**", "*"])
        self.assertEqual(example_inverted_left_triangle(1), ["*"])
        self.assertEqual(example_inverted_left_triangle(-1), [])

    def test_example_100(self) -> None:
        self.assertEqual(example_pyramid_row(1, 3), "  *  ")
        self.assertEqual(example_pyramid_row(2, 3), " *** ")
        self.assertEqual(example_pyramid_row(3, 3), "*****")
        self.assertEqual(example_pyramid_row(0, 3), "")
        self.assertEqual(example_pyramid_row(4, 3), "")

    def test_example_101(self) -> None:
        self.assertEqual(
            example_counting_pyramid(3),
            ["  1  ", " 1 2 ", "1 2 3"],
        )
        self.assertEqual(example_counting_pyramid(1), ["1"])
        self.assertEqual(example_counting_pyramid(0), [])

    def test_example_102(self) -> None:
        self.assertEqual(
            example_bordered_box(5, 4),
            ["+---+", "|   |", "|   |", "+---+"],
        )
        self.assertEqual(example_bordered_box(2, 2), ["++", "++"])
        self.assertEqual(example_bordered_box(1, 4), [])
        self.assertEqual(example_bordered_box(4, 1), [])

    def test_example_103(self) -> None:
        top = ["  *  ", " *** ", "*****"]
        self.assertEqual(
            example_mirror_rows(top),
            ["  *  ", " *** ", "*****", " *** ", "  *  "],
        )
        self.assertEqual(top, ["  *  ", " *** ", "*****"])
        self.assertEqual(example_mirror_rows(["*"]), ["*"])
        self.assertEqual(example_mirror_rows([]), [])

    def test_example_104(self) -> None:
        self.assertEqual(
            example_inverted_pyramid(3),
            ["*****", " *** ", "  *  "],
        )
        self.assertEqual(example_inverted_pyramid(1), ["*"])
        self.assertEqual(example_inverted_pyramid(0), [])

    def test_example_105(self) -> None:
        self.assertEqual(example_checkerboard(3), ["#.#", ".#.", "#.#"])
        self.assertEqual(example_checkerboard(2, "X", "O"), ["XO", "OX"])
        self.assertEqual(example_checkerboard(0), [])

    def test_example_106(self) -> None:
        self.assertEqual(
            example_hollow_star_diamond(3),
            ["  *  ", " * * ", "*   *", " * * ", "  *  "],
        )
        self.assertEqual(example_hollow_star_diamond(1), ["*"])
        self.assertEqual(example_hollow_star_diamond(0), [])

    def test_example_107(self) -> None:
        self.assertEqual(
            example_edge_distance_grid(5),
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 2, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0],
            ],
        )
        self.assertEqual(example_edge_distance_grid(1), [[0]])
        self.assertEqual(example_edge_distance_grid(0), [])

    def test_example_108(self) -> None:
        grid3 = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        self.assertEqual(
            example_format_number_grid(grid3, aligned=False),
            ["123", "894", "765"],
        )
        grid4 = [
            [1, 2, 3, 4],
            [12, 13, 14, 5],
            [11, 16, 15, 6],
            [10, 9, 8, 7],
        ]
        self.assertEqual(
            example_format_number_grid(grid4, aligned=True),
            [
                " 1  2  3  4",
                "12 13 14  5",
                "11 16 15  6",
                "10  9  8  7",
            ],
        )
        self.assertEqual(example_format_number_grid([]), [])


class TestYourActivities(unittest.TestCase):
    """Tests for your implementations ('You Do') across Activities 097-108."""

    def test_activity_097(self) -> None:
        self.assertEqual(
            solve_solid_rectangle(5, 3),
            ["*****", "*****", "*****"],
        )
        self.assertEqual(solve_solid_rectangle(4, 2, "#"), ["####", "####"])
        self.assertEqual(solve_solid_rectangle(1, 3), ["*", "*", "*"])
        self.assertEqual(solve_solid_rectangle(0, 3), [])
        self.assertEqual(solve_solid_rectangle(4, -1), [])

    def test_activity_098(self) -> None:
        self.assertEqual(solve_create_number_triangle(3), ["1", "22", "333"])
        self.assertEqual(
            solve_create_number_triangle(5),
            ["1", "22", "333", "4444", "55555"],
        )
        self.assertEqual(solve_create_number_triangle(1), ["1"])
        self.assertEqual(solve_create_number_triangle(0), [])
        self.assertEqual(solve_create_number_triangle(-2), [])

    def test_activity_099(self) -> None:
        self.assertEqual(solve_right_aligned_triangle(3), ["  *", " **", "***"])
        self.assertEqual(
            solve_right_aligned_triangle(4),
            ["   *", "  **", " ***", "****"],
        )
        self.assertEqual(solve_right_aligned_triangle(1), ["*"])
        self.assertEqual(solve_right_aligned_triangle(0), [])

    def test_activity_100(self) -> None:
        self.assertEqual(
            solve_create_pyramid(3),
            ["  *  ", " *** ", "*****"],
        )
        self.assertEqual(
            solve_create_pyramid(4),
            ["   *   ", "  ***  ", " ***** ", "*******"],
        )
        self.assertEqual(solve_create_pyramid(1), ["*"])
        self.assertEqual(solve_create_pyramid(0), [])

    def test_activity_101(self) -> None:
        self.assertEqual(
            solve_create_number_pyramid(3),
            ["  1  ", " 2 2 ", "3 3 3"],
        )
        self.assertEqual(
            solve_create_number_pyramid(4),
            ["   1   ", "  2 2  ", " 3 3 3 ", "4 4 4 4"],
        )
        self.assertEqual(solve_create_number_pyramid(1), ["1"])
        self.assertEqual(solve_create_number_pyramid(0), [])

    def test_activity_102(self) -> None:
        self.assertEqual(
            solve_create_hollow_square(4),
            ["****", "*  *", "*  *", "****"],
        )
        self.assertEqual(solve_create_hollow_square(2), ["**", "**"])
        self.assertEqual(solve_create_hollow_square(1), ["*"])
        self.assertEqual(solve_create_hollow_square(0), [])

        self.assertEqual(
            solve_titled_box("HI", 8),
            ["+------+", "|  HI  |", "+------+"],
        )
        self.assertEqual(
            solve_titled_box("HELLO", 4),
            ["+-------+", "| HELLO |", "+-------+"],
        )

    def test_activity_103(self) -> None:
        self.assertEqual(
            solve_create_diamond(5),
            ["  *  ", " *** ", "*****", " *** ", "  *  "],
        )
        self.assertEqual(solve_create_diamond(3), [" * ", "***", " * "])
        self.assertEqual(solve_create_diamond(1), ["*"])
        self.assertEqual(solve_create_diamond(0), [])
        self.assertEqual(solve_create_diamond(-3), [])
        with self.assertRaises(ValueError) as ctx:
            solve_create_diamond(4)
        self.assertEqual(str(ctx.exception), "n must be odd.")

    def test_activity_104(self) -> None:
        self.assertEqual(
            solve_create_hourglass(5),
            ["*****", " *** ", "  *  ", " *** ", "*****"],
        )
        self.assertEqual(solve_create_hourglass(3), ["***", " * ", "***"])
        self.assertEqual(solve_create_hourglass(1), ["*"])
        self.assertEqual(solve_create_hourglass(0), [])
        with self.assertRaises(ValueError) as ctx:
            solve_create_hourglass(4)
        self.assertEqual(str(ctx.exception), "n must be odd.")

    def test_activity_105(self) -> None:
        self.assertEqual(
            solve_x_cross(5),
            ["X   X", " X X ", "  X  ", " X X ", "X   X"],
        )
        self.assertEqual(
            solve_x_cross(4),
            ["X  X", " XX ", " XX ", "X  X"],
        )
        self.assertEqual(solve_x_cross(3, "*", "."), ["*.*", ".*.", "*.*"])
        self.assertEqual(solve_x_cross(1), ["X"])
        self.assertEqual(solve_x_cross(0), [])

    def test_activity_106(self) -> None:
        self.assertEqual(
            solve_create_alphabet_diamond(3),
            ["  A  ", " B B ", "C   C", " B B ", "  A  "],
        )
        self.assertEqual(
            solve_create_alphabet_diamond(4),
            [
                "   A   ",
                "  B B  ",
                " C   C ",
                "D     D",
                " C   C ",
                "  B B  ",
                "   A   ",
            ],
        )
        self.assertEqual(solve_create_alphabet_diamond(1), ["A"])
        self.assertEqual(solve_create_alphabet_diamond(0), [])
        with self.assertRaises(ValueError) as ctx:
            solve_create_alphabet_diamond(27)
        self.assertEqual(str(ctx.exception), "n must be at most 26.")

    def test_activity_107(self) -> None:
        self.assertEqual(
            solve_concentric_rings(3),
            ["33333", "32223", "32123", "32223", "33333"],
        )
        self.assertEqual(
            solve_concentric_rings(2),
            ["222", "212", "222"],
        )
        self.assertEqual(solve_concentric_rings(1), ["1"])
        self.assertEqual(solve_concentric_rings(0), [])
        with self.assertRaises(ValueError) as ctx:
            solve_concentric_rings(10)
        self.assertEqual(str(ctx.exception), "n must be between 1 and 9.")

    def test_activity_108(self) -> None:
        self.assertEqual(solve_create_number_spiral(3), ["123", "894", "765"])
        self.assertEqual(
            solve_create_number_spiral(4),
            ["1234", "1213145", "1116156", "10987"],
        )
        self.assertEqual(solve_create_number_spiral(1), ["1"])
        self.assertEqual(solve_create_number_spiral(0), [])

        self.assertEqual(solve_create_spiral_string(3), "123\n894\n765")
        self.assertEqual(
            solve_create_spiral_string(4, aligned=True),
            " 1  2  3  4\n12 13 14  5\n11 16 15  6\n10  9  8  7",
        )
        self.assertEqual(solve_create_spiral_string(0), "")


if __name__ == "__main__":
    unittest.main()
