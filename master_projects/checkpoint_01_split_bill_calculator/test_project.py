"""Tests for Checkpoint 01: Split Bill Calculator."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from master_projects.checkpoint_01_split_bill_calculator import project, worked_example


class TestWorkedExample(unittest.TestCase):
    """Verify the reference e-commerce checkout engine works out of the box."""

    def test_discount_and_tax_helpers(self) -> None:
        self.assertAlmostEqual(worked_example.calculate_discount(120.00, 20.0), 24.00)
        self.assertAlmostEqual(worked_example.calculate_sales_tax(96.00, 15.0), 14.40)

    def test_shipping_threshold_rules(self) -> None:
        self.assertEqual(worked_example.calculate_shipping(0.0), 0.0)
        self.assertEqual(worked_example.calculate_shipping(99.99), 12.50)
        self.assertEqual(worked_example.calculate_shipping(100.00), 0.0)
        self.assertEqual(worked_example.calculate_shipping(250.00), 0.0)

    def test_checkout_summary_under_free_shipping_after_discount(self) -> None:
        summary = worked_example.build_checkout_summary(120.00, discount_pct=20.0, tax_rate_pct=15.0)
        self.assertEqual(
            summary,
            {
                "subtotal": 120.00,
                "discount": 24.00,
                "taxable_subtotal": 96.00,
                "tax": 14.40,
                "shipping": 12.50,
                "grand_total": 122.90,
            },
        )

    def test_checkout_summary_validation_errors(self) -> None:
        with self.assertRaises(ValueError):
            worked_example.calculate_discount(-10.0, 10.0)
        with self.assertRaises(ValueError):
            worked_example.calculate_discount(50.0, 120.0)
        with self.assertRaises(ValueError):
            worked_example.calculate_sales_tax(50.0, -5.0)

    def test_format_checkout_line(self) -> None:
        line = worked_example.format_checkout_line("Shipping", 12.5, width=20)
        self.assertEqual(line, "Shipping      $12.50")
        self.assertEqual(len(line), 20)
        neg_line = worked_example.format_checkout_line("Discount", -24.0, width=20)
        self.assertEqual(neg_line, "Discount     -$24.00")


class TestMasterProject(unittest.TestCase):
    """TDD test suite for the student's Restaurant Bill & Fair Group Splitter."""

    def test_calculate_tax_rounding_and_validation(self) -> None:
        tax = project.calculate_tax(87.50, 8.5)
        self.assertIsInstance(tax, (int, float))
        self.assertAlmostEqual(tax, 7.44, places=2)
        self.assertAlmostEqual(project.calculate_tax(100.0, 0.0), 0.0, places=2)
        with self.assertRaises(ValueError):
            project.calculate_tax(-1.0, 10.0)
        with self.assertRaises(ValueError):
            project.calculate_tax(50.0, -2.0)

    def test_calculate_tip_pre_tax_and_validation(self) -> None:
        tip = project.calculate_tip(87.50, 18.0)
        self.assertIsInstance(tip, (int, float))
        self.assertAlmostEqual(tip, 15.75, places=2)
        self.assertAlmostEqual(project.calculate_tip(45.0, 0.0), 0.0, places=2)
        with self.assertRaises(ValueError):
            project.calculate_tip(-10.0, 15.0)
        with self.assertRaises(ValueError):
            project.calculate_tip(50.0, -5.0)

    def test_split_bill_even_division(self) -> None:
        result = project.split_bill(60.00, tax_rate_pct=0.0, tip_pct=20.0, num_people=4)
        self.assertIsInstance(result, dict)
        self.assertEqual(
            result,
            {
                "subtotal": 60.00,
                "tax": 0.00,
                "tip": 12.00,
                "total": 72.00,
                "per_person": 18.00,
                "remainder_cents": 0,
            },
        )

    def test_split_bill_with_remainder_cents_and_penny_conservation(self) -> None:
        result = project.split_bill(100.00, tax_rate_pct=10.0, tip_pct=15.0, num_people=3)
        self.assertIsInstance(result, dict)
        self.assertEqual(
            result,
            {
                "subtotal": 100.00,
                "tax": 10.00,
                "tip": 15.00,
                "total": 125.00,
                "per_person": 41.66,
                "remainder_cents": 2,
            },
        )
        reconstructed = round(result["per_person"] * 3 + result["remainder_cents"] / 100.0, 2)
        self.assertAlmostEqual(reconstructed, result["total"], places=2)

    def test_split_bill_fractional_rates_and_validation(self) -> None:
        result = project.split_bill(87.50, tax_rate_pct=8.5, tip_pct=18.0, num_people=4)
        self.assertIsInstance(result, dict)
        self.assertEqual(result["total"], 110.69)
        self.assertEqual(result["per_person"], 27.67)
        self.assertEqual(result["remainder_cents"], 1)

        with self.assertRaises(ValueError):
            project.split_bill(50.0, 10.0, 15.0, 0)
        with self.assertRaises(ValueError):
            project.split_bill(50.0, 10.0, 15.0, -3)
        with self.assertRaises(ValueError):
            project.split_bill(50.0, 10.0, 15.0, True)  # bool is not a valid diner count
        with self.assertRaises(ValueError):
            project.split_bill(-25.0, 10.0, 15.0, 2)

    def test_format_receipt_line_alignment_and_overflow(self) -> None:
        line = project.format_receipt_line("Subtotal", 85.5, width=20)
        self.assertIsInstance(line, str)
        self.assertEqual(line, "Subtotal      $85.50")
        self.assertEqual(len(line), 20)

        tight = project.format_receipt_line("Super Long Menu Item Name", 12.34, width=10)
        self.assertEqual(tight, "Super Long Menu Item Name $12.34")

        refund = project.format_receipt_line("Promo Credit", -5.0, width=22)
        self.assertEqual(refund, "Promo Credit    -$5.00")


if __name__ == "__main__":
    unittest.main()
