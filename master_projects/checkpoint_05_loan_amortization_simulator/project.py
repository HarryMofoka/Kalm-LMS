"""Checkpoint 05 — Micro-Loan Payoff & Amortization Simulator.

Implement each function below according to its docstring and README.md.
Run the tests with:
    python -m unittest master_projects/checkpoint_05_loan_amortization_simulator/test_project.py -v
"""

from __future__ import annotations

from typing import Any


def simulate_loan_payoff(
    principal: float,
    annual_rate_pct: float,
    monthly_payment: float,
) -> dict[str, Any]:
    """Simulate month-by-month loan amortization until the balance reaches $0.00.

    Each month:
        1. interest = round(balance * monthly_rate, 2)
        2. If round(balance + interest, 2) <= monthly_payment, pay exact payoff
           amount so ending_balance is 0.0; otherwise pay monthly_payment.
        3. Record snapshot:
           {"month", "payment", "interest", "principal_paid", "ending_balance"}

    Returns:
        Dict with keys:
            - "months": total months until paid off (int)
            - "total_paid": cumulative payments rounded to 2 decimals (float)
            - "total_interest": cumulative interest rounded to 2 decimals (float)
            - "schedule": list of monthly snapshot dicts

    Raises:
        ValueError: If principal <= 0, annual_rate_pct < 0, monthly_payment <= 0,
            or monthly_payment does not exceed first month's interest.
    """
    pass


def estimate_months_saved(
    principal: float,
    annual_rate_pct: float,
    base_payment: float,
    extra_payment: float,
) -> int:
    """Return how many fewer months it takes to pay off the loan with extra_payment.

    Raises:
        ValueError: If extra_payment < 0 or base loan parameters are invalid.
    """
    pass
