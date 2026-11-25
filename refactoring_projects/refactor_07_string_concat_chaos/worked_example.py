"""Worked Example for RF 07: CSV Row Builder (manual + & slicing -> join)."""


def before_build_csv(fields):
    """Messy version: builds CSV with repeated + concatenation and [:-1] slicing."""
    row = ""
    for item in fields:
        cleaned = str(item).strip()
        if cleaned != "":
            row = row + cleaned + ","
    if len(row) > 0:
        row = row[:-1]
    return row


def after_build_csv(fields):
    """Clean version: strips values and joins non-empty fields with ','."""
    cleaned_fields = [str(item).strip() for item in fields if str(item).strip()]
    return ",".join(cleaned_fields)


if __name__ == "__main__":
    sample = ["  Alice  ", "", "  Python 101 ", 42, "   "]
    print("Input: ", sample)
    print("Before:", repr(before_build_csv(sample)))
    print("After: ", repr(after_build_csv(sample)))
