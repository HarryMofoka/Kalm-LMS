"""
Activity 012: Formatted Receipts & Aligned Numeric Strings  [Unlocks Checkpoint 02!]
Difficulty: 12 / 132 (Rank 2 - Foundations Builder)

Context:
Raw numbers like `4.5` look messy on an invoice or terminal dashboard — users
expect `$4.50` neatly right-aligned under every other price! Python's f-string
format mini-language lets you control alignment (`<` left, `>` right, `^`
center), fixed column width, and decimal precision (`.2f`) in just a few
characters.

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
Write `example_price_line(item, price)` that formats a single receipt row of
width 26 characters:
- Left column: `item` left-aligned in a field of width 16 (`{item:<16}`).
- Right column: price formatted with a leading `$` and 2 decimals (`f"${price:.2f}"`),
  then right-aligned in a field of width 10 (`{price_text:>10}`).

Step-by-step walkthrough:
1. First format the dollar string:
       `price_text = f"${price:.2f}"`
   Notice why we format `price_text` first! If you wrote `f"${price:>9.2f}"`,
   the `$` would stick to the left edge (`"$    4.50"`) instead of hugging the
   digits (`"     $4.50"`). Formatting `f"${price:.2f}"` first keeps `$` right
   next to the number!
2. Combine the two fixed-width columns:
       `return f"{item:<16}{price_text:>10}"`
3. Total length (assuming `len(item) <= 16` and `len(price_text) <= 10`) is
   always `16 + 10 = 26` characters!

Edge cases:
- Whole dollars like `5` become `"$5.00"` thanks to `.2f`.
- `0` becomes `"$0.00"`.
- Large prices like `1250.5` become `"$1250.50"`.

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
You are writing the receipt printer for a cozy coffee shop. Write:
    `solve_mini_receipt(item1, price1, item2, price2, tax_rate)`
where `tax_rate` is a decimal (e.g., `0.08` for 8% tax).

Return a 5-line string joined by `"\n"` using the EXACT same 26-character
column layout (`16`-char left-aligned label + `10`-char right-aligned `$X.XX`
amount):
- Line 1: `item1` and `price1`
- Line 2: `item2` and `price2`
- Line 3: 26 hyphens (`"-" * 26`)
- Line 4: `"Tax"` and `tax` (where `tax = (price1 + price2) * tax_rate`)
- Line 5: `"TOTAL"` and `total` (where `total = (price1 + price2) + tax`)

Example:
`solve_mini_receipt("Latte", 4.5, "Croissant", 3.25, 0.08)` returns:
```
Latte                $4.50
Croissant            $3.25
--------------------------
Tax                  $0.62
TOTAL                $8.37
```
(No trailing newline at the very end!)

Rules:
- Use exact labels `"Tax"` and `"TOTAL"` (watch capitalization!).
- Compute `subtotal = price1 + price2`, `tax = subtotal * tax_rate`, and
  `total = subtotal + tax`.
- Format each monetary amount with `:.2f` and a `$` right next to the digits,
  right-aligned in 10 characters.

Hints:
- You can even reuse `example_price_line` or build a small helper formula for
  formatting each row, then join the 5 lines with `"\n".join([...])`!
- Completing this activity finishes **Module 01** and unlocks **Checkpoint 02**!
"""

from __future__ import annotations


def example_price_line(item: str, price: float) -> str:
    """Format a 26-char aligned receipt row: 16-char left item + 10-char right $price."""
    # Format the currency string first so `$` hugs the digits when right-aligned.
    price_text = f"${price:.2f}"
    return f"{item:<16}{price_text:>10}"


def solve_mini_receipt(
    item1: str, price1: float, item2: str, price2: float, tax_rate: float
) -> str:
    """Return a 5-line, 26-char-wide formatted cafe receipt string."""
    pass


if __name__ == "__main__":
    print(example_price_line("Espresso", 3.5))
    print(example_price_line("Blueberry Muffin", 4.25))
    print("-" * 26)
    print(example_price_line("TOTAL", 7.75))
