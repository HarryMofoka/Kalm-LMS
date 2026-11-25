"""Worked Example (Checkpoint 11): Coffee Roastery Supply Tracker.

A sibling reference system demonstrating safe, non-mutating dictionary merging,
atomic batch deductions, reorder threshold scanning, and inventory valuation.
"""

from __future__ import annotations


def merge_shipments(
    stock: dict[str, int],
    shipment: dict[str, int],
) -> dict[str, int]:
    """Merge an incoming supply shipment into current roastery stock.

    Neither ``stock`` nor ``shipment`` is mutated.

    Raises:
        ValueError: If any quantity in ``stock`` or ``shipment`` is negative.
    """
    for source_name, mapping in (("stock", stock), ("shipment", shipment)):
        for item, qty in mapping.items():
            if qty < 0:
                raise ValueError(
                    f"Negative quantity ({qty}) for '{item}' in {source_name}"
                )

    merged: dict[str, int] = dict(stock)
    for item, qty in shipment.items():
        merged[item] = merged.get(item, 0) + qty
    return merged


def consume_roast_batch(
    stock: dict[str, int],
    recipe: dict[str, int],
) -> dict[str, int]:
    """Deduct ingredients needed for a roast batch without mutating inputs.

    Validates all requirements up front so partial deductions can never occur.

    Raises:
        ValueError: If any recipe quantity is negative or stock is insufficient.
    """
    for item, needed in recipe.items():
        if needed < 0:
            raise ValueError(f"Recipe quantity for '{item}' cannot be negative")
        available = stock.get(item, 0)
        if available < needed:
            raise ValueError(
                f"Insufficient '{item}': need {needed}, have {available}"
            )

    updated: dict[str, int] = dict(stock)
    for item, needed in recipe.items():
        updated[item] = updated.get(item, 0) - needed
    return updated


def find_reorder_items(
    stock: dict[str, int],
    reorder_points: dict[str, int],
) -> list[str]:
    """Return sorted ingredient names strictly below their reorder point.

    Ingredients absent from ``stock`` are treated as having quantity 0.
    """
    alerts = [
        item
        for item, min_qty in reorder_points.items()
        if stock.get(item, 0) < min_qty
    ]
    return sorted(alerts)


def compute_supply_valuation(
    stock: dict[str, int],
    unit_costs: dict[str, float],
) -> float:
    """Calculate total monetary valuation of roastery stock (rounded to 2 dp).

    Raises:
        ValueError: If a quantity is negative, a stocked item has no unit cost,
            or a unit cost is negative.
    """
    total = 0.0
    for item, qty in stock.items():
        if qty < 0:
            raise ValueError(f"Negative stock quantity ({qty}) for '{item}'")
        if qty == 0:
            continue
        if item not in unit_costs:
            raise ValueError(f"Missing unit cost for stocked item '{item}'")
        cost = unit_costs[item]
        if cost < 0:
            raise ValueError(f"Negative unit cost ({cost}) for '{item}'")
        total += qty * cost
    return round(total, 2)


if __name__ == "__main__":
    opening_stock = {
        "ethiopia_yirgacheffe_kg": 18,
        "colombia_supremo_kg": 25,
        "oat_milk_cartons": 12,
    }
    morning_shipment = {
        "ethiopia_yirgacheffe_kg": 10,
        "brazil_santos_kg": 30,
    }
    espresso_blend_recipe = {
        "colombia_supremo_kg": 15,
        "brazil_santos_kg": 22,
    }
    reorder_points = {
        "ethiopia_yirgacheffe_kg": 15,
        "colombia_supremo_kg": 12,
        "brazil_santos_kg": 10,
        "oat_milk_cartons": 12,
        "paper_filters_box": 5,
    }
    unit_costs = {
        "ethiopia_yirgacheffe_kg": 14.50,
        "colombia_supremo_kg": 11.75,
        "brazil_santos_kg": 9.80,
        "oat_milk_cartons": 2.40,
    }

    after_delivery = merge_shipments(opening_stock, morning_shipment)
    after_roast = consume_roast_batch(after_delivery, espresso_blend_recipe)
    reorders = find_reorder_items(after_roast, reorder_points)
    valuation = compute_supply_valuation(after_roast, unit_costs)

    print("=== Coffee Roastery Supply Tracker ===")
    print("Opening stock (unchanged):", opening_stock)
    print("After morning delivery:   ", after_delivery)
    print("After espresso roast:     ", after_roast)
    print("Reorder alerts:           ", reorders)
    print(f"Total supply valuation:   ${valuation:,.2f}")
