# Refactor 03 — The 6-Level Nested `if` Pyramid (Checkpoint 03)

> **Mission:** Flatten a 6-level deep "arrow anti-pattern" delivery discount checker into crisp, flat **guard clauses** (`<= 2` nesting depth) without changing a single branch!

## Backstory & Problem Statement

QuickBite Delivery's checkout team calls `evaluate_delivery_discount` the **"Sideways Pyramid of Doom."**

Every time marketing added a new discount rule — minimum cart total, membership check, minimum item count, coupon code, weekend promo — a rushed developer indented *another* `if/else` level inside the previous one. Now the main business logic sits **24 spaces from the left margin**, and matching each `else:` back to its `if:` requires a ruler taped to your monitor.

Your mission is to flatten `evaluate_delivery_discount` using **early-return guard clauses**, while keeping every single return string identical for all inputs.

## Code Smells Checklist

Look for these classic Checkpoint 03 smells inside `messy_code.py`:

- [ ] **6-level arrow anti-pattern** (`if` inside `if` inside `if` ...) that forces readers to track 6 simultaneous mental conditions.
- [ ] **Distant `else:` blocks** separated by 15–30 lines from the `if:` condition they belong to.
- [ ] **Single delayed `return result`** at the bottom forcing every failure path to jump through six levels of indentation instead of returning immediately.

## Worked Refactoring Walkthrough (Before -> After)

Open `worked_example.py` to see a library book-borrowing eligibility checker flattened from 6 levels down to 1:

**Before (`before_can_borrow`) — 6 levels deep:**
```python
def before_can_borrow(has_card, is_suspended, late_fees, active_loans, book_available, is_reference_only):
    status = ""
    if has_card:
        if not is_suspended:
            if late_fees == 0:
                if active_loans < 5:
                    if book_available:
                        if not is_reference_only:
                            status = "Approved"
                        else:
                            status = "Denied: reference-only book"
                    else:
                        status = "Denied: book unavailable"
                else:
                    status = "Denied: loan limit reached"
            else:
                status = "Denied: unpaid late fees"
        else:
            status = "Denied: account suspended"
    else:
        status = "Denied: library card required"
    return status
```

**After (`after_can_borrow`) — flat guard clauses (depth 1!):**
```python
def after_can_borrow(has_card, is_suspended, late_fees, active_loans, book_available, is_reference_only):
    if not has_card:
        return "Denied: library card required"
    if is_suspended:
        return "Denied: account suspended"
    if late_fees != 0:
        return "Denied: unpaid late fees"
    if active_loans >= 5:
        return "Denied: loan limit reached"
    if not book_available:
        return "Denied: book unavailable"
    if is_reference_only:
        return "Denied: reference-only book"
    return "Approved"
```

Notice the secret trick of guard clauses: **invert each check and return early for the failure/simple cases first!** The happy path stays completely unindented.

## Your Refactoring Mission

Edit `messy_code.py` while respecting these rules:

1. **Preserve the exact function signature:**
   `evaluate_delivery_discount(is_member, cart_total, item_count, has_coupon, is_weekend)`
2. **Flatten `if` nesting depth to `<= 2`** (down from `6` in the messy baseline — aim for depth `1`!).
3. **Use early-return guard clauses** (`if ...: return ...`) instead of storing into `result` and nesting `else:` blocks.
4. **Preserve every single branch's exact output string and precedence order** (e.g., an empty cart still fails the empty-cart check before the minimum-total or membership checks!).
5. **Keep `TestBehaviorSafetyNet` green** at every step!

## Running the Tests

From inside the `ExamPrep/` folder:

```bash
python -m unittest refactoring_projects.refactor_03_nested_if_pyramid.test_refactor -v
```

Or run directly from this folder:

```bash
python test_refactor.py
```

Goal: turn `TestRefactorGoals` from **RED** to **GREEN** while keeping `TestWorkedExample` and `TestBehaviorSafetyNet` **GREEN**!
