"""Checkpoint 16 Master Project: Mini `git diff` Line-Comparison Engine.

Implement the four functions below using Longest Common Subsequence (LCS)
dynamic programming and backtracking. See README.md and worked_example.py for
guidance.
"""

from __future__ import annotations


def lcs_table(old_lines: list[str], new_lines: list[str]) -> list[list[int]]:
    """Build the (m + 1) x (n + 1) LCS dynamic programming table.

    ``table[i][j]`` must equal the length of the Longest Common Subsequence of
    ``old_lines[:i]`` and ``new_lines[:j]``.
    """
    pass


def compute_diff(
    old_lines: list[str], new_lines: list[str]
) -> list[tuple[str, str]]:
    """Compute a minimal line diff between ``old_lines`` and ``new_lines``.

    Returns a list of ``(op, line)`` tuples where ``op`` is one of:
    - ``" "``: line unchanged (part of the LCS)
    - ``"-"``: line removed from ``old_lines``
    - ``"+"``: line added in ``new_lines``

    When breaking ties during backtracking, prefer emitting removals (``"-"``)
    before additions (``"+"``) in the final forward order.
    """
    pass


def format_unified_diff(
    old_lines: list[str], new_lines: list[str]
) -> list[str]:
    """Return human-readable diff lines comparing ``old_lines`` and ``new_lines``.

    Formatting rules per ``(op, line)``:
    - ``(" ", line)`` -> ``f"  {line}"`` (or ``""`` when ``line == ""``)
    - ``("-", line)`` -> ``f"- {line}"`` (or ``"-"`` when ``line == ""``)
    - ``("+", line)`` -> ``f"+ {line}"`` (or ``"+"`` when ``line == ""``)
    """
    pass


def diff_stats(diff_ops: list[tuple[str, str]]) -> dict[str, int]:
    """Summarize diff operations into ``{"added", "removed", "unchanged"}``.

    Raises ``ValueError`` if any operation uses an unknown op code.
    """
    pass
