"""Unit tests for Module 08: Algorithms and Problem Solving (Activities 085-096)."""

from __future__ import annotations

import importlib
import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

_PKG = "activities.08_algorithms_and_problem_solving"

_m085 = importlib.import_module(f"{_PKG}.activity_085_linear_search_sentinels")
_m086 = importlib.import_module(f"{_PKG}.activity_086_binary_search")
_m087 = importlib.import_module(f"{_PKG}.activity_087_two_pointers")
_m088 = importlib.import_module(f"{_PKG}.activity_088_stacks_and_undo")
_m089 = importlib.import_module(f"{_PKG}.activity_089_bracket_matching")
_m090 = importlib.import_module(f"{_PKG}.activity_090_sliding_window")
_m091 = importlib.import_module(f"{_PKG}.activity_091_kadanes_algorithm")
_m092 = importlib.import_module(f"{_PKG}.activity_092_selection_and_insertion_sort")
_m093 = importlib.import_module(f"{_PKG}.activity_093_pascals_triangle")
_m094 = importlib.import_module(f"{_PKG}.activity_094_spiral_matrix")
_m095 = importlib.import_module(f"{_PKG}.activity_095_merge_sort_and_inversions")
_m096 = importlib.import_module(f"{_PKG}.activity_096_dynamic_programming_intro")

example_first_and_last_index = _m085.example_first_and_last_index
solve_find_all_indices = _m085.solve_find_all_indices

example_binary_search = _m086.example_binary_search
solve_lower_bound = _m086.solve_lower_bound

example_sorted_two_sum = _m087.example_sorted_two_sum
solve_merge_sorted_lists = _m087.solve_merge_sorted_lists

example_reverse_with_stack = _m088.example_reverse_with_stack
solve_apply_backspaces = _m088.solve_apply_backspaces

example_valid_parens_only = _m089.example_valid_parens_only
solve_valid_brackets = _m089.solve_valid_brackets

example_longest_identical_run = _m090.example_longest_identical_run
solve_longest_unique_substring = _m090.solve_longest_unique_substring

example_max_stock_profit = _m091.example_max_stock_profit
solve_max_subarray_sum = _m091.solve_max_subarray_sum

example_selection_sort = _m092.example_selection_sort
solve_insertion_sort_with_swaps = _m092.solve_insertion_sort_with_swaps

example_pascal_row = _m093.example_pascal_row
solve_pascal_triangle = _m093.solve_pascal_triangle

example_read_spiral = _m094.example_read_spiral
solve_spiral_matrix = _m094.solve_spiral_matrix

example_merge_sort = _m095.example_merge_sort
solve_count_inversions = _m095.solve_count_inversions

example_climb_stairs = _m096.example_climb_stairs
solve_longest_common_subsequence = _m096.solve_longest_common_subsequence


