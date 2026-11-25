"""
Activity 089 — Stack Bracket Matching
Difficulty: 89 / 132

Context:
    Compilers and IDEs catch mismatched parentheses before your code even runs.
    Why can't a simple integer counter validate `([)]`? Because the count of
    openings equals closings, yet the *nesting order* is broken! A **stack**
    remembers which exact opener is currently waiting to be closed.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Implement `example_valid_parens_only(text)` that uses a stack to check
    whether `'('` and `')'` in `text` are balanced (ignoring all other chars).

Step-by-Step Explanation:
    1. When we see `'('`, push `'('` onto `stack`.
    2. When we see `')'`:
       - If `stack` is empty, there is no matching opener -> return `False`!
       - Otherwise pop the top `'('`.
    3. At the end, every opener must have been closed -> return `len(stack) == 0`.

Edge Cases:
    - `""` or `"2 + 3"` -> `True` (zero unmatched parens)
    - `")("` -> `False` (closing before opening!)
    - `"((a + b)"` -> `False` (unclosed opener left on stack!)

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem:
    Implement `solve_valid_brackets(text)` that validates nested `'()'`, `'[]'`,
    and `'{}'` brackets in `text` using a stack.

Rules:
    1. Ignore all non-bracket characters (letters, digits, spaces, operators).
    2. Use a dictionary mapping each closing bracket to its expected opening
       bracket: `matching = {")": "(", "]": "[", "}": "{"}`.
    3. For every opening bracket (`"("`, `"["`, `"{"`), push it onto `stack`.
    4. For every closing bracket (`")"`, `"]"`, `"}"`):
       - If `stack` is empty OR `stack.pop() != matching[ch]`, return `False`.
    5. Return `True` if and only if `stack` is empty at the end.

Examples:
    solve_valid_brackets("({[]})")             -> True
    solve_valid_brackets("def f(x): return [x]") -> True
    solve_valid_brackets("([)]")               -> False
    solve_valid_brackets("(([]")               -> False
    solve_valid_brackets("]")                  -> False
    solve_valid_brackets("")                   -> True
"""

from __future__ import annotations


def example_valid_parens_only(text: str) -> bool:
    """Return True if all '(' and ')' in ``text`` are properly balanced."""
    stack: list[str] = []
    for ch in text:
        if ch == "(":
            stack.append(ch)
        elif ch == ")":
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0


def solve_valid_brackets(text: str) -> bool:
    """Return True if all (), [], and {} brackets in ``text`` are validly nested."""
    pass


if __name__ == "__main__":
    for expr in ["(a + (b * c))", ")(", "((x)", "plain text"]:
        print(f"{expr!r:16} -> {example_valid_parens_only(expr)}")
