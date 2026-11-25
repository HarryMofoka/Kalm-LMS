"""Worked Example (RF 16): O(n^2) brute-force stock profit -> O(n) single pass.

Compare `before_max_profit` (checks every buy/sell pair) with `after_max_profit`
(tracks the lowest price seen so far in a single pass).
"""

from time import perf_counter


def before_max_profit(prices):
    """Brute-force O(n^2): tries every possible (buy_day, sell_day) pair."""
    best = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            diff = prices[j] - prices[i]
            if diff > best:
                best = diff
    return best


def after_max_profit(prices):
    """Clean O(n) single pass: remembers the lowest buy price seen so far."""
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


if __name__ == "__main__":
    sample = [7, 1, 5, 3, 6, 4]
    print("Sample prices:", sample)
    print("before_max_profit:", before_max_profit(sample))
    print("after_max_profit: ", after_max_profit(sample))

    big_prices = [(i * 37) % 500 for i in range(2500)]
    t0 = perf_counter()
    res_before = before_max_profit(big_prices)
    dt_before = perf_counter() - t0

    t0 = perf_counter()
    res_after = after_max_profit(big_prices)
    dt_after = perf_counter() - t0

    print(f"\nOn {len(big_prices)} prices:")
    print(f"  Before O(n^2): result={res_before}, time={dt_before:.4f}s")
    print(f"  After  O(n):   result={res_after}, time={dt_after:.6f}s")
