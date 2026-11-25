"""Unit tests for Module 03: Loops Fundamentals (Activities 025-036)."""

from __future__ import annotations

from importlib import import_module
import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

_PKG = "activities.03_loops_fundamentals"

_a025 = import_module(f"{_PKG}.activity_025_for_loop_counting")
example_count_up = _a025.example_count_up
solve_sum_to_n = _a025.solve_sum_to_n

_a026 = import_module(f"{_PKG}.activity_026_step_ranges_filtering")
example_even_numbers = _a026.example_even_numbers
solve_sum_multiples_3_or_5 = _a026.solve_sum_multiples_3_or_5

_a027 = import_module(f"{_PKG}.activity_027_product_accumulator")
example_integer_power = _a027.example_integer_power
solve_factorial = _a027.solve_factorial

_a028 = import_module(f"{_PKG}.activity_028_while_countdown_collatz")
example_halving_steps = _a028.example_halving_steps
solve_collatz_steps = _a028.solve_collatz_steps

_a029 = import_module(f"{_PKG}.activity_029_while_digit_loops")
example_count_digits = _a029.example_count_digits
solve_digit_stats = _a029.solve_digit_stats

_a030 = import_module(f"{_PKG}.activity_030_running_totals_thresholds")
example_days_to_goal = _a030.example_days_to_goal
solve_months_to_payoff = _a030.solve_months_to_payoff

_a031 = import_module(f"{_PKG}.activity_031_fizzbuzz_variations")
example_fizzbuzz = _a031.example_fizzbuzz
solve_fizzbuzzbazz = _a031.solve_fizzbuzzbazz

_a032 = import_module(f"{_PKG}.activity_032_fibonacci_sequence")
example_first_n_fibonacci = _a032.example_first_n_fibonacci
solve_fibonacci_up_to = _a032.solve_fibonacci_up_to

_a033 = import_module(f"{_PKG}.activity_033_divisors_and_primality")
example_divisors = _a033.example_divisors
solve_is_prime = _a033.solve_is_prime

_a034 = import_module(f"{_PKG}.activity_034_primes_in_range")
example_count_primes_up_to = _a034.example_count_primes_up_to
solve_primes_in_range = _a034.solve_primes_in_range

_a035 = import_module(f"{_PKG}.activity_035_number_theory_loops")
example_gcd = _a035.example_gcd
solve_lcm_and_fraction = _a035.solve_lcm_and_fraction

_a036 = import_module(f"{_PKG}.activity_036_nested_loop_grids")
example_multiplication_row = _a036.example_multiplication_row
solve_grid_and_pair_sums = _a036.solve_grid_and_pair_sums


