"""Tests for Checkpoint 05: Micro-Loan Payoff & Amortization Simulator."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from master_projects.checkpoint_05_loan_amortization_simulator import project, worked_example


class TestWorkedExample(unittest.TestCase):
    """Verify the reference emergency fund compound savings simulator works out of the box."""

    def test_compound_savings_goal_schedule_and_totals(self) -> None:
        res = worked_example.simulate_savings_goal(
            starting_balance=1000.0,
            monthly_contribution=500.0,
            annual_rate_pct=12.0,
            target_amount=2500.0,
        )
        self.assertEqual(res["months"], 3)
        self.assertEqual(res["total_contributed"], 1500.0)
        self.assertEqual(res["total_interest"], 45.35)
        self.assertEqual(res["final_balance"], 2545.35)
        self.assertEqual(len(res["schedule"]), 3)
        self.assertEqual(res["schedule"][0]["ending_balance"], 1510.0)
        self.assertEqual(res["schedule"][-1]["ending_balance"], 2545.35)

    def test_zero_interest_savings_goal(self) -> None:
        res = worked_example.simulate_savings_goal(200.0, 200.0, 0.0, 1000.0)
        self.assertEqual(res["months"], 4)
        self.assertEqual(res["total_interest"], 0.0)
        self.assertEqual(res["final_balance"], 1000.0)

    def test_already_at_or_above_target(self) -> None:
        res = worked_example.simulate_savings_goal(5000.0, 250.0, 5.0, 3000.0)
        self.assertEqual(res["months"], 0)
        self.assertEqual(res["schedule"], [])
        self.assertEqual(res["final_balance"], 5000.0)
        self.assertEqual(res["total_interest"], 0.0)

    def test_interest_only_growth_reaches_target(self) -> None:
        res = worked_example.simulate_savings_goal(1000.0, 0.0, 12.0, 1020.0)
        self.assertEqual(res["months"], 2)
        self.assertEqual(res["total_contributed"], 0.0)
        self.assertGreaterEqual(res["final_balance"], 1020.0)

    def test_invalid_and_unreachable_goals_raise_value_error(self) -> None:
        with self.assertRaises(ValueError):
            worked_example.simulate_savings_goal(0.0, 0.0, 5.0, 1000.0)
        with self.assertRaises(ValueError):
            worked_example.simulate_savings_goal(500.0, 0.0, 0.0, 1000.0)
        with self.assertRaises(ValueError):
            worked_example.simulate_savings_goal(-100.0, 200.0, 5.0, 1000.0)


class TestMasterProject(unittest.TestCase):
    """TDD test suite for the student's Micro-Loan Payoff & Amortization Simulator."""

    def test_zero_interest_loan_with_partial_final_payment(self) -> None:
        res = project.simulate_loan_payoff(1000.0, annual_rate_pct=0.0, monthly_payment=300.0)
        self.assertIsInstance(res, dict)
        self.assertEqual(res.get("months"), 4)
        self.assertEqual(res.get("total_paid"), 1000.0)
        self.assertEqual(res.get("total_interest"), 0.0)
        schedule = res.get("schedule")
        self.assertIsInstance(schedule, list)
        self.assertEqual(len(schedule), 4)
        self.assertEqual(
            schedule[-1],
            {
                "month": 4,
                "payment": 100.0,
                "interest": 0.0,
                "principal_paid": 100.0,
                "ending_balance": 0.0,
            },
        )

    def test_interest_bearing_loan_exact_amortization_schedule(self) -> None:
        res = project.simulate_loan_payoff(1000.0, annual_rate_pct=12.0, monthly_payment=200.0)
        self.assertIsInstance(res, dict)
        self.assertEqual(res.get("months"), 6)
        self.assertEqual(res.get("total_interest"), 31.12)
        self.assertEqual(res.get("total_paid"), 1031.12)

        schedule = res.get("schedule")
        self.assertIsInstance(schedule, list)
        self.assertEqual(len(schedule), 6)
        self.assertEqual(
            schedule[0],
            {
                "month": 1,
                "payment": 200.0,
                "interest": 10.0,
                "principal_paid": 190.0,
                "ending_balance": 810.0,
            },
        )
        self.assertEqual(
            schedule[-1],
            {
                "month": 6,
                "payment": 31.12,
                "interest": 0.31,
                "principal_paid": 30.81,
                "ending_balance": 0.0,
            },
        )

    def test_single_month_full_payoff(self) -> None:
        res = project.simulate_loan_payoff(500.0, annual_rate_pct=12.0, monthly_payment=1000.0)
        self.assertIsInstance(res, dict)
        self.assertEqual(res.get("months"), 1)
        self.assertEqual(res.get("total_interest"), 5.0)
        self.assertEqual(res.get("total_paid"), 505.0)
        schedule = res.get("schedule")
        self.assertIsInstance(schedule, list)
        self.assertEqual(schedule[0]["ending_balance"], 0.0)

    def test_negative_amortization_raises_value_error(self) -> None:
        # Monthly interest on $1,000 at 12% APR is $10.00; payment <= $10 never pays off loan.
        with self.assertRaises(ValueError):
            project.simulate_loan_payoff(1000.0, annual_rate_pct=12.0, monthly_payment=10.0)
        with self.assertRaises(ValueError):
            project.simulate_loan_payoff(1000.0, annual_rate_pct=12.0, monthly_payment=5.0)

    def test_invalid_loan_parameters_raise_value_error(self) -> None:
        with self.assertRaises(ValueError):
            project.simulate_loan_payoff(0.0, 10.0, 100.0)
        with self.assertRaises(ValueError):
            project.simulate_loan_payoff(-500.0, 10.0, 100.0)
        with self.assertRaises(ValueError):
            project.simulate_loan_payoff(500.0, -5.0, 100.0)
        with self.assertRaises(ValueError):
            project.simulate_loan_payoff(500.0, 10.0, 0.0)

    def test_estimate_months_saved_and_validation(self) -> None:
        saved = project.estimate_months_saved(1000.0, 12.0, base_payment=200.0, extra_payment=100.0)
        self.assertIsInstance(saved, int)
        self.assertEqual(saved, 2)

        zero_extra = project.estimate_months_saved(1000.0, 12.0, base_payment=200.0, extra_payment=0.0)
        self.assertEqual(zero_extra, 0)

        with self.assertRaises(ValueError):
            project.estimate_months_saved(1000.0, 12.0, base_payment=200.0, extra_payment=-50.0)


if __name__ == "__main__":
    unittest.main()
