"""Unit tests for Module 02: Conditionals, Logic & Validation (Activities 013-024)."""

from __future__ import annotations

from importlib import import_module
import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

_PKG = "activities.02_conditionals_and_logic"

_a013 = import_module(f"{_PKG}.activity_013_booleans_and_comparisons")
example_is_positive = _a013.example_is_positive
solve_is_even_and_positive = _a013.solve_is_even_and_positive

_a014 = import_module(f"{_PKG}.activity_014_if_else_branching")
example_ticket_price = _a014.example_ticket_price
solve_bonus_points = _a014.solve_bonus_points

_a015 = import_module(f"{_PKG}.activity_015_elif_chains")
example_letter_grade = _a015.example_letter_grade
solve_bmi_category = _a015.solve_bmi_category

_a016 = import_module(f"{_PKG}.activity_016_logical_operators")
example_can_ride_coaster = _a016.example_can_ride_coaster
solve_movie_discount = _a016.solve_movie_discount

_a017 = import_module(f"{_PKG}.activity_017_clamping_and_median")
example_clamp = _a017.example_clamp
solve_median_of_three = _a017.solve_median_of_three

_a018 = import_module(f"{_PKG}.activity_018_guard_clauses")
example_safe_divide = _a018.example_safe_divide
solve_safe_percent_change = _a018.solve_safe_percent_change

_a019 = import_module(f"{_PKG}.activity_019_leap_year_calendar")
example_is_leap_year = _a019.example_is_leap_year
solve_days_in_month = _a019.solve_days_in_month

_a020 = import_module(f"{_PKG}.activity_020_triangle_geometry")
example_is_valid_triangle = _a020.example_is_valid_triangle
solve_classify_triangle = _a020.solve_classify_triangle

_a021 = import_module(f"{_PKG}.activity_021_game_rules_matrix")
example_rps_winner = _a021.example_rps_winner
solve_rpsls_winner = _a021.solve_rpsls_winner

_a022 = import_module(f"{_PKG}.activity_022_tiered_pricing")
example_parking_fee = _a022.example_parking_fee
solve_progressive_tax = _a022.solve_progressive_tax

_a023 = import_module(f"{_PKG}.activity_023_type_validation")
example_validate_str_length = _a023.example_validate_str_length
solve_validate_positive_int = _a023.solve_validate_positive_int

_a024 = import_module(f"{_PKG}.activity_024_value_validation")
example_validate_age = _a024.example_validate_age
solve_validate_date = _a024.solve_validate_date


class TestWorkedExamples(unittest.TestCase):
    """Verify every worked example in Module 02."""

    def test_example_013(self) -> None:
        self.assertIs(example_is_positive(5), True)
        self.assertIs(example_is_positive(0.001), True)
        self.assertIs(example_is_positive(0), False)
        self.assertIs(example_is_positive(-3.5), False)

    def test_example_014(self) -> None:
        self.assertEqual(example_ticket_price(0), 10)
        self.assertEqual(example_ticket_price(17), 10)
        self.assertEqual(example_ticket_price(18), 18)
        self.assertEqual(example_ticket_price(65), 18)

    def test_example_015(self) -> None:
        self.assertEqual(example_letter_grade(95), "A")
        self.assertEqual(example_letter_grade(90), "A")
        self.assertEqual(example_letter_grade(89.9), "B")
        self.assertEqual(example_letter_grade(80), "B")
        self.assertEqual(example_letter_grade(70), "C")
        self.assertEqual(example_letter_grade(60), "D")
        self.assertEqual(example_letter_grade(59.9), "F")

    def test_example_016(self) -> None:
        self.assertIs(example_can_ride_coaster(140, False, False), True)
        self.assertIs(example_can_ride_coaster(110, True, False), True)
        self.assertIs(example_can_ride_coaster(110, False, False), False)
        self.assertIs(example_can_ride_coaster(109, True, False), False)
        self.assertIs(example_can_ride_coaster(180, True, True), False)

    def test_example_017(self) -> None:
        self.assertEqual(example_clamp(50, 0, 100), 50)
        self.assertEqual(example_clamp(-10, 0, 100), 0)
        self.assertEqual(example_clamp(150, 0, 100), 100)
        self.assertEqual(example_clamp(5, 5, 5), 5)

    def test_example_018(self) -> None:
        self.assertEqual(example_safe_divide(10, 4), 2.5)
        self.assertEqual(example_safe_divide(1, 3), 0.3333)
        self.assertEqual(example_safe_divide(0, 5), 0.0)
        self.assertIsNone(example_safe_divide(10, 0))

    def test_example_019(self) -> None:
        self.assertIs(example_is_leap_year(2024), True)
        self.assertIs(example_is_leap_year(2000), True)
        self.assertIs(example_is_leap_year(1900), False)
        self.assertIs(example_is_leap_year(2023), False)

    def test_example_020(self) -> None:
        self.assertIs(example_is_valid_triangle(3, 4, 5), True)
        self.assertIs(example_is_valid_triangle(1, 2, 3), False)
        self.assertIs(example_is_valid_triangle(0, 5, 5), False)
        self.assertIs(example_is_valid_triangle(-3, 4, 5), False)

    def test_example_021(self) -> None:
        self.assertEqual(example_rps_winner("Rock", "scissors"), "player1")
        self.assertEqual(example_rps_winner("rock", "paper"), "player2")
        self.assertEqual(example_rps_winner("  Paper ", "PAPER"), "tie")
        self.assertEqual(example_rps_winner("laser", "laser"), "invalid")

    def test_example_022(self) -> None:
        self.assertEqual(example_parking_fee(-2), 0.0)
        self.assertEqual(example_parking_fee(0), 0.0)
        self.assertEqual(example_parking_fee(2), 6.0)
        self.assertEqual(example_parking_fee(4), 10.0)
        self.assertEqual(example_parking_fee(5), 12.0)
        self.assertEqual(example_parking_fee(7), 14.0)

    def test_example_023(self) -> None:
        self.assertEqual(example_validate_str_length("Python"), 6)
        self.assertEqual(example_validate_str_length(""), 0)
        with self.assertRaises(TypeError):
            example_validate_str_length(123)
        with self.assertRaises(TypeError):
            example_validate_str_length(None)

    def test_example_024(self) -> None:
        self.assertEqual(example_validate_age(0), 0)
        self.assertEqual(example_validate_age(25), 25)
        self.assertEqual(example_validate_age(130), 130)
        with self.assertRaises(TypeError):
            example_validate_age(True)
        with self.assertRaises(TypeError):
            example_validate_age("25")  # type: ignore[arg-type]
        with self.assertRaises(ValueError):
            example_validate_age(-1)
        with self.assertRaises(ValueError):
            example_validate_age(131)


