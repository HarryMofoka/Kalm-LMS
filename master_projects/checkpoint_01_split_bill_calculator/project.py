"""Checkpoint 01 — Restaurant Bill, Tax, Tip & Fair Group Splitter.

Implement each function below according to its docstring and README.md.
Run the tests with:
    python -m unittest master_projects/checkpoint_01_split_bill_calculator/test_project.py -v
"""

from __future__ import annotations


def calculate_tax(subtotal: float, tax_rate_pct: float) -> float:
    """Return the sales tax on subtotal, rounded to 2 decimal places.

    Raises:
        ValueError: If subtotal < 0 or tax_rate_pct < 0.
    """
    pass


def calculate_tip(subtotal: float, tip_pct: float) -> float:
    """Return the tip calculated on the pre-tax subtotal, rounded to 2 decimal places.

    Raises:
        ValueError: If subtotal < 0 or tip_pct < 0.
    """
    pass


def split_bill(
    subtotal: float,
    tax_rate_pct: float,
    tip_pct: float,
    num_people: int,
) -> dict[str, float | int]:
    """Compute a restaurant bill breakdown and fair integer-cent split.

    Args:
        subtotal: Pre-tax meal subtotal (>= 0).
        tax_rate_pct: Sales tax rate as a percentage (>= 0).
        tip_pct: Tip rate as a percentage of pre-tax subtotal (>= 0).
        num_people: Number of diners sharing the bill (integer >= 1).

    Returns:
        A dict with keys:
            - "subtotal": rounded subtotal (float)
            - "tax": calculated tax (float)
            - "tip": calculated tip (float)
            - "total": rounded subtotal + tax + tip (float)
            - "per_person": base equal share floored to exact cents (float)
            - "remainder_cents": leftover cents after equal division (int)

    Raises:
        ValueError: If monetary/rate inputs are negative or num_people < 1 (or non-int/bool).
    """
    pass


def format_receipt_line(label: str, amount: float, width: int = 30) -> str:
    """Format a fixed-width receipt line with left-aligned label and right-aligned price.

    Formats non-negative amounts as "$X.XX" and negative amounts as "-$X.XX".
    Maintains at least one space between label and the formatted amount even if
    the combined length meets or exceeds width.
    """
    pass
