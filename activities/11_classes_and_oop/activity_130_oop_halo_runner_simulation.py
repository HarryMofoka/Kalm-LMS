"""
Activity 130: OOP HaloRunner Simulation Class
Difficulty: 130 / 132

In Module 10, every runner function recomputed its path from scratch on each call.
With OOP, a `HaloRunner` object remembers its track (`path`), its current step
counter, its completed laps, and can `step()` forward or backward and `reset()`!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — ExampleClock (Modulo Simulation Object)
===============================================================================
Problem:
    Build `ExampleClock(hour=0, minute=0)` that tracks elapsed minutes on a
    24-hour (1,440-minute) cycle:
      - `tick(minutes=1) -> str`: advances the clock by `minutes` (must be >= 0)
        and returns `"HH:MM"`.
      - `days_elapsed` (`@property`): full 24-hour cycles completed.
      - `formatted() -> str`: current `"HH:MM"` display.
      - `reset() -> None`: returns clock to `00:00` and 0 days elapsed.

Step-by-Step Breakdown:
    1. Store ONE single source of truth: `self._total_minutes`!
    2. Derive EVERYTHING else via floor division (`//`) and modulo (`%`):
         - `days_elapsed = self._total_minutes // 1440`
         - `day_minute = self._total_minutes % 1440`
         - `hour, minute = divmod(day_minute, 60)`
    3. Single source of truth = ZERO risk of `hour`, `minute`, and `days` ever
       getting out of sync!

===============================================================================
PART 2: YOUR TURN ("YOU DO") — HaloRunner(path)
===============================================================================
Problem:
    Implement `HaloRunner` for simulating a runner on ANY perimeter path
    (square, rectangle, triangle, diamond — anything!):
      - `__init__(self, path: list[tuple[int, int]]) -> None`
        * Raises `ValueError` if `path` is empty.
        * Stores a defensive copy `self._path = list(path)` (so mutating the
          caller's list later cannot corrupt the runner!).
        * Starts at step counter `0` (index `0`, `path[0]`).
      - `@property def position(self) -> tuple[int, int]`
        * Returns current `(row, col)` cell: `self._path[self._steps % len(self._path)]`.
      - `@property def index(self) -> int`
        * Returns current path index `0 .. len(self._path) - 1`.
      - `@property def laps_completed(self) -> int`
        * Returns full laps completed from the origin:
              abs(self._steps) // len(self._path)
      - `step(self, n: int = 1) -> tuple[int, int]`
        * Advances the runner by `n` steps (`n` may be positive clockwise,
          zero, or negative counter-clockwise!), and returns the new `self.position`.
      - `reset(self) -> None`
        * Resets step count back to `0` (back at `path[0]`, `laps_completed == 0`).

    Examples:
        track = [(0, 0), (0, 1), (1, 1), (1, 0)]  # 4-cell square
        runner = HaloRunner(track)
        runner.position         -> (0, 0)
        runner.laps_completed   -> 0
        runner.step()           -> (0, 1)
        runner.step(4)          -> (0, 1)   # 5 total steps -> 1 full lap!
        runner.laps_completed   -> 1
        runner.reset()
        runner.position         -> (0, 0)
        runner.step(-1)         -> (1, 0)   # wraps counter-clockwise!
        runner.laps_completed   -> 0

    Edge-case hints:
        - Mutating the original `track` list AFTER creating `HaloRunner(track)`
          must NOT alter the runner's path!
        - `HaloRunner([])` MUST raise `ValueError`.
"""
from __future__ import annotations


class ExampleClock:
    """A 24-hour clock powered by a single modulo counter."""

    MINUTES_PER_DAY = 24 * 60

    def __init__(self, hour: int = 0, minute: int = 0) -> None:
        if not (0 <= hour < 24 and 0 <= minute < 60):
            raise ValueError("hour must be 0..23 and minute must be 0..59")
        self._total_minutes = hour * 60 + minute

    @property
    def days_elapsed(self) -> int:
        """Number of complete 24-hour days elapsed."""
        return self._total_minutes // self.MINUTES_PER_DAY

    def formatted(self) -> str:
        """Return current time formatted as 'HH:MM'."""
        day_minutes = self._total_minutes % self.MINUTES_PER_DAY
        hour, minute = divmod(day_minutes, 60)
        return f"{hour:02d}:{minute:02d}"

    def tick(self, minutes: int = 1) -> str:
        """Advance clock by non-negative `minutes` and return formatted time."""
        if minutes < 0:
            raise ValueError("minutes must be non-negative")
        self._total_minutes += minutes
        return self.formatted()

    def reset(self) -> None:
        """Reset clock to 00:00 on day 0."""
        self._total_minutes = 0


class HaloRunner:
    """An OOP runner moving around any non-empty coordinate path with lap tracking."""

    def __init__(self, path: list[tuple[int, int]]) -> None:
        """Store a defensive copy of non-empty `path` and start at step 0."""
        pass

    @property
    def position(self) -> tuple[int, int]:
        """Return current (row, col) coordinate on the path."""
        pass

    @property
    def index(self) -> int:
        """Return current wrapped index in 0..len(path)-1."""
        pass

    @property
    def laps_completed(self) -> int:
        """Return total complete laps away from start: abs(steps) // len(path)."""
        pass

    def step(self, n: int = 1) -> tuple[int, int]:
        """Move `n` steps (positive CW or negative CCW) and return new position."""
        pass

    def reset(self) -> None:
        """Reset runner back to step 0."""
        pass


if __name__ == "__main__":
    clock = ExampleClock(23, 45)
    print("Start:", clock.formatted(), "days:", clock.days_elapsed)
    print("+30m :", clock.tick(30), "days:", clock.days_elapsed)
    clock.reset()
    print("Reset:", clock.formatted(), "days:", clock.days_elapsed)
