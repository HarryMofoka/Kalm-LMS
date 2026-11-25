# Refactor 01 — Messy Receipt Math (Checkpoint 01)

> **Mission:** Rescue a working shipping-cost calculator buried under cryptic 1-letter variable names (`a, b, c, x1, x2, z`) and unexplained magic numbers (`15.0`, `2.5`, `0.5`, `45.0`, `0.15`).

## Backstory & Problem Statement

Last Friday at 16:58, your teammate "Speedy Sam" pushed `calculate_shipping_total` to production right before leaving on a three-week hike with zero cell reception.

The good news: the math is **100% right** and finance signed off on every single cent.  
The bad news: nobody on the team can tell what `x1`, `x2`, `b`, or `45.0` mean, and next month the courier is raising the express surcharge! If someone guesses the wrong number, customers will be overcharged.

Your job is to **refactor `messy_code.py`** so any developer can read it in 5 seconds — without changing a single cent of its output.

## Code Smells Checklist

Look for these classic Checkpoint 01 smells inside `messy_code.py`:

- [ ] **Cryptic parameter names** (`w`, `d`, `e`) that force callers to guess units and types.
- [ ] **Cryptic local variables** (`a`, `b`, `c`, `x1`, `x2`, `z`) that hide what each step calculates.
- [ ] **Unexplained magic numbers** (`15.0`, `2.5`, `0.5`, `45.0`, `0.15`) hard-coded directly inside formulas instead of named `UPPER_CASE` module constants.
- [ ] **Missing docstring** explaining the function's purpose, inputs, and return value.

## Worked Refactoring Walkthrough (Before -> After)

Open `worked_example.py` to see a sibling cafe receipt calculator transformed step by step:

**Before (`before_calc`)**:
```python
def before_calc(p, q, t):
    a = p * q
    b = a * 0.10
    c = a + b
    d = c * 0.15
    x = 2.50 if t else 0.0
    return round(c + d + x, 2)
```

**After (`after_calculate_order_total`)**:
```python
SERVICE_TIP_RATE = 0.10
VAT_RATE = 0.15
TAKEAWAY_PACKAGING_FEE = 2.50


def after_calculate_order_total(unit_price, quantity, is_takeaway):
    """Calculate the final cafe order total including tip, VAT, and optional packaging."""
    subtotal = unit_price * quantity
    service_tip = subtotal * SERVICE_TIP_RATE
    taxable_total = subtotal + service_tip
    vat_amount = taxable_total * VAT_RATE
    packaging_fee = TAKEAWAY_PACKAGING_FEE if is_takeaway else 0.0
    grand_total = taxable_total + vat_amount + packaging_fee
    return round(grand_total, 2)
```

Notice how the formula didn't change at all — yet the business rules instantly jump off the page!

## Your Refactoring Mission

Edit `messy_code.py` while respecting these rules:

1. **Preserve the function name and positional parameter order:**
   - Function name must remain `calculate_shipping_total`.
   - Keep the exact 3 positional parameters in the same order: `(weight_kg, distance_km, is_express)`.
   - **Do rename** the cryptic parameter names `(w, d, e)` to clear, descriptive names!
2. **Eliminate cryptic names:** Replace every single-letter or numbered variable (`w, d, e, a, b, c, x1, x2, z`) with self-explanatory names.
3. **Extract named `UPPER_CASE` module constants:** Move all shipping rates, surcharges, and tax rates (`15.0`, `2.5`, `0.5`, `45.0`, `0.15`) to descriptive `UPPER_CASE` constants at the top of `messy_code.py`.
4. **Add a clear docstring** to `calculate_shipping_total`.
5. **Keep `TestBehaviorSafetyNet` green** at every step!

## Running the Tests

From inside the `ExamPrep/` folder:

```bash
python -m unittest refactoring_projects.refactor_01_messy_receipt_math.test_refactor -v
```

Or run the test file directly from this mission folder:

```bash
python test_refactor.py
```

Goal: turn `TestRefactorGoals` from **RED** to **GREEN** while keeping `TestWorkedExample` and `TestBehaviorSafetyNet` **GREEN**!
