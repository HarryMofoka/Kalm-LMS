"""Unit tests for Module 07: Functions, Validation, and TDD (Activities 073-084)."""

from __future__ import annotations

import importlib
import io
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

_PKG = "activities.07_functions_validation_and_tdd"

_m073 = importlib.import_module(f"{_PKG}.activity_073_pure_return_vs_print")
_m074 = importlib.import_module(f"{_PKG}.activity_074_helper_decomposition")
_m075 = importlib.import_module(f"{_PKG}.activity_075_default_args_and_flags")
_m076 = importlib.import_module(f"{_PKG}.activity_076_strict_input_validation")
_m077 = importlib.import_module(f"{_PKG}.activity_077_list_validation_and_immutability")
_m078 = importlib.import_module(f"{_PKG}.activity_078_safe_validation_pipelines")
_m079 = importlib.import_module(f"{_PKG}.activity_079_custom_sort_keys")
_m080 = importlib.import_module(f"{_PKG}.activity_080_multi_criteria_leaderboards")
_m081 = importlib.import_module(f"{_PKG}.activity_081_higher_order_functions")
_m082 = importlib.import_module(f"{_PKG}.activity_082_recursion_intro")
_m083 = importlib.import_module(f"{_PKG}.activity_083_recursion_vs_iteration")
_m084 = importlib.import_module(f"{_PKG}.activity_084_property_invariants_and_tdd")

example_format_row = _m073.example_format_row
solve_build_banner_lines = _m073.solve_build_banner_lines

example_vowel_density = _m074.example_vowel_density
clean_word = _m074.clean_word
solve_word_length_stats = _m074.solve_word_length_stats

example_greet_customer = _m075.example_greet_customer
solve_format_currency = _m075.solve_format_currency

example_count_vowels_strict = _m076.example_count_vowels_strict
solve_merge_dicts = _m076.solve_merge_dicts
solve_is_prime = _m076.solve_is_prime

example_validate_int_list = _m077.example_validate_int_list
solve_sorted_strings_copy = _m077.solve_sorted_strings_copy

example_collect_password_errors = _m078.example_collect_password_errors
solve_validate_profile = _m078.solve_validate_profile

example_sort_by_second = _m079.example_sort_by_second
solve_sort_words_by_length = _m079.solve_sort_words_by_length

example_rank_students = _m080.example_rank_students
solve_rank_teams = _m080.solve_rank_teams

example_apply_transform = _m081.example_apply_transform
solve_group_by = _m081.solve_group_by

example_recursive_sum = _m082.example_recursive_sum
solve_is_palindrome_recursive = _m082.solve_is_palindrome_recursive
solve_fast_pow = _m082.solve_fast_pow

example_flatten_recursive = _m083.example_flatten_recursive
solve_nested_sum_iterative = _m083.solve_nested_sum_iterative

example_verify_sort_invariants = _m084.example_verify_sort_invariants
solve_verify_walk_invariants = _m084.solve_verify_walk_invariants


