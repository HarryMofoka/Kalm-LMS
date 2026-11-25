# Checkpoint 01 — Restaurant Bill, Tax, Tip & Fair Group Splitter

- **Unlocked After:** Activity 006 (Variables, Arithmetic & Rounding)
- **Difficulty:** Beginner
- **Core Concepts:** Numeric types, percentages, `round()`, integer cent math (`//`, `%`), input validation, formatted output

---

## Real-World Value

Every Point-of-Sale (POS) terminal (Square, Toast, Yoco), food-delivery app (Uber Eats, DoorDash, Mr D), and group payment splitter (Splitwise, Revolut) runs a receipt math engine under the hood.

Floating-point money math has a famous trap: splitting **\$125.00** among **3 people** gives `41.666666...`. If you naively round each share to `\$41.67`, the restaurant collects `\$125.01` (phantom cent!). If you floor each share to `\$41.66`, the restaurant is short `\$0.02`. Real FinTech systems convert totals into **integer cents**, divide with `//`, and explicitly track the `remainder_cents` (`%`) so every single penny reconciles to the exact bill total.

---

## Problem Statement

Build a restaurant billing and fair group-splitting engine in `project.py` that:

1. Calculates sales tax on a meal subtotal.
2. Calculates a tip on the **pre-tax** subtotal.
3. Splits the grand total across `num_people` using exact integer-cent arithmetic so that:
   `per_person * num_people + remainder_cents / 100 == total`
4. Formats clean, fixed-width thermal receipt lines (`Label` on the left, `$amount` right-aligned).
5. Rejects invalid inputs (negative money/rates, or fewer than 1 person) with `ValueError`.

---

## How a Similar Functioning System Was Done (`worked_example.py`)

Before writing your own engine, inspect and run **`worked_example.py`** — a complete **E-commerce Checkout & Shipping Totals Engine**.

```bash
python master_projects/checkpoint_01_split_bill_calculator/worked_example.py
```

### Architectural Walkthrough

1. **Single-Responsibility Helpers:** Rather than cramming every percentage formula into one giant function, `worked_example.py` splits discount, sales tax, and shipping rules into small, independently testable helpers (`calculate_discount`, `calculate_sales_tax`, `calculate_shipping`).
2. **Guard Clauses at the Boundary:** Every helper checks its preconditions first (e.g., `subtotal < 0`, `discount_pct` outside `0..100`) and raises `ValueError` immediately before any math runs.
3. **Round at Each Accounting Line:** Each line item on a real invoice (`discount`, `taxable_subtotal`, `tax`, `shipping`) is rounded to 2 decimal places (`round(..., 2)`), and `grand_total` is computed from those rounded line items so the printed receipt adds up visually to the penny.
4. **Presentation Separate from Logic:** `build_checkout_summary()` returns pure structured data (`dict`), while `format_checkout_line()` handles spacing and `$` formatting.

### Traced Example (`worked_example.py`)

Call: `build_checkout_summary(subtotal=120.00, discount_pct=20.0, tax_rate_pct=15.0)`

| Step | Formula | Result |
|---|---|---|
| 1. `discount` | `round(120.00 * 0.20, 2)` | `24.00` |
| 2. `taxable_subtotal` | `round(120.00 - 24.00, 2)` | `96.00` |
| 3. `tax` | `round(96.00 * 0.15, 2)` | `14.40` |
| 4. `shipping` | `96.00 < 100.00` threshold -> standard fee | `12.50` |
| 5. `grand_total` | `round(96.00 + 14.40 + 12.50, 2)` | `122.90` |

Notice how applying the 20% discount drops the order from `\$120.00` to `\$96.00` — just under the `\$100.00` free-shipping threshold — so `shipping` becomes `\$12.50`. Order of operations matters!

---

## Your Project Brief (`project.py`)

Implement the following 4 functions in `project.py`:

### 1. `calculate_tax(subtotal: float, tax_rate_pct: float) -> float`
- Computes tax as `round(subtotal * (tax_rate_pct / 100.0), 2)`.
- Raises `ValueError` if `subtotal < 0` or `tax_rate_pct < 0`.

### 2. `calculate_tip(subtotal: float, tip_pct: float) -> float`
- Computes tip on the **pre-tax** `subtotal`: `round(subtotal * (tip_pct / 100.0), 2)`.
- Raises `ValueError` if `subtotal < 0` or `tip_pct < 0`.

### 3. `split_bill(subtotal: float, tax_rate_pct: float, tip_pct: float, num_people: int) -> dict[str, float | int]`
- Validates that `subtotal >= 0`, `tax_rate_pct >= 0`, `tip_pct >= 0`, and `num_people` is an `int` (not a `bool`) with `num_people >= 1`. Raises `ValueError` otherwise.
- Rounds `subtotal` to 2 decimals, calculates `tax` and `tip`, and computes `total = round(subtotal + tax + tip, 2)`.
- Converts `total` to integer cents (`total_cents = round(total * 100)`):
  - `per_person = round((total_cents // num_people) / 100.0, 2)`
  - `remainder_cents = total_cents % num_people`
- Returns a dictionary with exact keys:
  ```python
  {
      "subtotal": float,
      "tax": float,
      "tip": float,
      "total": float,
      "per_person": float,
      "remainder_cents": int,
  }
  ```

### 4. `format_receipt_line(label: str, amount: float, width: int = 30) -> str`
- Formats `amount` as `f"${amount:.2f}"` (or `f"-${abs(amount):.2f}"` if negative).
- Left-aligns `label` and right-aligns the price string within `width` characters using spaces.
- Always keeps **at least 1 space** between `label` and the price string if `len(label) + len(price_str) >= width`.
- Example: `format_receipt_line("Subtotal", 85.5, width=20)` -> `"Subtotal      $85.50"`.

### Acceptance Criteria
- All 6 tests in `TestMasterProject` pass alongside the 5 existing tests in `TestWorkedExample`.
- Penny-conservation holds on every split: `round(per_person * num_people + remainder_cents / 100.0, 2) == total`.

### Fun Stretch Ideas (After Tests Pass)
- Add a CLI runner under `if __name__ == "__main__":` that prints a full restaurant receipt and tells you which diners cover the extra `remainder_cents`.
- Support custom currency symbols (`"R"`, `"€"`, `"£"`, `"$"`) in `format_receipt_line`.

---

## Running Tests

Run from the `ExamPrep/` directory:

```bash
python -m unittest master_projects/checkpoint_01_split_bill_calculator/test_project.py -v
```
