"""Unit tests for Module 01: Variables, Math & Formatting (Activities 001-012)."""

from __future__ import annotations

from importlib import import_module
import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

_PKG = "activities.01_variables_and_math"

_a001 = import_module(f"{_PKG}.activity_001_fstring_greeting")
example_welcome_banner = _a001.example_welcome_banner
solve_gamer_badge = _a001.solve_gamer_badge

_a002 = import_module(f"{_PKG}.activity_002_basic_arithmetic")
example_rectangle_metrics = _a002.example_rectangle_metrics
solve_trapezoid_and_triangle = _a002.solve_trapezoid_and_triangle

_a003 = import_module(f"{_PKG}.activity_003_unit_conversion")
example_celsius_to_fahrenheit = _a003.example_celsius_to_fahrenheit
solve_trip_speed_conversion = _a003.solve_trip_speed_conversion

_a004 = import_module(f"{_PKG}.activity_004_floor_div_and_modulo")
example_minutes_to_hours = _a004.example_minutes_to_hours
solve_seconds_to_dhms = _a004.solve_seconds_to_dhms

_a005 = import_module(f"{_PKG}.activity_005_rounding_and_percentages")
example_discounted_price = _a005.example_discounted_price
solve_bill_split = _a005.solve_bill_split

_a006 = import_module(f"{_PKG}.activity_006_powers_and_distance")
example_hypotenuse = _a006.example_hypotenuse
solve_euclidean_distance = _a006.solve_euclidean_distance

_a007 = import_module(f"{_PKG}.activity_007_digit_extraction")
example_last_two_digits = _a007.example_last_two_digits
solve_three_digit_ops = _a007.solve_three_digit_ops

_a008 = import_module(f"{_PKG}.activity_008_clock_modulo_wrap")
example_clock_hours = _a008.example_clock_hours
solve_clock_with_rollover = _a008.solve_clock_with_rollover

_a009 = import_module(f"{_PKG}.activity_009_interest_and_rates")
example_simple_interest = _a009.example_simple_interest
solve_compound_interest = _a009.solve_compound_interest

_a010 = import_module(f"{_PKG}.activity_010_ceiling_division")
example_boxes_needed = _a010.example_boxes_needed
solve_bus_seating = _a010.solve_bus_seating

_a011 = import_module(f"{_PKG}.activity_011_weighted_averages")
example_weighted_score = _a011.example_weighted_score
solve_required_final_score = _a011.solve_required_final_score

_a012 = import_module(f"{_PKG}.activity_012_formatted_receipts")
example_price_line = _a012.example_price_line
solve_mini_receipt = _a012.solve_mini_receipt


