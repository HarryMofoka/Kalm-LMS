"""
Activity 122: __str__, __repr__ & Clean Object Display
Difficulty: 122 / 132

Ever printed an object and seen `<MovieTicket object at 0x000001F3...>`?
Python gives every class two special display methods:
  - `__str__`:  friendly, readable text for end users (`print(obj)`, `str(obj)`).
  - `__repr__`: unambiguous developer text (`repr(obj)`), ideally valid Python
                that shows how to recreate the object!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — ExamplePoint
===============================================================================
Problem:
    Build `ExamplePoint(x, y)` with:
      - `self.x`, `self.y`
      - `__str__` -> `f"({self.x}, {self.y})"`
      - `__repr__` -> `f"ExamplePoint(x={self.x!r}, y={self.y!r})"`
      - `distance_to_origin()` -> Euclidean distance rounded to 2 decimals.

Step-by-Step Breakdown:
    1. Notice `{self.x!r}` in `__repr__`: the `!r` flag formats with `repr()`.
    2. When you put objects inside a list (`print([p1, p2])`), Python uses
       `__repr__` for each element, whereas `print(p1)` uses `__str__`!

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Temperature
===============================================================================
Problem:
    Implement `Temperature` for a weather station dashboard:
      - `__init__(self, celsius: float) -> None`
        * Stores `self.celsius = float(celsius)`.
      - `to_fahrenheit(self) -> float`
        * Returns `round(self.celsius * 9 / 5 + 32, 2)`.
      - `@classmethod def from_fahrenheit(cls, fahrenheit: float) -> Temperature`
        * Converts Fahrenheit to Celsius rounded to 2 decimal places:
              round((fahrenheit - 32) * 5 / 9, 2)
          and returns a new `cls(...)` instance!
      - `__str__(self) -> str`
        * Returns `f"{self.celsius:.1f}°C ({self.to_fahrenheit():.1f}°F)"`.
      - `__repr__(self) -> str`
        * Returns `f"Temperature(celsius={self.celsius!r})"`.

    Examples:
        t = Temperature(0)
        t.celsius                -> 0.0
        t.to_fahrenheit()        -> 32.0
        str(t)                   -> "0.0°C (32.0°F)"
        repr(t)                  -> "Temperature(celsius=0.0)"

        boiling = Temperature.from_fahrenheit(212)
        boiling.celsius          -> 100.0
        str(boiling)             -> "100.0°C (212.0°F)"

    Edge-case hints:
        - Check negative crossover: `-40°C == -40°F`!
        - `str()` and `repr()` MUST return `str` objects (never print directly!).
        - Using `cls(...)` inside `@classmethod` ensures subclasses work cleanly.
"""
from __future__ import annotations


class ExamplePoint:
    """A 2D coordinate with clean __str__ and __repr__ representations."""

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def distance_to_origin(self) -> float:
        """Return Euclidean distance from (0, 0) rounded to 2 decimals."""
        return round((self.x ** 2 + self.y ** 2) ** 0.5, 2)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"ExamplePoint(x={self.x!r}, y={self.y!r})"


class Temperature:
    """A temperature stored in Celsius with Fahrenheit conversion and clean display."""

    def __init__(self, celsius: float) -> None:
        """Store temperature as float Celsius."""
        pass

    def to_fahrenheit(self) -> float:
        """Convert self.celsius to Fahrenheit rounded to 2 decimals."""
        pass

    @classmethod
    def from_fahrenheit(cls, fahrenheit: float) -> Temperature:
        """Construct a Temperature from a Fahrenheit reading."""
        pass

    def __str__(self) -> str:
        """Return '<C:.1f>°C (<F:.1f>°F)'."""
        pass

    def __repr__(self) -> str:
        """Return 'Temperature(celsius=<value>)'."""
        pass


if __name__ == "__main__":
    p = ExamplePoint(3, 4)
    print("str :", str(p))
    print("repr:", repr(p))
    print("dist:", p.distance_to_origin())
