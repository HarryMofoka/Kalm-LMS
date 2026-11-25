"""Test suite for Module 06: Dictionaries & Sets (Activities 061-072)."""

from __future__ import annotations

import importlib
import string
import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

_m061 = importlib.import_module("activities.06_dictionaries_and_sets.activity_061_dict_creation_squares")
_m062 = importlib.import_module("activities.06_dictionaries_and_sets.activity_062_char_frequency_map")
_m063 = importlib.import_module("activities.06_dictionaries_and_sets.activity_063_word_frequency_topk")
_m064 = importlib.import_module("activities.06_dictionaries_and_sets.activity_064_merging_dicts_safely")
_m065 = importlib.import_module("activities.06_dictionaries_and_sets.activity_065_inverting_filtering_dicts")
_m066 = importlib.import_module("activities.06_dictionaries_and_sets.activity_066_nested_dicts_inventory")
_m067 = importlib.import_module("activities.06_dictionaries_and_sets.activity_067_set_operations")
_m068 = importlib.import_module("activities.06_dictionaries_and_sets.activity_068_fast_membership_missing")
_m069 = importlib.import_module("activities.06_dictionaries_and_sets.activity_069_anagram_checking")
_m070 = importlib.import_module("activities.06_dictionaries_and_sets.activity_070_grouping_by_key")
_m071 = importlib.import_module("activities.06_dictionaries_and_sets.activity_071_two_sum_and_pairs")
_m072 = importlib.import_module("activities.06_dictionaries_and_sets.activity_072_inverted_index_and_cache")

example_squares_map = _m061.example_squares_map
solve_generate_squared_dict = _m061.solve_generate_squared_dict
example_char_frequency = _m062.example_char_frequency
solve_alphabet_frequency = _m062.solve_alphabet_frequency
example_word_counts = _m063.example_word_counts
solve_most_frequent_word = _m063.solve_most_frequent_word
example_override_merge = _m064.example_override_merge
solve_sum_merge_dicts = _m064.solve_sum_merge_dicts
example_filter_above_threshold = _m065.example_filter_above_threshold
solve_invert_dict_grouped = _m065.solve_invert_dict_grouped
example_cart_total = _m066.example_cart_total
solve_apply_stock_updates = _m066.solve_apply_stock_updates
example_common_elements = _m067.example_common_elements
solve_symmetric_difference_sorted = _m067.solve_symmetric_difference_sorted
example_find_missing_number = _m068.example_find_missing_number
solve_find_duplicates_in_order = _m068.solve_find_duplicates_in_order
example_is_anagram = _m069.example_is_anagram
solve_can_form_palindrome = _m069.solve_can_form_palindrome
example_group_by_first_letter = _m070.example_group_by_first_letter
solve_find_anagram_groups = _m070.solve_find_anagram_groups
example_two_sum = _m071.example_two_sum
solve_all_disjoint_pairs = _m071.solve_all_disjoint_pairs
example_build_inverted_index = _m072.example_build_inverted_index
solve_query_docs_with_all_tags = _m072.solve_query_docs_with_all_tags


