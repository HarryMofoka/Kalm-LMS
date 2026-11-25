"""Tests for Refactoring Mission 07: String Concatenation Chaos."""

import ast
import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from refactoring_projects.refactor_07_string_concat_chaos import messy_code, worked_example


class TestWorkedExample(unittest.TestCase):
    """Verify the Before and After worked example implementations match."""

    def test_before_and_after_match_typical(self):
        fields = ["  Alice  ", "", "  Python 101 ", 42, "   "]
        expected = "Alice,Python 101,42"
        self.assertEqual(worked_example.before_build_csv(fields), expected)
        self.assertEqual(worked_example.after_build_csv(fields), expected)

    def test_before_and_after_match_edge_cases(self):
        cases = [
            [],
            ["", "   ", "\t"],
            ["only-one"],
            [1, 2, 3],
        ]
        for fields in cases:
            self.assertEqual(
                worked_example.before_build_csv(fields),
                worked_example.after_build_csv(fields),
            )


class TestBehaviorSafetyNet(unittest.TestCase):
    """Safety net: must stay 100% GREEN before, during, and after refactoring."""

    def test_typical_article_and_tags(self):
        result = messy_code.format_slug_and_tags(
            "  Hello, World!!  Python_3 - Rocks! ",
            ["  Python ", "WEB Dev", "#Exam_Prep!"],
        )
        self.assertEqual(
            result,
            {
                "slug": "hello-world-python-3-rocks",
                "tag_line": "#python, #web-dev, #exam-prep",
            },
        )

    def test_empty_and_punctuation_only_inputs(self):
        self.assertEqual(
            messy_code.format_slug_and_tags("", []),
            {"slug": "", "tag_line": ""},
        )
        self.assertEqual(
            messy_code.format_slug_and_tags("!!! --- ___", ["", "   ", "###"]),
            {"slug": "", "tag_line": ""},
        )

    def test_single_word_and_single_tag(self):
        self.assertEqual(
            messy_code.format_slug_and_tags("Intro", ["basics"]),
            {"slug": "intro", "tag_line": "#basics"},
        )

    def test_mixed_separators_and_numbers(self):
        result = messy_code.format_slug_and_tags(
            "2026_Final   Exam--Guide",
            ["CS 101", "  tip-2 "],
        )
        self.assertEqual(
            result,
            {
                "slug": "2026-final-exam-guide",
                "tag_line": "#cs-101, #tip-2",
            },
        )

    def test_skips_blank_tags_in_middle(self):
        result = messy_code.format_slug_and_tags(
            "C++ & Python: Exam Prep",
            ["first", "   ", "!!!", "second"],
        )
        self.assertEqual(
            result,
            {
                "slug": "c-python-exam-prep",
                "tag_line": "#first, #second",
            },
        )


class TestRefactorGoals(unittest.TestCase):
    """Structural refactoring goals: starts RED on baseline, turn GREEN!"""

    def _parse_messy_ast(self):
        source = Path(messy_code.__file__).read_text(encoding="utf-8")
        return ast.parse(source)

    def test_uses_str_join(self):
        tree = self._parse_messy_ast()
        join_calls = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr == "join"
        ]
        self.assertGreaterEqual(
            len(join_calls),
            1,
            "Use `.join(...)` to assemble strings cleanly instead of manual `+` loops.",
        )

    def test_no_string_concat_inside_loops(self):
        tree = self._parse_messy_ast()
        offending_lines = []
        for loop in ast.walk(tree):
            if not isinstance(loop, (ast.For, ast.While)):
                continue
            for stmt in ast.walk(loop):
                if isinstance(stmt, ast.AugAssign) and isinstance(stmt.op, ast.Add):
                    if not (
                        isinstance(stmt.value, ast.Constant)
                        and isinstance(stmt.value.value, int)
                    ):
                        offending_lines.append(stmt.lineno)
                elif isinstance(stmt, ast.Assign) and isinstance(stmt.value, ast.BinOp):
                    if isinstance(stmt.value.op, ast.Add):
                        target_names = {
                            t.id for t in stmt.targets if isinstance(t, ast.Name)
                        }
                        rhs_names = {
                            n.id
                            for n in ast.walk(stmt.value)
                            if isinstance(n, ast.Name)
                        }
                        if target_names & rhs_names:
                            offending_lines.append(stmt.lineno)
        self.assertEqual(
            offending_lines,
            [],
            f"Found string concatenation inside loops on line(s) {sorted(set(offending_lines))}; "
            "collect items in a list and combine with `.join(...)`.",
        )

    def test_extracts_helper_function(self):
        tree = self._parse_messy_ast()
        functions = [
            node for node in tree.body if isinstance(node, ast.FunctionDef)
        ]
        self.assertGreaterEqual(
            len(functions),
            2,
            f"Found only {len(functions)} function(s) in messy_code.py; "
            "extract at least one reusable helper (e.g., `slugify` or `normalize_tag`).",
        )

    def test_no_manual_trailing_delimiter_slicing(self):
        tree = self._parse_messy_ast()
        trailing_slices = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Subscript) and isinstance(node.slice, ast.Slice):
                sl = node.slice
                if (
                    sl.lower is None
                    and sl.step is None
                    and isinstance(sl.upper, ast.UnaryOp)
                    and isinstance(sl.upper.op, ast.USub)
                    and isinstance(sl.upper.operand, ast.Constant)
                    and sl.upper.operand.value in (1, 2)
                ):
                    trailing_slices.append(node.lineno)
        self.assertEqual(
            trailing_slices,
            [],
            f"Found manual trailing-delimiter slicing (`[:-1]` / `[:-2]`) on line(s) {trailing_slices}; "
            "use `.join(...)` so no trailing delimiter is ever added.",
        )


if __name__ == "__main__":
    unittest.main()
