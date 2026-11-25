"""Master Project (Checkpoint 11): Multi-Warehouse Inventory Ledger.

Implement the five functions below according to the specification in README.md.
Run tests from ExamPrep/ with:
    python -m unittest master_projects/checkpoint_11_inventory_ledger/test_project.py -v
"""

from __future__ import annotations


def merge_warehouses(
    wh1: dict[str, int],
    wh2: dict[str, int],
) -> dict[str, int]:
    """Combine stock counts from two warehouses into a new dictionary.

    Shared SKUs have their quantities summed; unique SKUs from either warehouse
    are preserved. Neither ``wh1`` nor ``wh2`` may be mutated.

    Args:
        wh1: Mapping of SKU -> quantity for the first warehouse.
        wh2: Mapping of SKU -> quantity for the second warehouse.

    Returns:
        A new dictionary with combined SKU quantities.

    Raises:
        ValueError: If any quantity in ``wh1`` or ``wh2`` is negative.
    """
    pass


def apply_stock_delta(
    inventory: dict[str, int],
    deltas: dict[str, int],
) -> dict[str, int]:
    """Apply restock (+) and dispatch (-) deltas to an inventory snapshot.

    Missing SKUs in ``inventory`` start from 0. SKUs whose resulting count is 0
    remain in the returned dictionary. Neither input dictionary may be mutated.

    Args:
        inventory: Current mapping of SKU -> quantity.
        deltas: Mapping of SKU -> signed quantity change.

    Returns:
        A new dictionary reflecting all applied deltas.

    Raises:
        ValueError: If any SKU's resulting quantity would be negative.
    """
    pass


def transfer_stock(
    source: dict[str, int],
    dest: dict[str, int],
    sku: str,
    qty: int,
) -> tuple[dict[str, int], dict[str, int]]:
    """Transfer ``qty`` units of ``sku`` from ``source`` to ``dest``.

    Neither ``source`` nor ``dest`` may be mutated.

    Args:
        source: Source warehouse inventory mapping.
        dest: Destination warehouse inventory mapping.
        sku: Product SKU identifier to transfer.
        qty: Positive integer quantity to transfer.

    Returns:
        A tuple ``(new_source, new_dest)`` with updated stock dictionaries.

    Raises:
        ValueError: If ``qty <= 0`` or ``source`` has fewer than ``qty`` units
            of ``sku``.
    """
    pass


def low_stock_alerts(
    inventory: dict[str, int],
    thresholds: dict[str, int],
) -> list[str]:
    """Return alphabetically sorted SKUs strictly below their minimum threshold.

    SKUs present in ``thresholds`` but absent from ``inventory`` are treated
    as having 0 units in stock.

    Args:
        inventory: Current mapping of SKU -> quantity.
        thresholds: Mapping of SKU -> minimum acceptable stock level.

    Returns:
        Alphabetically sorted list of SKUs where ``stock < threshold``.
    """
    pass


def inventory_valuation(
    inventory: dict[str, int],
    unit_prices: dict[str, float],
) -> float:
    """Compute total monetary value of ``inventory``, rounded to 2 decimals.

    Args:
        inventory: Mapping of SKU -> quantity.
        unit_prices: Mapping of SKU -> unit price.

    Returns:
        Total valuation as a float rounded to 2 decimal places (``0.0`` when
        inventory is empty).

    Raises:
        ValueError: If any quantity is negative, any stocked SKU (``qty > 0``)
            is missing from ``unit_prices``, or any used unit price is negative.
    """
    pass
