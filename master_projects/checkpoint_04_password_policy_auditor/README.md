# Checkpoint 04 — Production Password Policy Auditor

- **Unlocked After:** Activity 024 (Complex Logic & Validation)
- **Difficulty:** Intermediate
- **Core Concepts:** Multi-rule validation without short-circuiting, defensive type checks (`TypeError`), boolean predicates (`any`, `all`), structured audit responses, score-to-tier classification

---

## Real-World Value

Every authentication platform — Auth0, Okta, AWS Cognito, Django's `AUTH_PASSWORD_VALIDATORS`, and banking signup flows — enforces security policies at account creation time.

Notice how terrible user experience is when a signup form returns only the **first** error ("Too short"), then after you fix it says ("Missing a digit"), then ("Missing a symbol")! Production policy engines follow two critical engineering principles:
1. **Strict Type Guards First:** Reject non-string payloads (`None`, `int`, `list`) immediately with `TypeError` before inspecting characters.
2. **Collect All Violations:** Evaluate every policy rule independently and return a structured report (`valid`, `strength`, and the complete `errors` list of machine-readable error codes) in a single pass.

---

## Problem Statement

Build a production-grade Password Policy Auditor in `project.py` that:

1. Classifies a numeric strength score (`0..100`) into `"weak"`, `"medium"`, or `"strong"` via `classify_strength(score)` while rejecting non-integer types (`TypeError`, including `bool`!) and out-of-range scores (`ValueError`).
2. Audits a candidate `password` (and optional `username`) via `audit_password(password, username="")`:
   - Rejects non-`str` inputs with `TypeError`.
   - Checks all 7 security rules without short-circuiting and collects every failing error code.
   - Scores the password deterministically and classifies its strength using `classify_strength`.
   - Returns `{"valid": bool, "strength": str, "errors": list[str]}`.

---

## How a Similar Functioning System Was Done (`worked_example.py`)

Before building the password auditor, inspect and run **`worked_example.py`** — a complete **Username & Handle Compliance Auditor**.

```bash
python master_projects/checkpoint_04_password_policy_auditor/worked_example.py
```

### Architectural Walkthrough

1. **Type Guard Before Logic:** `if not isinstance(username, str): raise TypeError(...)` ensures callers get a clear type error instead of a cryptic `AttributeError: 'int' object has no attribute 'lower'`.
2. **Independent `if` Blocks (Not `elif`!):** Each rule appends a standardized, machine-readable error code (`"too_short"`, `"reserved_handle"`, etc.) to `errors: list[str]`. Because the checks are independent `if` statements rather than `elif`, a handle like `"_1"` accurately reports both `"too_short"` and `"must_start_with_letter"`.
3. **Derived Validity Flag:** `"valid": len(errors) == 0` guarantees the boolean flag can never drift out of sync with the `errors` list.

### Traced Example (`worked_example.py`)

Call: `audit_username("1a__!")`

| Rule Checked | Result | Error Added |
|---|---|---|
| Length `>= 3` (`5 >= 3`) | Pass | — |
| Length `<= 20` (`5 <= 20`) | Pass | — |
| Starts with letter (`'1'.isalpha()` is `False`) | Fail | `"must_start_with_letter"` |
| Allowed chars only (`'!'` is invalid) | Fail | `"invalid_characters"` |
| No consecutive underscores (`"__"` present) | Fail | `"consecutive_underscores"` |
| Not reserved (`"1a__!"` not in reserved set) | Pass | — |
| **Output** | `score = max(0, 100 - 3 * 25) = 25` | `{"valid": False, "score": 25, "errors": ["must_start_with_letter", "invalid_characters", "consecutive_underscores"]}` |

---

## Your Project Brief (`project.py`)

Implement the following 2 functions in `project.py`:

### 1. `classify_strength(score: int) -> str`
- Raises `TypeError` if `score` is not an `int` or is a `bool` (`isinstance(score, bool)`).
- Raises `ValueError` if `score < 0` or `score > 100`.
- Returns:
  - `"weak"` when `score < 50`
  - `"medium"` when `50 <= score < 80`
  - `"strong"` when `score >= 80`

### 2. `audit_password(password: str, username: str = "") -> dict[str, Any]`
- Raises `TypeError` if `not isinstance(password, str)` or `not isinstance(username, str)`.
- Checks all 7 security rules and appends the exact error code whenever a rule fails:

| Rule | Condition to Pass | Error Code When Violated | Score Points |
|---|---|---|---|
| Min length | `len(password) >= 8` | `"too_short"` | `+20` (`+10` bonus if `len >= 12`) |
| Uppercase | Contains at least one `c.isupper()` | `"missing_uppercase"` | `+15` |
| Lowercase | Contains at least one `c.islower()` | `"missing_lowercase"` | `+15` |
| Digit | Contains at least one `c.isdigit()` | `"missing_digit"` | `+15` |
| Symbol | Contains at least one character where `not c.isalnum() and not c.isspace()` | `"missing_symbol"` | `+15` |
| No whitespace | Contains NO character where `c.isspace()` | `"contains_whitespace"` | `+10` |
| No username | If `username != ""`, `username.lower() not in password.lower()` | `"contains_username"` | `-20` penalty if violated |

- Clamp final `score` to `0..100` (`max(0, min(100, score))`).
- Returns:
  ```python
  {
      "valid": len(errors) == 0,
      "strength": classify_strength(score),
      "errors": errors,
  }
  ```

### Acceptance Criteria
- All 7 tests in `TestMasterProject` pass alongside the 5 tests in `TestWorkedExample`.
- Multiple violations are all reported in a single call.
- Non-string inputs to `audit_password` and non-int inputs to `classify_strength` raise `TypeError`.

### Fun Stretch Ideas (After Tests Pass)
- Add a check rejecting the top 20 most leaked common passwords (e.g. `"Password1!"`, `"Qwerty123!"`).
- Add a helper that maps each machine-readable error code to a friendly localized message for a web UI.

---

## Running Tests

Run from the `ExamPrep/` directory:

```bash
python -m unittest master_projects/checkpoint_04_password_policy_auditor/test_project.py -v
```
