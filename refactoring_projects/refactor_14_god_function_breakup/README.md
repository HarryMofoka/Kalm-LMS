# Refactor 14 — Break Up a Monolithic God-Function

## Backstory & Problem Statement

Billing Ops just asked for two small tweaks to the invoice generator: add a new promo code and change how loyalty tiers are named. Sounds like a 2-minute job... until you open `messy_code.py` and stare at `generate_invoice_summary(customer_name, line_items, discount_code, tax_rate)`.

It is a **95-line monolithic god-function** that tries to do *everything* in one giant wall of code:

1. Input validation,
2. Line-item subtotaling,
3. Promo-code discount rules,
4. Tax & grand-total math,
5. Loyalty points & tier classification, and
6. Multi-line text receipt formatting.

Because six unrelated concerns are tangled inside one giant function, changing any single rule risks accidentally breaking the others.

## Code Smells Checklist

- [ ] **God function**: A single function exceeding 80+ lines handling 6 distinct responsibilities.
- [ ] **Deep cognitive load**: Dozens of local variables stay alive across unrelated sections of the function.
- [ ] **Untestable sub-steps**: You cannot test discount calculation, loyalty points, or receipt formatting independently.
- [ ] **Hard to read top-to-bottom**: The high-level invoice workflow is buried under low-level arithmetic and string building.

## Worked Refactoring Walkthrough (Before -> After)

Open `worked_example.py` to study `before_process_booking` vs `after_process_booking`:

- **Before (`before_process_booking`)**: One bloated function validating inputs, calculating room charges, applying member discounts, adding resort fees and tax, and assembling a confirmation receipt all inline.
- **After (`after_process_booking`)**: Broken into focused, single-purpose helper functions:
  - `_validate_booking_inputs(...)`
  - `_compute_booking_charges(...)`
  - `_format_booking_receipt(...)`
  - `after_process_booking(...)` reads like a clean 12-line table of contents orchestrating the helpers!

## Your Refactoring Mission

Break `generate_invoice_summary(customer_name, line_items, discount_code, tax_rate)` in `messy_code.py` into clean, single-responsibility helper functions while keeping **every single behavior and validation error identical**:

1. Keep `generate_invoice_summary` concise (**30 lines or fewer**).
2. Extract and delegate to **at least 3 module-level helper functions** (for example: `validate_invoice_inputs`, `compute_line_items`, `calculate_discount`, `calculate_loyalty`, `format_invoice_receipt`).
3. Ensure **no single function** in `messy_code.py` exceeds **35 lines**.

## Run the Tests

From the `ExamPrep` directory:

```bash
python -m unittest refactoring_projects/refactor_14_god_function_breakup/test_refactor.py -v
```

Or run the test file directly:

```bash
python ExamPrep/refactoring_projects/refactor_14_god_function_breakup/test_refactor.py -v
```

Verify that `TestWorkedExample` and `TestBehaviorSafetyNet` start **GREEN** while `TestRefactorGoals` starts **RED**, then decompose `messy_code.py` until all tests are **GREEN**!
