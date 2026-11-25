# Checkpoint 05 — Micro-Loan Payoff & Amortization Simulator

- **Unlocked After:** Activity 030 (Loops & Running State)
- **Difficulty:** Intermediate
- **Core Concepts:** `while` simulation loops, running state variables, infinite-loop termination guards, cent-rounded amortization schedules, comparative scenario modeling

---

## Real-World Value

Every FinTech lending portal, student-loan dashboard, bank mortgage calculator, and personal-finance app (YNAB, NerdWallet, Capitec / TymeBank calculators) runs an **amortization simulator**.

Real loans cannot be fully explained by a single flat percentage because interest compounds monthly on the **remaining principal**. Two production pitfalls make this a classic engineering test:
1. **The Infinite-Loop / Negative-Amortization Trap:** If a borrower's `monthly_payment` is less than or equal to the first month's interest, the balance never shrinks — a naive `while balance > 0:` loop will spin forever! Production simulators reject non-converging inputs upfront with `ValueError`.
2. **The Final-Month Overpayment Bug:** On the last month of a loan, the remaining balance plus final interest is almost always smaller than the normal `monthly_payment`. Capping the final payment prevents negative balances and keeps `total_paid == principal + total_interest` exact to the cent.

---

## Problem Statement

Build a Micro-Loan Payoff & Amortization Simulator in `project.py` that:

1. Simulates month-by-month loan repayment (`simulate_loan_payoff`) with exact 2-decimal rounding at each monthly step.
2. Guards against invalid inputs (`principal <= 0`, `annual_rate_pct < 0`, `monthly_payment <= 0`) AND negative amortization (`monthly_payment <= first_month_interest`) by raising `ValueError`.
3. Handles final partial-month payments cleanly so `ending_balance` lands on exactly `0.0`.
4. Returns `months`, `total_paid`, `total_interest`, and a full `schedule` list of monthly snapshot dicts.
5. Models accelerated repayment via `estimate_months_saved(principal, annual_rate_pct, base_payment, extra_payment)`.

---

## How a Similar Functioning System Was Done (`worked_example.py`)

Before building the loan simulator, read and run **`worked_example.py`** — a complete **Emergency Fund Compound Savings Goal Simulator**.

```bash
python master_projects/checkpoint_05_loan_amortization_simulator/worked_example.py
```

### Architectural Walkthrough

1. **Convergence Guard Before the Loop:** If `starting_balance < target_amount` and neither contributions nor compounding interest can grow the balance (`monthly_contribution == 0` and (`starting_balance == 0` or `annual_rate_pct == 0`)), `simulate_savings_goal` immediately raises `ValueError` instead of entering an infinite loop.
2. **Clean Running State:** Four scalar accumulators (`month`, `balance`, `total_contributed`, `total_interest`) plus one list (`schedule`) evolve in lockstep on every iteration of `while balance < target_amount:`.
3. **Immutable Snapshots:** Each month appends a fresh dictionary (`{"month": ..., "interest": ..., "contribution": ..., "ending_balance": ...}`) capturing the exact ledger state after that month's compounding and deposit.
4. **Zero-Iteration Edge Case:** If `starting_balance >= target_amount` on entry, the `while` condition is immediately `False`, returning `months=0` and `schedule=[]` cleanly.

### Traced Example (`worked_example.py`)

Call: `simulate_savings_goal(starting_balance=1000.0, monthly_contribution=500.0, annual_rate_pct=12.0, target_amount=2500.0)`
Monthly interest rate = `12.0% / 12 = 1.0%` (`0.01`).

| Month | Opening Balance | Interest (`1%`) | Contribution | Ending Balance |
|---|---|---|---|---|
| 1 | `\$1,000.00` | `\$10.00` | `\$500.00` | `\$1,510.00` |
| 2 | `\$1,510.00` | `\$15.10` | `\$500.00` | `\$2,025.10` |
| 3 | `\$2,025.10` | `\$20.25` | `\$500.00` | `\$2,545.35` (Target reached!) |

Summary: `months = 3`, `total_contributed = 1500.00`, `total_interest = 45.35`, `final_balance = 2545.35`.

---

## Your Project Brief (`project.py`)

Implement the following 2 functions in `project.py`:

### 1. `simulate_loan_payoff(principal: float, annual_rate_pct: float, monthly_payment: float) -> dict[str, Any]`
- **Input Validation (raise `ValueError`):**
  - `principal <= 0`, `annual_rate_pct < 0`, or `monthly_payment <= 0`.
  - Compute `monthly_rate = (annual_rate_pct / 100.0) / 12.0`.
  - First month's interest is `round(principal * monthly_rate, 2)`. If `monthly_payment <= principal * monthly_rate` or `monthly_payment <= round(principal * monthly_rate, 2)`, raise `ValueError` (payment cannot reduce principal).
- **Monthly Loop (`while balance > 0:`):**
  - `month += 1`
  - `interest = round(balance * monthly_rate, 2)`
  - If `round(balance + interest, 2) <= monthly_payment` (final month!):
    - `payment = round(balance + interest, 2)`
    - `principal_paid = balance`
    - `ending_balance = 0.0`
  - Else:
    - `payment = round(float(monthly_payment), 2)`
    - `principal_paid = round(payment - interest, 2)`
    - `ending_balance = round(balance - principal_paid, 2)`
  - Accumulate `total_paid = round(total_paid + payment, 2)` and `total_interest = round(total_interest + interest, 2)`.
  - Append monthly snapshot to `schedule`:
    ```python
    {
        "month": month,
        "payment": payment,
        "interest": interest,
        "principal_paid": principal_paid,
        "ending_balance": ending_balance,
    }
    ```
  - Update `balance = ending_balance`.
- **Return Value:**
  ```python
  {
      "months": month,
      "total_paid": total_paid,
      "total_interest": total_interest,
      "schedule": schedule,
  }
  ```

### 2. `estimate_months_saved(principal: float, annual_rate_pct: float, base_payment: float, extra_payment: float) -> int`
- Raises `ValueError` if `extra_payment < 0` (or if `simulate_loan_payoff` rejects the base loan parameters).
- Runs `simulate_loan_payoff` with `base_payment` and with `base_payment + extra_payment`.
- Returns `base["months"] - accelerated["months"]` (`int`).

### Acceptance Criteria
- All 6 tests in `TestMasterProject` pass alongside the 5 tests in `TestWorkedExample`.
- Accounting invariant holds for every loan: `round(principal + total_interest, 2) == total_paid`.
- Final schedule entry always ends with `ending_balance == 0.0`.

### Fun Stretch Ideas (After Tests Pass)
- Print a formatted ASCII amortization table under `if __name__ == "__main__":`.
- Write a companion function `estimate_interest_saved(...)` that shows how many dollars extra monthly payments save over the life of the loan!

---

## Running Tests

Run from the `ExamPrep/` directory:

```bash
python -m unittest master_projects/checkpoint_05_loan_amortization_simulator/test_project.py -v
```
