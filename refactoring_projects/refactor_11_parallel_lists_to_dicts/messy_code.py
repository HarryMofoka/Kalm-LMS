"""Messy Tuck-Shop POS System — Refactoring Target for Mission 11.

PROBLEM:
``process_tuckshop_orders`` explodes ``catalog_items`` into three fragile
parallel lists (``names``, ``prices``, ``stocks``) and performs an ``O(N)``
``for i in range(len(names)):`` linear scan for EVERY single order!

YOUR GOAL:
Replace the parallel lists and index scanning with a clean dictionary lookup
so that the code is safer, shorter, and handles 2,000 items x 2,000 orders
in well under 0.08 seconds.
"""

from typing import Dict, List, Sequence, Tuple, Union

CatalogItem = Tuple[str, float, int]
Order = Tuple[str, int]
OrderSummary = Dict[str, Union[float, int, List[Tuple[str, int, str]], Dict[str, int]]]


def process_tuckshop_orders(
    catalog_items: Sequence[CatalogItem],
    orders: Sequence[Order],
) -> OrderSummary:
    """Process tuck-shop orders against a catalog (parallel-list version!)."""
    names: List[str] = []
    prices: List[float] = []
    stocks: List[int] = []

    for item_name, unit_price, initial_stock in catalog_items:
        names.append(item_name)
        prices.append(unit_price)
        stocks.append(initial_stock)

    total_revenue = 0.0
    fulfilled_count = 0
    rejected: List[Tuple[str, int, str]] = []

    for order_item, qty in orders:
        found_idx = -1
        for i in range(len(names)):
            if names[i] == order_item:
                found_idx = i
                break

        if found_idx == -1:
            rejected.append((order_item, qty, "unknown_item"))
        elif qty <= 0:
            rejected.append((order_item, qty, "invalid_quantity"))
        elif stocks[found_idx] < qty:
            rejected.append((order_item, qty, "insufficient_stock"))
        else:
            stocks[found_idx] = stocks[found_idx] - qty
            total_revenue = total_revenue + (prices[found_idx] * qty)
            fulfilled_count = fulfilled_count + 1

    remaining_stock: Dict[str, int] = {}
    for i in range(len(names)):
        remaining_stock[names[i]] = stocks[i]

    return {
        "total_revenue": round(total_revenue, 2),
        "fulfilled_count": fulfilled_count,
        "rejected": rejected,
        "remaining_stock": remaining_stock,
    }
