"""Worked Example — Emergency Fund Compound Savings Goal Simulator.

Demonstrates loop-driven financial simulation, convergence guards against
infinite loops, cent-rounded running accumulators, and month-by-month schedules.
"""

from __future__ import annotations

from typing import Any


def simulate_savings_goal(
    starting_balance: float,
    monthly_contribution: float,
    annual_rate_pct: float,
    target_amount: float,
) -> dict[str, Any]:
    """Simulate monthly compounding + contributions until target_amount is reached.

    Raises:
        ValueError: If any input is negative, or if the target cannot be reached
            because both contributions and interest growth are zero.
    """
    if starting_balance < 0:
        raise ValueError("Starting balance cannot be negative.")
    if monthly_contribution < 0:
        raise ValueError("Monthly contribution cannot be negative.")
    if annual_rate_pct < 0:
        raise ValueError("Annual interest rate cannot be negative.")
    if target_amount < 0:
        raise ValueError("Target amount cannot be negative.")

    if starting_balance < target_amount and monthly_contribution == 0:
        if starting_balance == 0 or annual_rate_pct == 0:
            raise ValueError("Savings goal cannot be reached with zero growth.")

    monthly_rate = (annual_rate_pct / 100.0) / 12.0
    balance = round(float(starting_balance), 2)
    contribution = round(float(monthly_contribution), 2)

    month = 0
    total_contributed = 0.0
    total_interest = 0.0
    schedule: list[dict[str, int | float]] = []

    while balance < target_amount:
        month += 1
        interest = round(balance * monthly_rate, 2)
        balance = round(balance + interest + contribution, 2)
        total_interest = round(total_interest + interest, 2)
        total_contributed = round(total_contributed + contribution, 2)

        schedule.append(
            {
                "month": month,
                "interest": interest,
                "contribution": contribution,
                "ending_balance": balance,
            }
        )

    return {
        "months": month,
        "final_balance": balance,
        "total_contributed": total_contributed,
        "total_interest": total_interest,
        "schedule": schedule,
    }


if __name__ == "__main__":
    result = simulate_savings_goal(
        starting_balance=1000.0,
        monthly_contribution=500.0,
        annual_rate_pct=12.0,
        target_amount=2500.0,
    )
    print(f"Target reached in {result['months']} months!")
    print(
        f"Final balance: ${result['final_balance']:,.2f} "
        f"(Contributed: ${result['total_contributed']:,.2f}, "
        f"Interest earned: ${result['total_interest']:,.2f})\n"
    )
    print(f"{'Month':>5} | {'Interest':>10} | {'Contribution':>12} | {'Ending Balance':>14}")
    print("-" * 50)
    for row in result["schedule"]:
        print(
            f"{row['month']:>5} | ${row['interest']:>9,.2f} | "
            f"${row['contribution']:>11,.2f} | ${row['ending_balance']:>13,.2f}"
        )
