"""Worked Example — Username & Handle Compliance Auditor.

Demonstrates strict input type guards, non-short-circuiting multi-rule
validation, machine-readable error codes, and deterministic compliance scoring.
"""

from __future__ import annotations

from typing import Any

MIN_HANDLE_LENGTH: int = 3
MAX_HANDLE_LENGTH: int = 20
RESERVED_HANDLES: frozenset[str] = frozenset(
    {"admin", "root", "support", "system", "moderator"}
)


def audit_username(username: str) -> dict[str, Any]:
    """Audit a candidate username against platform handle compliance policies.

    Rules:
        1. Must be a str (raises TypeError otherwise).
        2. Length between 3 and 20 characters inclusive.
        3. Must start with an alphabetic letter.
        4. Only alphanumeric characters and underscores allowed.
        5. Must not contain consecutive underscores ('__').
        6. Must not match a reserved platform handle (case-insensitive).

    Returns:
        Dict with keys {"valid": bool, "score": int, "errors": list[str]}.
    """
    if not isinstance(username, str):
        raise TypeError(f"Username must be a str, got {type(username).__name__}.")

    errors: list[str] = []

    if len(username) < MIN_HANDLE_LENGTH:
        errors.append("too_short")
    if len(username) > MAX_HANDLE_LENGTH:
        errors.append("too_long")
    if not username or not username[0].isalpha():
        errors.append("must_start_with_letter")
    if not all(ch.isalnum() or ch == "_" for ch in username):
        errors.append("invalid_characters")
    if "__" in username:
        errors.append("consecutive_underscores")
    if username.lower() in RESERVED_HANDLES:
        errors.append("reserved_handle")

    score = max(0, 100 - len(errors) * 25)
    return {
        "valid": len(errors) == 0,
        "score": score,
        "errors": errors,
    }


if __name__ == "__main__":
    samples = ["dev_jane99", "Admin", "1a__!", "x", "this_handle_is_far_too_long_to_pass"]
    print(f"{'Candidate':<36} | {'Valid':<5} | {'Score':>5} | Errors")
    print("-" * 85)
    for candidate in samples:
        report = audit_username(candidate)
        print(
            f"{candidate:<36} | {str(report['valid']):<5} | "
            f"{report['score']:>5} | {report['errors']}"
        )
