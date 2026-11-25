# Refactoring Mission 08 — Messy Text Cleaner (CP 08)

## Backstory & Problem Statement

A community forum's comment moderator (`moderate_comment`) grew organically over six months into a single **60-line wall of tangled code**. Whitespace collapsing, shout-case detection, punctuation stripping, banned-word censoring (`***`), and status classification are all jammed together in one function with shared mutable counters and deeply nested loops.

Whenever a teammate wants to tweak just one rule — say, changing the shouting threshold or adding a punctuation character — they have to wade through the entire monolith and pray they don't break anything else.

Your mission: decompose `moderate_comment(text, banned_words)` into **focused, single-purpose helper functions** where every function is concise (25 lines or fewer) and reads like a clean pipeline!

## Code Smells Checklist

- [ ] **Long monolithic function (~60 lines)** doing five distinct jobs in one block.
- [ ] **Mixed levels of abstraction** — character-level whitespace scanning sits right next to high-level moderation policy rules.
- [ ] **Zero helper functions** — impossible to test or reuse individual steps like whitespace normalization or shout detection.
- [ ] **Hard-to-follow state flags** (`in_space`, `alpha_count`, `upper_count`, `flagged`) living in one giant scope.

## Worked Refactoring Walkthrough (Before -> After)

Open [`worked_example.py`](worked_example.py) to compare an email message normalizer before and after breaking it into single-purpose helpers:

### Before (`before_clean_message`)
One long function manually cleans whitespace on every line, skips blank lines, strips repeated `RE:` / `FWD:` prefixes from the subject line, and rejoins the text.

### After (`after_clean_message`)
```python
def normalize_line(line):
    return " ".join(line.split())


def strip_reply_prefixes(subject):
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
    lines = [normalize_line(line) for line in raw_message.splitlines()]
    return [line for line in lines if line]


def after_clean_message(raw_message):
    lines = extract_nonempty_lines(raw_message)
    if not lines:
        return ""
    lines[0] = strip_reply_prefixes(lines[0])
    return "\n".join(line for line in lines if line)
```

Read `after_clean_message`: you can understand the entire pipeline in 5 seconds because each step delegates to a focused, well-named helper!

## Your Refactoring Mission

Refactor [`messy_code.py`](messy_code.py) so that:

1. **`moderate_comment(text, banned_words)` is decomposed into at least 3 clean helper functions** (at least **4 total functions** in `messy_code.py`), for example:
   - `collapse_whitespace(text)`
   - `is_shouting_text(text)`
   - `strip_punctuation_tokens(text)`
   - `censor_tokens(tokens, banned_words)`
2. **`moderate_comment` delegates directly to your helpers** (calling at least 3 helper functions defined in the module).
3. **No single function in `messy_code.py` exceeds 25 lines** (including its `def` line and docstring).
4. **All `TestBehaviorSafetyNet` tests remain 100% GREEN!**

## Run the Tests

Run from the `ExamPrep` directory:

```bash
python -m unittest refactoring_projects/refactor_08_messy_text_cleaner/test_refactor.py -v
```
