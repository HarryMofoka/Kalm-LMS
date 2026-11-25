"""Messy blog slug and hashtag formatter — rescue this file!

It currently works and passes TestBehaviorSafetyNet, but builds strings
character-by-character with += inside loops, repeats ugly ASCII checks,
and hacks off trailing delimiters with [:-1] and [:-2].
"""


def format_slug_and_tags(title, tags):
    """Return a URL-friendly slug and formatted hashtag line.

    Rules:
        - Slug: lowercase alphanumeric words separated by single hyphens (`-`).
          Spaces, hyphens, underscores, tabs, and newlines act as word
          separators; other punctuation is dropped.
        - Tag line: each tag normalized with the same slug rules, ignoring any
          tag that becomes empty, prefixed with `#`, and separated by `, `.

    Returns:
        {"slug": <str>, "tag_line": <str>}
    """
    # Build slug character-by-character with manual ASCII checks and +=
    slug = ""
    prev_sep = True
    for ch in title:
        if ("a" <= ch <= "z") or ("A" <= ch <= "Z") or ("0" <= ch <= "9"):
            slug += ch.lower()
            prev_sep = False
        elif ch == " " or ch == "-" or ch == "_" or ch == "\t" or ch == "\n":
            if not prev_sep:
                slug += "-"
                prev_sep = True
    if len(slug) > 0 and slug[-1] == "-":
        slug = slug[:-1]

    # Copy-pasted loop to normalize every tag and stitch together with ", "
    tag_line = ""
    for raw_tag in tags:
        clean_tag = ""
        last_was_sep = True
        for ch in raw_tag:
            if ("a" <= ch <= "z") or ("A" <= ch <= "Z") or ("0" <= ch <= "9"):
                clean_tag += ch.lower()
                last_was_sep = False
            elif ch == " " or ch == "-" or ch == "_" or ch == "\t" or ch == "\n":
                if not last_was_sep:
                    clean_tag += "-"
                    last_was_sep = True
        if len(clean_tag) > 0 and clean_tag[-1] == "-":
            clean_tag = clean_tag[:-1]
        if clean_tag != "":
            tag_line = tag_line + "#" + clean_tag + ", "

    if len(tag_line) > 0:
        tag_line = tag_line[:-2]

    return {"slug": slug, "tag_line": tag_line}
