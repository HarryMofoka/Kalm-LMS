"""Test suite for Refactoring Mission 17: Fragile ASCII Printer."""

import ast
import inspect
import io
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from refactoring_projects.refactor_17_fragile_ascii_printer import (  # noqa: E402
    messy_code,
    worked_example,
)


def _capture_stdout(fn, *args):
    buf = io.StringIO()
    with redirect_stdout(buf):
        fn(*args)
    return buf.getvalue()


class TestWorkedExample(unittest.TestCase):
    """Verifies the worked example produces matching visible boxes and clean lines."""

    def test_before_and_after_visible_content_match(self):
        before_out = _capture_stdout(worked_example.before_print_box, 4)
        after_out = _capture_stdout(worked_example.after_print_box, 4)

        before_stripped = [line.strip() for line in before_out.splitlines()]
        after_lines = after_out.splitlines()
        self.assertEqual(before_stripped, after_lines)
        self.assertTrue(all(line == line.rstrip(" ") for line in after_lines))

    def test_pure_helpers_work_without_printing(self):
        self.assertEqual(worked_example.format_row(["*", ".", "*"]), "* . *")
        buf = io.StringIO()
        with redirect_stdout(buf):
            lines = worked_example.after_build_box(3)
        self.assertEqual(buf.getvalue(), "")
        self.assertEqual(lines, ["* * *", "* . *", "* * *"])


class TestBehaviorSafetyNet(unittest.TestCase):
    """Behavioral safety net — checks line counts and stripped badge shapes."""

    def test_badge_frame_5x4_visible_content(self):
        output = _capture_stdout(messy_code.print_badge_frame, 5, 4)
        lines = output.splitlines()
        self.assertEqual(len(lines), 4)
        self.assertEqual(
            [line.strip() for line in lines],
            [
                "# # # # #",
                "# . . . #",
                "# . . . #",
                "# # # # #",
            ],
        )

    def test_badge_frame_small_and_empty_dimensions(self):
        out_3x3 = _capture_stdout(messy_code.print_badge_frame, 3, 3)
        self.assertEqual(
            [line.strip() for line in out_3x3.splitlines()],
            ["# # #", "# . #", "# # #"],
        )

        out_1x1 = _capture_stdout(messy_code.print_badge_frame, 1, 1)
        self.assertEqual([line.strip() for line in out_1x1.splitlines()], ["#"])

        out_empty = _capture_stdout(messy_code.print_badge_frame, 0, 4)
        self.assertEqual(out_empty, "")


class TestRefactorGoals(unittest.TestCase):
    """Refactoring goals — RED on baseline, GREEN once refactored cleanly."""

    def test_printed_lines_have_zero_trailing_spaces(self):
        output = _capture_stdout(messy_code.print_badge_frame, 5, 4)
        lines = output.splitlines()
        self.assertEqual(len(lines), 4)
        for idx, line in enumerate(lines):
            self.assertEqual(
                line,
                line.rstrip(" "),
                f"Line {idx} has trailing spaces: {line!r}",
            )
        self.assertEqual(
            lines,
            [
                "# # # # #",
                "# . . . #",
                "# . . . #",
                "# # # # #",
            ],
        )

    def test_format_row_helper_exists_and_joins_cleanly(self):
        self.assertTrue(
            hasattr(messy_code, "format_row"),
            "Expected pure helper function `format_row(cells)` in messy_code.py.",
        )
        format_row = getattr(messy_code, "format_row")
        self.assertEqual(format_row(["#", ".", ".", "#"]), "# . . #")
        self.assertEqual(format_row(["#"]), "#")
        self.assertEqual(format_row([]), "")

    def test_build_badge_frame_is_pure_and_returns_lines(self):
        self.assertTrue(
            hasattr(messy_code, "build_badge_frame"),
            "Expected pure function `build_badge_frame(width, height)` in messy_code.py.",
        )
        build_badge_frame = getattr(messy_code, "build_badge_frame")

        buf = io.StringIO()
        with redirect_stdout(buf):
            lines = build_badge_frame(5, 4)
        self.assertEqual(
            buf.getvalue(),
            "",
            "build_badge_frame must be pure and must not print anything.",
        )
        self.assertEqual(
            lines,
            [
                "# # # # #",
                "# . . . #",
                "# . . . #",
                "# # # # #",
            ],
        )
        self.assertEqual(build_badge_frame(4, 1), ["# # # #"])
        self.assertEqual(build_badge_frame(1, 3), ["#", "#", "#"])
        self.assertEqual(build_badge_frame(0, 5), [])

    def test_print_badge_frame_delegates_without_end_space_hack(self):
        source = inspect.getsource(messy_code.print_badge_frame)
        tree = ast.parse(source)

        calls_builder = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id == "build_badge_frame":
                    calls_builder = True
                if node.func.id == "print":
                    for kw in node.keywords:
                        if kw.arg == "end":
                            self.fail(
                                "print_badge_frame should not use print(..., end=...) loops; "
                                "print complete lines from build_badge_frame instead."
                            )

        self.assertTrue(
            calls_builder,
            "print_badge_frame should delegate line construction to build_badge_frame.",
        )


if __name__ == "__main__":
    unittest.main()