class TestWorkedExamples(unittest.TestCase):
    """Verify every worked example in Module 03."""

    def test_example_025(self) -> None:
        self.assertEqual(example_count_up(5), [1, 2, 3, 4, 5])
        self.assertEqual(example_count_up(1), [1])
        self.assertEqual(example_count_up(0), [])
        self.assertEqual(example_count_up(-3), [])

    def test_example_026(self) -> None:
        self.assertEqual(example_even_numbers(10), [2, 4, 6, 8, 10])
        self.assertEqual(example_even_numbers(9), [2, 4, 6, 8])
        self.assertEqual(example_even_numbers(2), [2])
        self.assertEqual(example_even_numbers(1), [])
        self.assertEqual(example_even_numbers(-4), [])

    def test_example_027(self) -> None:
        self.assertEqual(example_integer_power(2, 5), 32)
        self.assertEqual(example_integer_power(7, 0), 1)
        self.assertEqual(example_integer_power(-3, 3), -27)
        self.assertEqual(example_integer_power(0, 0), 1)
        with self.assertRaises(ValueError):
            example_integer_power(2, -1)

    def test_example_028(self) -> None:
        self.assertEqual(example_halving_steps(1), 0)
        self.assertEqual(example_halving_steps(7), 2)
        self.assertEqual(example_halving_steps(8), 3)
        self.assertEqual(example_halving_steps(16), 4)
        with self.assertRaises(ValueError):
            example_halving_steps(0)
        with self.assertRaises(ValueError):
            example_halving_steps(-5)

    def test_example_029(self) -> None:
        self.assertEqual(example_count_digits(0), 1)
        self.assertEqual(example_count_digits(7), 1)
        self.assertEqual(example_count_digits(4823), 4)
        self.assertEqual(example_count_digits(-905), 3)
        self.assertEqual(example_count_digits(100000), 6)

    def test_example_030(self) -> None:
        self.assertEqual(example_days_to_goal(25, 100), 4)
        self.assertEqual(example_days_to_goal(30, 100), 4)
        self.assertEqual(example_days_to_goal(10, 0), 0)
        self.assertEqual(example_days_to_goal(0, 0), 0)
        with self.assertRaises(ValueError):
            example_days_to_goal(0, 100)
        with self.assertRaises(ValueError):
            example_days_to_goal(-5, 50)

    def test_example_031(self) -> None:
        self.assertEqual(example_fizzbuzz(0), [])
        self.assertEqual(
            example_fizzbuzz(15),
            [
                "1",
                "2",
                "Fizz",
                "4",
                "Buzz",
                "Fizz",
                "7",
                "8",
                "Fizz",
                "Buzz",
                "11",
                "Fizz",
                "13",
                "14",
                "FizzBuzz",
            ],
        )

    def test_example_032(self) -> None:
        self.assertEqual(example_first_n_fibonacci(-2), [])
        self.assertEqual(example_first_n_fibonacci(0), [])
        self.assertEqual(example_first_n_fibonacci(1), [0])
        self.assertEqual(example_first_n_fibonacci(2), [0, 1])
        self.assertEqual(example_first_n_fibonacci(8), [0, 1, 1, 2, 3, 5, 8, 13])

    def test_example_033(self) -> None:
        self.assertEqual(example_divisors(36), [1, 2, 3, 4, 6, 9, 12, 18, 36])
        self.assertEqual(example_divisors(13), [1, 13])
        self.assertEqual(example_divisors(1), [1])
        self.assertEqual(example_divisors(0), [])
        self.assertEqual(example_divisors(-12), [])

    def test_example_034(self) -> None:
        self.assertEqual(example_count_primes_up_to(-5), 0)
        self.assertEqual(example_count_primes_up_to(1), 0)
        self.assertEqual(example_count_primes_up_to(2), 1)
        self.assertEqual(example_count_primes_up_to(10), 4)
        self.assertEqual(example_count_primes_up_to(100), 25)

    def test_example_035(self) -> None:
        self.assertEqual(example_gcd(48, 18), 6)
        self.assertEqual(example_gcd(13, 20), 1)
        self.assertEqual(example_gcd(-12, 18), 6)
        self.assertEqual(example_gcd(0, 7), 7)
        self.assertEqual(example_gcd(7, 0), 7)
        self.assertEqual(example_gcd(0, 0), 0)

    def test_example_036(self) -> None:
        self.assertEqual(example_multiplication_row(3, 5), [3, 6, 9, 12, 15])
        self.assertEqual(example_multiplication_row(0, 4), [0, 0, 0, 0])
        self.assertEqual(example_multiplication_row(5, 0), [])
        self.assertEqual(example_multiplication_row(5, -2), [])