class TestWorkedExamples(unittest.TestCase):
    """Verify every worked example in Module 01."""

    def test_example_001(self) -> None:
        self.assertEqual(
            example_welcome_banner("Ada", "Python"),
            "Hello, Ada! Welcome to Python programming.",
        )
        self.assertEqual(
            example_welcome_banner("Grace Hopper", "COBOL"),
            "Hello, Grace Hopper! Welcome to COBOL programming.",
        )

    def test_example_002(self) -> None:
        self.assertEqual(example_rectangle_metrics(4, 7), (22, 28))
        self.assertEqual(example_rectangle_metrics(2.5, 4.0), (13.0, 10.0))
        self.assertEqual(example_rectangle_metrics(0, 5), (10, 0))

    def test_example_003(self) -> None:
        self.assertEqual(example_celsius_to_fahrenheit(0), 32.0)
        self.assertEqual(example_celsius_to_fahrenheit(100), 212.0)
        self.assertEqual(example_celsius_to_fahrenheit(-40), -40.0)
        self.assertEqual(example_celsius_to_fahrenheit(37), 98.6)

    def test_example_004(self) -> None:
        self.assertEqual(example_minutes_to_hours(135), (2, 15))
        self.assertEqual(example_minutes_to_hours(60), (1, 0))
        self.assertEqual(example_minutes_to_hours(59), (0, 59))
        self.assertEqual(example_minutes_to_hours(0), (0, 0))

    def test_example_005(self) -> None:
        self.assertEqual(example_discounted_price(100.0, 25.0), 75.0)
        self.assertEqual(example_discounted_price(49.99, 15.0), 42.49)
        self.assertEqual(example_discounted_price(80.0, 0.0), 80.0)
        self.assertEqual(example_discounted_price(80.0, 100.0), 0.0)

    def test_example_006(self) -> None:
        self.assertEqual(example_hypotenuse(3, 4), 5.0)
        self.assertEqual(example_hypotenuse(0, 0), 0.0)
        self.assertEqual(example_hypotenuse(0, 7), 7.0)
        self.assertEqual(example_hypotenuse(1, 1), 1.4142)

    def test_example_007(self) -> None:
        self.assertEqual(example_last_two_digits(482), (8, 2))
        self.assertEqual(example_last_two_digits(7), (0, 7))
        self.assertEqual(example_last_two_digits(0), (0, 0))
        self.assertEqual(example_last_two_digits(98765), (6, 5))

    def test_example_008(self) -> None:
        self.assertEqual(example_clock_hours(23, 2), 1)
        self.assertEqual(example_clock_hours(10, 48), 10)
        self.assertEqual(example_clock_hours(1, -3), 22)
        self.assertEqual(example_clock_hours(0, 0), 0)

    def test_example_009(self) -> None:
        self.assertEqual(example_simple_interest(1000.0, 0.05, 3), (150.0, 1150.0))
        self.assertEqual(example_simple_interest(2500.0, 0.035, 0.5), (43.75, 2543.75))
        self.assertEqual(example_simple_interest(500.0, 0.0, 5), (0.0, 500.0))

    def test_example_010(self) -> None:
        self.assertEqual(example_boxes_needed(12, 4), 3)
        self.assertEqual(example_boxes_needed(13, 4), 4)
        self.assertEqual(example_boxes_needed(0, 4), 0)
        self.assertEqual(example_boxes_needed(1, 10), 1)

    def test_example_011(self) -> None:
        self.assertEqual(example_weighted_score(90, 80, 85), 84.5)
        self.assertEqual(example_weighted_score(100, 100, 100), 100.0)
        self.assertEqual(example_weighted_score(70, 75, 82), 77.5)

    def test_example_012(self) -> None:
        line = example_price_line("Espresso", 3.5)
        self.assertEqual(line, "Espresso             $3.50")
        self.assertEqual(len(line), 26)
        self.assertEqual(
            example_price_line("Blueberry Muffin", 4.25),
            "Blueberry Muffin     $4.25",
        )
        self.assertEqual(
            example_price_line("Water", 0),
            "Water                $0.00",
        )


