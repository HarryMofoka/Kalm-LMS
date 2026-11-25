"""Worked Example — E-commerce Checkout & Shipping Totals Engine.

A complete sibling reference system demonstrating clean decomposition,
line-item rounding, guard clauses, and fixed-width receipt formatting.
"""

from __future__ import annotations

FREE_SHIPPING_THRESHOLD: float = 100.00
STANDARD_SHIPPING_FEE: float = 12.50


def calculate_discount(subtotal: float, discount_pct: float) -> float:
    """Return the currency discount amount rounded to 2 decimal places."""
    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative.")
    if not (0.0 <= discount_pct <= 100.0):
        raise ValueError("Discount percentage must be between 0 and 100.")
    return round(subtotal * (discount_pct / 100.0), 2)


def calculate_sales_tax(taxable_amount: float, tax_rate_pct: float) -> float:
    """Return sales tax on the taxable amount rounded to 2 decimal places."""
    if taxable_amount < 0:
        raise ValueError("Taxable amount cannot be negative.")
    if tax_rate_pct < 0:
        raise ValueError("Tax rate cannot be negative.")
    return round(taxable_amount * (tax_rate_pct / 100.0), 2)


def calculate_shipping(
    discounted_subtotal: float,
    free_threshold: float = FREE_SHIPPING_THRESHOLD,
    base_fee: float = STANDARD_SHIPPING_FEE,
) -> float:
    """Return shipping fee: free on empty carts or orders meeting free_threshold."""
    if discounted_subtotal < 0:
        raise ValueError("Discounted subtotal cannot be negative.")
    if discounted_subtotal == 0 or discounted_subtotal >= free_threshold:
        return 0.0
    return round(base_fee, 2)


def build_checkout_summary(
    subtotal: float,
    discount_pct: float = 0.0,
    tax_rate_pct: float = 15.0,
) -> dict[str, float]:
    """Compute a complete, penny-reconciled e-commerce checkout breakdown."""
    clean_subtotal = round(float(subtotal), 2)
    discount = calculate_discount(clean_subtotal, discount_pct)
    taxable_subtotal = round(clean_subtotal - discount, 2)
    tax = calculate_sales_tax(taxable_subtotal, tax_rate_pct)
    shipping = calculate_shipping(taxable_subtotal)
    grand_total = round(taxable_subtotal + tax + shipping, 2)

    return {
        "subtotal": clean_subtotal,
        "discount": discount,
        "taxable_subtotal": taxable_subtotal,
        "tax": tax,
        "shipping": shipping,
        "grand_total": grand_total,
    }


def format_checkout_line(label: str, amount: float, width: int = 28) -> str:
    """Format a left-aligned label and right-aligned dollar amount."""
    price_str = f"-${abs(amount):.2f}" if amount < 0 else f"${amount:.2f}"
    gap = max(1, width - len(label) - len(price_str))
    return f"{label}{' ' * gap}{price_str}"


if __name__ == "__main__":
    summary = build_checkout_summary(subtotal=120.00, discount_pct=20.0, tax_rate_pct=15.0)
    print("=" * 28)
    print("    ONLINE STORE RECEIPT    ")
    print("=" * 28)
    print(format_checkout_line("Subtotal", summary["subtotal"]))
    print(format_checkout_line("Discount (20%)", -summary["discount"]))
    print(format_checkout_line("Taxable Subtotal", summary["taxable_subtotal"]))
    print(format_checkout_line("Sales Tax (15%)", summary["tax"]))
    print(format_checkout_line("Shipping", summary["shipping"]))
    print("-" * 28)
    print(format_checkout_line("GRAND TOTAL", summary["grand_total"]))
    print("=" * 28)
