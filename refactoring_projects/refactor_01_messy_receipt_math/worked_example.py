"""Worked Example for Refactor 01: Cafe Order Tip & VAT Calculator.

Compares a cryptic, magic-number-filled implementation (`before_calc`)
with its clean, self-documenting refactored sibling (`after_calculate_order_total`).
"""

# ---------------------------------------------------------------------------
# BEFORE: Cryptic 1-letter variables & unexplained magic numbers
# ---------------------------------------------------------------------------


def before_calc(p, q, t):
    # What are p, q, t? What is 0.10 vs 0.15? Why 2.50? Nobody knows!
    a = p * q
    b = a * 0.10
    c = a + b
    d = c * 0.15
    x = 2.50 if t else 0.0
    return round(c + d + x, 2)


# ---------------------------------------------------------------------------
# AFTER: Named UPPER_CASE constants, descriptive names, and a clear docstring
# ---------------------------------------------------------------------------

SERVICE_TIP_RATE = 0.10
VAT_RATE = 0.15
TAKEAWAY_PACKAGING_FEE = 2.50


def after_calculate_order_total(unit_price, quantity, is_takeaway):
    """Calculate the final cafe order total with tip, VAT, and optional packaging.

    Args:
        unit_price: Price of a single menu item.
        quantity: Number of items ordered.
        is_takeaway: True if takeaway packaging fee applies.

    Returns:
        The rounded final order total to 2 decimal places.
    """
    subtotal = unit_price * quantity
    service_tip = subtotal * SERVICE_TIP_RATE
    taxable_total = subtotal + service_tip
    vat_amount = taxable_total * VAT_RATE
    packaging_fee = TAKEAWAY_PACKAGING_FEE if is_takeaway else 0.0
    grand_total = taxable_total + vat_amount + packaging_fee
    return round(grand_total, 2)


if __name__ == "__main__":
    sample_orders = [
        (45.0, 2, False),
        (45.0, 2, True),
        (19.95, 3, True),
    ]
    for price, qty, takeaway in sample_orders:
        old_result = before_calc(price, qty, takeaway)
        new_result = after_calculate_order_total(price, qty, takeaway)
        print(
            f"price={price}, qty={qty}, takeaway={takeaway} -> "
            f"before={old_result:.2f}, after={new_result:.2f}"
        )
