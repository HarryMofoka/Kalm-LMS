"""Worked Example for Checkpoint 17: CLI Build Status Box & Progress Bar Renderer.

Builds framed ASCII panels, progress meters, and CI summary blocks as pure
lists of strings with guaranteed zero trailing spaces.
"""

from __future__ import annotations


def render_meter(completed: int, total: int, width: int = 16) -> str:
    """Render an ASCII completion meter like ``[########........] 50%``."""
    if total <= 0:
        raise ValueError("total must be positive")
    if width <= 0:
        raise ValueError("width must be positive")

    clamped = max(0, min(completed, total))
    ratio = clamped / total
    filled = round(ratio * width)
    pct = round(ratio * 100)
    bar = "#" * filled + "." * (width - filled)
    return f"[{bar}] {pct}%"


def render_kv_panel(title: str, pairs: list[tuple[str, str]]) -> list[str]:
    """Render a framed key-value status box with aligned colons."""
    if pairs:
        key_width = max(len(k) for k, _ in pairs)
        body_lines = [f"{k:<{key_width}} : {v}" for k, v in pairs]
    else:
        body_lines = []

    inner_width = max([len(title)] + [len(row) for row in body_lines])
    border = "+" + "-" * (inner_width + 2) + "+"
    header = f"| {title:<{inner_width}} |"

    if not body_lines:
        return [border, header, border]

    rows = [f"| {row:<{inner_width}} |" for row in body_lines]
    return [border, header, border, *rows, border]


def render_build_summary(
    service: str,
    passed: int,
    total: int,
    metadata: list[tuple[str, str]],
) -> list[str]:
    """Combine a framed metadata panel with a test-pass progress meter."""
    meter = render_meter(passed, total, width=20)
    panel = render_kv_panel(
        f"BUILD SUMMARY: {service}",
        [*metadata, ("Tests", f"{passed}/{total}")],
    )
    return [*panel, "", f"Progress: {meter}"]


if __name__ == "__main__":
    summary_lines = render_build_summary(
        service="payments-api",
        passed=42,
        total=50,
        metadata=[
            ("Branch", "main"),
            ("Commit", "a1b2c3d"),
            ("Duration", "14.2s"),
        ],
    )
    print("\n".join(summary_lines))
