"""
Activity 129: Inheritance & Shared Base Classes
Difficulty: 129 / 132

When multiple classes share common structure and logic — like `SquareHaloShape`
and `RectangleHaloShape` both having a `name`, `perimeter_count()`, and
`summary()` — **inheritance** lets you put the shared behavior ONCE in a base
class and override ONLY the shape-specific method (`border_cells()`) in each
subclass!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — ExampleAnimal Hierarchy
===============================================================================
Problem:
    Build a base class `ExampleAnimal(name)` with:
      - `speak() -> str`: abstract hook raising `NotImplementedError`.
      - `describe() -> str`: shared method calling `self.speak()`!
    And subclasses `ExampleDog` & `ExampleCat` overriding `speak()`.

Step-by-Step Breakdown:
    1. `super().__init__(name)` delegates base initialization cleanly.
    2. Notice **polymorphism**: `describe()` lives ONLY on `ExampleAnimal`,
       yet calling `dog.describe()` invokes `ExampleDog.speak()` and
       `cat.describe()` invokes `ExampleCat.speak()`!

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Shape, SquareHaloShape & RectangleHaloShape
===============================================================================
Problem:
    Implement a 3-class halo-shape hierarchy:

    1. `Shape` (base class):
       - `__init__(self, name: str) -> None`: stores `self.name = name`.
       - `border_cells(self) -> list[tuple[int, int]]`: raises `NotImplementedError`.
       - `perimeter_count(self) -> int`: returns `len(self.border_cells())`
         (shared method — subclasses inherit it for free!).
       - `summary(self) -> str`: returns `f"{self.name}: {self.perimeter_count()} border cells"`.

    2. `SquareHaloShape(Shape)`:
       - `__init__(self, size: int) -> None`
         * Raises `ValueError` if `size <= 0`.
         * Calls `super().__init__(f"Square({size})")` and stores `self.size = size`.
       - `border_cells(self) -> list[tuple[int, int]]`
         * Returns the clockwise outline coordinates starting at `(0, 0)` with
           ZERO duplicate cells (`size == 1` -> `[(0, 0)]`).

    3. `RectangleHaloShape(Shape)`:
       - `__init__(self, width: int, height: int) -> None`
         * Raises `ValueError` if `width <= 0` or `height <= 0`.
         * Calls `super().__init__(f"Rectangle({width}x{height})")` and stores
           `self.width = width`, `self.height = height`.
       - `border_cells(self) -> list[tuple[int, int]]`
         * Returns the clockwise outline coordinates starting at `(0, 0)` with
           ZERO duplicate cells (handles thin `4x1`, `1x3`, `1x1`!).

    Examples:
        sq = SquareHaloShape(3)
        isinstance(sq, Shape)    -> True
        sq.perimeter_count()     -> 8
        sq.summary()             -> "Square(3): 8 border cells"

        rect = RectangleHaloShape(4, 1)
        rect.border_cells()      -> [(0, 0), (0, 1), (0, 2), (0, 3)]
        rect.perimeter_count()   -> 4
        rect.summary()           -> "Rectangle(4x1): 4 border cells"

    Edge-case hints:
        - Do NOT re-implement `perimeter_count()` or `summary()` in subclasses —
          inherit them directly from `Shape`!
        - Calling `Shape("generic").border_cells()` MUST raise `NotImplementedError`.
"""
from __future__ import annotations


class ExampleAnimal:
    """Base class demonstrating shared behavior + polymorphic speak() hook."""

    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        """Subclasses must override this method."""
        raise NotImplementedError("Subclasses must implement speak()")

    def describe(self) -> str:
        """Shared concrete method that relies on the subclass's speak()."""
        return f"{self.name} says '{self.speak()}'"


class ExampleDog(ExampleAnimal):
    """Dog subclass of ExampleAnimal."""

    def __init__(self, name: str) -> None:
        super().__init__(name)

    def speak(self) -> str:
        return "Woof!"


class ExampleCat(ExampleAnimal):
    """Cat subclass of ExampleAnimal."""

    def __init__(self, name: str) -> None:
        super().__init__(name)

    def speak(self) -> str:
        return "Meow!"


class Shape:
    """Base class for halo shapes sharing perimeter_count() and summary()."""

    def __init__(self, name: str) -> None:
        """Store shape name."""
        pass

    def border_cells(self) -> list[tuple[int, int]]:
        """Return clockwise border coordinates (subclasses must override)."""
        pass

    def perimeter_count(self) -> int:
        """Return number of unique border cells using self.border_cells()."""
        pass

    def summary(self) -> str:
        """Return '<name>: <count> border cells'."""
        pass


class SquareHaloShape(Shape):
    """A size x size square halo inheriting from Shape."""

    def __init__(self, size: int) -> None:
        """Validate size > 0, call super().__init__(f'Square({size})'), store size."""
        pass

    def border_cells(self) -> list[tuple[int, int]]:
        """Return clockwise square outline cells from (0, 0) with no duplicates."""
        pass


class RectangleHaloShape(Shape):
    """A width x height rectangle halo inheriting from Shape."""

    def __init__(self, width: int, height: int) -> None:
        """Validate positive dimensions, call super().__init__, store width & height."""
        pass

    def border_cells(self) -> list[tuple[int, int]]:
        """Return clockwise rectangle outline cells (thin-shape safe, no duplicates)."""
        pass


if __name__ == "__main__":
    pets: list[ExampleAnimal] = [ExampleDog("Rex"), ExampleCat("Pixel")]
    for pet in pets:
        print(pet.describe())
