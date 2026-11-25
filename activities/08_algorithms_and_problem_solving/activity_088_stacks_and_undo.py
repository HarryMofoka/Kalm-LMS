"""
Activity 088 — Stack Basics & Undo History
Difficulty: 88 / 132

Context:
    Every Ctrl+Z undo button, browser Back button, and Backspace key runs on
    one simple data structure: a **Stack** (LIFO — Last In, First Out).
    In Python, a regular `list` is an O(1) stack using `.append(x)` to push
    and `.pop()` to remove the most recent item!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Implement `example_reverse_with_stack(items)` that uses an explicit stack
    to reverse `items` into a NEW list without mutating `items`.

Step-by-Step Explanation:
    1. Push every item onto `stack` (`stack.append(item)`).
    2. Pop items off `stack` one by one (`while stack: reversed_items.append(stack.pop())`).
    3. Because the last item pushed is the first item popped, the output comes
       out in exact reverse order!

Edge Cases:
    - Empty list `[]` -> `[]`
    - Single element `[42]` -> `[42]`
    - Original list is untouched (`result is not items`).

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem:
    Implement `solve_apply_backspaces(keystrokes)` that simulates typing in a
    minimal text editor where `'#'` means **Backspace** (delete the last
    surviving character).

Rules:
    1. Maintain a `stack: list[str] = []`.
    2. Iterate over each character `ch` in `keystrokes`:
       - If `ch == "#"`: pop from `stack` ONLY if `stack` is non-empty!
         (Pressing backspace on an empty buffer does nothing — never crash
         with `IndexError`!)
       - Otherwise: push `ch` onto `stack`.
    3. Join the remaining characters with `"".join(stack)` and return the string.

Examples:
    solve_apply_backspaces("ab#c")      -> "ac"
    solve_apply_backspaces("ab##")      -> ""
    solve_apply_backspaces("a##b")      -> "b"
    solve_apply_backspaces("###hello#") -> "hell"
    solve_apply_backspaces("")          -> ""
"""

from __future__ import annotations

from typing import Any


def example_reverse_with_stack(items: list[Any]) -> list[Any]:
    """Return a new reversed copy of ``items`` using explicit stack push/pop."""
    stack: list[Any] = []
    for item in items:
        stack.append(item)

    reversed_items: list[Any] = []
    while stack:
        reversed_items.append(stack.pop())
    return reversed_items


def solve_apply_backspaces(keystrokes: str) -> str:
    """Return the final string after applying '#' backspace strokes via a stack."""
    pass


if __name__ == "__main__":
    actions = ["open", "type", "bold", "save"]
    print("Original:", actions)
    print("Undo order:", example_reverse_with_stack(actions))
