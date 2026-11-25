"""Messy Formula Bracket Validator — Refactoring Target for Mission 15.

PROBLEM:
This validator uses three separate integer counters (``round_cnt``,
``square_cnt``, ``curly_cnt``) and a repetitive ``if/elif`` chain.
It passes simple balanced and missing-bracket checks, BUT completely fails
on illegally interleaved brackets like ``"([)]"`` or ``"{[}]"`` because
separate counters cannot track nesting order!

YOUR GOAL:
Replace the three counters with a clean bracket-pair dictionary and a LIFO
stack (``stack.append(...)`` / ``stack.pop()``).
"""


def validate_formula_brackets(expr: str) -> bool:
    """Validate (), [], and {} brackets in a formula (buggy counter version!)."""
    round_cnt = 0
    square_cnt = 0
    curly_cnt = 0

    for ch in expr:
        if ch == "(":
            round_cnt += 1
        elif ch == ")":
            round_cnt -= 1
            if round_cnt < 0:
                return False
        elif ch == "[":
            square_cnt += 1
        elif ch == "]":
            square_cnt -= 1
            if square_cnt < 0:
                return False
        elif ch == "{":
            curly_cnt += 1
        elif ch == "}":
            curly_cnt -= 1
            if curly_cnt < 0:
                return False

    return round_cnt == 0 and square_cnt == 0 and curly_cnt == 0
