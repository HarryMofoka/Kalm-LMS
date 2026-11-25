"""Unit tests for Checkpoint 15: Source Code Bracket & Quote Linter."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from master_projects.checkpoint_15_code_linter_bracket_checker import (
    project,
    worked_example,
)


class TestWorkedExample(unittest.TestCase):
    """Verify the HTML/XML Tag Balance Checker reference implementation."""

    def test_valid_nested_markup_with_self_closing_tags(self) -> None:
        html = (
            '<div class="card">\n'
            '  <img src="icon.png" />\n'
            "  <p>Line 1<br/>Line 2</p>\n"
            "</div>"
        )
        self.assertEqual(
            worked_example.check_markup_balance(html),
            {"valid": True, "error": None},
        )

    def test_mismatched_closing_tag_reports_exact_line(self) -> None:
        html = "<div>\n  <p>Oops</div>\n</p>"
        result = worked_example.check_markup_balance(html)
        self.assertIs(result["valid"], False)
        self.assertEqual(result["error"]["line"], 2)
        self.assertIn("</p>", result["error"]["message"])
        self.assertIn("</div>", result["error"]["message"])

    def test_unexpected_closing_tag_on_empty_stack(self) -> None:
        html = "<p>ok</p>\n</span>"
        result = worked_example.check_markup_balance(html)
        self.assertIs(result["valid"], False)
        self.assertEqual(result["error"]["line"], 2)
        self.assertIn("</span>", result["error"]["message"])

    def test_unclosed_opening_tag_reports_opening_line(self) -> None:
        html = "<section>\n  <div>\n    <p>Done</p>\n</section>"
        result = worked_example.check_markup_balance(html)
        self.assertIs(result["valid"], False)
        self.assertEqual(result["error"]["line"], 4)

        eof_unclosed = "<section>\n  <article>\n    <p>Hello</p>"
        eof_result = worked_example.check_markup_balance(eof_unclosed)
        self.assertIs(eof_result["valid"], False)
        self.assertEqual(eof_result["error"]["line"], 2)
        self.assertIn("<article>", eof_result["error"]["message"])

    def test_comments_with_broken_tags_are_ignored(self) -> None:
        html = "<div>\n  <!-- <unclosed> </span>\n  multi-line -->\n  <p>OK</p>\n</div>"
        self.assertEqual(
            worked_example.check_markup_balance(html),
            {"valid": True, "error": None},
        )


class TestMasterProject(unittest.TestCase):
    """Tests for the student's Source Code Bracket & Quote Linter."""

    def test_lint_brackets_valid_multiline_code(self) -> None:
        code = (
            "def summarize(records):\n"
            "    totals = {'ok': [1, (2 + 3)], 'empty': []}\n"
            "    return (totals['ok'][0], len(records))\n"
        )
        self.assertEqual(project.lint_brackets(code), {"valid": True, "error": None})
        self.assertEqual(project.lint_brackets(""), {"valid": True, "error": None})

    def test_lint_brackets_ignores_strings_escapes_and_comments(self) -> None:
        code = (
            'msg = "escaped quote \\" and fake brackets ([{ # not a comment"\n'
            "single = 'another \\' )]} test'\n"
            "items = [1, 2, 3]  # comment with unclosed ({[\n"
        )
        self.assertEqual(project.lint_brackets(code), {"valid": True, "error": None})

    def test_lint_brackets_mismatched_reports_exact_line_and_col(self) -> None:
        bad_code = (
            "def compute(items):\n"
            "    data = [1, (2 + 3]\n"
            "    return data\n"
        )
        result = project.lint_brackets(bad_code)
        self.assertIsInstance(result, dict)
        self.assertIs(result["valid"], False)
        self.assertIsInstance(result["error"], dict)
        self.assertEqual(result["error"]["line"], 2)
        self.assertEqual(result["error"]["col"], 22)
        self.assertIn(")", result["error"]["message"])
        self.assertIn("]", result["error"]["message"])

    def test_lint_brackets_unexpected_closing_bracket(self) -> None:
        code = "x = 1\ny = 2)\n"
        result = project.lint_brackets(code)
        self.assertIsInstance(result, dict)
        self.assertIs(result["valid"], False)
        self.assertEqual(result["error"]["line"], 2)
        self.assertEqual(result["error"]["col"], 6)
        self.assertIn(")", result["error"]["message"])

    def test_lint_brackets_unclosed_opening_bracket_at_eof(self) -> None:
        code = "cfg = {\n    'a': [1, 2]\n"
        result = project.lint_brackets(code)
        self.assertIsInstance(result, dict)
        self.assertIs(result["valid"], False)
        self.assertEqual(result["error"]["line"], 1)
        self.assertEqual(result["error"]["col"], 7)
        self.assertIn("{", result["error"]["message"])

    def test_lint_brackets_unterminated_string_literal(self) -> None:
        code = 'x = (1 + 2)\nmsg = "hello (world\n'
        result = project.lint_brackets(code)
        self.assertIsInstance(result, dict)
        self.assertIs(result["valid"], False)
        self.assertEqual(result["error"]["line"], 2)
        self.assertEqual(result["error"]["col"], 7)
        self.assertIn("string", result["error"]["message"].lower())

    def test_find_matching_pairs_sorted_and_invalid_raises_value_error(self) -> None:
        self.assertEqual(
            project.find_matching_pairs("fn(a[0], {1: (2)})"),
            [(2, 17), (4, 6), (9, 16), (13, 15)],
        )
        self.assertEqual(
            project.find_matching_pairs("s = '(not [a] bracket)' # {ignored}"),
            [],
        )
        self.assertEqual(
            project.find_matching_pairs('call("esc \\" )")'),
            [(4, 15)],
        )

        with self.assertRaises(ValueError):
            project.find_matching_pairs("arr = [1, (2, 3]")
        with self.assertRaises(ValueError):
            project.find_matching_pairs("arr = [1, 2")
        with self.assertRaises(ValueError):
            project.find_matching_pairs('s = "unterminated')


if __name__ == "__main__":
    unittest.main()
