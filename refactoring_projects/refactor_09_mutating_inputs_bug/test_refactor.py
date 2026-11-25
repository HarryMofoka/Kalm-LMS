"""Tests for Refactoring Mission 09: Mutating Inputs Bug."""

import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from refactoring_projects.refactor_09_mutating_inputs_bug import messy_code, worked_example


class TestWorkedExample(unittest.TestCase):
    """Verify the Before and After worked example implementations."""

    def test_before_and_after_return_same_results(self):
        sample = [("Sunset", 42), ("Neon Drive", 115), ("Lo-Fi Rain", 88), ("Alpha", 88)]
        for limit in (0, 1, 2, 10):
            self.assertEqual(
                worked_example.before_top_tracks(list(sample), limit),
                worked_example.after_top_tracks(list(sample), limit),
            )
        self.assertEqual(worked_example.after_top_tracks([], 3), [])

    def test_after_preserves_caller_list_unlike_before(self):
        playlist = [("Sunset", 42), ("Neon Drive", 115), ("Lo-Fi Rain", 88)]
        snapshot = list(playlist)
        result = worked_example.after_top_tracks(playlist, 2)
        self.assertEqual(result, [("Neon Drive", 115), ("Lo-Fi Rain", 88)])
        self.assertEqual(playlist, snapshot)
        self.assertIsNot(result, playlist)


class TestBehaviorSafetyNet(unittest.TestCase):
    """Safety net: tests returned values on single-occurrence inputs (GREEN on baseline)."""

    def test_removes_blacklisted_adds_promo_and_sorts(self):
        result = messy_code.prepare_checkout_cart(
            ["milk", "recalled_egg", "bread"],
            "free_mug",
            ["recalled_egg"],
        )
        self.assertEqual(result, ["bread", "free_mug", "milk"])

    def test_does_not_duplicate_existing_promo_item(self):
        result = messy_code.prepare_checkout_cart(
            ["bananas", "apples"],
            "apples",
            [],
        )
        self.assertEqual(result, ["apples", "bananas"])

    def test_skips_blacklisted_or_empty_promo_item(self):
        self.assertEqual(
            messy_code.prepare_checkout_cart(["apples"], "recalled_toy", ["recalled_toy"]),
            ["apples"],
        )
        self.assertEqual(
            messy_code.prepare_checkout_cart(["tea", "coffee"], None, []),
            ["coffee", "tea"],
        )
        self.assertEqual(
            messy_code.prepare_checkout_cart(["tea", "coffee"], "", []),
            ["coffee", "tea"],
        )

    def test_empty_cart_with_and_without_promo(self):
        self.assertEqual(
            messy_code.prepare_checkout_cart([], "sticker", []),
            ["sticker"],
        )
        self.assertEqual(
            messy_code.prepare_checkout_cart([], None, []),
            [],
        )

    def test_preserves_legitimate_duplicate_items(self):
        result = messy_code.prepare_checkout_cart(
            ["milk", "bread", "milk"],
            None,
            ["recalled_egg"],
        )
        self.assertEqual(result, ["bread", "milk", "milk"])


class TestRefactorGoals(unittest.TestCase):
    """Safety & correctness goals: starts RED on baseline, turn GREEN!"""

    def test_does_not_mutate_caller_items(self):
        original_items = ["milk", "recalled_egg", "bread"]
        snapshot = list(original_items)
        result = messy_code.prepare_checkout_cart(
            original_items,
            "free_mug",
            ["recalled_egg"],
        )
        self.assertEqual(result, ["bread", "free_mug", "milk"])
        self.assertEqual(
            original_items,
            snapshot,
            "Caller's `items` list was mutated in place! Build and return a new list.",
        )

    def test_does_not_mutate_caller_blacklist(self):
        original_blacklist = ["zebra_recall", "apple_recall"]
        snapshot = list(original_blacklist)
        messy_code.prepare_checkout_cart(["milk"], "free_mug", original_blacklist)
        self.assertEqual(
            original_blacklist,
            snapshot,
            "Caller's `blacklist` list was mutated in place! Do not sort or modify inputs.",
        )

    def test_returns_new_list_object_not_alias(self):
        original_items = ["bread", "milk"]
        result = messy_code.prepare_checkout_cart(original_items, None, [])
        self.assertEqual(result, ["bread", "milk"])
        self.assertIsNot(
            result,
            original_items,
            "Returned the exact same list object as `items` (aliasing bug)! Return a fresh list.",
        )

    def test_removes_all_duplicate_blacklisted_items(self):
        original_items = ["bad", "milk", "bad", "bread", "bad"]
        snapshot = list(original_items)
        result = messy_code.prepare_checkout_cart(original_items, "mug", ["bad"])
        self.assertEqual(
            result,
            ["bread", "milk", "mug"],
            "Failed to remove all duplicate occurrences of blacklisted items!",
        )
        self.assertEqual(original_items, snapshot)


if __name__ == "__main__":
    unittest.main()
