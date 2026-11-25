"""Worked Example for Refactor 03: Library Borrowing Eligibility Checker.

Compares a 6-level deep arrow anti-pattern (`before_can_borrow`) with a clean,
flat guard-clause implementation (`after_can_borrow`).
"""

# ---------------------------------------------------------------------------
# BEFORE: 6-level nested if/else pyramid (the "Arrow Anti-Pattern")
# ---------------------------------------------------------------------------


def before_can_borrow(
    has_card,
    is_suspended,
    late_fees,
    active_loans,
    book_available,
    is_reference_only,
):
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


# ---------------------------------------------------------------------------
# AFTER: Flat guard clauses — maximum nesting depth is 1!
# ---------------------------------------------------------------------------


def after_can_borrow(
    has_card,
    is_suspended,
    late_fees,
    active_loans,
    book_available,
    is_reference_only,
):
    """Determine whether a library patron can borrow a specific book."""
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


if __name__ == "__main__":
    sample_cases = [
        (False, False, 0, 0, True, False),
        (True, True, 0, 0, True, False),
        (True, False, 15.0, 2, True, False),
        (True, False, 0, 5, True, False),
        (True, False, 0, 2, False, False),
        (True, False, 0, 2, True, True),
        (True, False, 0, 2, True, False),
    ]
    for case in sample_cases:
        print(
            f"{case} -> before={before_can_borrow(*case)!r} | "
            f"after={after_can_borrow(*case)!r}"
        )
