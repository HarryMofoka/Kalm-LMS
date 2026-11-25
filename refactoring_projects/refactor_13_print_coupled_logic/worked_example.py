"""Worked Example for CP 13: Decoupling computation & formatting from print().

Compare:
- ``before_print_summary``: mixes calculations and formatting directly inside print().
- ``after_format_summary`` + ``after_print_summary``: pure formatting helper + thin wrapper.
"""

from typing import List, Sequence, Tuple


def before_print_summary(sales: Sequence[Tuple[str, float]]) -> None:
    """Messy version: computes totals and prints everything directly."""
    print("=== DAILY SALES ===")
    if len(sales) == 0:
        print("No sales recorded.")
        return

    total = 0.0
    best_item = ""
    best_amount = -1.0
    for item, amount in sales:
        total += amount
        if amount > best_amount:
            best_amount = amount
            best_item = item
        print(f"- {item}: ${amount:.2f}")

    print("-------------------")
    print(f"Transactions: {len(sales)}")
    print(f"Total Revenue: ${total:.2f}")
    print(f"Average Sale: ${total / len(sales):.2f}")
    print(f"Top Item: {best_item} (${best_amount:.2f})")


def after_format_summary(sales: Sequence[Tuple[str, float]]) -> List[str]:
    """Clean pure function: computes summary and returns lines without printing."""
    lines: List[str] = ["=== DAILY SALES ==="]
    if not sales:
        lines.append("No sales recorded.")
        return lines

    total = sum(amount for _, amount in sales)
    best_item, best_amount = max(sales, key=lambda entry: entry[1])

    for item, amount in sales:
        lines.append(f"- {item}: ${amount:.2f}")

    lines.extend(
        [
            "-------------------",
            f"Transactions: {len(sales)}",
            f"Total Revenue: ${total:.2f}",
            f"Average Sale: ${total / len(sales):.2f}",
            f"Top Item: {best_item} (${best_amount:.2f})",
        ]
    )
    return lines


def after_print_summary(sales: Sequence[Tuple[str, float]]) -> None:
    """Thin I/O wrapper that delegates all formatting to the pure helper."""
    print("\n".join(after_format_summary(sales)))


if __name__ == "__main__":
    sample_sales = [("Coffee", 4.50), ("Sandwich", 9.25), ("Muffin", 3.75)]
    print("--- BEFORE ---")
    before_print_summary(sample_sales)
    print("\n--- AFTER ---")
    after_print_summary(sample_sales)
    print("\nReusable pure lines:", after_format_summary(sample_sales))
