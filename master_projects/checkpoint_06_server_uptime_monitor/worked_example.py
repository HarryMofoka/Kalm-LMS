"""Worked Example: IoT Weather Station Sensor Health Analyzer.

Demonstrates loop-based streak tracking, contiguous error-window detection,
percentage analytics, and structured health report generation for a real-world
IoT telemetry stream.
"""

from __future__ import annotations


def is_valid_reading(
    reading: float | None,
    min_valid: float = -50.0,
    max_valid: float = 60.0,
) -> bool:
    """Return True if a sensor temperature reading is present and within bounds."""
    if reading is None:
        return False
    return min_valid <= reading <= max_valid


def calculate_health_pct(
    readings: list[float | None],
    min_valid: float = -50.0,
    max_valid: float = 60.0,
) -> float:
    """Return the percentage of valid readings, rounded to 2 decimal places.

    Returns 0.0 when no readings are provided.
    """
    if not readings:
        return 0.0

    valid_count = 0
    for reading in readings:
        if is_valid_reading(reading, min_valid, max_valid):
            valid_count += 1

    return round((valid_count / len(readings)) * 100.0, 2)


def longest_error_streak(
    readings: list[float | None],
    min_valid: float = -50.0,
    max_valid: float = 60.0,
) -> int:
    """Return the length of the longest consecutive run of invalid readings."""
    longest = 0
    current = 0

    for reading in readings:
        if not is_valid_reading(reading, min_valid, max_valid):
            current += 1
            if current > longest:
                longest = current
        else:
            current = 0

    return longest


def find_error_bursts(
    readings: list[float | None],
    min_burst: int = 2,
    min_valid: float = -50.0,
    max_valid: float = 60.0,
) -> list[tuple[int, int]]:
    """Find inclusive (start_idx, end_idx) windows of invalid readings >= min_burst."""
    bursts: list[tuple[int, int]] = []
    burst_start: int | None = None

    for idx, reading in enumerate(readings):
        if not is_valid_reading(reading, min_valid, max_valid):
            if burst_start is None:
                burst_start = idx
        else:
            if burst_start is not None:
                burst_end = idx - 1
                if (burst_end - burst_start + 1) >= min_burst:
                    bursts.append((burst_start, burst_end))
                burst_start = None

    # Close a burst that runs all the way to the end of the stream.
    if burst_start is not None:
        burst_end = len(readings) - 1
        if (burst_end - burst_start + 1) >= min_burst:
            bursts.append((burst_start, burst_end))

    return bursts


def sensor_health_summary(
    readings: list[float | None],
    alert_threshold_streak: int = 3,
    min_health_pct: float = 90.0,
) -> dict[str, object]:
    """Build a complete IoT weather station health summary dictionary."""
    total = len(readings)
    valid = sum(1 for r in readings if is_valid_reading(r))
    errors = total - valid
    health_pct = calculate_health_pct(readings)
    max_streak = longest_error_streak(readings)
    bursts = find_error_bursts(readings, min_burst=2)

    if total == 0:
        status = "NO_DATA"
        alert_triggered = True
    elif max_streak >= alert_threshold_streak or health_pct < min_health_pct - 15.0:
        status = "CRITICAL"
        alert_triggered = True
    elif health_pct < min_health_pct or len(bursts) > 0:
        status = "WARNING"
        alert_triggered = True
    else:
        status = "HEALTHY"
        alert_triggered = False

    return {
        "total_readings": total,
        "valid_readings": valid,
        "error_readings": errors,
        "health_pct": health_pct,
        "longest_error_streak": max_streak,
        "error_bursts": bursts,
        "alert_triggered": alert_triggered,
        "status": status,
    }


if __name__ == "__main__":
    sample_readings: list[float | None] = [
        21.4, 21.8, None, None, None, 22.1, 22.5, 999.9, 23.0, 22.8,
        22.3, 21.9, None, None, 21.5, 21.2, 20.8, 20.5, 20.1, 19.9,
    ]
    report = sensor_health_summary(sample_readings)
    print("=== IoT Weather Station Sensor Health Report ===")
    for key, value in report.items():
        print(f"  {key:22s}: {value}")
