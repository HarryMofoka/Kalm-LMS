"""Test suite for Module 05: Lists & Tuples (Activities 049-060)."""

from __future__ import annotations

import importlib
import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

_m049 = importlib.import_module("activities.05_lists_and_tuples.activity_049_manual_length_and_sum")
_m050 = importlib.import_module("activities.05_lists_and_tuples.activity_050_finding_extremes")
_m051 = importlib.import_module("activities.05_lists_and_tuples.activity_051_filtering_and_transforming")
_m052 = importlib.import_module("activities.05_lists_and_tuples.activity_052_deduplication")
_m053 = importlib.import_module("activities.05_lists_and_tuples.activity_053_slicing_and_rotation")
_m054 = importlib.import_module("activities.05_lists_and_tuples.activity_054_chunking_and_pairing")
_m055 = importlib.import_module("activities.05_lists_and_tuples.activity_055_prefix_sums")
_m056 = importlib.import_module("activities.05_lists_and_tuples.activity_056_sliding_window")
_m057 = importlib.import_module("activities.05_lists_and_tuples.activity_057_flattening_and_nested")
_m058 = importlib.import_module("activities.05_lists_and_tuples.activity_058_matrix_transpose_diagonals")
_m059 = importlib.import_module("activities.05_lists_and_tuples.activity_059_coordinate_tuples")
_m060 = importlib.import_module("activities.05_lists_and_tuples.activity_060_grid_creation_neighbors")

example_manual_length = _m049.example_manual_length
solve_sum_positive_evens = _m049.solve_sum_positive_evens
example_find_min = _m050.example_find_min
solve_find_min_max = _m050.solve_find_min_max
example_square_all = _m051.example_square_all
solve_normalize_scores = _m051.solve_normalize_scores
example_unique_preserve_order = _m052.example_unique_preserve_order
solve_remove_consecutive_dups = _m052.solve_remove_consecutive_dups
example_rotate_left = _m053.example_rotate_left
solve_rotate_right = _m053.solve_rotate_right
example_pair_lists = _m054.example_pair_lists
solve_chunk_list = _m054.solve_chunk_list
example_prefix_sums = _m055.example_prefix_sums
solve_range_sum_queries = _m055.solve_range_sum_queries
example_max_window_sum = _m056.example_max_window_sum
solve_moving_average = _m056.solve_moving_average
example_flatten_2d = _m057.example_flatten_2d
solve_row_and_col_sums = _m057.solve_row_and_col_sums
example_transpose = _m058.example_transpose
solve_diagonal_sums = _m058.solve_diagonal_sums
example_nearest_to_origin = _m059.example_nearest_to_origin
solve_path_manhattan_distance = _m059.solve_path_manhattan_distance
example_create_grid = _m060.example_create_grid
solve_count_live_neighbors = _m060.solve_count_live_neighbors


