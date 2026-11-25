"""Master Project — Checkpoint 10: Cinema Seat Grid & Group Allocator.

Implement the pure (non-mutating) 2D cinema seat booking functions below
according to README.md.
"""

from __future__ import annotations

OPEN_SEAT = "O"
BOOKED_SEAT = "X"


def create_seat_map(rows: int, cols: int) -> list[list[str]]:
    """Create a rows x cols 2D seat map filled with 'O' (no row aliasing).

    Args:
        rows: Number of rows (must satisfy 1 <= rows <= 26 for labels A..Z).
        cols: Number of seats per row (must be >= 1).

    Returns:
        Independent 2D list of 'O' strings.

    Raises:
        ValueError: If rows is outside 1..26 or cols < 1.
    """
    pass


def book_seat(
    seat_map: list[list[str]],
    row: int,
    col: int,
) -> list[list[str]]:
    """Return a new 2D seat map with (row, col) booked as 'X' (non-mutating).

    Args:
        seat_map: Existing 2D seat grid (must not be mutated).
        row: 0-based row index.
        col: 0-based column index.

    Returns:
        New 2D list with seat (row, col) set to 'X'.

    Raises:
        ValueError: If (row, col) is out of bounds (including negative indices)
            or if the seat is already booked ('X').
    """
    pass


def find_contiguous_seats(
    seat_map: list[list[str]],
    group_size: int,
) -> tuple[int, int] | None:
    """Find the first (row, start_col) with group_size consecutive 'O' seats.

    Scans rows top-to-bottom (0..rows-1) and columns left-to-right.

    Args:
        seat_map: Current 2D seat grid.
        group_size: Number of adjacent seats needed in the same row (>= 1).

    Returns:
        (row, start_col) of the first available contiguous block, or None if
        no single row has enough contiguous open seats.

    Raises:
        ValueError: If group_size < 1.
    """
    pass


def book_group(
    seat_map: list[list[str]],
    group_size: int,
) -> tuple[list[list[str]], tuple[int, int]]:
    """Allocate and book the first contiguous block of group_size open seats.

    Args:
        seat_map: Existing 2D seat grid (must not be mutated).
        group_size: Number of adjacent seats to book (>= 1).

    Returns:
        Tuple of (updated_seat_map, (row, start_col)) with the group marked 'X'.

    Raises:
        ValueError: If group_size < 1 or no contiguous block of size group_size
            is available.
    """
    pass


def occupancy_stats(seat_map: list[list[str]]) -> dict[str, object]:
    """Compute cinema occupancy metrics from a 2D seat map.

    Args:
        seat_map: Current 2D seat grid.

    Returns:
        Dictionary with keys:
            - "total_seats" (int)
            - "booked_seats" (int)
            - "available_seats" (int)
            - "occupancy_pct" (float): rounded to 2 decimal places (0.0 if empty)
            - "full_rows" (int): count of non-empty rows where all seats are 'X'
    """
    pass


def render_seat_map(seat_map: list[list[str]]) -> str:
    """Render the cinema seat map with row labels A, B, C... and zero trailing spaces.

    Example:
        A: O X X O
        B: O O O O

    Args:
        seat_map: Current 2D seat grid.

    Returns:
        Multi-line ASCII map joined by '\\n', or '' if seat_map is empty.
    """
    pass
