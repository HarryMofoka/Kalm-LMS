"""Worked Example (Checkpoint 15): HTML/XML Tag Balance Checker.

A sibling reference system demonstrating how a LIFO stack combined with a
comment-aware scanner catches mismatched, unexpected, and unclosed tags with
exact 1-indexed line reporting.
"""

from __future__ import annotations


def parse_tags(markup: str) -> list[dict]:
    """Extract opening and closing tags with 1-indexed line numbers.

    Ignores HTML comments (``<!-- ... -->``), declarations/processing tags
    (``<!DOCTYPE ...>``, ``<?xml ...?>``), and self-closing tags
    (``<br/>``, ``<img src="x" />``).
    """
    tags: list[dict] = []
    i = 0
    line = 1
    length = len(markup)

    while i < length:
        # Skip HTML comments (potentially multi-line)
        if markup.startswith("<!--", i):
            end = markup.find("-->", i + 4)
            if end == -1:
                break
            line += markup[i : end + 3].count("\n")
            i = end + 3
            continue

        if markup[i] == "<":
            end = markup.find(">", i + 1)
            if end == -1:
                break

            tag_line = line
            raw_inside = markup[i + 1 : end].strip()
            line += markup[i : end + 1].count("\n")
            i = end + 1

            if not raw_inside or raw_inside[0] in {"!", "?"}:
                continue
            if raw_inside.endswith("/"):
                # Self-closing tag such as <br/> or <img src="logo.png" />
                continue

            if raw_inside.startswith("/"):
                name_part = raw_inside[1:].strip().split()
                if name_part:
                    tags.append(
                        {"name": name_part[0].lower(), "kind": "close", "line": tag_line}
                    )
            else:
                name_part = raw_inside.split()
                if name_part:
                    tags.append(
                        {"name": name_part[0].lower(), "kind": "open", "line": tag_line}
                    )
            continue

        if markup[i] == "\n":
            line += 1
        i += 1

    return tags


def check_markup_balance(markup: str) -> dict:
    """Validate that all HTML/XML tags in ``markup`` are properly balanced.

    Returns:
        ``{"valid": True, "error": None}`` if balanced, otherwise
        ``{"valid": False, "error": {"line": int, "message": str}}`` reporting
        the first mismatch, unexpected closing tag, or innermost unclosed tag.
    """
    stack: list[tuple[str, int]] = []

    for token in parse_tags(markup):
        name = token["name"]
        kind = token["kind"]
        line = token["line"]

        if kind == "open":
            stack.append((name, line))
        else:
            if not stack:
                return {
                    "valid": False,
                    "error": {
                        "line": line,
                        "message": f"Unexpected closing tag '</{name}>'",
                    },
                }
            open_name, _open_line = stack.pop()
            if open_name != name:
                return {
                    "valid": False,
                    "error": {
                        "line": line,
                        "message": (
                            f"Mismatched tag: expected '</{open_name}>', "
                            f"got '</{name}>'"
                        ),
                    },
                }

    if stack:
        open_name, open_line = stack[-1]
        return {
            "valid": False,
            "error": {
                "line": open_line,
                "message": f"Unclosed tag '<{open_name}>'",
            },
        }

    return {"valid": True, "error": None}


if __name__ == "__main__":
    valid_html = """<section class="hero">
    <!-- Hero banner with self-closing image -->
    <h1>Welcome</h1>
    <img src="banner.png" />
    <p>Build real systems.<br/>Ship with confidence.</p>
</section>"""

    broken_html = """<div>
    <p>Hello world</div>
</p>"""

    unclosed_html = """<main>
    <article>
        <h2>Draft Post</h2>
</main>"""

    print("=== HTML/XML Tag Balance Checker ===")
    print("Valid HTML:   ", check_markup_balance(valid_html))
    print("Broken HTML:  ", check_markup_balance(broken_html))
    print("Unclosed HTML:", check_markup_balance(unclosed_html))