class TestWorkedExamples(unittest.TestCase):
    """Verify all 12 worked examples in Module 06 pass out of the box."""

    def test_example_061(self) -> None:
        self.assertEqual(example_squares_map(4), {1: 1, 2: 4, 3: 9, 4: 16})
        self.assertEqual(example_squares_map(1), {1: 1})
        self.assertEqual(example_squares_map(0), {})
        self.assertEqual(example_squares_map(-3), {})

    def test_example_062(self) -> None:
        self.assertEqual(example_char_frequency("banana"), {"b": 1, "a": 3, "n": 2})
        self.assertEqual(example_char_frequency("AaA"), {"A": 2, "a": 1})
        self.assertEqual(example_char_frequency(""), {})

    def test_example_063(self) -> None:
        self.assertEqual(
            example_word_counts("The cat, and the hat!"),
            {"the": 2, "cat": 1, "and": 1, "hat": 1},
        )
        self.assertEqual(example_word_counts("!!! ---"), {})

    def test_example_064(self) -> None:
        base = {"a": 1, "b": 2}
        updates = {"b": 99, "c": 3}
        self.assertEqual(
            example_override_merge(base, updates),
            {"a": 1, "b": 99, "c": 3},
        )
        self.assertEqual(base, {"a": 1, "b": 2})
        self.assertEqual(updates, {"b": 99, "c": 3})

    def test_example_065(self) -> None:
        scores = {"ada": 95, "bo": 70, "cal": 85}
        self.assertEqual(
            example_filter_above_threshold(scores, 70),
            {"ada": 95, "cal": 85},
        )
        self.assertEqual(scores, {"ada": 95, "bo": 70, "cal": 85})
        self.assertEqual(example_filter_above_threshold(scores, 100), {})

    def test_example_066(self) -> None:
        catalog = {
            "apple": {"price": 1.25, "stock": 10},
            "bread": {"price": 2.50, "stock": 5},
        }
        self.assertEqual(
            example_cart_total(catalog, {"apple": 4, "bread": 1, "ghost": 2, "zero": 0}),
            7.5,
        )
        self.assertEqual(example_cart_total(catalog, {"apple": -3}), 0.0)
        self.assertEqual(example_cart_total(catalog, {}), 0.0)

    def test_example_067(self) -> None:
        self.assertEqual(example_common_elements([3, 1, 2, 2], [2, 3, 4]), [2, 3])
        self.assertEqual(example_common_elements([1, 2], [3, 4]), [])
        self.assertEqual(example_common_elements([], [1, 2]), [])

    def test_example_068(self) -> None:
        self.assertEqual(example_find_missing_number([3, 1, 4], 4), 2)
        self.assertIsNone(example_find_missing_number([1, 2, 3], 3))
        self.assertEqual(example_find_missing_number([], 1), 1)
        self.assertIsNone(example_find_missing_number([], 0))

    def test_example_069(self) -> None:
        self.assertTrue(example_is_anagram("Listen", "Silent"))
        self.assertTrue(example_is_anagram("Astronomer", "Moon starer"))
        self.assertFalse(example_is_anagram("hello", "helloo"))
        self.assertTrue(example_is_anagram("", "   "))

    def test_example_070(self) -> None:
        self.assertEqual(
            example_group_by_first_letter(["Apple", "ant", "Bear", ""]),
            {"a": ["Apple", "ant"], "b": ["Bear"]},
        )
        self.assertEqual(example_group_by_first_letter([]), {})

    def test_example_071(self) -> None:
        self.assertEqual(example_two_sum([2, 7, 11, 15], 9), (0, 1))
        self.assertEqual(example_two_sum([3, 3], 6), (0, 1))
        self.assertEqual(example_two_sum([3, 2, 4], 6), (1, 2))
        self.assertIsNone(example_two_sum([3], 6))
        self.assertIsNone(example_two_sum([1, 2, 3], 10))

    def test_example_072(self) -> None:
        docs = {
            "doc2": "Python dicts and sets!",
            "doc1": "Python lists and Python loops.",
        }
        self.assertEqual(
            example_build_inverted_index(docs),
            {
                "python": ["doc1", "doc2"],
                "dicts": ["doc2"],
                "and": ["doc1", "doc2"],
                "sets": ["doc2"],
                "lists": ["doc1"],
                "loops": ["doc1"],
            },
        )
        self.assertEqual(example_build_inverted_index({}), {})


