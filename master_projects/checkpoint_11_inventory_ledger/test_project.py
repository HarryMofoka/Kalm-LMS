"""Unit tests for Checkpoint 11: Multi-Warehouse Inventory Ledger."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from master_projects.checkpoint_11_inventory_ledger import project, worked_example


class TestWorkedExample(unittest.TestCase):
    """Verify the Coffee Roastery Supply Tracker reference implementation."""

    def test_merge_shipments_sums_and_preserves_inputs(self) -> None:
        stock = {"ethiopia": 10, "colombia": 5}
        shipment = {"colombia": 7, "brazil": 12}
        merged = worked_example.merge_shipments(stock, shipment)

        self.assertEqual(merged, {"ethiopia": 10, "colombia": 12, "brazil": 12})
        self.assertEqual(stock, {"ethiopia": 10, "colombia": 5})
        self.assertEqual(shipment, {"colombia": 7, "brazil": 12})

    def test_merge_shipments_rejects_negative_quantities(self) -> None:
        with self.assertRaises(ValueError):
            worked_example.merge_shipments({"ethiopia": 5}, {"ethiopia": -1})

    def test_consume_roast_batch_deducts_atomically(self) -> None:
        stock = {"ethiopia": 10, "brazil": 4}
        after = worked_example.consume_roast_batch(stock, {"ethiopia": 6, "brazil": 4})
        self.assertEqual(after, {"ethiopia": 4, "brazil": 0})
        self.assertEqual(stock, {"ethiopia": 10, "brazil": 4})

        with self.assertRaises(ValueError):
            worked_example.consume_roast_batch(stock, {"ethiopia": 2, "brazil": 5})
        self.assertEqual(stock, {"ethiopia": 10, "brazil": 4})

    def test_find_reorder_items_sorted_and_handles_missing(self) -> None:
        stock = {"beans_a": 10, "beans_b": 4}
        reorder_points = {"beans_c": 1, "beans_b": 5, "beans_a": 10}
        self.assertEqual(
            worked_example.find_reorder_items(stock, reorder_points),
            ["beans_b", "beans_c"],
        )

    def test_compute_supply_valuation_and_missing_cost(self) -> None:
        stock = {"ethiopia": 3, "brazil": 2, "empty_item": 0}
        costs = {"ethiopia": 12.335, "brazil": 10.0}
        self.assertEqual(worked_example.compute_supply_valuation(stock, costs), 57.01)

        with self.assertRaises(ValueError):
            worked_example.compute_supply_valuation({"unknown": 1}, costs)


class TestMasterProject(unittest.TestCase):
    """Tests for the student's Multi-Warehouse Inventory Ledger."""

    def test_merge_warehouses_sums_and_preserves_inputs(self) -> None:
        jhb = {"SKU-100": 15, "SKU-200": 8}
        cpt = {"SKU-200": 12, "SKU-300": 5}
        merged = project.merge_warehouses(jhb, cpt)

        self.assertEqual(merged, {"SKU-100": 15, "SKU-200": 20, "SKU-300": 5})
        self.assertEqual(jhb, {"SKU-100": 15, "SKU-200": 8})
        self.assertEqual(cpt, {"SKU-200": 12, "SKU-300": 5})
        self.assertEqual(project.merge_warehouses({}, {}), {})

    def test_merge_warehouses_rejects_negative_stock(self) -> None:
        with self.assertRaises(ValueError):
            project.merge_warehouses({"SKU-100": -1}, {"SKU-200": 3})
        with self.assertRaises(ValueError):
            project.merge_warehouses({"SKU-100": 5}, {"SKU-200": -2})

    def test_apply_stock_delta_updates_and_rejects_negative_result(self) -> None:
        inv = {"SKU-A": 10, "SKU-B": 3}
        deltas = {"SKU-A": -4, "SKU-B": -3, "SKU-C": 7}
        updated = project.apply_stock_delta(inv, deltas)

        self.assertEqual(updated, {"SKU-A": 6, "SKU-B": 0, "SKU-C": 7})
        self.assertEqual(inv, {"SKU-A": 10, "SKU-B": 3})
        self.assertEqual(deltas, {"SKU-A": -4, "SKU-B": -3, "SKU-C": 7})

        with self.assertRaises(ValueError):
            project.apply_stock_delta(inv, {"SKU-A": 5, "SKU-B": -4})
        self.assertEqual(inv, {"SKU-A": 10, "SKU-B": 3})

    def test_transfer_stock_success_and_validation(self) -> None:
        source = {"SKU-A": 10, "SKU-B": 2}
        dest = {"SKU-B": 5}
        result = project.transfer_stock(source, dest, "SKU-A", 4)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        new_src, new_dst = result

        self.assertEqual(new_src, {"SKU-A": 6, "SKU-B": 2})
        self.assertEqual(new_dst, {"SKU-B": 5, "SKU-A": 4})
        self.assertEqual(source, {"SKU-A": 10, "SKU-B": 2})
        self.assertEqual(dest, {"SKU-B": 5})

        with self.assertRaises(ValueError):
            project.transfer_stock(source, dest, "SKU-A", 0)
        with self.assertRaises(ValueError):
            project.transfer_stock(source, dest, "SKU-A", -3)
        with self.assertRaises(ValueError):
            project.transfer_stock(source, dest, "SKU-B", 3)
        with self.assertRaises(ValueError):
            project.transfer_stock(source, dest, "SKU-MISSING", 1)

    def test_low_stock_alerts_sorted_and_handles_missing_and_boundary(self) -> None:
        inventory = {"SKU-Z": 2, "SKU-M": 10, "SKU-A": 0}
        thresholds = {
            "SKU-Z": 5,
            "SKU-M": 10,  # Equal to threshold -> NOT low stock
            "SKU-A": 1,
            "SKU-B": 3,   # Missing from inventory -> treated as 0 -> low stock
        }
        self.assertEqual(
            project.low_stock_alerts(inventory, thresholds),
            ["SKU-A", "SKU-B", "SKU-Z"],
        )

    def test_inventory_valuation_accuracy_and_validation(self) -> None:
        inventory = {"SKU-A": 3, "SKU-B": 2, "SKU-ZERO": 0}
        prices = {"SKU-A": 19.99, "SKU-B": 4.50}
        self.assertEqual(project.inventory_valuation(inventory, prices), 68.97)
        self.assertEqual(project.inventory_valuation({}, prices), 0.0)

        with self.assertRaises(ValueError):
            project.inventory_valuation({"SKU-NO-PRICE": 1}, prices)
        with self.assertRaises(ValueError):
            project.inventory_valuation({"SKU-A": -1}, prices)
        with self.assertRaises(ValueError):
            project.inventory_valuation({"SKU-A": 1}, {"SKU-A": -5.0})


if __name__ == "__main__":
    unittest.main()
