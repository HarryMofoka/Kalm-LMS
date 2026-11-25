"""Messy comment moderation monolith — rescue this file!

It currently works and passes TestBehaviorSafetyNet, but jams whitespace
collapsing, shout-case detection, punctuation stripping, banned-word
censoring, and status classification into one huge unreadable function.
"""


def moderate_comment(text, banned_words):
    """Clean and moderate a user comment.

    Returns a dict with:
        - "cleaned_text": normalized comment with outer token punctuation
          stripped and banned words replaced by "***"
        - "flagged_count": number of censored banned words
        - "is_shouting": True if >= 4 letters and > 70% of letters are uppercase
        - "status": "empty" | "flagged" | "warning" | "ok"
    """
    # 1. Collapse all whitespace runs into single spaces
    collapsed = ""
    prev_space = True
    for ch in text:
        if ch in (" ", "\t", "\n", "\r"):
            if not prev_space:
                collapsed += " "
                prev_space = True
        else:
            collapsed += ch
            prev_space = False
    if len(collapsed) > 0 and collapsed[-1] == " ":
        collapsed = collapsed[:-1]

    if collapsed == "":
        return {
            "cleaned_text": "",
            "flagged_count": 0,
            "is_shouting": False,
            "status": "empty",
        }

    # 2. Detect shout-case before stripping or censoring
    alpha_count = 0
    upper_count = 0
    for ch in collapsed:
        if ch.isalpha():
            alpha_count += 1
            if ch.isupper():
                upper_count += 1
    is_shouting = alpha_count >= 4 and (upper_count / alpha_count) > 0.7

    # 3. Strip edge punctuation from each token and drop empty tokens
    punct_chars = ".,!?;:\"'()[]"
    raw_tokens = collapsed.split(" ")
    clean_tokens = []
    for tok in raw_tokens:
        start = 0
        end = len(tok)
        while start < end and tok[start] in punct_chars:
            start += 1
        while end > start and tok[end - 1] in punct_chars:
            end -= 1
        stripped = tok[start:end]
        if stripped != "":
            clean_tokens.append(stripped)

    if len(clean_tokens) == 0:
        return {
            "cleaned_text": "",
            "flagged_count": 0,
            "is_shouting": False,
            "status": "empty",
        }

    # 4. Normalize banned word list and censor matching tokens
    normalized_banned = set()
    for word in banned_words:
        w = word.strip().strip(punct_chars).lower()
        if w != "":
            normalized_banned.add(w)

    censored_tokens = []
    flagged_count = 0
    for tok in clean_tokens:
        if tok.lower() in normalized_banned:
            censored_tokens.append("***")
            flagged_count += 1
        else:
            censored_tokens.append(tok)

    # 5. Classify moderation status and return summary
    cleaned_text = " ".join(censored_tokens)
    if flagged_count > 0:
        status = "flagged"
    elif is_shouting:
        status = "warning"
    else:
        status = "ok"

    return {
        "cleaned_text": cleaned_text,
        "flagged_count": flagged_count,
        "is_shouting": is_shouting,
        "status": status,
    }
