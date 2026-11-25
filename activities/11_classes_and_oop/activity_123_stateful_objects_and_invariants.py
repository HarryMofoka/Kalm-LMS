"""
Activity 123: Stateful Objects & Class Invariants
Difficulty: 123 / 132

An **invariant** is a safety promise an object NEVER breaks — at creation time
OR after any method call! For example, a fuel tank can never hold negative fuel
and can never exceed its maximum capacity.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — ExampleCounter
===============================================================================
Problem:
    Build `ExampleCounter(start=0, max_value=None)` enforcing the invariant:
        0 <= self.value (and self.value <= max_value if max_value is not None)
      - `__init__`: validates `start >= 0`, `max_value is None or max_value >= 0`,
        and `max_value is None or start <= max_value` (else raises `ValueError`).
      - `increment(amount=1) -> int`: rejects `amount < 0` or overflowing
        `max_value` with `ValueError`, updates `self.value`, and returns it.
      - `reset() -> None`: resets `self.value = 0`.

Step-by-Step Breakdown:
    1. Check invariants BEFORE mutating `self.value`! That way, if an invalid
       call raises `ValueError`, the object stays in its valid previous state.
    2. Never leave an object "half-updated" after an error.

===============================================================================
PART 2: YOUR TURN ("YOU DO") — FuelTank
===============================================================================
Problem:
    Implement `FuelTank` enforcing the invariant `0.0 <= self.fuel <= self.capacity`:
      - `__init__(self, capacity: float, fuel: float = 0.0) -> None`
        * Raises `ValueError` if `capacity <= 0` or `fuel < 0` or `fuel > capacity`.
        * Stores `self.capacity = float(capacity)` and `self.fuel = float(fuel)`.
      - `refuel(self, liters: float) -> float`
        * Raises `ValueError` if `liters <= 0` or `self.fuel + liters > self.capacity`.
        * Adds `liters` to `self.fuel` and returns updated `self.fuel`.
      - `drive(self, liters_needed: float) -> float`
        * Raises `ValueError` if `liters_needed <= 0` or `liters_needed > self.fuel`.
        * Subtracts `liters_needed` from `self.fuel` and returns remaining `self.fuel`.
      - `percent_full(self) -> float`
        * Returns `round((self.fuel / self.capacity) * 100, 1)`.

    Examples:
        tank = FuelTank(50, fuel=10)
        tank.refuel(15)      -> 25.0
        tank.percent_full()  -> 50.0
        tank.drive(5)        -> 20.0
        tank.refuel(40)      -> raises ValueError (20 + 40 > 50); tank.fuel stays 20.0!
        tank.drive(25)       -> raises ValueError (25 > 20); tank.fuel stays 20.0!

    Edge-case hints:
        - `refuel(0)` and `drive(0)` MUST raise `ValueError` (must be strictly `> 0`).
        - Filling to exact capacity (`fuel + liters == capacity`) IS allowed!
        - Driving to exact empty (`liters_needed == fuel`) IS allowed (`fuel` becomes `0.0`)!
"""
from __future__ import annotations


class ExampleCounter:
    """A bounded non-negative counter preserving 0 <= value <= max_value."""

    def __init__(self, start: int = 0, max_value: int | None = None) -> None:
        if start < 0:
            raise ValueError("start must be non-negative")
        if max_value is not None and (max_value < 0 or start > max_value):
            raise ValueError("invalid max_value for given start")
        self.value = start
        self.max_value = max_value

    def increment(self, amount: int = 1) -> int:
        """Increase counter by `amount`, raising ValueError if invalid or over max."""
        if amount < 0:
            raise ValueError("amount must be non-negative")
        if self.max_value is not None and self.value + amount > self.max_value:
            raise ValueError("counter would exceed max_value")
        self.value += amount
        return self.value

    def reset(self) -> None:
        """Reset counter back to 0."""
        self.value = 0


class FuelTank:
    """A vehicle fuel tank enforcing 0 <= fuel <= capacity on every operation."""

    def __init__(self, capacity: float, fuel: float = 0.0) -> None:
        """Initialize tank with positive capacity and 0 <= fuel <= capacity."""
        pass

    def refuel(self, liters: float) -> float:
        """Add positive liters without overflowing capacity; return updated fuel."""
        pass

    def drive(self, liters_needed: float) -> float:
        """Consume positive liters_needed without going below zero; return fuel."""
        pass

    def percent_full(self) -> float:
        """Return fuel level as a percentage rounded to 1 decimal place."""
        pass


if __name__ == "__main__":
    c = ExampleCounter(start=2, max_value=5)
    print("Initial:", c.value)
    print("After +3:", c.increment(3))
    c.reset()
    print("After reset:", c.value)
