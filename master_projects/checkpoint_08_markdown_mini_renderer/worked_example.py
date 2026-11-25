"""Worked Example: Transactional Email Template Engine.

Demonstrates cursor-based {{var}} template substitution with strict/default
missing-variable handling and clean RFC-style paragraph word wrapping.
"""

from __future__ import annotations


def substitute_placeholders(
    template: str,
    context: dict[str, object],
    default: str | None = None,
) -> str:
    """Replace {{ key }} placeholders in template using values from context.

    Args:
        template: Raw template string containing {{ var }} tokens.
        context: Mapping of variable names to replacement values.
        default: Fallback string for missing keys. If None, missing keys raise KeyError.
    """
    result: list[str] = []
    pos = 0

    while pos < len(template):
        start = template.find("{{", pos)
        if start == -1:
            result.append(template[pos:])
            break

        end = template.find("}}", start + 2)
        if end == -1:
            # Unclosed '{{' — preserve remaining text literally.
            result.append(template[pos:])
            break

        result.append(template[pos:start])
        key = template[start + 2 : end].strip()

        if key in context:
            result.append(str(context[key]))
        elif default is not None:
            result.append(default)
        else:
            raise KeyError(key)

        pos = end + 2

    return "".join(result)


def wrap_paragraph(text: str, width: int = 72) -> list[str]:
    """Word-wrap a single paragraph cleanly to at most `width` characters per line.

    Never emits trailing spaces. Words longer than `width` occupy their own line.
    """
    if width < 1:
        raise ValueError("wrap width must be at least 1")

    words = text.split()
    if not words:
        return []

    lines: list[str] = []
    current_line = words[0]

    for word in words[1:]:
        if len(current_line) + 1 + len(word) <= width:
            current_line = f"{current_line} {word}"
        else:
            lines.append(current_line)
            current_line = word

    lines.append(current_line)
    return lines


def render_template(
    template: str,
    context: dict[str, object],
    default: str | None = None,
    wrap_width: int | None = None,
) -> str:
    """Render a multi-paragraph template with optional line wrapping.

    Preserves blank lines separating paragraphs when wrap_width is provided.
    """
    substituted = substitute_placeholders(template, context, default=default)
    if wrap_width is None:
        return substituted

    if wrap_width < 1:
        raise ValueError("wrap_width must be at least 1")

    output_lines: list[str] = []
    for raw_line in substituted.splitlines():
        if not raw_line.strip():
            output_lines.append("")
        else:
            output_lines.extend(wrap_paragraph(raw_line, width=wrap_width))

    return "\n".join(output_lines)


if __name__ == "__main__":
    email_template = (
        "Hi {{ customer_name }},\n\n"
        "Thank you for ordering {{ item }} (Order #{{ order_id }}). "
        "Your parcel is being packed at our {{ warehouse }} depot and "
        "will arrive within {{ eta_days }} business days.\n\n"
        "Best regards,\n"
        "The {{ company }} Team"
    )
    rendered = render_template(
        email_template,
        context={
            "customer_name": "Sipho",
            "item": "Mechanical Keyboard",
            "order_id": 48219,
            "warehouse": "Johannesburg",
            "eta_days": 2,
            "company": "ByteCraft",
        },
        wrap_width=52,
    )
    print("=== Rendered Transactional Email ===")
    print(rendered)