class TestYourActivities(unittest.TestCase):
    """Verify student solutions for Module 01 (Activities 001-012)."""

    def test_activity_001(self) -> None:
        self.assertEqual(
            solve_gamer_badge("ShadowFox", 42, "Iron Owls"),
            "Player ShadowFox (Lv.42) - Guild: Iron Owls",
        )
        self.assertEqual(
            solve_gamer_badge("Nova", 1, "Wanderers"),
            "Player Nova (Lv.1) - Guild: Wanderers",
        )
        self.assertEqual(
            solve_gamer_badge("Pixel Knight", 99, "Code Crafters"),
            "Player Pixel Knight (Lv.99) - Guild: Code Crafters",
        )

    def test_activity_002(self) -> None:
        self.assertEqual(solve_trapezoid_and_triangle(10, 6, 4), (20.0, 32.0))
        self.assertEqual(solve_trapezoid_and_triangle(5, 5, 3), (7.5, 15.0))
        self.assertEqual(solve_trapezoid_and_triangle(7.5, 2.5, 4.0), (15.0, 20.0))
        self.assertEqual(solve_trapezoid_and_triangle(0, 8, 5), (0.0, 20.0))

    def test_activity_003(self) -> None:
        self.assertEqual(solve_trip_speed_conversion(100, 2), (62.14, 31.07))
        self.assertEqual(solve_trip_speed_conversion(0, 1.5), (0.0, 0.0))
        self.assertEqual(solve_trip_speed_conversion(160.9344, 1), (100.0, 100.0))
        self.assertEqual(solve_trip_speed_conversion(50, 0.5), (31.07, 62.14))

    def test_activity_004(self) -> None:
        self.assertEqual(solve_seconds_to_dhms(0), (0, 0, 0, 0))
        self.assertEqual(solve_seconds_to_dhms(3661), (0, 1, 1, 1))
        self.assertEqual(solve_seconds_to_dhms(90061), (1, 1, 1, 1))
        self.assertEqual(solve_seconds_to_dhms(172800), (2, 0, 0, 0))
        self.assertEqual(solve_seconds_to_dhms(86399), (0, 23, 59, 59))

    def test_activity_005(self) -> None:
        self.assertEqual(solve_bill_split(100.0, 8.0, 15.0, 4), (123.0, 30.75))
        self.assertEqual(solve_bill_split(50.0, 10.0, 20.0, 3), (65.0, 21.67))
        self.assertEqual(solve_bill_split(80.0, 0.0, 0.0, 2), (80.0, 40.0))
        self.assertEqual(solve_bill_split(33.33, 7.5, 18.0, 1), (41.83, 41.83))

    def test_activity_006(self) -> None:
        self.assertEqual(solve_euclidean_distance(0, 0, 3, 4), 5.0)
        self.assertEqual(solve_euclidean_distance(1, 2, 1, 2), 0.0)
        self.assertEqual(solve_euclidean_distance(-2, -3, 1, 1), 5.0)
        self.assertEqual(solve_euclidean_distance(0, 0, 1, 1), 1.4142)

    def test_activity_007(self) -> None:
        self.assertEqual(solve_three_digit_ops(374), (14, 473))
        self.assertEqual(solve_three_digit_ops(500), (5, 5))
        self.assertEqual(solve_three_digit_ops(101), (2, 101))
        self.assertEqual(solve_three_digit_ops(999), (27, 999))

    def test_activity_008(self) -> None:
        self.assertEqual(solve_clock_with_rollover(8, 15, 45), (0, 9, 0))
        self.assertEqual(solve_clock_with_rollover(22, 30, 120), (1, 0, 30))
        self.assertEqual(solve_clock_with_rollover(23, 59, 1), (1, 0, 0))
        self.assertEqual(solve_clock_with_rollover(10, 0, 2880), (2, 10, 0))
        self.assertEqual(solve_clock_with_rollover(1, 0, -90), (-1, 23, 30))

    def test_activity_009(self) -> None:
        self.assertEqual(solve_compound_interest(1000.0, 0.05, 1, 2), (1102.5, 102.5))
        self.assertEqual(solve_compound_interest(1000.0, 0.12, 12, 1), (1126.83, 126.83))
        self.assertEqual(solve_compound_interest(500.0, 0.0, 4, 5), (500.0, 0.0))
        self.assertEqual(solve_compound_interest(2000.0, 0.08, 4, 0), (2000.0, 0.0))

    def test_activity_010(self) -> None:
        self.assertEqual(solve_bus_seating(100, 40), (3, 20))
        self.assertEqual(solve_bus_seating(80, 40), (2, 0))
        self.assertEqual(solve_bus_seating(0, 40), (0, 0))
        self.assertEqual(solve_bus_seating(1, 40), (1, 39))

    def test_activity_011(self) -> None:
        self.assertEqual(solve_required_final_score(80.0, 0.6, 85.0), 92.5)
        self.assertEqual(solve_required_final_score(90.0, 0.7, 90.0), 90.0)
        self.assertEqual(solve_required_final_score(70.0, 0.5, 90.0), 110.0)
        self.assertEqual(solve_required_final_score(95.0, 0.8, 70.0), -30.0)

    def test_activity_012(self) -> None:
        expected = "\n".join(
            [
                "Latte                $4.50",
                "Croissant            $3.25",
                "--------------------------",
                "Tax                  $0.62",
                "TOTAL                $8.37",
            ]
        )
        self.assertEqual(
            solve_mini_receipt("Latte", 4.5, "Croissant", 3.25, 0.08),
            expected,
        )

        expected_zero_tax = "\n".join(
            [
                "Tea                  $2.00",
                "Scone                $3.00",
                "--------------------------",
                "Tax                  $0.00",
                "TOTAL                $5.00",
            ]
        )
        self.assertEqual(
            solve_mini_receipt("Tea", 2.0, "Scone", 3.0, 0.0),
            expected_zero_tax,
        )


if __name__ == "__main__":
    unittest.main()
