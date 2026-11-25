"""Worked Example for Refactor 04: Security Access Checker.

Demonstrates turning redundant `== True`/`== False` checks and tangled boolean
flags (`before_has_access`) into a concise boolean expression (`after_has_access`).
"""

# ---------------------------------------------------------------------------
# BEFORE: Boolean soup — `== True`, `== False`, flag juggling, redundant return
# ---------------------------------------------------------------------------


def before_has_access(is_admin, is_active, has_badge, is_locked_out):
    allowed = False
    if is_active == True:  # noqa: E712
        if is_locked_out == False:  # noqa: E712
            if is_admin == True:  # noqa: E712
                allowed = True
            else:
                if has_badge == True:  # noqa: E712
                    allowed = True
                else:
                    allowed = False
        else:
            allowed = False
    else:
        allowed = False

    if allowed == True:  # noqa: E712
        return True
    else:
        return False


# ---------------------------------------------------------------------------
# AFTER: Direct, self-documenting boolean expression
# ---------------------------------------------------------------------------


def after_has_access(is_admin, is_active, has_badge, is_locked_out):
    """Return True if an active, unlocked user is an admin or holds a badge."""
    account_in_good_standing = is_active and not is_locked_out
    has_credentials = is_admin or has_badge
    return account_in_good_standing and has_credentials


if __name__ == "__main__":
    test_cases = [
        (True, True, False, False),
        (False, True, True, False),
        (True, True, True, True),
        (False, True, False, False),
        (True, False, True, False),
    ]
    for case in test_cases:
        print(
            f"{case} -> before={before_has_access(*case)} | "
            f"after={after_has_access(*case)}"
        )