class TestYourActivities(unittest.TestCase):
    """Test suite for student implementations in Module 06 (Activities 061-072)."""

    def test_activity_061(self) -> None:
        self.assertEqual(solve_generate_squared_dict(3), {1: 1, 2: 4, 3: 9})
        self.assertEqual(solve_generate_squared_dict(1), {1: 1})
        self.assertEqual(solve_generate_squared_dict(0), {})
        self.assertEqual(solve_generate_squared_dict(-1), {-1: 1})
        self.assertEqual(solve_generate_squared_dict(-3), {-3: 9, -2: 4, -1: 1})

    def test_activity_062(self) -> None:
        expected_abba = {ch: 0 for ch in string.ascii_lowercase}
        expected_abba["a"] = 2
        expected_abba["b"] = 2
        self.assertEqual(solve_alphabet_frequency("Abba! 123"), expected_abba)

        expected_empty = {ch: 0 for ch in string.ascii_lowercase}
        self.assertEqual(solve_alphabet_frequency(""), expected_empty)

        pangram_counts = solve_alphabet_frequency(
            "The quick brown fox jumps over the lazy dog!"
        )
        self.assertIsInstance(pangram_counts, dict)
        self.assertEqual(len(pangram_counts), 26)
        self.assertEqual(pangram_counts["o"], 4)
        self.assertEqual(pangram_counts["z"], 1)

    def test_activity_063(self) -> None:
        self.assertEqual(solve_most_frequent_word("red blue red green blue"), "blue")
        self.assertEqual(solve_most_frequent_word("Cat, dog, cat! Dog? Bat."), "cat")
        self.assertEqual(
            solve_most_frequent_word("One two two three three three"),
            "three",
        )
        self.assertEqual(solve_most_frequent_word("Hello!"), "hello")
        self.assertEqual(solve_most_frequent_word("!!!   ---"), "")
        self.assertEqual(solve_most_frequent_word(""), "")

    def test_activity_064(self) -> None:
        first = {"a": 2, "b": 3}
        second = {"b": 4, "c": 5}
        self.assertEqual(
            solve_sum_merge_dicts(first, second),
            {"a": 2, "b": 7, "c": 5},
        )
        self.assertEqual(first, {"a": 2, "b": 3})
        self.assertEqual(second, {"b": 4, "c": 5})
        self.assertEqual(solve_sum_merge_dicts({"x": 10}, {"x": -10}), {"x": 0})
        self.assertEqual(solve_sum_merge_dicts({"a": 1}, {}), {"a": 1})
        self.assertEqual(solve_sum_merge_dicts({}, {"b": 2}), {"b": 2})
        self.assertEqual(solve_sum_merge_dicts({}, {}), {})

    def test_activity_065(self) -> None:
        original = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
        self.assertEqual(
            solve_invert_dict_grouped(original),
            {1: ["a", "c"], 2: ["b", "e"], 3: ["d"]},
        )
        self.assertEqual(original, {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2})
        self.assertEqual(
            solve_invert_dict_grouped({"ada": "A", "bob": "B", "cal": "A"}),
            {"A": ["ada", "cal"], "B": ["bob"]},
        )
        self.assertEqual(solve_invert_dict_grouped({"only": 42}), {42: ["only"]})
        self.assertEqual(solve_invert_dict_grouped({}), {})

    def test_activity_066(self) -> None:
        inventory = {
            "pen": {"stock": 5, "price": 2},
            "book": {"stock": 2, "price": 15},
            "eraser": {"stock": 0, "price": 1},
        }
        deltas = {"pen": -5, "book": 3, "eraser": -2, "ghost": 10}
        result = solve_apply_stock_updates(inventory, deltas)
        self.assertEqual(
            result,
            (
                {
                    "pen": {"stock": 0, "price": 2},
                    "book": {"stock": 5, "price": 15},
                    "eraser": {"stock": 0, "price": 1},
                },
                ["eraser", "pen"],
            ),
        )
        # Ensure original outer and inner dicts were NOT mutated.
        self.assertEqual(inventory["pen"]["stock"], 5)
        self.assertEqual(inventory["book"]["stock"], 2)
        self.assertEqual(solve_apply_stock_updates({}, {"pen": 5}), ({}, []))

    def test_activity_067(self) -> None:
        self.assertEqual(
            solve_symmetric_difference_sorted([1, 2, 2, 3], [2, 3, 4, 4]),
            [1, 4],
        )
        self.assertEqual(
            solve_symmetric_difference_sorted(["a", "b"], ["b", "c"]),
            ["a", "c"],
        )
        self.assertEqual(solve_symmetric_difference_sorted([1, 2], [1, 2]), [])
        self.assertEqual(solve_symmetric_difference_sorted([], [3, 1, 2]), [1, 2, 3])
        self.assertEqual(solve_symmetric_difference_sorted([], []), [])

    def test_activity_068(self) -> None:
        original = ["a", "b", "c", "b", "a", "b"]
        self.assertEqual(solve_find_duplicates_in_order(original), ["b", "a"])
        self.assertEqual(original, ["a", "b", "c", "b", "a", "b"])
        self.assertEqual(
            solve_find_duplicates_in_order([1, 2, 3, 2, 1, 4, 4, 2]),
            [2, 1, 4],
        )
        self.assertEqual(solve_find_duplicates_in_order([1, 2, 3, 4]), [])
        self.assertEqual(solve_find_duplicates_in_order([5, 5, 5, 5]), [5])
        self.assertEqual(solve_find_duplicates_in_order([]), [])

    def test_activity_069(self) -> None:
        self.assertIs(solve_can_form_palindrome("civic"), True)
        self.assertIs(solve_can_form_palindrome("ivicc"), True)
        self.assertIs(solve_can_form_palindrome("Tact Coa"), True)
        self.assertIs(solve_can_form_palindrome("aabbcc"), True)
        self.assertIs(solve_can_form_palindrome("hello"), False)
        self.assertIs(solve_can_form_palindrome("ab"), False)
        self.assertIs(solve_can_form_palindrome("   "), True)
        self.assertIs(solve_can_form_palindrome(""), True)

    def test_activity_070(self) -> None:
        self.assertEqual(
            solve_find_anagram_groups(["eat", "tea", "tan", "ate", "nat", "bat"]),
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        )
        self.assertEqual(
            solve_find_anagram_groups(
                ["Listen", "Silent", "Dormitory", "Dirty room"]
            ),
            [["Listen", "Silent"], ["Dormitory", "Dirty room"]],
        )
        self.assertEqual(solve_find_anagram_groups(["solo"]), [["solo"]])
        self.assertEqual(solve_find_anagram_groups([]), [])

    def test_activity_071(self) -> None:
        self.assertEqual(
            solve_all_disjoint_pairs([2, 7, 11, 15, 7, 2], 9),
            [(0, 1), (4, 5)],
        )
        self.assertEqual(
            solve_all_disjoint_pairs([3, 3, 3, 3], 6),
            [(0, 1), (2, 3)],
        )
        self.assertEqual(solve_all_disjoint_pairs([3, 3, 3], 6), [(0, 1)])
        self.assertEqual(
            solve_all_disjoint_pairs([1, 1, 5, 5], 6),
            [(0, 2), (1, 3)],
        )
        self.assertEqual(solve_all_disjoint_pairs([1, 2, 3], 10), [])
        self.assertEqual(solve_all_disjoint_pairs([], 5), [])

    def test_activity_072(self) -> None:
        doc_tags = {
            "d1": {"Python", "exam", "loops"},
            "d2": {"python", "dicts"},
            "d3": {"PYTHON", "exam", "dicts"},
        }
        self.assertEqual(
            solve_query_docs_with_all_tags(doc_tags, ["python", "exam"]),
            ["d1", "d3"],
        )
        self.assertEqual(
            solve_query_docs_with_all_tags(doc_tags, ["PYTHON", "Dicts", "Exam"]),
            ["d3"],
        )
        self.assertEqual(solve_query_docs_with_all_tags(doc_tags, ["rust"]), [])
        self.assertEqual(
            solve_query_docs_with_all_tags(doc_tags, []),
            ["d1", "d2", "d3"],
        )
        self.assertEqual(solve_query_docs_with_all_tags({}, ["python"]), [])
        # Ensure original sets were not mutated.
        self.assertEqual(doc_tags["d1"], {"Python", "exam", "loops"})


if __name__ == "__main__":
    unittest.main()
