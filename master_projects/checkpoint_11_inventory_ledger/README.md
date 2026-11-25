# Checkpoint 11 — Multi-Warehouse Inventory Ledger

- **Unlocked After:** Activity 066 — Dictionaries & Safe Merging
- **Difficulty:** Intermediate
- **Core Concepts:** Dictionaries, defensive copying (non-mutating updates), atomic validation, threshold filtering, monetary valuation

---

## Real-World Value

Every modern e-commerce platform and retail ERP — **Shopify Fulfillment**, **Takealot**, **Amazon FBA**, and warehouse management systems (WMS) — must reconcile stock levels across multiple fulfillment centers in real time.

When two warehouses report stock simultaneously, or an order attempts to dispatch more units than actually exist on a shelf, sloppy dictionary mutations cause **phantom inventory**, **overselling**, and **corrupted audit trails**. The exact patterns in this checkpoint (pure dictionary merges, atomic stock deltas, safe inter-warehouse transfers, and automated low-stock alerts) appear constantly in backend production code and technical take-home interviews.

---

## Problem Statement

You are building the core inventory ledger module for a multi-warehouse retail backend. Given dictionaries mapping product SKUs (`str`) to unit counts (`int`), your engine must:

1. Safely merge stock from two warehouses without mutating either input.
2. Apply restock/dispatch deltas **atomically** — rejecting the entire batch if any SKU would drop below zero.
3. Transfer stock between a source and destination warehouse while preserving input immutability.
4. Generate alphabetically sorted low-stock reorder alerts against per-SKU minimum thresholds.
5. Compute accurate total inventory valuation against a unit price catalog.

---

## How a Similar Functioning System Was Done (`worked_example.py`)

Before writing your own module, inspect and run the sibling system in [`worked_example.py`](./worked_example.py): a **Coffee Roastery Supply Tracker**.

Run it from `ExamPrep/`:

```bash
python master_projects/checkpoint_11_inventory_ledger/worked_example.py
```

### Architecture & Key Patterns Demonstrated

1. **Non-Mutating Dictionary Merging (`merge_shipments`)**:
   - Copies the base `stock` dictionary first (`merged = dict(stock)`), validates every quantity is non-negative, and accumulates shipment counts using `merged.get(item, 0) + qty`.
   - Callers can safely keep historical snapshots without accidental aliasing bugs.
2. **Atomic Validation Before Mutation (`consume_roast_batch`)**:
   - Checks every ingredient in `recipe` *before* constructing the updated state. If even one bean variety is short, it raises `ValueError` immediately so partial deductions never happen.
3. **Boundary-Aware Threshold Alerts (`find_reorder_items`)**:
   - Iterates over `reorder_points` (not `stock`!) so an ingredient completely missing from `stock` is treated as `0` units and still triggers a reorder alert.
   - Uses strict `<` comparison (`current < threshold`): having stock *equal* to the reorder point is considered stocked; dipping below it triggers an alert.
4. **Validated Financial Valuation (`compute_supply_valuation`)**:
   - Multiplies quantities by unit costs, validates that every stocked item (`qty > 0`) has a known non-negative cost, and rounds the final sum to 2 decimal places (`round(total, 2)`).

---

## Your Project Brief (`project.py`)

Implement the five functions in [`project.py`](./project.py):

### 1. `merge_warehouses(wh1: dict[str, int], wh2: dict[str, int]) -> dict[str, int]`
- Returns a **new** dictionary combining all SKUs from `wh1` and `wh2`, summing quantities when a SKU appears in both.
- **Must not mutate** `wh1` or `wh2`.
- Raises `ValueError` if any quantity in `wh1` or `wh2` is negative (`< 0`).

```python
merge_warehouses({"SKU-A": 10, "SKU-B": 4}, {"SKU-B": 6, "SKU-C": 2})
# -> {"SKU-A": 10, "SKU-B": 10, "SKU-C": 2}
```

### 2. `apply_stock_delta(inventory: dict[str, int], deltas: dict[str, int]) -> dict[str, int]`
- Applies positive (restock) and negative (dispatch/sale) changes from `deltas` to `inventory` and returns a **new** dictionary.
- SKUs present in `deltas` but absent from `inventory` start at `0`.
- Keep SKUs whose resulting quantity is `0` in the returned dictionary.
- **Atomic rule:** If any resulting stock quantity would be `< 0`, raise `ValueError`.
- **Must not mutate** `inventory` or `deltas`.

```python
apply_stock_delta({"SKU-A": 5}, {"SKU-A": -5, "SKU-B": 3})
# -> {"SKU-A": 0, "SKU-B": 3}

apply_stock_delta({"SKU-A": 5}, {"SKU-A": -6})
# -> raises ValueError
```

### 3. `transfer_stock(source: dict[str, int], dest: dict[str, int], sku: str, qty: int) -> tuple[dict[str, int], dict[str, int]]`
- Transfers `qty` units of `sku` from `source` to `dest`, returning `(new_source, new_dest)`.
- Raises `ValueError` if `qty <= 0` or if `source.get(sku, 0) < qty`.
- If `sku` does not yet exist in `dest`, initializes it to `qty`.
- **Must not mutate** `source` or `dest`.

```python
transfer_stock({"SKU-A": 10}, {"SKU-B": 2}, "SKU-A", 4)
# -> ({"SKU-A": 6}, {"SKU-B": 2, "SKU-A": 4})
```

### 4. `low_stock_alerts(inventory: dict[str, int], thresholds: dict[str, int]) -> list[str]`
- Inspects every `sku, min_qty` pair in `thresholds`.
- Flags `sku` if `inventory.get(sku, 0) < min_qty` (missing SKUs count as `0`; stock equal to `min_qty` is **not** flagged).
- Returns the flagged SKUs sorted alphabetically (`list[str]`).

```python
low_stock_alerts({"SKU-B": 3, "SKU-A": 5}, {"SKU-B": 5, "SKU-A": 5, "SKU-C": 1})
# -> ["SKU-B", "SKU-C"]
```

### 5. `inventory_valuation(inventory: dict[str, int], unit_prices: dict[str, float]) -> float`
- Computes total inventory value: $\sum (\text{qty} \times \text{unit\_price})$, rounded to 2 decimal places (`round(total, 2)`).
- Returns `0.0` for an empty inventory.
- Raises `ValueError` if:
  - any quantity in `inventory` is `< 0`,
  - a SKU with `qty > 0` is missing from `unit_prices`, or
  - a used unit price is `< 0`.

---

## Running the Tests

From inside the `ExamPrep/` directory:

```bash
python -m unittest master_projects/checkpoint_11_inventory_ledger/test_project.py -v
```

- `TestWorkedExample` tests pass immediately so you can study the verified reference system.
- `TestMasterProject` tests fail initially and turn green as you build `project.py`.
