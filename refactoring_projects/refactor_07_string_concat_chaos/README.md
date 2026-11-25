# Refactoring Mission 07 — String Concatenation Chaos (CP 07)

## Backstory & Problem Statement

A blogging platform's URL-slug and hashtag formatter (`format_slug_and_tags`) was written by hand using character-by-character string concatenation (`slug += ...`), copy-pasted ASCII range checks (`"a" <= ch <= "z"`), and fragile trailing-delimiter slicing (`tag_line = tag_line[:-2]`).

In Python, strings are **immutable**, so repeatedly concatenating inside a loop allocates a brand-new string on every step, clutters logic with separator-tracking flags, and leads to off-by-one trailing-comma bugs.

Your mission: clean up `messy_code.py` by replacing string concatenation loops and trailing-character slicing with `.join()`, clean string methods, and at least one reusable helper function!

## Code Smells Checklist

- [ ] **Repeated `+=` / `+` string concatenation inside loops** instead of collecting pieces and calling `sep.join(...)`.
- [ ] **Trailing delimiter hacks** like `slug = slug[:-1]` and `tag_line = tag_line[:-2]`.
- [ ] **Manual ASCII character comparisons** (`"a" <= ch <= "z" or "A" <= ch <= "Z" or "0" <= ch <= "9"`) instead of `.isalnum()` / `.lower()`.
- [ ] **Copy-pasted normalization logic** repeated for both `title` and every item in `tags` instead of an extracted helper (e.g., `slugify` or `normalize_tag`).

## Worked Refactoring Walkthrough (Before -> After)

Open [`worked_example.py`](worked_example.py) to compare a CSV row builder before and after refactoring:

### Before (`before_build_csv`)
```python
def before_build_csv(fields):
    row = ""
    for item in fields:
        cleaned = str(item).strip()
        if cleaned != "":
            row = row + cleaned + ","
    if len(row) > 0:
        row = row[:-1]
    return row
```

### After (`after_build_csv`)
```python
def after_build_csv(fields):
    cleaned_fields = [str(item).strip() for item in fields if str(item).strip()]
    return ",".join(cleaned_fields)
```

With `",".join(...)`, there is no manual `row = row + ...`, no trailing comma to slice off, and empty inputs work automatically!

## Your Refactoring Mission

Refactor [`messy_code.py`](messy_code.py) so that `format_slug_and_tags(title, tags)`:

1. **Uses `.join(...)`** to assemble the hyphen-separated slug and `", "`-separated tag line.
2. **Eliminates string `+=` / `s = s + ...` concatenation inside loops**.
3. **Eliminates manual trailing-delimiter slicing** (`[:-1]`, `[:-2]`).
4. **Extracts at least one clean helper function** (such as `slugify(text)` and/or `normalize_tag(tag)`) so title and tag normalization share clean, readable code.
5. **Preserves 100% identical behavior** across all `TestBehaviorSafetyNet` tests!

## Run the Tests

Run from the `ExamPrep` directory:

```bash
python -m unittest refactoring_projects/refactor_07_string_concat_chaos/test_refactor.py -v
```
