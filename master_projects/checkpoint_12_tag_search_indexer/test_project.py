"""Unit tests for Checkpoint 12: Inverted Index & Mini Full-Text Search Engine."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from master_projects.checkpoint_12_tag_search_indexer import project, worked_example


class TestWorkedExample(unittest.TestCase):
    """Verify the Recipe Ingredient Matcher reference implementation."""

    def setUp(self) -> None:
        self.recipes = {
            "pasta": "Spaghetti, Garlic, Olive-Oil, Chili!",
            "shakshuka": "tomato garlic onion egg chili",
            "salad": "tomato mozzarella basil olive-oil",
        }
        self.index = worked_example.build_ingredient_index(self.recipes)

    def test_normalize_ingredients_strips_punctuation_and_cases(self) -> None:
        self.assertEqual(
            worked_example.normalize_ingredients("Garlic, Olive-Oil & 2 Eggs!"),
            {"garlic", "olive", "oil", "2", "eggs"},
        )

    def test_build_ingredient_index_maps_terms_to_recipe_sets(self) -> None:
        self.assertEqual(self.index["garlic"], {"pasta", "shakshuka"})
        self.assertEqual(self.index["tomato"], {"shakshuka", "salad"})
        self.assertEqual(self.index["basil"], {"salad"})

    def test_find_exact_recipes_intersection_and_missing_term(self) -> None:
        self.assertEqual(
            worked_example.find_exact_recipes(self.index, ["GARLIC", "chili"]),
            ["pasta", "shakshuka"],
        )
        self.assertEqual(
            worked_example.find_exact_recipes(self.index, ["garlic", "saffron"]),
            [],
        )

    def test_find_exact_recipes_empty_query(self) -> None:
        self.assertEqual(worked_example.find_exact_recipes(self.index, []), [])

    def test_rank_recipes_by_pantry_sorts_desc_then_alpha(self) -> None:
        ranked = worked_example.rank_recipes_by_pantry(
            self.index, ["tomato", "garlic", "tomato", "basil"]
        )
        # shakshuka: tomato + garlic (2), salad: tomato + basil (2), pasta: garlic (1)
        self.assertEqual(ranked, [("salad", 2), ("shakshuka", 2), ("pasta", 1)])


class TestMasterProject(unittest.TestCase):
    """Tests for the student's Inverted Index & Mini Full-Text Search Engine."""

    def setUp(self) -> None:
        self.docs = {
            "doc_a": "Python 3 search engine with inverted index",
            "doc_b": "Fast search engine using Python sets and dicts",
            "doc_c": "Docker container deployment guide for web apps",
            "doc_d": "Python dicts and sets performance guide",
        }

    def test_tokenize_lowercases_splits_punctuation_and_filters_stop_words(self) -> None:
        tokens = project.tokenize("Fast, 24/7 API-Search & fast indexing!")
        self.assertEqual(tokens, ["fast", "24", "7", "api", "search", "fast", "indexing"])

        filtered = project.tokenize(
            "The quick brown fox and the dog",
            stop_words={"THE", "and"},
        )
        self.assertEqual(filtered, ["quick", "brown", "fox", "dog"])

    def test_build_inverted_index_maps_terms_to_doc_sets(self) -> None:
        stop_words = {"with", "and", "for", "using"}
        index = project.build_inverted_index(self.docs, stop_words=stop_words)

        self.assertIsInstance(index, dict)
        self.assertEqual(index["python"], {"doc_a", "doc_b", "doc_d"})
        self.assertEqual(index["search"], {"doc_a", "doc_b"})
        self.assertEqual(index["docker"], {"doc_c"})
        self.assertNotIn("and", index)
        self.assertNotIn("with", index)

    def test_search_all_intersection_sorted_and_handles_missing_or_empty(self) -> None:
        index = project.build_inverted_index(self.docs)

        self.assertEqual(project.search_all(index, "Python sets"), ["doc_b", "doc_d"])
        self.assertEqual(project.search_all(index, "python search"), ["doc_a", "doc_b"])
        self.assertEqual(project.search_all(index, "python docker"), [])
        self.assertEqual(project.search_all(index, "   !!!  "), [])
        self.assertEqual(
            project.search_all(index, "and for", stop_words={"and", "for"}),
            [],
        )

    def test_search_any_ranks_by_distinct_match_count_and_tie_breaks(self) -> None:
        index = project.build_inverted_index(self.docs)

        # Query terms (unique): {"python", "sets", "guide"}
        # doc_d: python, sets, guide (3)
        # doc_b: python, sets (2)
        # doc_a: python (1)
        # doc_c: guide (1)
        # Repeated "python" in query must NOT double-count doc_a!
        ranked = project.search_any(index, "python python sets guide")
        self.assertEqual(ranked, ["doc_d", "doc_b", "doc_a", "doc_c"])
        self.assertEqual(project.search_any(index, ""), [])

    def test_suggest_related_docs_jaccard_ranking_and_top_k(self) -> None:
        mini_docs = {
            "d1": "python search index",
            "d2": "python search engine",     # |&|=2, |||=4 -> 0.5
            "d3": "python index engine rank", # |&|=2, |||=5 -> 0.4
            "d4": "python docker",            # |&|=1, |||=4 -> 0.25
            "d5": "rust compiler wasm",       # |&|=0 -> excluded
            "d0": "python search engine",     # ties with d2 at 0.5 -> d0 before d2
        }
        top_two = project.suggest_related_docs(mini_docs, "d1", top_k=2)
        self.assertEqual(top_two, [("d0", 0.5), ("d2", 0.5)])

        all_related = project.suggest_related_docs(mini_docs, "d1", top_k=10)
        self.assertEqual(
            all_related,
            [("d0", 0.5), ("d2", 0.5), ("d3", 0.4), ("d4", 0.25)],
        )
        self.assertEqual(project.suggest_related_docs(mini_docs, "d1", top_k=0), [])

    def test_suggest_related_docs_unknown_id_raises_key_error(self) -> None:
        with self.assertRaises(KeyError):
            project.suggest_related_docs(self.docs, "nonexistent_doc")


if __name__ == "__main__":
    unittest.main()
