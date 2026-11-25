"""Automated tests for Checkpoint 08: Mini Markdown & Template Renderer."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from master_projects.checkpoint_08_markdown_mini_renderer import (  # noqa: E402
    project,
    worked_example,
)


class TestWorkedExample(unittest.TestCase):
    """Verify the Transactional Email Template Engine reference works."""

    def test_substitute_placeholders_basic_and_whitespace(self) -> None:
        tpl = "Hello {{  name  }}, your code is {{code}}!"
        result = worked_example.substitute_placeholders(
            tpl, {"name": "Lerato", "code": 4092}
        )
        self.assertEqual(result, "Hello Lerato, your code is 4092!")

    def test_substitute_placeholders_missing_strict_vs_default(self) -> None:
        tpl = "Order {{id}} for {{missing_user}}"
        with self.assertRaises(KeyError):
            worked_example.substitute_placeholders(tpl, {"id": 7})

        fallback = worked_example.substitute_placeholders(
            tpl, {"id": 7}, default="Guest"
        )
        self.assertEqual(fallback, "Order 7 for Guest")

    def test_wrap_paragraph_widths_and_no_trailing_spaces(self) -> None:
        text = "Python template engines make transactional emails super clean"
        lines = worked_example.wrap_paragraph(text, width=22)
        self.assertEqual(
            lines,
            [
                "Python template",
                "engines make",
                "transactional emails",
                "super clean",
            ],
        )
        for line in lines:
            self.assertEqual(line, line.rstrip())

    def test_wrap_paragraph_invalid_width_raises(self) -> None:
        with self.assertRaises(ValueError):
            worked_example.wrap_paragraph("hello world", width=0)

    def test_render_template_preserves_paragraphs(self) -> None:
        tpl = "Hi {{user}},\n\nWelcome to {{app}} cloud platform today!"
        rendered = worked_example.render_template(
            tpl, {"user": "Ada", "app": "Nova"}, wrap_width=20
        )
        self.assertEqual(
            rendered,
            "Hi Ada,\n\nWelcome to Nova\ncloud platform\ntoday!",
        )


class TestMasterProject(unittest.TestCase):
    """TDD test suite for the student's Mini Markdown & Template Renderer."""

    def test_render_placeholders_basic_and_whitespace_tolerant(self) -> None:
        template = "Deploy {{  service }} v{{version}} to {{ env }}."
        rendered = project.render_placeholders(
            template,
            {"service": "auth-api", "version": 3, "env": "prod"},
        )
        self.assertEqual(rendered, "Deploy auth-api v3 to prod.")

        # Unclosed delimiter stays literal
        unclosed = "Hello {{name}} and {{unclosed"
        self.assertEqual(
            project.render_placeholders(unclosed, {"name": "Sam"}),
            "Hello Sam and {{unclosed",
        )

    def test_render_placeholders_missing_strict_and_non_strict(self) -> None:
        template = "User: {{ user }}, Role: {{ role }}"
        with self.assertRaises(KeyError):
            project.render_placeholders(template, {"user": "Mpho"}, strict=True)

        non_strict = project.render_placeholders(
            template, {"user": "Mpho"}, strict=False, default="N/A"
        )
        self.assertEqual(non_strict, "User: Mpho, Role: N/A")

    def test_convert_inline_markdown_bold_and_code(self) -> None:
        line = "Run `pip install` for **fast** and **reliable** `builds`."
        self.assertEqual(
            project.convert_inline_markdown(line),
            "Run <code>pip install</code> for <strong>fast</strong> and "
            "<strong>reliable</strong> <code>builds</code>.",
        )

    def test_convert_inline_markdown_preserves_code_and_unmatched(self) -> None:
        # Bold markers inside inline code must stay literal
        code_protected = "Literal `**not_bold**` vs **real bold**"
        self.assertEqual(
            project.convert_inline_markdown(code_protected),
            "Literal <code>**not_bold**</code> vs <strong>real bold</strong>",
        )

        # Unmatched markers stay literal
        unmatched = "Keep **unclosed and `lone tick intact"
        self.assertEqual(project.convert_inline_markdown(unmatched), unmatched)

    def test_render_markdown_document_headings_paragraphs_and_lists(self) -> None:
        md = (
            "# Release Guide\n"
            "\n"
            "## Steps\n"
            "\n"
            "Use `make test` before **shipping**.\n"
            "\n"
            "- Check **linting**\n"
            "- Run `pytest`\n"
            "\n"
            "All done!"
        )
        expected = "\n".join(
            [
                "<h1>Release Guide</h1>",
                "<h2>Steps</h2>",
                "<p>Use <code>make test</code> before <strong>shipping</strong>.</p>",
                "<ul>",
                "<li>Check <strong>linting</strong></li>",
                "<li>Run <code>pytest</code></li>",
                "</ul>",
                "<p>All done!</p>",
            ]
        )
        self.assertEqual(project.render_markdown_document(md), expected)

    def test_render_markdown_document_with_placeholders_and_empty_input(self) -> None:
        md = "# Welcome, {{ name }}!\n\n- Plan: **{{ tier }}**\n- Token: `{{ prefix }}`"
        expected = "\n".join(
            [
                "<h1>Welcome, Naledi!</h1>",
                "<ul>",
                "<li>Plan: <strong>Pro</strong></li>",
                "<li>Token: <code>live_</code></li>",
                "</ul>",
            ]
        )
        self.assertEqual(
            project.render_markdown_document(
                md,
                values={"name": "Naledi", "tier": "Pro", "prefix": "live_"},
            ),
            expected,
        )
        self.assertEqual(project.render_markdown_document("   \n\n  "), "")


if __name__ == "__main__":
    unittest.main()
