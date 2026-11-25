"""Worked Example — Progressive Income Tax Bracket Calculator.

Demonstrates continuous marginal bracket math, boundary classification,
zero-division guards, and structured financial breakdowns.
"""

from __future__ import annotations

BRACKET_1_LIMIT: float = 20_000.0
BRACKET_2_LIMIT: float = 50_000.0
BRACKET_1_RATE: float = 0.10
BRACKET_2_RATE: float = 0.20
BRACKET_3_RATE: float = 0.30


def marginal_bracket_label(income: float) -> str:
    """Return the label of the highest marginal bracket reached by income."""
    if income < 0:
        raise ValueError("Income cannot be negative.")
    if income <= BRACKET_1_LIMIT:
        return "Bracket 1 (10%)"
    if income <= BRACKET_2_LIMIT:
        return "Bracket 2 (20%)"
    return "Bracket 3 (30%)"


def calculate_progressive_tax(income: float) -> dict[str, float | str]:
    """Calculate marginal tax across 3 progressive annual income brackets.

    Brackets:
        - $0 .. $20,000     : 10%
        - $20,000 .. $50,000: 20%
        - Above $50,000     : 30%
    """
    if income < 0:
        raise ValueError("Income cannot be negative.")

    tier1_slice = min(income, BRACKET_1_LIMIT)
    tier2_slice = min(max(income - BRACKET_1_LIMIT, 0.0), BRACKET_2_LIMIT - BRACKET_1_LIMIT)
    tier3_slice = max(income - BRACKET_2_LIMIT, 0.0)

    tier1_tax = round(tier1_slice * BRACKET_1_RATE, 2)
    tier2_tax = round(tier2_slice * BRACKET_2_RATE, 2)
    tier3_tax = round(tier3_slice * BRACKET_3_RATE, 2)
    total_tax = round(tier1_tax + tier2_tax + tier3_tax, 2)
    net_income = round(income - total_tax, 2)
    effective_rate_pct = 0.0 if income == 0 else round((total_tax / income) * 100.0, 2)

    return {
        "income": round(float(income), 2),
        "top_bracket": marginal_bracket_label(income),
        "tier1_tax": tier1_tax,
        "tier2_tax": tier2_tax,
        "tier3_tax": tier3_tax,
        "total_tax": total_tax,
        "effective_rate_pct": effective_rate_pct,
        "net_income": net_income,
    }


if __name__ == "__main__":
    print(f"{'Income':>12} | {'Top Bracket':<16} | {'Total Tax':>11} | {'Eff. Rate':>9} | {'Net Income':>12}")
    print("-" * 72)
    for sample_income in (0, 18_000, 35_000, 65_000, 120_000):
        res = calculate_progressive_tax(sample_income)
        print(
            f"${res['income']:>11,.2f} | {res['top_bracket']:<16} | "
            f"${res['total_tax']:>10,.2f} | {res['effective_rate_pct']:>8.2f}% | "
            f"${res['net_income']:>11,.2f}"
        )
