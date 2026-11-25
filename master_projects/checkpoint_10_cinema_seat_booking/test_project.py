"""Automated tests for Checkpoint 10: Cinema Seat Grid & Group Allocator."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from master_projects.checkpoint_10_cinema_seat_booking import (  # noqa: E402
    project,
    worked_example,
)


class TestWorkedExample(unittest.TestCase):
    """Verify the Parking Garage 2D Bay Allocator reference works."""

    def test_create_garage_no_row_aliasing_and_validation(self) -> None:
        garage = worked_example.create_garage(3, 4)
        self.assertEqual(len(garage), 3)
        self.assertEqual(len(garage[0]), 4)
        self.assertIsNot(garage[0], garage[1])
        self.assertIsNot(garage[1], garage[2])

        with self.assertRaises(ValueError):
            worked_example.create_garage(0, 4)
        with self.assertRaises(ValueError):
            worked_example.create_garage(2, 0)

    def test_find_nearest_open_bay_and_full_garage(self) -> None:
        garage = [["P", "P"], ["P", "."]]
        self.assertEqual(worked_example.find_nearest_open_bay(garage), (1, 1))
        full = [["P", "P"], ["P", "P"]]
        self.assertIsNone(worked_example.find_nearest_open_bay(full))

    def test_reserve_bay_pure_and_error_cases(self) -> None:
        garage = worked_example.create_garage(2, 2)
        updated = worked_example.reserve_bay(garage, 0, 1)
        self.assertEqual(updated, [[".", "P"], [".", "."]])
        self.assertEqual(garage, [[".", "."], [".", "."]])

        with self.assertRaises(ValueError):
            worked_example.reserve_bay(updated, 0, 1)  # already occupied
        with self.assertRaises(ValueError):
            worked_example.reserve_bay(updated, -1, 0)  # negative level
        with self.assertRaises(ValueError):
            worked_example.reserve_bay(updated, 0, 5)  # col out of bounds

    def test_garage_occupancy_stats(self) -> None:
        garage = [["P", "P", "."], [".", ".", "."]]
        self.assertEqual(
            worked_example.garage_occupancy(garage),
            {
                "total_bays": 6,
                "occupied": 2,
                "available": 4,
                "occupancy_pct": 33.33,
            },
        )

    def test_render_garage_map_format_and_no_trailing_spaces(self) -> None:
        garage = [["P", ".", "P"], [".", ".", "."]]
        rendered = worked_example.render_garage_map(garage)
        self.assertEqual(rendered, "L1: P . P\nL2: . . .")
        for line in rendered.splitlines():
            self.assertEqual(line, line.rstrip())


class TestMasterProject(unittest.TestCase):
    """TDD test suite for the student's Cinema Seat Grid & Group Allocator."""

    def test_create_seat_map_dimensions_no_aliasing_and_validation(self) -> None:
        seat_map = project.create_seat_map(3, 4)
        self.assertEqual(
            seat_map,
            [
                ["O", "O", "O", "O"],
                ["O", "O", "O", "O"],
                ["O", "O", "O", "O"],
            ],
        )
        # Ensure rows are distinct list objects (no aliasing bug!)
        self.assertIsNot(seat_map[0], seat_map[1])
        self.assertIsNot(seat_map[1], seat_map[2])

        for bad_r, bad_c in [(0, 4), (27, 4), (3, 0), (-1, 3)]:
            with self.subTest(rows=bad_r, cols=bad_c):
                with self.assertRaises(ValueError):
                    project.create_seat_map(bad_r, bad_c)

    def test_book_seat_pure_and_rejects_taken_or_out_of_bounds(self) -> None:
        original = [["O", "O", "O"], ["O", "O", "O"]]
        updated = project.book_seat(original, 0, 1)
        self.assertEqual(updated, [["O", "X", "O"], ["O", "O", "O"]])
        # Original grid must remain untouched
        self.assertEqual(original, [["O", "O", "O"], ["O", "O", "O"]])

        # Booking an already-booked seat or out-of-bounds seat raises ValueError
        with self.assertRaises(ValueError):
            project.book_seat(updated, 0, 1)
        for bad_r, bad_c in [(-1, 0), (0, -1), (2, 0), (0, 3)]:
            with self.subTest(row=bad_r, col=bad_c):
                with self.assertRaises(ValueError):
                    project.book_seat(original, bad_r, bad_c)

    def test_find_contiguous_seats_first_match_and_none(self) -> None:
        grid = [
            ["X", "O", "X", "O", "O"],
            ["O", "O", "O", "X", "O"],
            ["O", "O", "O", "O", "O"],
        ]
        # Row 0 has 2 contiguous seats at col 3; Row 1 has 3 at col 0; Row 2 has 4 at col 0
        self.assertEqual(project.find_contiguous_seats(grid, 2), (0, 3))
        self.assertEqual(project.find_contiguous_seats(grid, 3), (1, 0))
        self.assertEqual(project.find_contiguous_seats(grid, 5), (2, 0))
        self.assertIsNone(project.find_contiguous_seats(grid, 6))

        with self.assertRaises(ValueError):
            project.find_contiguous_seats(grid, 0)

    def test_book_group_allocates_block_pure_and_raises_when_unavailable(self) -> None:
        original = [
            ["X", "O", "X", "O"],
            ["O", "O", "O", "O"],
        ]
        result = project.book_group(original, 3)
        self.assertEqual(
            result,
            (
                [
                    ["X", "O", "X", "O"],
                    ["X", "X", "X", "O"],
                ],
                (1, 0),
            ),
        )
        # Input must not be mutated
        self.assertEqual(
            original,
            [
                ["X", "O", "X", "O"],
                ["O", "O", "O", "O"],
            ],
        )

        # Cannot fit a group of 5 in a 4-seat row
        with self.assertRaises(ValueError):
            project.book_group(original, 5)
        with self.assertRaises(ValueError):
            project.book_group(original, 0)

    def test_occupancy_stats_counts_percentage_and_full_rows(self) -> None:
        grid = [
            ["X", "X", "X"],
            ["X", "O", "O"],
            ["O", "O", "O"],
        ]
        self.assertEqual(
            project.occupancy_stats(grid),
            {
                "total_seats": 9,
                "booked_seats": 4,
                "available_seats": 5,
                "occupancy_pct": 44.44,
                "full_rows": 1,
            },
        )
        self.assertEqual(
            project.occupancy_stats([]),
            {
                "total_seats": 0,
                "booked_seats": 0,
                "available_seats": 0,
                "occupancy_pct": 0.0,
                "full_rows": 0,
            },
        )

    def test_render_seat_map_row_labels_and_zero_trailing_spaces(self) -> None:
        grid = [
            ["O", "X", "X", "O"],
            ["O", "O", "O", "O"],
            ["X", "X", "X", "X"],
        ]
        rendered = project.render_seat_map(grid)
        self.assertEqual(
            rendered,
            "A: O X X O\nB: O O O O\nC: X X X X",
        )
        for line in rendered.splitlines():
            self.assertEqual(line, line.rstrip())
        self.assertEqual(project.render_seat_map([]), "")

    def test_full_cinema_booking_workflow(self) -> None:
        grid = project.create_seat_map(2, 4)
        self.assertIsNotNone(grid)
        grid = project.book_seat(grid, 0, 0)
        self.assertIsNotNone(grid)
        group_result = project.book_group(grid, 3)
        self.assertIsNotNone(group_result)
        grid, coords = group_result
        self.assertEqual(coords, (0, 1))
        self.assertEqual(project.render_seat_map(grid), "A: X X X X\nB: O O O O")
        stats = project.occupancy_stats(grid)
        self.assertEqual(
            stats,
            {
                "total_seats": 8,
                "booked_seats": 4,
                "available_seats": 4,
                "occupancy_pct": 50.0,
                "full_rows": 1,
            },
        )


if __name__ == "__main__":
    unittest.main()
