"""Worked Example for CP 12: Replacing O(n^2) nested loops with O(n) sets.

Compare:
- ``before_common_users``: O(n * m) nested loop + list deduplication.
- ``after_common_users``: O(n + m) set intersection.
"""

import time
from typing import List, Sequence


def before_common_users(group_a: Sequence[str], group_b: Sequence[str]) -> List[str]:
    """Sluggish O(n * m) nested-loop scan to find shared usernames."""
    common: List[str] = []
    for user in group_a:
        for other in group_b:
            if user == other and user not in common:
                common.append(user)
    return sorted(common)


def after_common_users(group_a: Sequence[str], group_b: Sequence[str]) -> List[str]:
    """Clean O(n + m) set intersection."""
    return sorted(set(group_a) & set(group_b))


if __name__ == "__main__":
    a = [f"u_{i}" for i in range(1200)]
    b = [f"u_{i}" for i in range(600, 1800)]

    t0 = time.perf_counter()
    res_before = before_common_users(a, b)
    t_before = time.perf_counter() - t0

    t0 = time.perf_counter()
    res_after = after_common_users(a, b)
    t_after = time.perf_counter() - t0

    print(f"Matched count: {len(res_after)}, identical: {res_before == res_after}")
    print(f"Before: {t_before:.4f}s | After: {t_after:.5f}s")
