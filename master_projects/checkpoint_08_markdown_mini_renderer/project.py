"""Master Project — Checkpoint 08: Mini Markdown & Template Renderer.

Implement placeholder substitution, inline Markdown conversion, and full
Markdown-to-HTML document rendering according to README.md.
"""

from __future__ import annotations


def render_placeholders(
    text: str,
    values: dict[str, object],
    strict: bool = True,
    default: str = "",
) -> str:
    """Substitute {{ key }} placeholders in text using values.

    Whitespace inside braces is ignored (e.g. "{{  name  }}" looks up "name").
    Unclosed "{{" tokens with no matching "}}" are preserved literally.

    Args:
        text: Input string possibly containing {{ key }} placeholders.
        values: Mapping from key names to values (converted with str()).
        strict: If True, raise KeyError when a placeholder key is missing.
            If False, substitute `default` for missing keys.
        default: Fallback string used when strict=False and a key is missing.

    Returns:
        Rendered string with placeholders resolved.

    Raises:
        KeyError: If strict=True and a referenced key is absent from values.
    """
    pass


def convert_inline_markdown(text: str) -> str:
    """Convert inline `code` and **bold** Markdown spans to HTML tags.

    Rules:
        - `code`   -> <code>code</code>
        - **bold** -> <strong>bold</strong>
        - Markers inside `code` spans remain literal (not converted to bold).
        - Unmatched delimiters or empty spans (`` or ****) remain unchanged.

    Args:
        text: Single line of text containing optional inline Markdown.

    Returns:
        String with inline Markdown converted to <code> and <strong> tags.
    """
    pass


def render_markdown_document(
    md_text: str,
    values: dict[str, object] | None = None,
    strict: bool = True,
    default: str = "",
) -> str:
    """Render a Markdown document (with optional {{var}} placeholders) to HTML.

    Supported block syntax (per stripped line):
        - "# Title"   -> "<h1>Title</h1>"
        - "## Title"  -> "<h2>Title</h2>"
        - "- item"    -> consecutive items wrapped in "<ul>\\n<li>...</li>\\n</ul>"
        - Other lines -> "<p>...</p>"
        - Blank lines -> separate blocks and close open lists

    Inline Markdown (`code` and **bold**) is applied inside headings, list
    items, and paragraphs.

    Args:
        md_text: Multi-line Markdown document text.
        values: Optional placeholder values dict; if provided,
            render_placeholders is applied before Markdown conversion.
        strict: Passed through to render_placeholders when values is not None.
        default: Passed through to render_placeholders when values is not None.

    Returns:
        Clean HTML lines joined by "\\n" (or "" for empty/whitespace-only input).
    """
    pass
