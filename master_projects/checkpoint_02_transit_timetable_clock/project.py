"""Checkpoint 02 — City Bus & Train Wrap-Around Timetable Engine.

Implement each function below according to its docstring and README.md.
Run the tests with:
    python -m unittest master_projects/checkpoint_02_transit_timetable_clock/test_project.py -v
"""

from __future__ import annotations

MINUTES_PER_DAY: int = 1440


def to_minutes(hour: int, minute: int) -> int:
    """Convert 24-hour (hour, minute) into total minutes since midnight (0..1439).

    Raises:
        ValueError: If hour is outside 0..23 or minute is outside 0..59.
    """
    pass


def format_clock_24h(total_minutes: int) -> str:
    """Format total_minutes as a zero-padded 'HH:MM' 24-hour string (mod 1440)."""
    pass


def arrival_time(
    depart_hour: int,
    depart_minute: int,
    duration_minutes: int,
) -> tuple[str, int]:
    """Compute arrival clock string and days_later for a trip.

    Args:
        depart_hour: Departure hour (0..23).
        depart_minute: Departure minute (0..59).
        duration_minutes: Non-negative trip duration in minutes.

    Returns:
        Tuple of (hh_mm_str, days_later).

    Raises:
        ValueError: If departure time is invalid or duration_minutes < 0.
    """
    pass


def trip_duration_minutes(
    depart_hour: int,
    depart_minute: int,
    arrive_hour: int,
    arrive_minute: int,
) -> int:
    """Return shortest non-negative trip duration in minutes, wrapping overnight.

    Raises:
        ValueError: If either clock time is out of range.
    """
    pass


def next_departure(
    current_hour: int,
    current_minute: int,
    frequency_minutes: int,
    first_hour: int = 0,
    first_minute: int = 0,
) -> tuple[str, int]:
    """Compute the next scheduled departure time and wait minutes.

    Departures run every `frequency_minutes` starting at (first_hour, first_minute).
    If current time is at or before the first departure, returns the first departure.
    If current time lands exactly on a departure, wait_minutes is 0.

    Returns:
        Tuple of (next_departure_hh_mm, wait_minutes).

    Raises:
        ValueError: If any time is invalid or frequency_minutes <= 0.
    """
    pass