class TestYourActivities(unittest.TestCase):
    """Verify student solutions for Module 02 (Activities 013-024)."""

    def test_activity_013(self) -> None:
        self.assertIs(solve_is_even_and_positive(4), True)
        self.assertIs(solve_is_even_and_positive(2), True)
        self.assertIs(solve_is_even_and_positive(0), False)
        self.assertIs(solve_is_even_and_positive(-6), False)
        self.assertIs(solve_is_even_and_positive(9), False)
        self.assertIs(solve_is_even_and_positive(1), False)

    def test_activity_014(self) -> None:
        self.assertEqual(solve_bonus_points(10), 30)
        self.assertEqual(solve_bonus_points(7), 16)
        self.assertEqual(solve_bonus_points(0), 10)
        self.assertEqual(solve_bonus_points(1), -2)
        self.assertEqual(solve_bonus_points(-4), 2)
        self.assertEqual(solve_bonus_points(-3), -14)

    def test_activity_015(self) -> None:
        self.assertEqual(solve_bmi_category(50, 1.75), "Underweight")
        self.assertEqual(solve_bmi_category(70, 1.75), "Normal")
        self.assertEqual(solve_bmi_category(85, 1.75), "Overweight")
        self.assertEqual(solve_bmi_category(100, 1.75), "Obese")
        # Exact boundary checks: 18.5, 25.0, 30.0
        self.assertEqual(solve_bmi_category(74, 2.0), "Normal")
        self.assertEqual(solve_bmi_category(100, 2.0), "Overweight")
        self.assertEqual(solve_bmi_category(120, 2.0), "Obese")

    def test_activity_016(self) -> None:
        self.assertIs(solve_movie_discount(10, False, False, False), True)
        self.assertIs(solve_movie_discount(11, False, False, False), True)
        self.assertIs(solve_movie_discount(12, False, False, False), False)
        self.assertIs(solve_movie_discount(64, False, False, False), False)
        self.assertIs(solve_movie_discount(65, False, False, False), True)
        self.assertIs(solve_movie_discount(30, True, False, False), True)
        self.assertIs(solve_movie_discount(30, False, True, False), True)
        self.assertIs(solve_movie_discount(10, True, True, True), False)

    def test_activity_017(self) -> None:
        # All 6 orderings of (1, 2, 3)
        for triple in (
            (1, 2, 3),
            (1, 3, 2),
            (2, 1, 3),
            (2, 3, 1),
            (3, 1, 2),
            (3, 2, 1),
        ):
            self.assertEqual(solve_median_of_three(*triple), 2)
        # Duplicates & negatives
        self.assertEqual(solve_median_of_three(5, 5, 2), 5)
        self.assertEqual(solve_median_of_three(2, 5, 2), 2)
        self.assertEqual(solve_median_of_three(4, 4, 4), 4)
        self.assertEqual(solve_median_of_three(-1, -5, -3), -3)

    def test_activity_018(self) -> None:
        self.assertEqual(solve_safe_percent_change(100, 125), 25.0)
        self.assertEqual(solve_safe_percent_change(200, 150), -25.0)
        self.assertEqual(solve_safe_percent_change(-100, -50), 50.0)
        self.assertEqual(solve_safe_percent_change(80, 80), 0.0)
        self.assertIsNone(solve_safe_percent_change(0, 50))
        self.assertIsNone(solve_safe_percent_change(0, 0))

    def test_activity_019(self) -> None:
        self.assertEqual(solve_days_in_month(2024, 2), 29)
        self.assertEqual(solve_days_in_month(2023, 2), 28)
        self.assertEqual(solve_days_in_month(1900, 2), 28)
        self.assertEqual(solve_days_in_month(2000, 2), 29)
        self.assertEqual(solve_days_in_month(2025, 4), 30)
        self.assertEqual(solve_days_in_month(2025, 6), 30)
        self.assertEqual(solve_days_in_month(2025, 9), 30)
        self.assertEqual(solve_days_in_month(2025, 11), 30)
        self.assertEqual(solve_days_in_month(2025, 1), 31)
        self.assertEqual(solve_days_in_month(2025, 8), 31)
        self.assertEqual(solve_days_in_month(2025, 12), 31)
        self.assertEqual(solve_days_in_month(2025, 0), 0)
        self.assertEqual(solve_days_in_month(2025, 13), 0)

    def test_activity_020(self) -> None:
        self.assertEqual(solve_classify_triangle(5, 5, 5), "equilateral")
        self.assertEqual(solve_classify_triangle(5, 5, 8), "isosceles")
        self.assertEqual(solve_classify_triangle(5, 8, 5), "isosceles")
        self.assertEqual(solve_classify_triangle(8, 5, 5), "isosceles")
        self.assertEqual(solve_classify_triangle(3, 4, 5), "scalene")
        self.assertEqual(solve_classify_triangle(1, 2, 3), "invalid")
        self.assertEqual(solve_classify_triangle(0, 0, 0), "invalid")
        self.assertEqual(solve_classify_triangle(5, 5, 12), "invalid")
        self.assertEqual(solve_classify_triangle(-3, 4, 5), "invalid")

    def test_activity_021(self) -> None:
        self.assertEqual(solve_rpsls_winner("rock", "lizard"), "player1")
        self.assertEqual(solve_rpsls_winner("spock", "rock"), "player1")
        self.assertEqual(solve_rpsls_winner("lizard", "spock"), "player1")
        self.assertEqual(solve_rpsls_winner("paper", "spock"), "player1")
        self.assertEqual(solve_rpsls_winner("scissors", "lizard"), "player1")
        self.assertEqual(solve_rpsls_winner("lizard", "rock"), "player2")
        self.assertEqual(solve_rpsls_winner("rock", "spock"), "player2")
        self.assertEqual(solve_rpsls_winner("SPOCK", "  Spock "), "tie")
        self.assertEqual(solve_rpsls_winner("rock", "laser"), "invalid")
        self.assertEqual(solve_rpsls_winner("laser", "laser"), "invalid")

    def test_activity_022(self) -> None:
        self.assertEqual(solve_progressive_tax(-500), 0.0)
        self.assertEqual(solve_progressive_tax(0), 0.0)
        self.assertEqual(solve_progressive_tax(10000), 0.0)
        self.assertEqual(solve_progressive_tax(25000), 1500.0)
        self.assertEqual(solve_progressive_tax(30000), 2000.0)
        self.assertEqual(solve_progressive_tax(50000), 6000.0)
        self.assertEqual(solve_progressive_tax(70000), 10000.0)
        self.assertEqual(solve_progressive_tax(100000), 19000.0)

    def test_activity_023(self) -> None:
        self.assertEqual(solve_validate_positive_int(1), 1)
        self.assertEqual(solve_validate_positive_int(42), 42)
        for bad_type in (True, False, 3.0, "5", None):
            with self.assertRaises(TypeError):
                solve_validate_positive_int(bad_type)
        for bad_val in (0, -1, -99):
            with self.assertRaises(ValueError):
                solve_validate_positive_int(bad_val)

    def test_activity_024(self) -> None:
        self.assertEqual(solve_validate_date(2024, 2, 29), (2024, 2, 29))
        self.assertEqual(solve_validate_date(2000, 2, 29), (2000, 2, 29))
        self.assertEqual(solve_validate_date(2025, 12, 31), (2025, 12, 31))
        for bad_type_args in (("2024", 1, 1), (2024, True, 1), (2024, 1, 1.0)):
            with self.assertRaises(TypeError):
                solve_validate_date(*bad_type_args)  # type: ignore[arg-type]
        for bad_val_args in (
            (0, 5, 5),
            (10000, 1, 1),
            (2024, 0, 10),
            (2024, 13, 10),
            (2023, 2, 29),
            (1900, 2, 29),
            (2024, 4, 31),
            (2024, 1, 0),
        ):
            with self.assertRaises(ValueError):
                solve_validate_date(*bad_val_args)


if __name__ == "__main__":
    unittest.main()
