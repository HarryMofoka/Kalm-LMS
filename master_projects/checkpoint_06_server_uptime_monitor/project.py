"""Master Project — Checkpoint 06: Server Heartbeat & SLA Uptime Analyzer.

Implement the SRE uptime monitoring functions below according to README.md.
Each heartbeat entry is a bool: True means the server responded healthy,
False means the server failed the probe.
"""

from __future__ import annotations


def calculate_uptime_pct(heartbeats: list[bool]) -> float:
    """Calculate server uptime percentage rounded to 2 decimal places.

    Args:
        heartbeats: Chronological list of probe results (True = UP, False = DOWN).

    Returns:
        Percentage of True heartbeats rounded to 2 decimal places,
        or 0.0 if heartbeats is empty.
    """
    pass


def longest_outage_streak(heartbeats: list[bool]) -> int:
    """Find the longest consecutive run of failed (False) heartbeats.

    Args:
        heartbeats: Chronological list of probe results (True = UP, False = DOWN).

    Returns:
        Length of the longest consecutive False streak (0 if none or empty).
    """
    pass


def find_outage_windows(heartbeats: list[bool]) -> list[tuple[int, int]]:
    """Return inclusive (start_idx, end_idx) tuples for every contiguous outage.

    Args:
        heartbeats: Chronological list of probe results (True = UP, False = DOWN).

    Returns:
        List of (start_idx, end_idx) tuples in chronological order for every
        contiguous run of one or more False values. Empty list if no outages.
    """
    pass


def sla_report(
    heartbeats: list[bool],
    target_sla: float = 99.0,
) -> dict[str, object]:
    """Generate a full SRE SLA uptime and incident status report.

    Args:
        heartbeats: Chronological list of probe results (True = UP, False = DOWN).
        target_sla: Required minimum uptime percentage (default: 99.0).

    Returns:
        Dictionary with keys:
            - "total_checks" (int)
            - "up_checks" (int)
            - "down_checks" (int)
            - "uptime_pct" (float)
            - "target_sla" (float)
            - "sla_met" (bool): True if total_checks > 0 and uptime_pct >= target_sla
            - "longest_outage" (int)
            - "outage_windows" (list[tuple[int, int]])
            - "incident_count" (int): len(outage_windows)
            - "status" (str):
                "NO_DATA" if total_checks == 0;
                "HEALTHY" if sla_met and longest_outage < 3;
                "DEGRADED" if (sla_met and longest_outage >= 3)
                    or (not sla_met and uptime_pct >= target_sla - 5.0);
                "CRITICAL" if total_checks > 0 and uptime_pct < target_sla - 5.0.
    """
    pass
