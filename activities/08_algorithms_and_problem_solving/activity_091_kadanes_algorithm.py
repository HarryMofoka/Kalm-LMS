"""
Activity 091 — Kadane's Algorithm
Difficulty: 91 / 132

Context:
    A classic single-pass dynamic programming gem! Whether you are finding the
    best single buy/sell stock profit or the maximum-sum contiguous subarray,
    you never need nested loops — tracking the best value ending right HERE
    solves both in O(n) time and O(1) space.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Implement `example_max_stock_profit(prices)` returning the maximum profit
    achievable from ONE buy followed later by ONE sell (`0` if prices only
    decrease or fewer than 2 prices are given).

Step-by-Step Explanation:
    1. If `len(prices) < 2`, no buy-then-sell pair exists -> return `0`.
    2. Track `min_price = prices[0]` (cheapest day seen so far) and
       `best_profit = 0`.
    3. For each subsequent `price` in `prices[1:]`:
       - Selling today earns `price - min_price`.
       - Update `best_profit = max(best_profit, price - min_price)`.
       - Update `min_price = min(min_price, price)`.
    4. Return `best_profit`.

Edge Cases:
    - `[]` or `[10]` -> `0`
    - Strictly decreasing `[9, 7, 4, 1]` -> `0` (better not to trade!)
    - `[7, 1, 5, 3, 6, 4]` -> `5` (buy at `1`, sell at `6`)

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem:
    Implement `solve_max_subarray_sum(numbers)` using **Kadane's algorithm**:
    Return the maximum sum of any **non-empty** contiguous subarray of `numbers`
    (return `0` ONLY when `numbers` itself is empty `[]`).

Rules & The All-Negatives Trap:
    1. If `not numbers`: return `0`.
    2. Initialize BOTH `current_sum = numbers[0]` AND `best_sum = numbers[0]`
       (NEVER initialize `best_sum = 0`, because that fails on all-negative
       lists like `[-5, -2, -8]` where the right answer is `-2`, NOT `0`!).
    3. For each `num` in `numbers[1:]`:
       - Either start fresh at `num`, or extend the previous subarray:
         `current_sum = max(num, current_sum + num)`
       - Update `best_sum = max(best_sum, current_sum)`.
    4. Return `best_sum`.

Examples:
    solve_max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) -> 6   ([4, -1, 2, 1])
    solve_max_subarray_sum([-5, -2, -8])                    -> -2  ([-2])
    solve_max_subarray_sum([5])                             -> 5
    solve_max_subarray_sum([])                              -> 0
"""

from __future__ import annotations


def example_max_stock_profit(prices: list[int | float]) -> int | float:
    """Return the maximum profit from one buy followed by one sell."""
    if len(prices) < 2:
        return 0

    min_price = prices[0]
    best_profit: int | float = 0
    for price in prices[1:]:
        profit = price - min_price
        if profit > best_profit:
            best_profit = profit
        if price < min_price:
            min_price = price
    return best_profit


def solve_max_subarray_sum(numbers: list[int]) -> int:
    """Return the maximum sum of a non-empty contiguous subarray (0 if empty)."""
    pass


if __name__ == "__main__":
    print("Profit on [7, 1, 5, 3, 6, 4]:", example_max_stock_profit([7, 1, 5, 3, 6, 4]))
    print("Profit on [9, 7, 4, 1]:", example_max_stock_profit([9, 7, 4, 1]))