class TestWorkedExamples(unittest.TestCase):
    """Verify all 12 worked examples in Module 05 pass out of the box."""

    def test_example_049(self) -> None:
        self.assertEqual(example_manual_length([10, 20, 30]), 3)
        self.assertEqual(example_manual_length([None, False, 0]), 3)
        self.assertEqual(example_manual_length([]), 0)

    def test_example_050(self) -> None:
        self.assertEqual(example_find_min([7, 2, 9, -4, 5]), -4)
        self.assertEqual(example_find_min([10, 20, 30]), 10)
        self.assertEqual(example_find_min([42]), 42)
        self.assertIsNone(example_find_min([]))

    def test_example_051(self) -> None:
        original = [1, -2, 0, 5]
        self.assertEqual(example_square_all(original), [1, 4, 0, 25])
        self.assertEqual(original, [1, -2, 0, 5])
        self.assertEqual(example_square_all([]), [])

    def test_example_052(self) -> None:
        original = [3, 1, 2, 1, 3, 4]
        self.assertEqual(example_unique_preserve_order(original), [3, 1, 2, 4])
        self.assertEqual(original, [3, 1, 2, 1, 3, 4])
        self.assertEqual(example_unique_preserve_order([]), [])

    def test_example_053(self) -> None:
        original = [1, 2, 3, 4]
        self.assertEqual(example_rotate_left(original), [2, 3, 4, 1])
        self.assertEqual(original, [1, 2, 3, 4])
        self.assertEqual(example_rotate_left([99]), [99])
        self.assertEqual(example_rotate_left([]), [])

    def test_example_054(self) -> None:
        self.assertEqual(
            example_pair_lists(["a", "b"], [1, 2, 3]),
            [("a", 1), ("b", 2)],
        )
        self.assertEqual(example_pair_lists([], [1, 2]), [])

    def test_example_055(self) -> None:
        self.assertEqual(example_prefix_sums([3, 1, 4, 1]), [3, 4, 8, 9])
        self.assertEqual(example_prefix_sums([5, -2, 3, -6]), [5, 3, 6, 0])
        self.assertEqual(example_prefix_sums([]), [])

    def test_example_056(self) -> None:
        self.assertEqual(example_max_window_sum([2, 1, 5, 1, 3, 2], 3), 9)
        self.assertEqual(example_max_window_sum([-5, -2, -8, -1], 2), -7)
        self.assertIsNone(example_max_window_sum([1, 2], 3))
        self.assertIsNone(example_max_window_sum([1, 2], 0))

    def test_example_057(self) -> None:
        self.assertEqual(example_flatten_2d([[1, 2], [], [3, 4, 5]]), [1, 2, 3, 4, 5])
        self.assertEqual(example_flatten_2d([[], []]), [])
        self.assertEqual(example_flatten_2d([]), [])

    def test_example_058(self) -> None:
        mat = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(example_transpose(mat), [[1, 4], [2, 5], [3, 6]])
        self.assertEqual(mat, [[1, 2, 3], [4, 5, 6]])
        self.assertEqual(example_transpose([[1, 2, 3]]), [[1], [2], [3]])
        self.assertEqual(example_transpose([]), [])
        self.assertEqual(example_transpose([[]]), [])

    def test_example_059(self) -> None:
        self.assertEqual(
            example_nearest_to_origin([(3, 4), (-1, 2), (2, -1)]),
            (-1, 2),
        )
        self.assertEqual(example_nearest_to_origin([(0, 0), (1, 1)]), (0, 0))
        self.assertIsNone(example_nearest_to_origin([]))

    def test_example_060(self) -> None:
        grid = example_create_grid(3, 2, 0)
        self.assertEqual(grid, [[0, 0], [0, 0], [0, 0]])
        grid[0][0] = 7
        self.assertEqual(grid[1][0], 0)
        self.assertEqual(grid[2][0], 0)
        self.assertEqual(example_create_grid(0, 3, 1), [])
        self.assertEqual(example_create_grid(2, 0, 1), [])


