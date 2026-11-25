"""
Activity 022: Tiered / Progressive Bracket Pricing
Difficulty: 22 / 132 (Rank 3 - Logic Architect)

Context:
One of the most famous misunderstandings in everyday math is how progressive
brackets work! Moving into a higher tax bracket does NOT tax your ENTIRE
income at the higher rate — ONLY the dollars *inside* that higher slice get
the higher rate! The exact same pattern governs utility bills, cloud API tiers,
and garage parking fees.

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
A downtown parking garage charges progressive hourly rates:
- `hours <= 0`: `$0.00`
- First 2 hours (hours 1–2): `$3.00` per hour
- Next 3 hours (hours 3–5): `$2.00` per hour
- Every hour after 5 (hours 6+): `$1.00` per hour

Write `example_parking_fee(hours)` returning the total fee as a float.

Step-by-step walkthrough:
Let's trace `hours = 7`:
- First 2 hours cost `2 * 3.0 = $6.00`.
- Next 3 hours (hours 3, 4, 5) cost `3 * 2.0 = $6.00`.
- Remaining 2 hours (hours 6, 7) cost `2 * 1.0 = $2.00`.
- Total = `$6.00 + $6.00 + $2.00 = $14.00`!

How to code this cleanly?
Handle each bracket cumulative base + marginal slice:
- `if hours <= 0: return 0.0`
- `if hours <= 2: return hours * 3.0`
- `if hours <= 5: return 2 * 3.0 + (hours - 2) * 2.0`
- `return 2 * 3.0 + 3 * 2.0 + (hours - 5) * 1.0`

Edge cases:
- `0` or negative hours -> `0.0`.
- Boundary `hours = 2` -> `6.0`; `hours = 3` -> `8.0` (continuous, no jump!).
- Boundary `hours = 5` -> `12.0`; `hours = 6` -> `13.0`.

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
Write `solve_progressive_tax(income)` to compute total progressive income tax
(rounded to 2 decimal places) using these marginal brackets:
- `income <= 0`: `$0.0`
- First `$10,000` (`$0` to `$10,000`):       `0%`  (max tax in bracket = `$0`)
- Next `$20,000`  (`$10,000` to `$30,000`):  `10%` (max tax in bracket = `$2,000`)
- Next `$40,000`  (`$30,000` to `$70,000`):  `20%` (max tax in bracket = `$8,000`)
- Above `$70,000`:                           `30%`

Walkthrough of `$50,000` income:
- First `$10,000` @ 0%  = `$0.00`
- Next  `$20,000` @ 10% = `$2,000.00` (covers up to `$30,000`)
- Last  `$20,000` @ 20% = `$4,000.00` (`50,000 - 30,000`)
- Total tax = `$6,000.00`!

Rules:
- Return `0.0` for `income <= 0` or `income <= 10_000`.
- Return `round(tax, 2)` as a float.

Examples:
- `solve_progressive_tax(-500)` -> `0.0`
- `solve_progressive_tax(10000)` -> `0.0`
- `solve_progressive_tax(25000)` -> `1500.0`
- `solve_progressive_tax(50000)` -> `6000.0`
- `solve_progressive_tax(70000)` -> `10000.0`
- `solve_progressive_tax(100000)` -> `19000.0`

Hints:
- Test exact bracket edges (`10_000`, `30_000`, `70_000`)! A progressive tax
  function should NEVER suddenly jump when income increases by `$1`.
"""

from __future__ import annotations


def example_parking_fee(hours: int) -> float:
    """Calculate progressive garage parking fee for the given number of hours."""
    if hours <= 0:
        return 0.0
    if hours <= 2:
        return hours * 3.0
    if hours <= 5:
        # First 2 hours at $3/hr + remaining hours at $2/hr
        return (2 * 3.0) + (hours - 2) * 2.0
    # First 2 hours at $3/hr + next 3 hours at $2/hr + excess at $1/hr
    return (2 * 3.0) + (3 * 2.0) + (hours - 5) * 1.0


def solve_progressive_tax(income: float) -> float:
    """Compute progressive marginal income tax rounded to 2 decimal places."""
    pass


if __name__ == "__main__":
    for h in (0, 2, 4, 5, 7):
        print(f"{h} hours -> ${example_parking_fee(h):.2f}")
