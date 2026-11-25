"""Worked Example for RF 08: Email Normalizer (monolith -> focused helpers)."""


def before_clean_message(raw_message):
    """Messy version: mixes whitespace cleanup, blank-line filtering, and prefix stripping."""
    raw_lines = raw_message.splitlines()
    cleaned_lines = []
    for raw_line in raw_lines:
        piece = ""
        in_space = False
        for ch in raw_line.strip():
            if ch in (" ", "\t"):
                if not in_space:
                    piece += " "
                    in_space = True
            else:
                piece += ch
                in_space = False
        if piece != "":
            cleaned_lines.append(piece)

    if len(cleaned_lines) == 0:
        return ""

    first = cleaned_lines[0]
    changed = True
    while changed:
        changed = False
        upper_first = first.upper()
        if upper_first.startswith("RE:"):
            first = first[3:].lstrip()
            changed = True
        elif upper_first.startswith("FWD:"):
            first = first[4:].lstrip()
            changed = True
    cleaned_lines[0] = first

    final_lines = []
    for line in cleaned_lines:
        if line != "":
            final_lines.append(line)
    return "\n".join(final_lines)


def normalize_line(line):
    """Collapse internal runs of whitespace and trim outer spaces."""
    return " ".join(line.split())


def strip_reply_prefixes(subject):
    """Strip leading RE: and FWD: markers (case-insensitive) from a subject line."""
    cleaned = subject
    while True:
        upper = cleaned.upper()
        if upper.startswith("RE:"):
            cleaned = cleaned[3:].lstrip()
        elif upper.startswith("FWD:"):
            cleaned = cleaned[4:].lstrip()
        else:
            return cleaned


def extract_nonempty_lines(raw_message):
    """Normalize each line and drop empty lines."""
    normalized = [normalize_line(line) for line in raw_message.splitlines()]
    return [line for line in normalized if line]


def after_clean_message(raw_message):
    """Clean version: readable 5-line pipeline delegating to single-purpose helpers."""
    lines = extract_nonempty_lines(raw_message)
    if not lines:
        return ""
    lines[0] = strip_reply_prefixes(lines[0])
    return "\n".join(line for line in lines if line)


if __name__ == "__main__":
    sample_email = (
        "   Re:   FWD:  Exam   Schedule   Update  \n"
        "\n"
        "   Hi   everyone,\t\n"
        "   The   lab   starts   at   10:00.  \n"
        "   \n"
    )
    print("=== Before ===")
    print(before_clean_message(sample_email))
    print("=== After ===")
    print(after_clean_message(sample_email))