class TestWorkedExamples(unittest.TestCase):
    """Verify all 12 worked examples ('I Do') pass completely."""

    def test_example_073(self) -> None:
        self.assertEqual(example_format_row(["#", " ", "#"]), "#   #")
        self.assertEqual(example_format_row(["X"]), "X")
        self.assertEqual(example_format_row([]), "")

    def test_example_074(self) -> None:
        self.assertEqual(example_vowel_density("Hello, World!"), 0.3)
        self.assertEqual(example_vowel_density("AEIOU"), 1.0)
        self.assertEqual(example_vowel_density("12345!!!"), 0.0)
        self.assertEqual(example_vowel_density(""), 0.0)

    def test_example_075(self) -> None:
        self.assertEqual(example_greet_customer("Ada"), "Hello, Member Ada.")
        self.assertEqual(
            example_greet_customer("Ada", title="Dr.", excited=True),
            "Hello, Dr. Ada!",
        )
        self.assertEqual(example_greet_customer("Ada", title=""), "Hello, Ada.")
        self.assertEqual(
            example_greet_customer("Ada", title="  ", excited=True),
            "Hello, Ada!",
        )

    def test_example_076(self) -> None:
        self.assertEqual(example_count_vowels_strict("Programming"), 3)
        self.assertEqual(example_count_vowels_strict(""), 0)
        with self.assertRaises(TypeError) as ctx:
            example_count_vowels_strict(123)  # type: ignore[arg-type]
        self.assertEqual(str(ctx.exception), "Input must be a string.")

    def test_example_077(self) -> None:
        original = [5, 2, 9, 1]
        result = example_validate_int_list(original)
        self.assertEqual(result, [1, 2, 5, 9])
        self.assertEqual(original, [5, 2, 9, 1])
        self.assertIsNot(result, original)
        self.assertEqual(example_validate_int_list([]), [])
        with self.assertRaises(TypeError) as ctx:
            example_validate_int_list([1, True, 3])  # type: ignore[list-item]
        self.assertEqual(str(ctx.exception), "Input must be a list of integers.")
        with self.assertRaises(TypeError):
            example_validate_int_list((1, 2))  # type: ignore[arg-type]

    def test_example_078(self) -> None:
        self.assertEqual(example_collect_password_errors("Secret99"), [])
        self.assertEqual(
            example_collect_password_errors("abc"),
            [
                "Must be at least 8 characters.",
                "Must contain an uppercase letter.",
                "Must contain a digit.",
            ],
        )
        self.assertEqual(
            example_collect_password_errors("Bad Pass 9"),
            ["Must not contain spaces."],
        )
        self.assertEqual(
            example_collect_password_errors(999),  # type: ignore[arg-type]
            ["Password must be a string."],
        )

    def test_example_079(self) -> None:
        data = [("beta", 2), ("alpha", 2), ("gamma", 1)]
        result = example_sort_by_second(data)
        self.assertEqual(result, [("gamma", 1), ("alpha", 2), ("beta", 2)])
        self.assertEqual(data, [("beta", 2), ("alpha", 2), ("gamma", 1)])
        self.assertEqual(example_sort_by_second([]), [])

    def test_example_080(self) -> None:
        roster = [("Zoe", 88), ("Bob", 95), ("Alice", 95), ("Mia", -5), ("Dan", -10)]
        result = example_rank_students(roster)
        self.assertEqual(
            result,
            [("Alice", 95), ("Bob", 95), ("Zoe", 88), ("Mia", -5), ("Dan", -10)],
        )
        self.assertEqual(roster[0], ("Zoe", 88))

    def test_example_081(self) -> None:
        nums = [1, 2, 3]
        self.assertEqual(example_apply_transform(nums, lambda x: x * 10), [10, 20, 30])
        self.assertEqual(nums, [1, 2, 3])
        self.assertEqual(example_apply_transform([], str), [])
        with self.assertRaises(TypeError) as ctx:
            example_apply_transform([1, 2], 123)  # type: ignore[arg-type]
        self.assertEqual(str(ctx.exception), "transform_fn must be callable.")

    def test_example_082(self) -> None:
        self.assertEqual(example_recursive_sum([]), 0)
        self.assertEqual(example_recursive_sum([4, 7, 2]), 13)
        self.assertEqual(example_recursive_sum([-3, 1.5, 2.5]), 1.0)

    def test_example_083(self) -> None:
        nested = [1, [2, [3, 4], []], 5]
        self.assertEqual(example_flatten_recursive(nested), [1, 2, 3, 4, 5])
        self.assertEqual(nested, [1, [2, [3, 4], []], 5])
        self.assertEqual(example_flatten_recursive([[], [[]]]), [])

    def test_example_084(self) -> None:
        self.assertEqual(
            example_verify_sort_invariants([3, 1, 2, 1], [1, 1, 2, 3]),
            (True, []),
        )
        self.assertEqual(
            example_verify_sort_invariants([], []),
            (True, []),
        )
        self.assertEqual(
            example_verify_sort_invariants([3, 1, 3], [3, 1]),
            (
                False,
                [
                    "Length mismatch.",
                    "Elements changed.",
                    "Not sorted in non-decreasing order.",
                ],
            ),
        )


