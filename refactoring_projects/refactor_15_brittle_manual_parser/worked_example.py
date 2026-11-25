"""Worked Example for CP 15: Replacing messy counters with a stack validator.

Compare:
- ``before_check_parens``: ad-hoc open/close counters + error flag.
- ``after_check_parens``: clean LIFO stack using ``append`` and ``pop``.
"""

from typing import List


def before_check_parens(expr: str) -> bool:
    """Messy counter-and-flag implementation for single parenthesis type."""
    open_cnt = 0
    close_cnt = 0
    had_negative = False

    for ch in expr:
        if ch == "(":
            open_cnt = open_cnt + 1
        elif ch == ")":
            close_cnt = close_cnt + 1
            if close_cnt > open_cnt:
                had_negative = True
                break

    if had_negative:
        return False
    if open_cnt == close_cnt:
        return True
    else:
        return False


def after_check_parens(expr: str) -> bool:
    """Clean stack-based validator that scales naturally to multiple brackets."""
    stack: List[str] = []
    for ch in expr:
        if ch == "(":
            stack.append(ch)
        elif ch == ")":
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0


if __name__ == "__main__":
    samples = ["((a + b) * c)", "())(", "((1 + 2)", ""]
    for sample in samples:
        print(
            f"{sample!r:16} -> before={before_check_parens(sample)}, "
            f"after={after_check_parens(sample)}"
        )
