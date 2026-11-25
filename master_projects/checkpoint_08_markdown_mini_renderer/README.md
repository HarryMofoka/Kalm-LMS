# Checkpoint 08 — Mini Markdown & Template Renderer

- **Unlocked After:** Activity 048 *(Text Processing & Template Engines)*
- **Difficulty:** ★★★☆☆ (Intermediate)
- **Core Concepts:** Multi-stage text pipelines, delimiter scanning (`{{var}}`, `` `code` ``, `**bold**`), stateful line-by-line block rendering, strict vs fallback template resolution

---

## Real-World Value

Every developer uses text rendering engines daily:

- **Static Site Generators & Docs:** Hugo, MkDocs, Jekyll, GitHub README renderers, and Notion/Slack message formatters turn human-friendly Markdown into clean HTML.
- **Transactional Template Engines:** Jinja2, Mustache, Handlebars, and SendGrid Dynamic Templates inject runtime variables (`{{ customer_name }}`, `{{ invoice_id }}`) into reusable notification templates.

Building a mini template + Markdown engine teaches you how real compilers and renderers work: splitting a hard text problem into **clean, composable stages** (variable substitution -> block structure parsing -> inline formatting).

---

## Problem Statement

Build a Mini Markdown & Template Renderer that:
1. Substitutes `{{ key }}` placeholders with whitespace tolerance and configurable strict vs default missing-key behavior.
2. Converts inline Markdown (`` `code` `` and `**bold**`) to HTML (`<code>...</code>` and `<strong>...</strong>`) without corrupting bold markers inside inline code spans.
3. Renders an entire Markdown document containing `# H1`, `## H2`, `- unordered list items`, and paragraphs into clean, well-formed HTML lines.

---

## How a Similar Functioning System Was Done (`worked_example.py`)

Study [`worked_example.py`](worked_example.py) — a **Transactional Email Template Engine**.

E-commerce and SaaS platforms send plain-text emails (receipts, password resets, shipping updates) that must fill in `{{ variable }}` placeholders and cleanly wrap paragraphs to 72 characters so email clients display them neatly.

### Key Architectural Patterns in `worked_example.py`

1. **Cursor-Based Placeholder Scanner (`substitute_placeholders`):**
   Uses `str.find("{{", cursor)` and `str.find("}}", start)` to walk left-to-right in a single linear pass — avoiding fragile chained `.replace()` bugs (for example, when a substituted value itself contains `{{`!).
2. **Explicit Strict vs Fallback Policy:**
   When `default is None`, missing placeholders raise `KeyError(key)` immediately (fail-fast in production builds). When a fallback `default` is supplied, missing keys resolve safely to `default`.
3. **Zero-Trailing-Space Word Wrapping (`wrap_paragraph`):**
   Splits text into words and greedily packs lines up to `width` characters, preserving paragraph breaks inside `render_template(template, context, ...)`.

Run the reference demo:

```bash
python master_projects/checkpoint_08_markdown_mini_renderer/worked_example.py
```

---

## Your Project Brief (`project.py`)

Implement the three functions in [`project.py`](project.py).

### 1. `render_placeholders(text: str, values: dict[str, object], strict: bool = True, default: str = "") -> str`
- Scan `text` left-to-right for `{{...}}` placeholders.
- Trim whitespace inside braces so `{{name}}` and `{{  name  }}` both look up `"name"`.
- Convert matched values using `str(values[key])`.
- If `key` is missing from `values`:
  - When `strict=True`: raise `KeyError(key)`.
  - When `strict=False`: substitute `default` (defaults to `""`).
- If an unclosed `{{` has no matching `}}`, leave the remaining text untouched as literal characters.

### 2. `convert_inline_markdown(text: str) -> str`
- Convert inline formatting into HTML:
  - `` `code` `` -> `<code>code</code>`
  - `**bold**` -> `<strong>bold</strong>`
- **Code-span protection:** Anything inside backticks `` `...` `` is literal code — e.g. `` `**not bold**` `` must render as `<code>**not bold**</code>`, NOT with `<strong>` tags!
- **Unmatched delimiters:** A lone `` ` `` or lone `**` with no closing partner stays literal plain text.
- **Empty spans:** Empty `` `` `` or `****` stay literal (or only wrap non-empty spans). Multiple spans on the same line must all be converted.

### 3. `render_markdown_document(md_text: str, values: dict[str, object] | None = None, strict: bool = True, default: str = "") -> str`
- **Stage 1 (Optional Template Pass):** If `values is not None`, first run `render_placeholders(md_text, values, strict=strict, default=default)`.
- **Stage 2 (Line-by-Line Block Rendering):** Process `.splitlines()`:
  - Strip leading/trailing whitespace on each line (`stripped = line.strip()`).
  - **Blank lines** (`stripped == ""`): close any currently open `<ul>` list (`"</ul>"`), then skip.
  - **H2 Headings** (`stripped.startswith("## ")`): close open `<ul>` if needed; emit `f"<h2>{convert_inline_markdown(stripped[3:].strip())}</h2>"`.
  - **H1 Headings** (`stripped.startswith("# ")`): close open `<ul>` if needed; emit `f"<h1>{convert_inline_markdown(stripped[2:].strip())}</h1>"`.
  - **List Items** (`stripped.startswith("- ")`): if not currently in a list, emit `"<ul>"`; then emit `f"<li>{convert_inline_markdown(stripped[2:].strip())}</li>"`.
  - **Paragraphs** (any other non-empty line): close open `<ul>` if needed; emit `f"<p>{convert_inline_markdown(stripped)}</p>"`.
- **Stage 3 (Finalize):** Close any open `<ul>` at end-of-document and join all HTML lines with `"\n"` (returns `""` for empty/whitespace-only documents).

#### Example Output
Input:
```markdown
# Hello, {{ user }}!

## Quick Start

Run `pytest` for **fast** feedback.

- Supports **bold**
- Supports `inline_code`
```
With `values={"user": "Naledi"}`:
```html
<h1>Hello, Naledi!</h1>
<h2>Quick Start</h2>
<p>Run <code>pytest</code> for <strong>fast</strong> feedback.</p>
<ul>
<li>Supports <strong>bold</strong></li>
<li>Supports <code>inline_code</code></li>
</ul>
```

---

## Running Tests

From the `ExamPrep/` directory:

```bash
python -m unittest master_projects/checkpoint_08_markdown_mini_renderer/test_project.py -v
```