class TestYourActivities(unittest.TestCase):
    """Test suite for student implementations in Module 05 (Activities 049-060)."""

    def test_activity_049(self) -> None:
        self.assertEqual(solve_sum_positive_evens([1, 2, 3, 4, -6, 0, 8]), 14)
        self.assertEqual(solve_sum_positive_evens([-4, -2, 0, 1, 3]), 0)
        self.assertEqual(solve_sum_positive_evens([2, 2, 10]), 14)
        self.assertEqual(solve_sum_positive_evens([]), 0)

    def test_activity_050(self) -> None:
        self.assertEqual(solve_find_min_max([7, 2, 9, -4, 5]), (-4, 9))
        self.assertEqual(solve_find_min_max([-10, -3, -25]), (-25, -3))
        self.assertEqual(solve_find_min_max([42]), (42, 42))
        self.assertEqual(solve_find_min_max([1.5, 1.5, 1.5]), (1.5, 1.5))
        self.assertIsNone(solve_find_min_max([]))

    def test_activity_051(self) -> None:
        raw = [-5, 0, 50, 87, 100, 120]
        self.assertEqual(solve_normalize_scores(raw), [0.0, 0.5, 0.87, 1.0])
        self.assertEqual(raw, [-5, 0, 50, 87, 100, 120])
        self.assertEqual(solve_normalize_scores([33.3, 66.7, -1, 101]), [0.33, 0.67])
        self.assertEqual(solve_normalize_scores([-10, 150, 200]), [])
        self.assertEqual(solve_normalize_scores([]), [])

    def test_activity_052(self) -> None:
        original = [1, 1, 2, 2, 2, 3, 1, 1]
        self.assertEqual(solve_remove_consecutive_dups(original), [1, 2, 3, 1])
        self.assertEqual(original, [1, 1, 2, 2, 2, 3, 1, 1])
        self.assertEqual(
            solve_remove_consecutive_dups(["a", "a", "b", "a"]),
            ["a", "b", "a"],
        )
        self.assertEqual(
            solve_remove_consecutive_dups([None, None, 1, 1, None]),
            [None, 1, None],
        )
        self.assertEqual(solve_remove_consecutive_dups([5]), [5])
        self.assertEqual(solve_remove_consecutive_dups([]), [])

    def test_activity_053(self) -> None:
        original = [1, 2, 3, 4, 5]
        self.assertEqual(solve_rotate_right(original, 2), [4, 5, 1, 2, 3])
        self.assertEqual(original, [1, 2, 3, 4, 5])
        self.assertEqual(solve_rotate_right(original, 7), [4, 5, 1, 2, 3])
        zero_rot = solve_rotate_right(original, 0)
        self.assertEqual(zero_rot, [1, 2, 3, 4, 5])
        self.assertIsNot(zero_rot, original)
        self.assertEqual(solve_rotate_right([1, 2, 3], 3), [1, 2, 3])
        self.assertEqual(solve_rotate_right([1, 2, 3, 4], -1), [2, 3, 4, 1])
        self.assertEqual(solve_rotate_right([], 5), [])

    def test_activity_054(self) -> None:
        original = [1, 2, 3, 4, 5]
        self.assertEqual(solve_chunk_list(original, 2), [[1, 2], [3, 4], [5]])
        self.assertEqual(original, [1, 2, 3, 4, 5])
        self.assertEqual(solve_chunk_list([1, 2, 3, 4], 2), [[1, 2], [3, 4]])
        self.assertEqual(solve_chunk_list([1, 2], 5), [[1, 2]])
        self.assertEqual(solve_chunk_list(["a", "b", "c"], 1), [["a"], ["b"], ["c"]])
        self.assertEqual(solve_chunk_list([], 3), [])
        with self.assertRaises(ValueError):
            solve_chunk_list([1, 2, 3], 0)
        with self.assertRaises(ValueError):
            solve_chunk_list([], -2)

    def test_activity_055(self) -> None:
        self.assertEqual(
            solve_range_sum_queries(
                [2, 4, 1, 7, 3],
                [(0, 2), (1, 3), (2, 4), (4, 4)],
            ),
            [7, 12, 11, 3],
        )
        self.assertEqual(
            solve_range_sum_queries([5, -3, 2, -1], [(0, 3), (1, 2), (0, 0)]),
            [3, -1, 5],
        )
        self.assertEqual(solve_range_sum_queries([10, 20], []), [])

    def test_activity_056(self) -> None:
        self.assertEqual(solve_moving_average([2, 4, 6, 8, 10], 3), [4.0, 6.0, 8.0])
        self.assertEqual(solve_moving_average([1, 2, 3, 4], 2), [1.5, 2.5, 3.5])
        self.assertEqual(solve_moving_average([1, 2, 4], 3), [2.33])
        self.assertEqual(solve_moving_average([10, -10, 10], 2), [0.0, 0.0])
        self.assertEqual(solve_moving_average([5, 10], 5), [])
        self.assertEqual(solve_moving_average([5, 10], 0), [])
        self.assertEqual(solve_moving_average([], 2), [])

    def test_activity_057(self) -> None:
        self.assertEqual(
            solve_row_and_col_sums([[1, 2, 3], [4, 5, 6]]),
            ([6, 15], [5, 7, 9]),
        )
        self.assertEqual(solve_row_and_col_sums([[10]]), ([10], [10]))
        self.assertEqual(
            solve_row_and_col_sums([[-1, 2], [3, -4], [5, 6]]),
            ([1, -1, 11], [7, 4]),
        )
        self.assertEqual(solve_row_and_col_sums([]), ([], []))
        self.assertEqual(solve_row_and_col_sums([[]]), ([], []))

    def test_activity_058(self) -> None:
        self.assertEqual(
            solve_diagonal_sums([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            (15, 15),
        )
        self.assertEqual(solve_diagonal_sums([[2, 10], [3, 5]]), (7, 13))
        self.assertEqual(solve_diagonal_sums([[42]]), (42, 42))
        self.assertEqual(solve_diagonal_sums([]), (0, 0))

    def test_activity_059(self) -> None:
        self.assertEqual(
            solve_path_manhattan_distance([(0, 0), (3, 4), (3, 1)]),
            10,
        )
        self.assertEqual(
            solve_path_manhattan_distance([(-2, 5), (1, 1), (-1, -1)]),
            11,
        )
        self.assertEqual(solve_path_manhattan_distance([(2, 2), (2, 2)]), 0)
        self.assertEqual(solve_path_manhattan_distance([(5, 5)]), 0)
        self.assertEqual(solve_path_manhattan_distance([]), 0)

    def test_activity_060(self) -> None:
        grid = [
            [1, 1, 0],
            [1, 0, 1],
            [0, 1, 0],
        ]
        self.assertEqual(solve_count_live_neighbors(grid, 1, 1), 4)
        self.assertEqual(solve_count_live_neighbors(grid, 0, 0), 2)
        self.assertEqual(solve_count_live_neighbors(grid, 0, 2), 2)
        self.assertEqual(solve_count_live_neighbors(grid, 1, 0), 1)
        self.assertEqual(solve_count_live_neighbors(grid, 2, 2), 2)
        self.assertEqual(solve_count_live_neighbors(grid, -1, 0), 0)
        self.assertEqual(solve_count_live_neighbors(grid, 3, 0), 0)
        self.assertEqual(solve_count_live_neighbors([], 0, 0), 0)


if __name__ == "__main__":
    unittest.main()