class TestWorkedExamples(unittest.TestCase):
    """Verify all 12 worked examples ('I Do') pass completely."""

    def test_example_085(self) -> None:
        self.assertEqual(example_first_and_last_index([4, 2, 4, 9, 4], 4), (0, 4))
        self.assertEqual(example_first_and_last_index([1, 2, 3], 2), (1, 1))
        self.assertEqual(example_first_and_last_index([1, 2, 3], 9), (-1, -1))
        self.assertEqual(example_first_and_last_index([], 1), (-1, -1))

    def test_example_086(self) -> None:
        nums = [2, 5, 8, 12, 16, 23, 38, 56]
        self.assertEqual(example_binary_search(nums, 2), 0)
        self.assertEqual(example_binary_search(nums, 16), 4)
        self.assertEqual(example_binary_search(nums, 56), 7)
        self.assertEqual(example_binary_search(nums, 20), -1)
        self.assertEqual(example_binary_search([], 5), -1)
        self.assertEqual(example_binary_search([9], 9), 0)

    def test_example_087(self) -> None:
        self.assertEqual(example_sorted_two_sum([-4, -1, 3, 7], 2), (1, 2))
        self.assertEqual(example_sorted_two_sum([3, 3], 6), (0, 1))
        self.assertIsNone(example_sorted_two_sum([1, 2, 4], 10))
        self.assertIsNone(example_sorted_two_sum([], 0))
        self.assertIsNone(example_sorted_two_sum([5], 5))

    def test_example_088(self) -> None:
        original = [1, 2, 3, 4]
        result = example_reverse_with_stack(original)
        self.assertEqual(result, [4, 3, 2, 1])
        self.assertEqual(original, [1, 2, 3, 4])
        self.assertIsNot(result, original)
        self.assertEqual(example_reverse_with_stack([]), [])

    def test_example_089(self) -> None:
        self.assertIs(example_valid_parens_only("(a + (b * c))"), True)
        self.assertIs(example_valid_parens_only(""), True)
        self.assertIs(example_valid_parens_only(")("), False)
        self.assertIs(example_valid_parens_only("((x)"), False)

    def test_example_090(self) -> None:
        self.assertEqual(example_longest_identical_run("aaabbccccd"), 4)
        self.assertEqual(example_longest_identical_run("abcd"), 1)
        self.assertEqual(example_longest_identical_run("aAAa"), 2)
        self.assertEqual(example_longest_identical_run(""), 0)

    def test_example_091(self) -> None:
        self.assertEqual(example_max_stock_profit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(example_max_stock_profit([9, 7, 4, 1]), 0)
        self.assertEqual(example_max_stock_profit([5]), 0)
        self.assertEqual(example_max_stock_profit([]), 0)

    def test_example_092(self) -> None:
        raw = [64, 25, 12, 22, 11, 12]
        result = example_selection_sort(raw)
        self.assertEqual(result, [11, 12, 12, 22, 25, 64])
        self.assertEqual(raw, [64, 25, 12, 22, 11, 12])
        self.assertEqual(example_selection_sort([]), [])

    def test_example_093(self) -> None:
        self.assertEqual(example_pascal_row(-1), [])
        self.assertEqual(example_pascal_row(0), [1])
        self.assertEqual(example_pascal_row(1), [1, 1])
        self.assertEqual(example_pascal_row(4), [1, 4, 6, 4, 1])

    def test_example_094(self) -> None:
        self.assertEqual(
            example_read_spiral([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            [1, 2, 3, 6, 9, 8, 7, 4, 5],
        )
        self.assertEqual(example_read_spiral([[1, 2, 3, 4]]), [1, 2, 3, 4])
        self.assertEqual(example_read_spiral([[1], [2], [3]]), [1, 2, 3])
        self.assertEqual(example_read_spiral([]), [])

    def test_example_095(self) -> None:
        raw = [38, 27, 43, 3, 9, 82, 10]
        result = example_merge_sort(raw)
        self.assertEqual(result, [3, 9, 10, 27, 38, 43, 82])
        self.assertEqual(raw, [38, 27, 43, 3, 9, 82, 10])
        self.assertEqual(example_merge_sort([]), [])
        self.assertEqual(example_merge_sort([-3, 0, -3, 2]), [-3, -3, 0, 2])

    def test_example_096(self) -> None:
        self.assertEqual(example_climb_stairs(0), 0)
        self.assertEqual(example_climb_stairs(-2), 0)
        self.assertEqual(example_climb_stairs(1), 1)
        self.assertEqual(example_climb_stairs(2), 2)
        self.assertEqual(example_climb_stairs(5), 8)
        self.assertEqual(example_climb_stairs(10), 89)


class TestYourActivities(unittest.TestCase):
    """Tests for your implementations ('You Do') across Activities 085-096."""

    def test_activity_085(self) -> None:
        data = [4, 2, 4, 9, 4]
        self.assertEqual(solve_find_all_indices(data, 4), [0, 2, 4])
        self.assertEqual(data, [4, 2, 4, 9, 4])
        self.assertEqual(solve_find_all_indices(["a", "b", "c"], "z"), [])
        self.assertEqual(solve_find_all_indices([], 10), [])
        self.assertEqual(solve_find_all_indices([5], 5), [0])

    def test_activity_086(self) -> None:
        self.assertEqual(solve_lower_bound([1, 3, 5, 7], 5), 2)
        self.assertEqual(solve_lower_bound([1, 3, 5, 7], 4), 2)
        self.assertEqual(solve_lower_bound([1, 2, 2, 2, 5], 2), 1)
        self.assertEqual(solve_lower_bound([1, 3, 5], 0), 0)
        self.assertEqual(solve_lower_bound([1, 3, 5], 10), 3)
        self.assertEqual(solve_lower_bound([], 42), 0)

    def test_activity_087(self) -> None:
        a = [1, 3, 5]
        b = [2, 3, 6, 8]
        merged = solve_merge_sorted_lists(a, b)
        self.assertEqual(merged, [1, 2, 3, 3, 5, 6, 8])
        self.assertEqual(a, [1, 3, 5])
        self.assertEqual(b, [2, 3, 6, 8])
        self.assertEqual(solve_merge_sorted_lists([], [1, 4]), [1, 4])
        self.assertEqual(solve_merge_sorted_lists([-5, 0], [-3, 2]), [-5, -3, 0, 2])
        self.assertEqual(solve_merge_sorted_lists([], []), [])

    def test_activity_088(self) -> None:
        self.assertEqual(solve_apply_backspaces("ab#c"), "ac")
        self.assertEqual(solve_apply_backspaces("ab##"), "")
        self.assertEqual(solve_apply_backspaces("a##b"), "b")
        self.assertEqual(solve_apply_backspaces("###hello#"), "hell")
        self.assertEqual(solve_apply_backspaces(""), "")

    def test_activity_089(self) -> None:
        self.assertIs(solve_valid_brackets("({[]})"), True)
        self.assertIs(solve_valid_brackets("def f(x): return [x, {1: 2}]"), True)
        self.assertIs(solve_valid_brackets(""), True)
        self.assertIs(solve_valid_brackets("([)]"), False)
        self.assertIs(solve_valid_brackets("(([]"), False)
        self.assertIs(solve_valid_brackets("]"), False)
        self.assertIs(solve_valid_brackets("{[}]"), False)

    def test_activity_090(self) -> None:
        self.assertEqual(solve_longest_unique_substring("abcabcbb"), 3)
        self.assertEqual(solve_longest_unique_substring("bbbbb"), 1)
        self.assertEqual(solve_longest_unique_substring("pwwkew"), 3)
        self.assertEqual(solve_longest_unique_substring("dvdf"), 3)
        self.assertEqual(solve_longest_unique_substring("abba"), 2)
        self.assertEqual(solve_longest_unique_substring(""), 0)

    def test_activity_091(self) -> None:
        self.assertEqual(
            solve_max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]),
            6,
        )
        self.assertEqual(solve_max_subarray_sum([-5, -2, -8]), -2)
        self.assertEqual(solve_max_subarray_sum([-10]), -10)
        self.assertEqual(solve_max_subarray_sum([5]), 5)
        self.assertEqual(solve_max_subarray_sum([]), 0)

    def test_activity_092(self) -> None:
        original = [2, 4, 1, 3, 5]
        self.assertEqual(
            solve_insertion_sort_with_swaps(original),
            ([1, 2, 3, 4, 5], 3),
        )
        self.assertEqual(original, [2, 4, 1, 3, 5])
        self.assertEqual(solve_insertion_sort_with_swaps([3, 2, 1]), ([1, 2, 3], 3))
        self.assertEqual(solve_insertion_sort_with_swaps([1, 2, 3]), ([1, 2, 3], 0))
        self.assertEqual(solve_insertion_sort_with_swaps([5]), ([5], 0))
        self.assertEqual(solve_insertion_sort_with_swaps([]), ([], 0))

    def test_activity_093(self) -> None:
        self.assertEqual(solve_pascal_triangle(0), [])
        self.assertEqual(solve_pascal_triangle(-3), [])
        self.assertEqual(solve_pascal_triangle(1), [[1]])
        self.assertEqual(
            solve_pascal_triangle(5),
            [
                [1],
                [1, 1],
                [1, 2, 1],
                [1, 3, 3, 1],
                [1, 4, 6, 4, 1],
            ],
        )

    def test_activity_094(self) -> None:
        self.assertEqual(solve_spiral_matrix(0), [])
        self.assertEqual(solve_spiral_matrix(-1), [])
        self.assertEqual(solve_spiral_matrix(1), [[1]])
        self.assertEqual(
            solve_spiral_matrix(3),
            [
                [1, 2, 3],
                [8, 9, 4],
                [7, 6, 5],
            ],
        )
        self.assertEqual(
            solve_spiral_matrix(4),
            [
                [1, 2, 3, 4],
                [12, 13, 14, 5],
                [11, 16, 15, 6],
                [10, 9, 8, 7],
            ],
        )

    def test_activity_095(self) -> None:
        arr = [2, 4, 1, 3, 5]
        self.assertEqual(solve_count_inversions(arr), 3)
        self.assertEqual(arr, [2, 4, 1, 3, 5])
        self.assertEqual(solve_count_inversions([]), 0)
        self.assertEqual(solve_count_inversions([1, 2, 3, 4]), 0)
        self.assertEqual(solve_count_inversions([4, 3, 2, 1]), 6)
        self.assertEqual(solve_count_inversions([2, 2, 2]), 0)
        # Larger reverse-sorted list (500 items -> 500 * 499 // 2 = 124750 inversions)
        self.assertEqual(solve_count_inversions(list(range(500, 0, -1))), 124750)

    def test_activity_096(self) -> None:
        self.assertEqual(solve_longest_common_subsequence("ABCDGH", "AEDFHR"), 3)
        self.assertEqual(solve_longest_common_subsequence("AGGTAB", "GXTXAYB"), 4)
        self.assertEqual(solve_longest_common_subsequence("abc", "def"), 0)
        self.assertEqual(solve_longest_common_subsequence("", "python"), 0)
        self.assertEqual(solve_longest_common_subsequence("python", "python"), 6)
        self.assertEqual(solve_longest_common_subsequence("banana", "atana"), 4)


if __name__ == "__main__":
    unittest.main()
