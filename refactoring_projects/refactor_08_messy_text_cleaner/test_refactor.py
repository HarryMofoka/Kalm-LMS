"""Tests for Refactoring Mission 08: Messy Text Cleaner."""

import ast
import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from refactoring_projects.refactor_08_messy_text_cleaner import messy_code, worked_example


class TestWorkedExample(unittest.TestCase):
    """Verify the Before and After worked example implementations match."""

    def test_before_and_after_match_typical(self):
        raw = (
            "   Re:   FWD:  Exam   Schedule   Update  \n"
            "\n"
            "   Hi   everyone,\t\n"
            "   The   lab   starts   at   10:00.  \n"
            "   \n"
        )
        expected = "Exam Schedule Update\nHi everyone,\nThe lab starts at 10:00."
        self.assertEqual(worked_example.before_clean_message(raw), expected)
        self.assertEqual(worked_example.after_clean_message(raw), expected)

    def test_before_and_after_match_edge_cases(self):
        cases = [
            "",
            "   \n\t\n  ",
            "Re:   re:   Hello   world",
            "Single   line   only",
            "FWD:   \nBody line",
        ]
        for raw in cases:
            self.assertEqual(
                worked_example.before_clean_message(raw),
                worked_example.after_clean_message(raw),
            )


class TestBehaviorSafetyNet(unittest.TestCase):
    """Safety net: must stay 100% GREEN before, during, and after refactoring."""

    def test_clean_normal_comment(self):
        result = messy_code.moderate_comment("  Great   post,   thanks!  ", ["spam"])
        self.assertEqual(
            result,
            {
                "cleaned_text": "Great post thanks",
                "flagged_count": 0,
                "is_shouting": False,
                "status": "ok",
            },
        )

    def test_censors_banned_words_case_insensitive_with_punctuation(self):
        result = messy_code.moderate_comment(
            "  Buy   SPAM!!! and free (SCAM)?? now...  ",
            ["spam", "Scam"],
        )
        self.assertEqual(
            result,
            {
                "cleaned_text": "Buy *** and free *** now",
                "flagged_count": 2,
                "is_shouting": False,
                "status": "flagged",
            },
        )

    def test_detects_shouting_warning(self):
        result = messy_code.moderate_comment(
            "  STOP   DOING   THIS   NOW!!!  ",
            ["spam"],
        )
        self.assertEqual(
            result,
            {
                "cleaned_text": "STOP DOING THIS NOW",
                "flagged_count": 0,
                "is_shouting": True,
                "status": "warning",
            },
        )

    def test_shouting_and_banned_prioritizes_flagged(self):
        result = messy_code.moderate_comment(
            "YOU ARE TOTAL SPAM!!!",
            ["spam"],
        )
        self.assertEqual(
            result,
            {
                "cleaned_text": "YOU ARE TOTAL ***",
                "flagged_count": 1,
                "is_shouting": True,
                "status": "flagged",
            },
        )

    def test_short_uppercase_is_not_shouting(self):
        result = messy_code.moderate_comment("OK!", ["spam"])
        self.assertEqual(
            result,
            {
                "cleaned_text": "OK",
                "flagged_count": 0,
                "is_shouting": False,
                "status": "ok",
            },
        )

    def test_empty_and_punctuation_only_comments(self):
        for raw in ("", "   \t\n  ", "!!! ... ???"):
            self.assertEqual(
                messy_code.moderate_comment(raw, ["spam"]),
                {
                    "cleaned_text": "",
                    "flagged_count": 0,
                    "is_shouting": False,
                    "status": "empty",
                },
            )


class TestRefactorGoals(unittest.TestCase):
    """Structural refactoring goals: starts RED on baseline, turn GREEN!"""

    def _parse_messy_ast(self):
        source = Path(messy_code.__file__).read_text(encoding="utf-8")
        return ast.parse(source)

    def test_decomposed_into_at_least_four_functions(self):
        tree = self._parse_messy_ast()
        functions = [
            node for node in tree.body if isinstance(node, ast.FunctionDef)
        ]
        self.assertGreaterEqual(
            len(functions),
            4,
            f"Found only {len(functions)} function(s) in messy_code.py; "
            "decompose `moderate_comment` into at least 3 clean helpers (>= 4 functions total).",
        )

    def test_no_function_exceeds_25_lines(self):
        tree = self._parse_messy_ast()
        too_long = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                line_span = node.end_lineno - node.lineno + 1
                if line_span > 25:
                    too_long.append((node.name, line_span))
        self.assertEqual(
            too_long,
            [],
            f"Functions exceeding 25 lines: {too_long}. "
            "Break large functions into small, focused helpers (<= 25 lines each).",
        )

    def test_moderate_comment_delegates_to_helpers(self):
        tree = self._parse_messy_ast()
        module_funcs = {
            node.name for node in tree.body if isinstance(node, ast.FunctionDef)
        }
        helper_names = module_funcs - {"moderate_comment"}
        moderate_node = next(
            (
                node
                for node in tree.body
                if isinstance(node, ast.FunctionDef) and node.name == "moderate_comment"
            ),
            None,
        )
        self.assertIsNotNone(moderate_node, "`moderate_comment` function must exist.")
        called_helpers = {
            node.func.id
            for node in ast.walk(moderate_node)
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id in helper_names
        }
        self.assertGreaterEqual(
            len(called_helpers),
            3,
            f"`moderate_comment` only calls {len(called_helpers)} helper(s) ({sorted(called_helpers)}); "
            "delegate to at least 3 focused helper functions.",
        )


if __name__ == "__main__":
    unittest.main()
