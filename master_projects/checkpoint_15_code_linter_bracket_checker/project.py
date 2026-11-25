"""Master Project (Checkpoint 15): Source Code Bracket & Quote Linter.

Implement the two functions below according to the specification in README.md.
Run tests from ExamPrep/ with:
    python -m unittest master_projects/checkpoint_15_code_linter_bracket_checker/test_project.py -v
"""

from __future__ import annotations


def lint_brackets(source_code: str) -> dict:
    """Validate bracket balance ``()``, ``[]``, ``{}`` across multi-line source code.

    Ignores brackets inside single-quoted (``'...'``) and double-quoted
    (``"..."``) string literals (supporting backslash escapes like ``\\"``,
    ``\\'``, ``\\\\``) and inside ``#`` line comments.

    Tracks 1-indexed ``line`` and ``col`` coordinates and stops on the first
    error detected:
        - Unexpected closing bracket on empty stack
        - Mismatched closing bracket
        - Unterminated string literal (at newline or EOF; reports opening quote)
        - Unclosed opening bracket remaining at EOF (reports top of stack)

    Args:
        source_code: Multi-line source string to lint.

    Returns:
        ``{"valid": True, "error": None}`` if valid, or
        ``{"valid": False, "error": {"line": int, "col": int, "message": str}}``.
    """
    pass


def find_matching_pairs(line: str) -> list[tuple[int, int]]:
    """Return sorted ``(open_idx, close_idx)`` 0-indexed bracket pairs in ``line``.

    Ignores brackets inside single/double-quoted strings (respecting backslash
    escapes) and ``#`` comments. Results are sorted by ``open_idx`` ascending.

    Args:
        line: Single line of source code.

    Returns:
        List of ``(open_idx, close_idx)`` tuples sorted by ``open_idx``.

    Raises:
        ValueError: If brackets are mismatched, unexpected, unclosed, or if a
            string literal is unterminated.
    """
    pass
