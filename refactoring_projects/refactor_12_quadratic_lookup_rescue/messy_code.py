"""Messy Access Log Auditor — Refactoring Target for Mission 12.

PROBLEM:
``audit_access_logs`` computes ``unauthorized``, ``duplicates``, and
``active_allowed`` using quadratic ``O(n^2)`` list scans:
- ``u not in allowed_users`` inside a loop,
- ``seen_users.count(u) > 1`` inside a loop, and
- a double ``for`` loop comparing ``allowed_users`` against ``seen_users``!

YOUR GOAL:
Refactor ``audit_access_logs`` to use ``set`` / ``dict`` (or ``Counter``)
for ``O(n)`` performance without changing the output format.
"""

from typing import Dict, List, Sequence


def audit_access_logs(
    allowed_users: Sequence[str],
    seen_users: Sequence[str],
) -> Dict[str, List[str]]:
    """Audit badge access logs (sluggish O(n^2) list-scanning version!)."""
    unauthorized: List[str] = []
    for user in seen_users:
        if user not in allowed_users and user not in unauthorized:
            unauthorized.append(user)

    duplicates: List[str] = []
    for user in seen_users:
        if seen_users.count(user) > 1 and user not in duplicates:
            duplicates.append(user)

    active_allowed: List[str] = []
    for allowed_user in allowed_users:
        for seen_user in seen_users:
            if allowed_user == seen_user:
                if allowed_user not in active_allowed:
                    active_allowed.append(allowed_user)
                break

    return {
        "unauthorized": sorted(unauthorized),
        "duplicates": sorted(duplicates),
        "active_allowed": sorted(active_allowed),
    }
