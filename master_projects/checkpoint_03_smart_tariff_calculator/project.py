"""Checkpoint 03 — Smart Prepaid Electricity Tariff Calculator.

Implement each function below according to its docstring and README.md.
Run the tests with:
    python -m unittest master_projects/checkpoint_03_smart_tariff_calculator/test_project.py -v
"""

from __future__ import annotations

TIER_1_LIMIT_KWH: float = 100.0
TIER_2_LIMIT_KWH: float = 350.0
TIER_1_RATE: float = 1.50
TIER_2_RATE: float = 2.20
TIER_3_RATE: float = 3.10
FIXED_SERVICE_FEE: float = 25.00
PEAK_BONUS_DISCOUNT_PCT: float = 10.0


def validate_reading(prev_reading: float, curr_reading: float) -> float:
    """Validate meter readings and return kWh consumed rounded to 2 decimal places.

    Raises:
        ValueError: If either reading is negative or curr_reading < prev_reading.
    """
    pass


def tariff_tier_label(kwh: float) -> str:
    """Return the tariff tier name reached for a given kWh usage.

    Tiers:
        - kwh <= 100        -> "Tier 1 (Lifeline)"
        - 100 < kwh <= 350  -> "Tier 2 (Standard)"
        - kwh > 350         -> "Tier 3 (High Usage)"

    Raises:
        ValueError: If kwh < 0.
    """
    pass


def calculate_electricity_bill(kwh: float, peak_bonus: bool = False) -> dict[str, float | str]:
    """Compute a progressive 3-tier prepaid electricity bill.

    Rates:
        - First 100 kWh      : $1.50 / kWh
        - Next 250 kWh       : $2.20 / kWh (100 .. 350 kWh)
        - Above 350 kWh      : $3.10 / kWh
        - Fixed service fee  : $25.00 (always included)
        - peak_bonus=True    : 10% discount on usage_charge only

    Returns:
        Dict with keys:
            - "kwh": rounded kWh usage (float)
            - "tier": tariff_tier_label(kwh) (str)
            - "usage_charge": rounded energy usage cost before discount (float)
            - "discount": rounded off-peak bonus discount (float)
            - "service_fee": FIXED_SERVICE_FEE (float)
            - "total": rounded usage_charge - discount + service_fee (float)

    Raises:
        ValueError: If kwh < 0.
    """
    pass


def kwh_for_budget(amount: float) -> float:
    """Return total kWh purchased for an energy-only prepaid amount, rounded to 2 decimals.

    Inverts the 3-tier progressive energy rates ($1.50 / $2.20 / $3.10 per kWh)
    without deducting the fixed service fee.

    Raises:
        ValueError: If amount < 0.
    """
    pass
