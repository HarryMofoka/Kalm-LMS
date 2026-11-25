"""
Activity 048: Template Placeholder Replacement  [Unlocks Checkpoint 08!]
Difficulty: 48 / 132

Context:
    Welcome to the Module 04 capstone! Email generators, web frameworks (like
    Jinja2 and Django), and report builders all scan template strings for
    placeholder tags and substitute values from a mapping—without accidentally
    re-expanding substituted values or crashing on malformed tags.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Single `{name}` Placeholder Replacer
===============================================================================
Problem:
    Replace every occurrence of `"{name}"` in `template` with `name`, using an
    explicit left-to-right scan (no `.replace()`).

Step-by-Step Explanation:
    1. Walk through `template` with an index `i = 0`, appending pieces to a
       `result` list.
    2. Whenever `template[i : i + len("{name}")] == "{name}"`, append `name`
       and advance `i += len("{name}")`.
    3. Otherwise, append `template[i]` and advance `i += 1`.
    4. Notice how a single left-to-right pass NEVER re-scans the inserted text!

Edge Cases:
    - `"Hello, {name}!"` with `"Ada"`          -> `"Hello, Ada!"`
    - `"{name} meets {name}"` with `"Bo"`      -> `"Bo meets Bo"`
    - `"No placeholder here"` with `"Ada"`     -> `"No placeholder here"`
    - `""` with `"Ada"`                        -> `""`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Multi-Key `{{var}}` Template Renderer
===============================================================================
Problem:
    Implement `solve_render_template(template: str, values: dict[str, str]) -> str`.
    Render `template` by replacing every `{{key}}` placeholder with `values[key]`
    according to these rules:
      1. Scan left-to-right in a SINGLE pass.
      2. When you encounter `"{{"`, look for the next closing `"}}"` at or after
         `i + 2` (using `template.find("}}", i + 2)`).
      3. If there is NO closing `"}}"`, keep the remaining text verbatim and stop.
      4. Otherwise, extract `key = template[i + 2 : close_idx].strip()`.
         - If `key` is in `values`, emit `str(values[key])`.
         - If `key` is NOT in `values`, leave the original placeholder slice
           `template[i : close_idx + 2]` untouched!
      5. Advance `i = close_idx + 2` so substituted values are NEVER re-scanned.

Examples:
    - `("Hi {{name}}, score: {{score}}!", {"name": "Ada", "score": "98"})`
      -> `"Hi Ada, score: 98!"`
    - `("Welcome {{ name }}!", {"name": "Kai"})`
      -> `"Welcome Kai!"`
    - `("Hello {{user}}, role={{role}}", {"user": "Sam"})`
      -> `"Hello Sam, role={{role}}"`
    - `("{{a}}", {"a": "{{b}}", "b": "WRONG"})`
      -> `"{{b}}"`  (single pass: does NOT recursively expand!)
    - `("Price: {{unclosed", {"unclosed": "10"})`
      -> `"Price: {{unclosed"`
    - `("", {"a": "1"})`
      -> `""`

Edge-Case Hints:
    - Why is a single-pass scanner better than looping `for k, v in values.items(): template = template.replace(...)`?
      1. It handles whitespace inside braces like `{{ name }}`.
      2. It avoids double-substitution when one value contains `"{{other_key}}"`.
"""

from __future__ import annotations


def example_fill_name(template: str, name: str) -> str:
    """Replace all occurrences of `{name}` in `template` using a single-pass scan."""
    placeholder = "{name}"
    size = len(placeholder)
    result: list[str] = []
    i = 0

    while i < len(template):
        if template[i : i + size] == placeholder:
            result.append(name)
            i += size
        else:
            result.append(template[i])
            i += 1
    return "".join(result)


def solve_render_template(template: str, values: dict[str, str]) -> str:
    """Render `{{key}}` placeholders in `template` using `values` in one pass."""
    pass


if __name__ == "__main__":
    print(example_fill_name("Welcome, {name}! Ready for the exam, {name}?", "Ada"))