class TestYourActivities(unittest.TestCase):
    """Verify student solutions for Module 03 (Activities 025-036)."""

    def test_activity_025(self) -> None:
        self.assertEqual(solve_sum_to_n(5), 15)
        self.assertEqual(solve_sum_to_n(1), 1)
        self.assertEqual(solve_sum_to_n(0), 0)
        self.assertEqual(solve_sum_to_n(-4), 0)
        self.assertEqual(solve_sum_to_n(100), 5050)

    def test_activity_026(self) -> None:
        self.assertEqual(solve_sum_multiples_3_or_5(10), 23)
        self.assertEqual(solve_sum_multiples_3_or_5(16), 60)
        self.assertEqual(solve_sum_multiples_3_or_5(20), 78)
        self.assertEqual(solve_sum_multiples_3_or_5(3), 0)
        self.assertEqual(solve_sum_multiples_3_or_5(0), 0)
        self.assertEqual(solve_sum_multiples_3_or_5(1000), 233168)

    def test_activity_027(self) -> None:
        self.assertEqual(solve_factorial(0), 1)
        self.assertEqual(solve_factorial(1), 1)
        self.assertEqual(solve_factorial(5), 120)
        self.assertEqual(solve_factorial(10), 3628800)
        with self.assertRaises(ValueError):
            solve_factorial(-1)
        with self.assertRaises(ValueError):
            solve_factorial(-10)

    def test_activity_028(self) -> None:
        self.assertEqual(solve_collatz_steps(1), 0)
        self.assertEqual(solve_collatz_steps(2), 1)
        self.assertEqual(solve_collatz_steps(6), 8)
        self.assertEqual(solve_collatz_steps(27), 111)
        with self.assertRaises(ValueError):
            solve_collatz_steps(0)
        with self.assertRaises(ValueError):
            solve_collatz_steps(-3)

    def test_activity_029(self) -> None:
        self.assertEqual(solve_digit_stats(4823), (17, 3))
        self.assertEqual(solve_digit_stats(-205), (7, 2))
        self.assertEqual(solve_digit_stats(0), (0, 1))
        self.assertEqual(solve_digit_stats(13579), (25, 0))
        self.assertEqual(solve_digit_stats(8), (8, 1))

    def test_activity_030(self) -> None:
        self.assertEqual(solve_months_to_payoff(100.0, 0.0, 30.0), 4)
        self.assertEqual(solve_months_to_payoff(100.0, 0.10, 60.0), 2)
        self.assertEqual(solve_months_to_payoff(0.0, 0.05, 50.0), 0)
        self.assertEqual(solve_months_to_payoff(-10.0, 0.05, 50.0), 0)
        with self.assertRaises(ValueError):
            solve_months_to_payoff(1000.0, 0.02, 20.0)
        with self.assertRaises(ValueError):
            solve_months_to_payoff(1000.0, 0.02, 15.0)
        with self.assertRaises(ValueError):
            solve_months_to_payoff(500.0, 0.0, 0.0)

    def test_activity_031(self) -> None:
        self.assertEqual(
            solve_fizzbuzzbazz(15),
            [
                "1",
                "2",
                "Fizz",
                "4",
                "Buzz",
                "Fizz",
                "Bazz",
                "8",
                "Fizz",
                "Buzz",
                "11",
                "Fizz",
                "13",
                "Bazz",
                "FizzBuzz",
            ],
        )
        self.assertEqual(solve_fizzbuzzbazz(0), [])
        self.assertEqual(
            solve_fizzbuzzbazz(12, fizz=2, buzz=3, bazz=4),
            [
                "1",
                "Fizz",
                "Buzz",
                "FizzBazz",
                "5",
                "FizzBuzz",
                "7",
                "FizzBazz",
                "Buzz",
                "Fizz",
                "11",
                "FizzBuzzBazz",
            ],
        )
        res_105 = solve_fizzbuzzbazz(105)
        self.assertIsInstance(res_105, list)
        self.assertEqual(res_105[20], "FizzBazz")
        self.assertEqual(res_105[34], "BuzzBazz")
        self.assertEqual(res_105[104], "FizzBuzzBazz")

    def test_activity_032(self) -> None:
        self.assertEqual(solve_fibonacci_up_to(-5), [])
        self.assertEqual(solve_fibonacci_up_to(0), [0])
        self.assertEqual(solve_fibonacci_up_to(1), [0, 1, 1])
        self.assertEqual(solve_fibonacci_up_to(10), [0, 1, 1, 2, 3, 5, 8])
        self.assertEqual(solve_fibonacci_up_to(13), [0, 1, 1, 2, 3, 5, 8, 13])

    def test_activity_033(self) -> None:
        for prime in (2, 3, 5, 7, 13, 97, 104729):
            self.assertIs(solve_is_prime(prime), True)
        for non_prime in (-7, 0, 1, 4, 9, 15, 25, 49, 121, 1000000):
            self.assertIs(solve_is_prime(non_prime), False)

    def test_activity_034(self) -> None:
        self.assertEqual(solve_primes_in_range(10, 30), [11, 13, 17, 19, 23, 29])
        self.assertEqual(solve_primes_in_range(1, 10), [2, 3, 5, 7])
        self.assertEqual(solve_primes_in_range(-5, 5), [2, 3, 5])
        self.assertEqual(solve_primes_in_range(14, 16), [])
        self.assertEqual(solve_primes_in_range(20, 10), [])
        self.assertEqual(solve_primes_in_range(2, 2), [2])
        self.assertEqual(solve_primes_in_range(0, 1), [])

    def test_activity_035(self) -> None:
        self.assertEqual(solve_lcm_and_fraction(12, 18), (36, (2, 3)))
        self.assertEqual(solve_lcm_and_fraction(7, 5), (35, (7, 5)))
        self.assertEqual(solve_lcm_and_fraction(10, 10), (10, (1, 1)))
        self.assertEqual(solve_lcm_and_fraction(4, 20), (20, (1, 5)))
        with self.assertRaises(ValueError):
            solve_lcm_and_fraction(0, 5)
        with self.assertRaises(ValueError):
            solve_lcm_and_fraction(5, 0)
        with self.assertRaises(ValueError):
            solve_lcm_and_fraction(-4, 6)

    def test_activity_036(self) -> None:
        self.assertEqual(
            solve_grid_and_pair_sums(4, 5),
            (
                [
                    [1, 2, 3, 4],
                    [2, 4, 6, 8],
                    [3, 6, 9, 12],
                    [4, 8, 12, 16],
                ],
                2,
            ),
        )
        self.assertEqual(
            solve_grid_and_pair_sums(3, 4),
            ([[1, 2, 3], [2, 4, 6], [3, 6, 9]], 1),
        )
        self.assertEqual(solve_grid_and_pair_sums(1, 2), ([[1]], 0))
        self.assertEqual(solve_grid_and_pair_sums(0, 5), ([], 0))
        self.assertEqual(solve_grid_and_pair_sums(-2, 3), ([], 0))


if __name__ == "__main__":
    unittest.main()
