"""Worked Example — Global Conference Slot & Countdown Clock Formatter.

Demonstrates linear-minute time math, modulo-1440 wrapping, floor-division day
rollovers, and cascading countdown formatting.
"""

from __future__ import annotations

MINUTES_PER_DAY: int = 1440


def hm_to_minutes(hour: int, minute: int) -> int:
    """Convert a 24-hour (hour, minute) pair into minutes since midnight."""
    if not (0 <= hour <= 23):
        raise ValueError(f"Hour must be between 0 and 23, got {hour}.")
    if not (0 <= minute <= 59):
        raise ValueError(f"Minute must be between 0 and 59, got {minute}.")
    return hour * 60 + minute


def minutes_to_clock(total_minutes: int) -> str:
    """Format any integer minute count as a wrapped 24-hour 'HH:MM' string."""
    wrapped = total_minutes % MINUTES_PER_DAY
    hours = wrapped // 60
    minutes = wrapped % 60
    return f"{hours:02d}:{minutes:02d}"


def convert_timezone_slot(
    hour: int,
    minute: int,
    offset_minutes: int,
) -> tuple[str, int]:
    """Shift a UTC conference slot by offset_minutes.

    Returns:
        A (local_hh_mm, day_shift) tuple where day_shift is -1 (previous day),
        0 (same day), +1 (next day), etc.
    """
    raw_minutes = hm_to_minutes(hour, minute) + offset_minutes
    day_shift = raw_minutes // MINUTES_PER_DAY
    local_clock = minutes_to_clock(raw_minutes)
    return local_clock, day_shift


def format_countdown(total_minutes: int) -> str:
    """Format a non-negative minute duration as 'Xd HHh MMm' or 'HHh MMm'."""
    if total_minutes < 0:
        raise ValueError("Countdown duration cannot be negative.")
    days = total_minutes // MINUTES_PER_DAY
    remaining = total_minutes % MINUTES_PER_DAY
    hours = remaining // 60
    minutes = remaining % 60
    if days > 0:
        return f"{days}d {hours:02d}h {minutes:02d}m"
    return f"{hours:02d}h {minutes:02d}m"


if __name__ == "__main__":
    print("=== Global Keynote: 22:30 UTC ===")
    cities = [
        ("New York (UTC-5)", -300),
        ("Johannesburg (UTC+2)", +120),
        ("Tokyo (UTC+9)", +540),
    ]
    for city, offset in cities:
        local_time, day_delta = convert_timezone_slot(22, 30, offset)
        day_tag = f" ({day_delta:+d} day)" if day_delta != 0 else " (same day)"
        print(f"  {city:<22} -> {local_time}{day_tag}")

    print("\n=== Event Countdowns ===")
    for mins in (75, 1505):
        print(f"  {mins:>4} minutes -> {format_countdown(mins)}")
