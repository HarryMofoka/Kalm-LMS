"""Tests for Checkpoint 03: Smart Prepaid Electricity Tariff Calculator."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from master_projects.checkpoint_03_smart_tariff_calculator import project, worked_example


class TestWorkedExample(unittest.TestCase):
    """Verify the reference progressive income tax calculator works out of the box."""

    def test_bracket_1_income(self) -> None:
        res = worked_example.calculate_progressive_tax(15_000)
        self.assertEqual(res["top_bracket"], "Bracket 1 (10%)")
        self.assertEqual(res["total_tax"], 1500.0)
        self.assertEqual(res["effective_rate_pct"], 10.0)
        self.assertEqual(res["net_income"], 13_500.0)

    def test_bracket_2_income(self) -> None:
        res = worked_example.calculate_progressive_tax(35_000)
        self.assertEqual(res["top_bracket"], "Bracket 2 (20%)")
        self.assertEqual(res["tier1_tax"], 2000.0)
        self.assertEqual(res["tier2_tax"], 3000.0)
        self.assertEqual(res["tier3_tax"], 0.0)
        self.assertEqual(res["total_tax"], 5000.0)

    def test_bracket_3_income_and_effective_rate(self) -> None:
        res = worked_example.calculate_progressive_tax(65_000)
        self.assertEqual(res["top_bracket"], "Bracket 3 (30%)")
        self.assertEqual(res["tier1_tax"], 2000.0)
        self.assertEqual(res["tier2_tax"], 6000.0)
        self.assertEqual(res["tier3_tax"], 4500.0)
        self.assertEqual(res["total_tax"], 12_500.0)
        self.assertEqual(res["effective_rate_pct"], 19.23)

    def test_zero_income_avoids_zero_division(self) -> None:
        res = worked_example.calculate_progressive_tax(0)
        self.assertEqual(res["total_tax"], 0.0)
        self.assertEqual(res["effective_rate_pct"], 0.0)
        self.assertEqual(res["net_income"], 0.0)

    def test_negative_income_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            worked_example.calculate_progressive_tax(-100)
        with self.assertRaises(ValueError):
            worked_example.marginal_bracket_label(-1)


class TestMasterProject(unittest.TestCase):
    """TDD test suite for the student's Smart Prepaid Electricity Tariff Calculator."""

    def test_validate_reading_valid_and_tamper_detection(self) -> None:
        usage = project.validate_reading(1250.5, 1400.75)
        self.assertIsInstance(usage, (int, float))
        self.assertAlmostEqual(usage, 150.25, places=2)
        self.assertAlmostEqual(project.validate_reading(500.0, 500.0), 0.0, places=2)

        with self.assertRaises(ValueError):
            project.validate_reading(1400.0, 1200.0)
        with self.assertRaises(ValueError):
            project.validate_reading(-5.0, 100.0)

    def test_tariff_tier_label_boundaries_and_validation(self) -> None:
        self.assertEqual(project.tariff_tier_label(0), "Tier 1 (Lifeline)")
        self.assertEqual(project.tariff_tier_label(100), "Tier 1 (Lifeline)")
        self.assertEqual(project.tariff_tier_label(100.5), "Tier 2 (Standard)")
        self.assertEqual(project.tariff_tier_label(350), "Tier 2 (Standard)")
        self.assertEqual(project.tariff_tier_label(351), "Tier 3 (High Usage)")
        with self.assertRaises(ValueError):
            project.tariff_tier_label(-10)

    def test_bill_tier_1_and_zero_kwh(self) -> None:
        bill = project.calculate_electricity_bill(80, peak_bonus=False)
        self.assertIsInstance(bill, dict)
        self.assertEqual(
            bill,
            {
                "kwh": 80.0,
                "tier": "Tier 1 (Lifeline)",
                "usage_charge": 120.0,
                "discount": 0.0,
                "service_fee": 25.0,
                "total": 145.0,
            },
        )

        zero_bill = project.calculate_electricity_bill(0)
        self.assertIsInstance(zero_bill, dict)
        self.assertEqual(zero_bill["usage_charge"], 0.0)
        self.assertEqual(zero_bill["total"], 25.0)

    def test_bill_tier_2_progressive_blocks(self) -> None:
        bill = project.calculate_electricity_bill(250, peak_bonus=False)
        self.assertIsInstance(bill, dict)
        self.assertEqual(bill["tier"], "Tier 2 (Standard)")
        self.assertEqual(bill["usage_charge"], 480.0)  # 100*1.50 + 150*2.20
        self.assertEqual(bill["discount"], 0.0)
        self.assertEqual(bill["total"], 505.0)

    def test_bill_tier_3_with_peak_bonus_discount(self) -> None:
        bill = project.calculate_electricity_bill(450, peak_bonus=True)
        self.assertIsInstance(bill, dict)
        self.assertEqual(
            bill,
            {
                "kwh": 450.0,
                "tier": "Tier 3 (High Usage)",
                "usage_charge": 1010.0,  # 150 + 550 + 310
                "discount": 101.0,  # 10% of usage_charge only
                "service_fee": 25.0,
                "total": 934.0,
            },
        )

    def test_bill_rejects_negative_kwh(self) -> None:
        with self.assertRaises(ValueError):
            project.calculate_electricity_bill(-1)

    def test_kwh_for_budget_across_all_three_tiers_and_validation(self) -> None:
        t1 = project.kwh_for_budget(120.0)
        self.assertIsInstance(t1, (int, float))
        self.assertAlmostEqual(t1, 80.0, places=2)

        t2 = project.kwh_for_budget(480.0)
        self.assertIsInstance(t2, (int, float))
        self.assertAlmostEqual(t2, 250.0, places=2)

        t3 = project.kwh_for_budget(1010.0)
        self.assertIsInstance(t3, (int, float))
        self.assertAlmostEqual(t3, 450.0, places=2)

        self.assertAlmostEqual(project.kwh_for_budget(0.0), 0.0, places=2)
        with self.assertRaises(ValueError):
            project.kwh_for_budget(-20.0)


if __name__ == "__main__":
    unittest.main()
