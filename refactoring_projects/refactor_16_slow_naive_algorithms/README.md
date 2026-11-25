# Refactoring Mission 16 — Slow Naive Algorithms (CP 16)

## Backstory & Problem Statement

An analytics intern built a quick financial telemetry script (`messy_code.py`) to scan daily profit/loss deltas and look up events in a sorted log of Unix timestamps.

It passed every tiny smoke test with 5 to 10 items — so it shipped to production. The next morning, the dashboard ground to a halt when fed a few thousand records:

- `best_profit_window(changes)` uses a brute-force nested `O(n²)` loop to test every possible start and end index.
- `find_sorted_timestamp(timestamps, target)` ignores the fact that `timestamps` is **already sorted** and scans every single element from index `0` (`O(n)`).

Your mission: keep the exact same answers on every input, while upgrading both functions to classic fast algorithms — **Kadane's algorithm (`O(n)`)** and **binary search (`O(log n)`)**!

---

## Code Smells Checklist

- [ ] **Nested brute-force loops (`O(n²)`)** when a single-pass running best suffices (`O(n)`).
- [ ] **Ignoring sortedness (`O(n)` linear scan)** instead of halving the search space each step (`O(log n)`).
- [ ] **Cryptic variable names** (`res`, `tmp`, `i`, `j`, `p`) hiding the algorithmic invariant.
- [ ] **Missing clear edge-case guards** for empty inputs.

---

## Worked Refactoring Walkthrough (`worked_example.py`)

In `worked_example.py`, we refactor a sibling problem — finding the maximum profit from one buy and one sell in a list of daily stock prices:

### Before (`O(n²)` brute force)
```python
def before_max_profit(prices):
    best = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            diff = prices[j] - prices[i]
            if diff > best:
                best = diff
    return best
```

### After (`O(n)` single pass)
```python
def after_max_profit(prices):
    if len(prices) < 2:
        return 0
    min_price = prices[0]
    best_profit = 0
    for price in prices[1:]:
        profit = price - min_price
        if profit > best_profit:
            best_profit = profit
        if price < min_price:
            min_price = price
    return best_profit
```

Notice the key insight: instead of re-checking every earlier buy day for every sell day, we carry forward the **only summary we need** (`min_price`). Kadane's algorithm uses that exact same single-pass idea for contiguous subarray sums!

---

## Your Refactoring Mission

Refactor `messy_code.py` so **all three test classes pass**:

1. **`best_profit_window(changes)`**:
   - Return the maximum sum of any **non-empty contiguous slice** of `changes` (or `0` if `changes` is empty).
   - Replace the nested `O(n²)` loops with **Kadane's `O(n)` algorithm**:
     - Track `current_sum` (best subarray ending here: `max(change, current_sum + change)`) and `best_sum`.
   - Must contain **no nested loops** and no `sum(...)` call inside a loop.
   - Must process 3,000 items in **under `0.05s`**.

2. **`find_sorted_timestamp(timestamps, target)`**:
   - Given a sorted ascending sequence `timestamps`, return the index of `target`, or `-1` if not found.
   - Replace the linear scan with **binary search** (`lo = 0`, `hi = len(timestamps) - 1`, halving each step — or `bisect.bisect_left`).
   - Must find hits and misses in a 10,000-element sorted sequence using **logarithmic lookups** (`<= 30` element accesses).

---

## Run the Tests

```bash
python -m unittest ExamPrep/refactoring_projects/refactor_16_slow_naive_algorithms/test_refactor.py
```

When you start:
- `TestWorkedExample` -> **PASS**
- `TestBehaviorSafetyNet` -> **PASS** (your safety net!)
- `TestRefactorGoals` -> **FAIL** (your refactoring targets!)

When you finish, **all 3 test classes should be GREEN**!
