"""
Activity 075 — Default Arguments & Keyword Flags
Difficulty: 75 / 132

Context:
    You are designing helper functions for an international storefront SDK.
    Most callers want sensible defaults (like USD `"$"` and 2 decimal places),
    while power users pass keyword flags to customize formatting cleanly
    without memorizing cryptic positional arguments.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Write `example_greet_customer(name, title="Member", excited=False)` that
    builds a friendly greeting:
      - With a non-empty title: `"Hello, {title} {name}{punct}"`
      - With an empty title `""`: `"Hello, {name}{punct}"`
      - `punct` is `"!"` when `excited=True`, otherwise `"."`.

Step-by-Step Explanation:
    1. Give `title` a default of `"Member"` and `excited` a default of `False`.
    2. Choose the punctuation based on the boolean flag `excited`.
    3. Cleanly handle an empty/whitespace-only `title` so we never emit a
       double space like `"Hello,  Ada."`.

Edge Cases:
    - Calling with positional arg only: `example_greet_customer("Ada")` -> `"Hello, Member Ada."`
    - Overriding one keyword flag: `example_greet_customer("Ada", excited=True)` -> `"Hello, Member Ada!"`
    - Empty title: `example_greet_customer("Ada", title="")` -> `"Hello, Ada."`

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem:
    Implement `solve_format_currency(amount, symbol="$", decimals=2, show_plus=False)`
    to format numeric prices cleanly.

Rules:
    1. Format the magnitude with thousands commas and `decimals` fixed decimal
       places: e.g., `1234.5` with `decimals=2` -> `"1,234.50"`.
    2. Normalize `-0.0` (or values that round to zero at `decimals` places, or
       `amount == 0`) so zero never displays a minus or plus sign:
       e.g., `0` -> `"$0.00"`, `-0.0` -> `"$0.00"`.
    3. Sign placement comes BEFORE the currency symbol:
       - If `amount < 0` (and formatted value isn't zero): `f"-{symbol}{formatted}"`
       - If `amount > 0` and `show_plus` is `True`: `f"+{symbol}{formatted}"`
       - Otherwise: `f"{symbol}{formatted}"`

Examples:
    solve_format_currency(1234.5)                          -> "$1,234.50"
    solve_format_currency(-42.1)                           -> "-$42.10"
    solve_format_currency(99.9, symbol="R ", decimals=2)   -> "R 99.90"
    solve_format_currency(1500, symbol="€", decimals=0)    -> "€1,500"
    solve_format_currency(25.5, show_plus=True)            -> "+$25.50"
    solve_format_currency(0, show_plus=True)               -> "$0.00"

Edge-Case Hints:
    - Check `round(amount, decimals) == 0` to cleanly eliminate `"-0.00"`.
    - Python f-strings support dynamic precision: `f"{abs_val:,.{decimals}f}"`.
"""

from __future__ import annotations


def example_greet_customer(
    name: str,
    title: str = "Member",
    excited: bool = False,
) -> str:
    """Return a greeting with an optional title and excitement flag."""
    punct = "!" if excited else "."
    clean_title = title.strip()
    if clean_title:
        return f"Hello, {clean_title} {name}{punct}"
    return f"Hello, {name}{punct}"


def solve_format_currency(
    amount: int | float,
    symbol: str = "$",
    decimals: int = 2,
    show_plus: bool = False,
) -> str:
    """Format a numeric amount as a currency string with commas and sign rules."""
    pass


if __name__ == "__main__":
    print(example_greet_customer("Ada"))
    print(example_greet_customer("Ada", title="Dr.", excited=True))
    print(example_greet_customer("Ada", title=""))
