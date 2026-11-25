# Checkpoint 03 — Smart Prepaid Electricity Tariff Calculator

- **Unlocked After:** Activity 018 (Conditionals & Tiered Logic)
- **Difficulty:** Intermediate
- **Core Concepts:** Progressive block tariffs, marginal vs. flat-rate math, boundary conditions (`<=` vs `<`), boolean feature flags, inverse piecewise functions

---

## Real-World Value

Municipal prepaid electricity utilities (Eskom, City Power, City of Cape Town's Inclining Block Tariff), cloud storage platforms (AWS S3 tiered pricing), and national income-tax systems (SARS, IRS) all rely on **progressive marginal brackets**.

One of the most common real-world billing bugs is applying the top tier's rate to the **entire** consumption instead of only the units that fall inside that tier. If someone uses **101 kWh**, only **1 kWh** is billed at Tier 2 — the first 100 kWh stays at the Lifeline Tier 1 rate! Mastering piecewise marginal calculations also lets you invert the tariff so a prepaid customer typing *"Give me \$300 worth of electricity"* gets the exact number of kWh units on their token.

---

## Problem Statement

Build a Smart Prepaid Electricity Tariff Calculator in `project.py` with the following 3-tier Inclining Block Tariff:

| Tier | Label | kWh Range | Rate per kWh |
|---|---|---|---|
| **Tier 1** | `"Tier 1 (Lifeline)"` | First `100` kWh (`0 .. 100`) | `\$1.50` |
| **Tier 2** | `"Tier 2 (Standard)"` | Next `250` kWh (`100 .. 350`) | `\$2.20` |
| **Tier 3** | `"Tier 3 (High Usage)"` | Above `350` kWh (`> 350`) | `\$3.10` |

Additional billing rules:
- **Fixed Service Fee:** `\$25.00` monthly grid connection fee applies to every bill (even at `0` kWh).
- **Off-Peak / Smart-Meter Bonus (`peak_bonus=True`):** Grants a **10% discount** on the `usage_charge` only (never on the fixed service fee).
- **Meter Validation:** Previous and current meter readings must be non-negative, and `curr_reading >= prev_reading` (detects meter rollbacks/tampering).
- **Prepaid Budget Inversion (`kwh_for_budget`):** Computes exact kWh purchased for a given energy budget (energy units only — no service fee deducted).

---

## How a Similar Functioning System Was Done (`worked_example.py`)

Before building the electricity engine, read and execute **`worked_example.py`** — a complete **Progressive Income Tax Bracket Calculator**.

```bash
python master_projects/checkpoint_03_smart_tariff_calculator/worked_example.py
```

### Architectural Walkthrough

1. **Named Constants for Brackets & Rates:** Hardcoding `20000` and `0.2` deep inside expressions makes tariff updates terrifying. `worked_example.py` defines top-level constants so every boundary is documented in one place.
2. **Slice-Per-Tier Marginal Math:** Instead of writing brittle nested `if/elif/else` formulas that duplicate earlier tiers, each tier computes the exact slice of income falling inside it:
   - `tier1_slice = min(income, 20_000)`
   - `tier2_slice = min(max(income - 20_000, 0), 30_000)`
   - `tier3_slice = max(income - 50_000, 0)`
   Notice how clean and bug-free this pattern is: boundary values (`20_000`, `50_000`) transition continuously with zero cliff jumps!
3. **Zero-Division Guard for Effective Rate:** When `income == 0`, `effective_rate_pct` safely returns `0.0` instead of crashing with `ZeroDivisionError`.

### Traced Example (`worked_example.py`)

Call: `calculate_progressive_tax(income=65_000)`

| Bracket | Slice Formula | Taxable Slice | Rate | Bracket Tax |
|---|---|---|---|---|
| Bracket 1 (`0..20k`) | `min(65000, 20000)` | `\$20,000` | `10%` | `\$2,000.00` |
| Bracket 2 (`20k..50k`) | `min(max(65000 - 20000, 0), 30000)` | `\$30,000` | `20%` | `\$6,000.00` |
| Bracket 3 (`>50k`) | `max(65000 - 50000, 0)` | `\$15,000` | `30%` | `\$4,500.00` |
| **Totals** | `total_tax = 12,500.00` | `net_income = 52,500.00` | Effective: `19.23%` | Top: `"Bracket 3 (30%)"` |

---

## Your Project Brief (`project.py`)

Implement these 4 functions in `project.py` (constants are already provided at the top of the file):

### 1. `validate_reading(prev_reading: float, curr_reading: float) -> float`
- Raises `ValueError` if `prev_reading < 0`, `curr_reading < 0`, or `curr_reading < prev_reading`.
- Returns `round(curr_reading - prev_reading, 2)`.

### 2. `tariff_tier_label(kwh: float) -> str`
- Raises `ValueError` if `kwh < 0`.
- Returns:
  - `"Tier 1 (Lifeline)"` when `kwh <= 100`
  - `"Tier 2 (Standard)"` when `100 < kwh <= 350`
  - `"Tier 3 (High Usage)"` when `kwh > 350`

### 3. `calculate_electricity_bill(kwh: float, peak_bonus: bool = False) -> dict[str, float | str]`
- Raises `ValueError` if `kwh < 0`.
- Computes progressive `usage_charge` across the 3 tiers, rounded to 2 decimals.
- Computes `discount = round(usage_charge * 0.10, 2)` if `peak_bonus` is `True`, else `0.0`.
- Computes `total = round(usage_charge - discount + FIXED_SERVICE_FEE, 2)`.
- Returns a dictionary with exact keys:
  ```python
  {
      "kwh": round(float(kwh), 2),
      "tier": tariff_tier_label(kwh),
      "usage_charge": usage_charge,
      "discount": discount,
      "service_fee": 25.00,
      "total": total,
  }
  ```

### 4. `kwh_for_budget(amount: float) -> float`
- Raises `ValueError` if `amount < 0`.
- Inverts the 3-tier energy tariff (for energy units only; does not deduct the fixed service fee):
  - Tier 1 fills up to `\$150.00` (`100 kWh * \$1.50`).
  - Tier 2 fills the next `\$550.00` (`250 kWh * \$2.20`, cumulative `\$700.00` -> `350 kWh`).
  - Any remaining budget above `\$700.00` buys units at `\$3.10 / kWh`.
- Returns total kWh rounded to 2 decimal places (`round(kwh, 2)`).
- Sanity check: `kwh_for_budget(480.0)` returns `250.0`, matching `calculate_electricity_bill(250)["usage_charge"] == 480.0`!

### Acceptance Criteria
- All 7 tests in `TestMasterProject` pass alongside the 5 tests in `TestWorkedExample`.
- Boundary values (`0`, `100`, `350` kWh and `\$150`, `\$700` budgets) behave continuously without off-by-one errors.

### Fun Stretch Ideas (After Tests Pass)
- Add a CLI prepaid token generator that accepts previous + current readings and prints an itemized municipal bill.
- Add VAT (e.g., 15%) on top of the final subtotal as an optional parameter.

---

## Running Tests

Run from the `ExamPrep/` directory:

```bash
python -m unittest master_projects/checkpoint_03_smart_tariff_calculator/test_project.py -v
```
