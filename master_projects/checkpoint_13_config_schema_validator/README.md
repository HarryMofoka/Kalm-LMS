# Checkpoint 13 — Production Config Schema Validator

- **Unlocked After:** Activity 078 — Functions, Validation Contracts & Exceptions
- **Difficulty:** Intermediate
- **Core Concepts:** Validation pipelines, defensive type checks (`bool` vs `int`), default merging, error aggregation, non-mutating contracts

---

## Real-World Value

One of the costliest outage patterns in backend engineering is a service booting cleanly with a misconfigured setting (`port: "8080"`, `workers: true`, `retries: -5`, or a typo like `tmeout: 30`) and only crashing **three hours later** during peak traffic.

Production tools like **Pydantic**, **JSON Schema**, **FastAPI**, and **CI config linters** solve this by validating the entire configuration payload upfront against a declarative schema — applying defaults safely and reporting **every** validation error in one structured result rather than failing blindly on the first typo.

---

## Problem Statement

You are building a declarative **Production Config Schema Validator** for microservices. Given a raw `config` dictionary and a `schema` dictionary describing field constraints (`type`, `required`, `default`, `min`, `max`, `choices`), your validator must:

1. Validate individual fields (`validate_field`), explicitly catching Python's classic `isinstance(True, int) == True` trap.
2. Fill in missing defaults without mutating input dictionaries or overwriting existing falsy values like `0`, `False`, or `""` (`apply_defaults`).
3. Orchestrate full config validation (`validate_config`), checking required keys, field rules, and optional rejection of unknown keys, returning `{"valid": bool, "errors": list[str], "resolved": dict}`.

---

## How a Similar Functioning System Was Done (`worked_example.py`)

Explore and run the sibling system in [`worked_example.py`](./worked_example.py): an **Environment Variable Preflight Checker**.

Run it from `ExamPrep/`:

```bash
python master_projects/checkpoint_13_config_schema_validator/worked_example.py
```

### Architecture & Key Patterns Demonstrated

1. **Dedicated Parsing Function (`parse_env_value`)**:
   - Separates string-to-type conversion (`str`, `int`, `float`, `bool`) from policy checks so each function has one focused responsibility and clear `ValueError` diagnostics.
2. **Per-Key Validation Contract (`check_env_var`)**:
   - Checks required presence first, then parses, then checks enum `choices`. Returns a clean `(parsed_value, error_message)` tuple instead of crashing mid-scan.
3. **Collect-All-Errors Preflight (`preflight_check`)**:
   - Iterates deterministically over sorted spec keys and gathers **every** misconfiguration before returning `{"ok": bool, "errors": list[str], "config": dict}` — saving operators from fixing one boot error at a time.

---

## Your Project Brief (`project.py`)

Implement the three functions in [`project.py`](./project.py):

### 1. `validate_field(name: str, value: object, rule: dict) -> list[str]`
Validates a single field's `value` against `rule`, returning a `list[str]` of human-readable error messages (empty list `[]` if valid). Every error message **must include the field `name`**.

Supported optional keys in `rule`:
- `"type"`: expected Python type (e.g., `int`, `float`, `str`, `bool`, `list`, `dict`).
  - **CRITICAL:** In Python, `bool` is a subclass of `int` (`isinstance(True, int)` is `True`!).
  - When `rule["type"] is int`: accept `isinstance(value, int) and not isinstance(value, bool)`. Reject `True`/`False`!
  - When `rule["type"] is float`: accept `isinstance(value, (int, float)) and not isinstance(value, bool)`. Reject `True`/`False`!
  - When `rule["type"] is bool`: accept only `isinstance(value, bool)`.
  - For all other types: accept `isinstance(value, expected_type)`.
  - If the type check fails, record a type error mentioning `name` and **return immediately** for this field (so range comparisons like `"abc" < 1` never crash with `TypeError`).
- `"min"`: inclusive minimum bound (`value < rule["min"]` produces an error mentioning `name`).
- `"max"`: inclusive maximum bound (`value > rule["max"]` produces an error mentioning `name`).
- `"choices"`: collection of allowed values (`value not in rule["choices"]` produces an error mentioning `name`).

```python
validate_field("workers", True, {"type": int, "min": 1})
# -> ["workers: expected int, got bool"]  (any clear message containing "workers")

validate_field("port", 8080, {"type": int, "min": 1024, "max": 65535})
# -> []
```

### 2. `apply_defaults(config: dict, schema: dict[str, dict]) -> dict`
- Returns a **new** dictionary starting with all key-value pairs from `config`.
- For each `field_name, rule` in `schema`: if `field_name` is **not** in `config` AND `"default"` is in `rule`, insert `field_name: rule["default"]`.
- **Never** overwrite an existing key in `config`, even when its value is falsy (`0`, `False`, `""`, or `None`).
- **Must not mutate** `config` or `schema`.

### 3. `validate_config(config: dict, schema: dict[str, dict], allow_unknown: bool = False) -> dict`
- Must **not** mutate `config` or `schema`.
- Computes `resolved = apply_defaults(config, schema)`.
- Collects all `errors: list[str]`:
  1. For each `name, rule` in `schema`:
     - If `name` is not in `resolved`:
       - If `rule.get("required", False)` is `True`, append an error mentioning `name` (e.g., `f"{name}: missing required field"`).
       - Otherwise skip (optional field with no default).
     - Else:
       - Extend `errors` with `validate_field(name, resolved[name], rule)`.
  2. If `allow_unknown` is `False`:
     - For each key in `resolved` that is not in `schema` (in sorted order), append an error mentioning the unknown key (e.g., `f"{key}: unknown field"`).
- Returns:
  ```python
  {
      "valid": len(errors) == 0,
      "errors": errors,
      "resolved": resolved,
  }
  ```

---

## Running the Tests

From inside the `ExamPrep/` directory:

```bash
python -m unittest master_projects/checkpoint_13_config_schema_validator/test_project.py -v
```

- `TestWorkedExample` passes immediately.
- `TestMasterProject` starts red and passes once you complete `project.py`.
