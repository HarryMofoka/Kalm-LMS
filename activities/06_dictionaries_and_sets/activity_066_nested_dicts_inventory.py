"""
Activity 066: Nested Dictionaries & Inventory Math  [Unlocks Checkpoint 11!]
Difficulty: 66 / 132

Context:
    Real applications store structured records as nested dictionaries—like a
    product catalog mapping item names to `{"price": ..., "stock": ...}`. Watch
    out for shallow copies: `dict(inventory)` copies ONLY the outer dictionary,
    so mutating an inner item dict would still corrupt the caller's inventory!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Total Shopping Cart Value
===============================================================================
Problem:
    Given:
      - `catalog`: `{item_name: {"price": float, "stock": int}}`
      - `cart`: `{item_name: quantity}`
    Return the total cost of valid items in `cart`, rounded to 2 decimal places.
    Ignore any item in `cart` that is missing from `catalog` or has `quantity <= 0`.

Step-by-Step Explanation:
    1. Initialize `total = 0.0`.
    2. Iterate `for item, qty in cart.items():`.
    3. Skip if `qty <= 0` or `item not in catalog`.
    4. Multiply `catalog[item]["price"] * qty`, add to `total`, and return
       `round(total, 2)` to eliminate binary floating-point dust.

Edge Cases:
    - Unknown item in `cart` is safely ignored (no `KeyError`).
    - Negative or zero quantity in `cart` is ignored.
    - Empty `cart` returns `0.0`.

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Apply Stock Updates & Report Out-of-Stock Items
===============================================================================
Problem:
    Implement `solve_apply_stock_updates(inventory: dict[str, dict[str, int]], deltas: dict[str, int]) -> tuple[dict[str, dict[str, int]], list[str]]`.
    Given:
      - `inventory`: nested dict mapping item names to detail dicts containing
        at least `"stock"` (e.g., `{"pen": {"stock": 5, "price": 2}}`),
      - `deltas`: dict mapping item names to integer stock adjustments
        (positive = restock, negative = units sold/removed).
    Perform the following WITHOUT mutating `inventory` OR any of its inner dicts:
      1. Create a fresh copy of `inventory` where each inner dict is also copied
         (e.g., `{name: dict(details) for name, details in inventory.items()}`).
      2. For each `item, change` in `deltas.items()`:
           - If `item` exists in the updated inventory, set its `"stock"` to
             `max(0, current_stock + change)` (stock NEVER goes negative!).
           - Ignore items in `deltas` that do not exist in `inventory`.
      3. Collect a **sorted** list of all item names in the updated inventory
         whose final `"stock"` equals `0`.
      4. Return `(updated_inventory, out_of_stock_items)`.

Examples:
    - `inventory = {"pen": {"stock": 5}, "book": {"stock": 2}, "eraser": {"stock": 0}}`
      `deltas    = {"pen": -5, "book": 3, "eraser": -2, "ghost": 10}`
      -> `({"pen": {"stock": 0}, "book": {"stock": 5}, "eraser": {"stock": 0}}, ["eraser", "pen"])`
    - `inventory = {"pen": {"stock": 3, "price": 2}}`, `deltas = {"pen": -10}`
      -> `({"pen": {"stock": 0, "price": 2}}, ["pen"])`  (extra keys like `"price"` preserved!)
    - `inventory = {}`, `deltas = {"pen": 5}`
      -> `({}, [])`

Edge-Case Hints:
    - Notice `dict(inventory)` alone is a SHALLOW copy! If you then wrote
      `updated[item]["stock"] = ...`, you'd mutate `inventory[item]["stock"]` too!
      Copying each inner dict (`dict(details)`) keeps the input 100% untouched.
    - Don't forget to check items that were ALREADY at `0` stock even if they
      weren't mentioned in `deltas`—they still belong in `out_of_stock_items`!
"""

from __future__ import annotations


def example_cart_total(
    catalog: dict[str, dict[str, int | float]],
    cart: dict[str, int],
) -> float:
    """Calculate the total price of valid items in `cart`, rounded to 2 decimals."""
    total = 0.0
    for item, qty in cart.items():
        if qty > 0 and item in catalog:
            total += catalog[item]["price"] * qty
    return round(total, 2)


def solve_apply_stock_updates(
    inventory: dict[str, dict[str, int]],
    deltas: dict[str, int],
) -> tuple[dict[str, dict[str, int]], list[str]]:
    """Apply stock deltas safely (clamping at 0) and return `(updated_inv, sorted_oos)`."""
    pass


if __name__ == "__main__":
    store = {
        "apple": {"price": 1.25, "stock": 10},
        "bread": {"price": 2.50, "stock": 5},
    }
    basket = {"apple": 4, "bread": 1, "unicorn": 2}
    print("Cart total: $", example_cart_total(store, basket))
