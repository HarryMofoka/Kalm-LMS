"""
Activity 005: Rounding & Percentages
Difficulty: 5 / 132 (Rank 1 - Absolute Beginner)

Context:
Retail checkouts, restaurant point-of-sale terminals, and personal finance apps
all turn human-friendly percentages (like `15` for 15%) into decimal multipliers
(`0.15`) and round currency values cleanly to two decimal places.

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
Write `example_discounted_price(price, discount_percent)` that computes the
final sale price after applying a percentage discount, rounded to 2 decimals.

Step-by-step walkthrough:
1. Convert `discount_percent` (e.g., `25` for 25% off) into a fraction by
   dividing by `100`: `discount_fraction = discount_percent / 100`.
2. The customer pays the remaining fraction `(1 - discount_fraction)` of the
   original `price`:
       `final_price = price * (1 - discount_fraction)`
3. Return `round(final_price, 2)`.

Edge cases:
- `0%` discount leaves the price unchanged.
- `100%` discount produces `0.0`.
- Fractional percentages like `12.5%` work seamlessly.

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
You and your friends just finished dinner and want to split the check fairly!
Write `solve_bill_split(subtotal, tax_percent, tip_percent, diners)` that
calculates:
1. `total_bill`: the subtotal PLUS tax PLUS tip, where BOTH tax and tip are
   calculated on the pre-tax `subtotal`.
2. `per_person`: `total_bill` divided evenly among `diners` (assume `diners >= 1`).

Return `(round(total_bill, 2), round(per_person, 2))`.

Rules:
- Tax amount = `subtotal * (tax_percent / 100)`.
- Tip amount = `subtotal * (tip_percent / 100)`.
- `total_bill = subtotal + tax_amount + tip_amount`.
- Compute `per_person = total_bill / diners` from the UNROUNDED `total_bill`,
  then round both values to 2 decimal places when returning!

Examples:
- `solve_bill_split(100.0, 8.0, 15.0, 4)` -> `(123.0, 30.75)`
- `solve_bill_split(50.0, 10.0, 20.0, 3)` -> `(65.0, 21.67)`
- `solve_bill_split(80.0, 0.0, 0.0, 2)` -> `(80.0, 40.0)`

Hints:
- Notice `subtotal * (1 + (tax_percent + tip_percent) / 100)` gives the exact
  same total as adding `tax_amount` and `tip_amount` separately.
"""

from __future__ import annotations


def example_discounted_price(price: float, discount_percent: float) -> float:
    """Return price after applying discount_percent off, rounded to 2 decimals."""
    # Convert percentage (e.g., 20) into a decimal rate (0.20).
    discount_rate = discount_percent / 100
    final_price = price * (1 - discount_rate)
    return round(final_price, 2)


def solve_bill_split(
    subtotal: float, tax_percent: float, tip_percent: float, diners: int
) -> tuple[float, float]:
    """Return (total_bill, per_person) rounded to 2 decimals, with tax & tip on subtotal."""
    pass


if __name__ == "__main__":
    print("$80 with 25% off:", example_discounted_price(80.0, 25.0))
    print("$49.99 with 15% off:", example_discounted_price(49.99, 15.0))
