"""
Activity 003: Unit Conversion & Speed Math
Difficulty: 3 / 132 (Rank 1 - Absolute Beginner)

Context:
In 1999, NASA lost the $125 million Mars Climate Orbiter because one team used
metric units while another used imperial units! Writing dedicated, tested
conversion functions prevents unit bugs in weather apps, fitness trackers, and
navigation systems.

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
Write `example_celsius_to_fahrenheit(celsius)` to convert a temperature from
degrees Celsius to degrees Fahrenheit, rounded to 2 decimal places.

Formula:
    F = C * 9 / 5 + 32

Step-by-step walkthrough:
1. Multiply `celsius` by `9 / 5` (which is `1.8`). Because `*` and `/` have
   higher precedence than `+`, `celsius * 9 / 5 + 32` evaluates the product
   and division left-to-right before adding `32`.
2. Wrap the result with `round(..., 2)` so floating-point quirks like
   `98.60000000000001` cleanly become `98.6`.
3. Return the rounded float.

Edge cases:
- `0` °C -> `32.0` °F (freezing point of water).
- `100` °C -> `212.0` °F (boiling point of water).
- `-40` °C -> `-40.0` °F (the magical point where both scales meet!).

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
You are building a dashboard for a European electric car exported to the US.
The trip computer records distance in `kilometers` and trip duration in `hours`
(assume `hours > 0`). Write `solve_trip_speed_conversion(kilometers, hours)`
that converts the trip into miles and average speed in miles per hour (mph),
returning `(miles, mph)` with both values rounded to 2 decimal places.

Conversion constant:
    `KM_TO_MILES = 0.621371`

Rules:
- Compute `raw_miles = kilometers * 0.621371`.
- Compute `raw_mph = raw_miles / hours` using the UNROUNDED `raw_miles` so you
  avoid compounding rounding errors!
- Return `(round(raw_miles, 2), round(raw_mph, 2))`.

Examples:
- `solve_trip_speed_conversion(100, 2)` -> `(62.14, 31.07)`
- `solve_trip_speed_conversion(0, 1.5)` -> `(0.0, 0.0)`
- `solve_trip_speed_conversion(160.9344, 1)` -> `(100.0, 100.0)`

Hints:
- Define `KM_TO_MILES = 0.621371` as a clear local constant inside your function.
- Always round at the very end, right before returning.
"""

from __future__ import annotations


def example_celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius temperature to Fahrenheit, rounded to 2 decimal places."""
    # Python 3 `/` always performs true (floating-point) division.
    fahrenheit = (celsius * 9 / 5) + 32
    return round(fahrenheit, 2)


def solve_trip_speed_conversion(
    kilometers: float, hours: float
) -> tuple[float, float]:
    """Convert (kilometers, hours) to (miles, mph), each rounded to 2 decimals."""
    pass


if __name__ == "__main__":
    print("0 C in F:", example_celsius_to_fahrenheit(0))
    print("37 C in F:", example_celsius_to_fahrenheit(37))
    print("-40 C in F:", example_celsius_to_fahrenheit(-40))
