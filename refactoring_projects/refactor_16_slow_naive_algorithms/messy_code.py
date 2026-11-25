"""Legacy telemetry analytics module — works on tiny inputs, crawls at scale.

TODO (Mission 16):
- Replace the brute-force O(n^2) nested loops in `best_profit_window` with
  Kadane's O(n) algorithm.
- Replace the O(n) linear scan in `find_sorted_timestamp` with O(log n)
  binary search.
"""


def best_profit_window(changes):
    """Return the maximum sum of any non-empty contiguous subarray of changes.

    Returns 0 if `changes` is empty.
    """
    n = len(changes)
    if n == 0:
        return 0

    # SMELL: brute-force O(n^2) nested loops checking every (start, end) window!
    res = changes[0]
    for i in range(n):
        tmp = 0
        for j in range(i, n):
            tmp = tmp + changes[j]
            if tmp > res:
                res = tmp
    return res


def find_sorted_timestamp(timestamps, target):
    """Return the index of `target` in sorted ascending `timestamps`, or -1."""
    # SMELL: linear scan ignores that `timestamps` is already sorted!
    p = -1
    for i in range(len(timestamps)):
        if timestamps[i] == target:
            p = i
            break
    return p
