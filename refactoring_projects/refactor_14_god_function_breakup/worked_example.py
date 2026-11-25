"""Worked Example for CP 14: Breaking a monolithic booking processor into helpers.

Compare:
- ``before_process_booking``: one long function mixing validation, pricing,
  discounts, tax, and text formatting.
- ``after_process_booking``: short orchestrator delegating to focused helpers.
"""

from typing import Dict, Union

BookingSummary = Dict[str, Union[str, int, float]]


def before_process_booking(
    guest_name: str,
    nights: int,
    nightly_rate: float,
    is_member: bool,
) -> BookingSummary:
    """Messy monolithic booking processor doing everything inline."""
    if not isinstance(guest_name, str) or guest_name.strip() == "":
        raise ValueError("Guest name must be a non-empty string.")
    clean_name = guest_name.strip()
    if isinstance(nights, bool) or not isinstance(nights, int) or nights <= 0:
        raise ValueError("Nights must be a positive integer.")
    if isinstance(nightly_rate, bool) or nightly_rate <= 0:
        raise ValueError("Nightly rate must be positive.")

    room_subtotal = round(nights * nightly_rate, 2)
    member_discount = 0.0
    if is_member:
        member_discount = round(room_subtotal * 0.15, 2)
    discounted_room = round(room_subtotal - member_discount, 2)

    resort_fee = round(nights * 12.50, 2)
    taxable = round(discounted_room + resort_fee, 2)
    tax = round(taxable * 0.10, 2)
    grand_total = round(taxable + tax, 2)

    lines = [
        f"BOOKING CONFIRMATION: {clean_name}",
        f"Stay: {nights} night(s) @ ${nightly_rate:.2f}/night",
        f"Room Subtotal: ${room_subtotal:.2f}",
        f"Member Discount: -${member_discount:.2f}",
        f"Resort Fee: ${resort_fee:.2f}",
        f"Tax (10%): ${tax:.2f}",
        f"Grand Total: ${grand_total:.2f}",
    ]
    confirmation = "\n".join(lines)

    return {
        "guest": clean_name,
        "nights": nights,
        "subtotal": room_subtotal,
        "discount": member_discount,
        "resort_fee": resort_fee,
        "tax": tax,
        "total": grand_total,
        "confirmation": confirmation,
    }


def _validate_booking_inputs(
    guest_name: str, nights: int, nightly_rate: float
) -> str:
    if not isinstance(guest_name, str) or not guest_name.strip():
        raise ValueError("Guest name must be a non-empty string.")
    if isinstance(nights, bool) or not isinstance(nights, int) or nights <= 0:
        raise ValueError("Nights must be a positive integer.")
    if isinstance(nightly_rate, bool) or nightly_rate <= 0:
        raise ValueError("Nightly rate must be positive.")
    return guest_name.strip()


def _compute_booking_charges(
    nights: int, nightly_rate: float, is_member: bool
) -> Dict[str, float]:
    subtotal = round(nights * nightly_rate, 2)
    discount = round(subtotal * 0.15, 2) if is_member else 0.0
    resort_fee = round(nights * 12.50, 2)
    taxable = round(subtotal - discount + resort_fee, 2)
    tax = round(taxable * 0.10, 2)
    total = round(taxable + tax, 2)
    return {
        "subtotal": subtotal,
        "discount": discount,
        "resort_fee": resort_fee,
        "tax": tax,
        "total": total,
    }


def _format_booking_receipt(
    guest: str, nights: int, nightly_rate: float, charges: Dict[str, float]
) -> str:
    return "\n".join(
        [
            f"BOOKING CONFIRMATION: {guest}",
            f"Stay: {nights} night(s) @ ${nightly_rate:.2f}/night",
            f"Room Subtotal: ${charges['subtotal']:.2f}",
            f"Member Discount: -${charges['discount']:.2f}",
            f"Resort Fee: ${charges['resort_fee']:.2f}",
            f"Tax (10%): ${charges['tax']:.2f}",
            f"Grand Total: ${charges['total']:.2f}",
        ]
    )


def after_process_booking(
    guest_name: str,
    nights: int,
    nightly_rate: float,
    is_member: bool,
) -> BookingSummary:
    """Clean modular booking processor delegating to single-purpose helpers."""
    clean_name = _validate_booking_inputs(guest_name, nights, nightly_rate)
    charges = _compute_booking_charges(nights, nightly_rate, is_member)
    confirmation = _format_booking_receipt(clean_name, nights, nightly_rate, charges)
    return {
        "guest": clean_name,
        "nights": nights,
        **charges,
        "confirmation": confirmation,
    }


if __name__ == "__main__":
    before = before_process_booking("Nadia", 3, 120.0, True)
    after = after_process_booking("Nadia", 3, 120.0, True)
    print(after["confirmation"])
    print("\nIdentical results:", before == after)