class TestYourActivities(unittest.TestCase):
    """Tests for your implementations ('You Do') across Activities 073-084."""

    def test_activity_073(self) -> None:
        buf = io.StringIO()
        with redirect_stdout(buf):
            lines = solve_build_banner_lines("GAME OVER")
        self.assertEqual(
            lines,
            [
                "=============",
                "= GAME OVER =",
                "=============",
            ],
        )
        self.assertEqual(buf.getvalue(), "")
        self.assertEqual(
            solve_build_banner_lines("HI", "*"),
            ["******", "* HI *", "******"],
        )
        self.assertEqual(
            solve_build_banner_lines(""),
            ["====", "=  =", "===="],
        )

    def test_activity_074(self) -> None:
        self.assertEqual(
            solve_word_length_stats("Hi, Python! 2026 rocks."),
            {"count": 3, "shortest": 2, "longest": 6, "average": 4.33},
        )
        self.assertEqual(
            solve_word_length_stats("42 ??? ---"),
            {"count": 0, "shortest": 0, "longest": 0, "average": 0.0},
        )
        self.assertEqual(
            solve_word_length_stats(""),
            {"count": 0, "shortest": 0, "longest": 0, "average": 0.0},
        )
        self.assertEqual(clean_word("PyThOn3!"), "python")
        self.assertEqual(clean_word("999"), "")

    def test_activity_075(self) -> None:
        self.assertEqual(solve_format_currency(1234.5), "$1,234.50")
        self.assertEqual(solve_format_currency(-42.1), "-$42.10")
        self.assertEqual(solve_format_currency(99.9, symbol="R ", decimals=2), "R 99.90")
        self.assertEqual(solve_format_currency(1500, symbol="€", decimals=0), "€1,500")
        self.assertEqual(solve_format_currency(25.5, show_plus=True), "+$25.50")
        self.assertEqual(solve_format_currency(0, show_plus=True), "$0.00")
        self.assertEqual(solve_format_currency(-0.0001, decimals=2), "$0.00")

    def test_activity_076(self) -> None:
        d1 = {"a": 2, "b": 3}
        d2 = {"b": 4, "c": 5}
        merged = solve_merge_dicts(d1, d2)
        self.assertEqual(merged, {"a": 2, "b": 7, "c": 5})
        self.assertEqual(d1, {"a": 2, "b": 3})
        self.assertEqual(d2, {"b": 4, "c": 5})
        with self.assertRaises(TypeError) as ctx_dict:
            solve_merge_dicts(d1, "not a dict")  # type: ignore[arg-type]
        self.assertEqual(str(ctx_dict.exception), "Both inputs must be dictionaries.")

        self.assertIs(solve_is_prime(2), True)
        self.assertIs(solve_is_prime(17), True)
        self.assertIs(solve_is_prime(1), False)
        self.assertIs(solve_is_prime(0), False)
        self.assertIs(solve_is_prime(-7), False)
        self.assertIs(solve_is_prime(25), False)
        for bad in (True, False, 3.0, "7", None):
            with self.assertRaises(TypeError) as ctx_prime:
                solve_is_prime(bad)  # type: ignore[arg-type]
            self.assertEqual(str(ctx_prime.exception), "Input must be an integer.")

    def test_activity_077(self) -> None:
        words = ["pear", "apple", "banana"]
        asc = solve_sorted_strings_copy(words)
        self.assertEqual(asc, ["apple", "banana", "pear"])
        self.assertEqual(words, ["pear", "apple", "banana"])
        self.assertIsNot(asc, words)

        desc = solve_sorted_strings_copy(words, reverse=True)
        self.assertEqual(desc, ["pear", "banana", "apple"])

        empty: list[str] = []
        empty_copy = solve_sorted_strings_copy(empty)
        self.assertEqual(empty_copy, [])
        self.assertIsNot(empty_copy, empty)

        for bad in ("hello", ("a", "b"), ["ok", 99], [None]):
            with self.assertRaises(TypeError) as ctx:
                solve_sorted_strings_copy(bad)  # type: ignore[arg-type]
            self.assertEqual(str(ctx.exception), "Input must be a list of strings.")

    def test_activity_078(self) -> None:
        valid = {"username": "ada", "age": 28, "email": "ada@example.com"}
        self.assertEqual(solve_validate_profile(valid), (True, []))

        all_bad = {"username": "  ", "age": True, "email": "no-at-sign"}
        self.assertEqual(
            solve_validate_profile(all_bad),
            (False, ["Invalid username.", "Invalid age.", "Invalid email."]),
        )

        self.assertEqual(
            solve_validate_profile("not a dict"),  # type: ignore[arg-type]
            (False, ["Profile must be a dictionary."]),
        )
        self.assertEqual(
            solve_validate_profile({"username": "bob", "age": 12, "email": "bob@site.org"}),
            (False, ["Invalid age."]),
        )
        self.assertEqual(
            solve_validate_profile({"username": "bob", "age": 20, "email": "a@b@c.com"}),
            (False, ["Invalid email."]),
        )
        self.assertEqual(
            solve_validate_profile({"username": "bob", "age": 20, "email": "@example.com"}),
            (False, ["Invalid email."]),
        )
        self.assertEqual(
            solve_validate_profile({"username": "bob", "age": 20, "email": "bob@.com"}),
            (False, ["Invalid email."]),
        )
        self.assertEqual(
            solve_validate_profile({"username": "bob", "age": 20, "email": "bob@site .com"}),
            (False, ["Invalid email."]),
        )

    def test_activity_079(self) -> None:
        words = ["banana", "fig", "apple", "bat", "ant"]
        result = solve_sort_words_by_length(words)
        self.assertEqual(result, ["ant", "bat", "fig", "apple", "banana"])
        self.assertEqual(words, ["banana", "fig", "apple", "bat", "ant"])
        self.assertIsNot(result, words)
        self.assertEqual(solve_sort_words_by_length(["b", "a", ""]), ["", "a", "b"])
        self.assertEqual(solve_sort_words_by_length([]), [])
        with self.assertRaises(TypeError) as ctx:
            solve_sort_words_by_length(("a", "b"))  # type: ignore[arg-type]
        self.assertEqual(str(ctx.exception), "Input must be a list of strings.")
        with self.assertRaises(TypeError) as ctx2:
            solve_sort_words_by_length(["a", 1])  # type: ignore[list-item]
        self.assertEqual(str(ctx2.exception), "Input must be a list of strings.")

    def test_activity_080(self) -> None:
        teams = [
            {"name": "Lions", "points": 12, "goal_diff": 4},
            {"name": "Eagles", "points": 12, "goal_diff": 7},
            {"name": "Bears", "points": 12, "goal_diff": 4},
            {"name": "Sharks", "points": 15, "goal_diff": 2},
            {"name": "Wolves", "points": 5, "goal_diff": -2},
            {"name": "Foxes", "points": 5, "goal_diff": -7},
        ]
        snapshot = [dict(t) for t in teams]
        self.assertEqual(
            solve_rank_teams(teams),
            ["Sharks", "Eagles", "Bears", "Lions", "Wolves", "Foxes"],
        )
        self.assertEqual(teams, snapshot)
        self.assertEqual(solve_rank_teams([]), [])

    def test_activity_081(self) -> None:
        words = ["ant", "bear", "cat", "dog", "elephant"]
        grouped = solve_group_by(words, len)
        self.assertEqual(
            grouped,
            {3: ["ant", "cat", "dog"], 4: ["bear"], 8: ["elephant"]},
        )
        self.assertEqual(list(grouped.keys()), [3, 4, 8])
        self.assertEqual(words, ["ant", "bear", "cat", "dog", "elephant"])
        self.assertEqual(solve_group_by([], len), {})
        with self.assertRaises(TypeError) as ctx:
            solve_group_by([1, 2], "not_callable")  # type: ignore[arg-type]
        self.assertEqual(str(ctx.exception), "key_fn must be callable.")

    def test_activity_082(self) -> None:
        self.assertIs(
            solve_is_palindrome_recursive("A man, a plan, a canal: Panama!"),
            True,
        )
        self.assertIs(solve_is_palindrome_recursive("racecar"), True)
        self.assertIs(solve_is_palindrome_recursive(""), True)
        self.assertIs(solve_is_palindrome_recursive("x"), True)
        self.assertIs(solve_is_palindrome_recursive("Python"), False)

        self.assertEqual(solve_fast_pow(2, 10), 1024)
        self.assertEqual(solve_fast_pow(5, 0), 1)
        self.assertEqual(solve_fast_pow(-3, 3), -27)
        self.assertEqual(solve_fast_pow(2, 1), 2)
        with self.assertRaises(ValueError) as ctx:
            solve_fast_pow(2, -1)
        self.assertEqual(str(ctx.exception), "Exponent must be non-negative.")

    def test_activity_083(self) -> None:
        nested = [1, [2, [3, 4]], 5]
        self.assertEqual(solve_nested_sum_iterative(nested), 15)
        self.assertEqual(nested, [1, [2, [3, 4]], 5])
        self.assertEqual(solve_nested_sum_iterative([[], [[10], [-2, 0.5]]]), 8.5)
        self.assertEqual(solve_nested_sum_iterative([[], [[]]]), 0)
        # Deeply nested structure (1500 levels) that would overflow recursion limit!
        deep: list = [7]
        for _ in range(1500):
            deep = [deep]
        self.assertEqual(solve_nested_sum_iterative(deep), 7)

    def test_activity_084(self) -> None:
        valid_walk = [
            (0, 0), (0, 1), (0, 2),
            (1, 2), (2, 2),
            (2, 1), (2, 0), (1, 0),
        ]
        self.assertEqual(solve_verify_walk_invariants(valid_walk, 8), (True, []))
        self.assertEqual(solve_verify_walk_invariants([], 0), (True, []))
        self.assertEqual(solve_verify_walk_invariants([(0, 0)], 1), (True, []))

        self.assertEqual(
            solve_verify_walk_invariants([(0, 1), (1, 2)], 2),
            (
                False,
                [
                    "Walk must start at (0, 0).",
                    "Non-adjacent step found.",
                    "Walk does not form a closed loop.",
                ],
            ),
        )
        self.assertEqual(
            solve_verify_walk_invariants([(0, 0), (0, 1), (0, 0)], 4),
            (
                False,
                [
                    "Length mismatch.",
                    "Duplicate coordinates found.",
                    "Walk does not form a closed loop.",
                ],
            ),
        )


if __name__ == "__main__":
    unittest.main()
