"""Messy Monolithic Invoice Generator — Refactoring Target for Mission 14.

PROBLEM:
``generate_invoice_summary`` is a single ~95-line god-function that mixes:
1. Input validation,
2. Line-item subtotaling,
3. Promo-code discount lookup,
4. Tax & grand-total computation,
5. Loyalty points & tier rules, and
6. Multi-line text receipt formatting.

YOUR GOAL:
Decompose ``generate_invoice_summary`` into clean, single-purpose helper
functions so that:
- ``generate_invoice_summary`` is <= 30 lines,
- It delegates to at least 3 extracted helper functions, and
- No function in this file exceeds 35 lines.
"""

from typing import Dict, List, Optional, Sequence, Tuple, Union

LineItem = Tuple[str, int, float]
InvoiceSummary = Dict[str, Union[str, int, float]]


def generate_invoice_summary(
    customer_name: str,
    line_items: Sequence[LineItem],
    discount_code: Optional[str],
    tax_rate: float,
) -> InvoiceSummary:
    """Validate, price, apply discounts/tax/loyalty, and format an invoice."""
    # --- 1. Validate customer & tax inputs ---
    if not isinstance(customer_name, str) or customer_name.strip() == "":
        raise ValueError("Customer name must be a non-empty string.")
    clean_customer = customer_name.strip()

    if isinstance(tax_rate, bool) or not isinstance(tax_rate, (int, float)):
        raise ValueError("Tax rate must be a number between 0 and 1.")
    if tax_rate < 0.0 or tax_rate > 1.0:
        raise ValueError("Tax rate must be between 0.0 and 1.0.")

    if not line_items:
        raise ValueError("Invoice must include at least one line item.")

    # --- 2. Validate & total every line item ---
    parsed_lines: List[Tuple[str, int, float, float]] = []
    raw_subtotal = 0.0
    total_units = 0
    for entry in line_items:
        if len(entry) != 3:
            raise ValueError("Each line item must be a (name, quantity, unit_price) tuple.")
        item_name, qty, unit_price = entry
        if not isinstance(item_name, str) or item_name.strip() == "":
            raise ValueError("Line item name must be a non-empty string.")
        if isinstance(qty, bool) or not isinstance(qty, int) or qty <= 0:
            raise ValueError("Line item quantity must be a positive integer.")
        if isinstance(unit_price, bool) or not isinstance(unit_price, (int, float)) or unit_price < 0:
            raise ValueError("Line item unit price must be non-negative.")

        clean_item = item_name.strip()
        line_total = round(qty * float(unit_price), 2)
        raw_subtotal = raw_subtotal + line_total
        total_units = total_units + qty
        parsed_lines.append((clean_item, qty, float(unit_price), line_total))

    subtotal = round(raw_subtotal, 2)

    # --- 3. Lookup & apply discount code ---
    normalized_code = ""
    if discount_code is not None:
        if not isinstance(discount_code, str):
            raise ValueError("Discount code must be a string or None.")
        normalized_code = discount_code.strip().upper()

    discount = 0.0
    if normalized_code == "":
        discount = 0.0
    elif normalized_code == "SAVE10":
        discount = round(subtotal * 0.10, 2)
    elif normalized_code == "SAVE20":
        if subtotal >= 100.0:
            discount = round(subtotal * 0.20, 2)
        else:
            discount = 0.0
    elif normalized_code == "WELCOME5":
        discount = round(min(5.0, subtotal), 2)
    else:
        raise ValueError(f"Unknown discount code: {discount_code}")

    # --- 4. Compute tax and grand total ---
    taxable_amount = round(subtotal - discount, 2)
    tax = round(taxable_amount * tax_rate, 2)
    total = round(taxable_amount + tax, 2)

    # --- 5. Compute loyalty points & membership tier ---
    loyalty_points = int(taxable_amount // 10)
    if total >= 200.0 and total_units >= 5:
        loyalty_points = loyalty_points + 25

    if loyalty_points >= 50:
        loyalty_tier = "Gold"
    elif loyalty_points >= 20:
        loyalty_tier = "Silver"
    else:
        loyalty_tier = "Bronze"

    # --- 6. Build formatted text receipt ---
    receipt_lines = [
        f"INVOICE FOR: {clean_customer}",
        "================================",
    ]
    for clean_item, qty, unit_price, line_total in parsed_lines:
        receipt_lines.append(
            f"- {clean_item} x{qty} @ ${unit_price:.2f} = ${line_total:.2f}"
        )
    receipt_lines.append("--------------------------------")
    receipt_lines.append(f"Subtotal: ${subtotal:.2f}")
    receipt_lines.append(f"Discount: -${discount:.2f}")
    receipt_lines.append(f"Tax ({tax_rate * 100:.1f}%): ${tax:.2f}")
    receipt_lines.append(f"TOTAL: ${total:.2f}")
    receipt_lines.append(f"Loyalty: {loyalty_points} pts ({loyalty_tier})")
    receipt = "\n".join(receipt_lines)

    return {
        "customer": clean_customer,
        "subtotal": subtotal,
        "discount": discount,
        "tax": tax,
        "total": total,
        "total_units": total_units,
        "loyalty_points": loyalty_points,
        "loyalty_tier": loyalty_tier,
        "receipt": receipt,
    }
