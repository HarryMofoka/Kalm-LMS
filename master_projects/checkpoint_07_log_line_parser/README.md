# Checkpoint 07 — Web Access Log Parser & PII Sanitizer

- **Unlocked After:** Activity 042 *(Strings, Parsing & Sanitization)*
- **Difficulty:** ★★☆☆☆ (Intermediate)
- **Core Concepts:** Delimited string parsing, strict field validation, PII/secret redaction, batch log aggregation

---

## Real-World Value

Modern web platforms powered by **Nginx, Apache, Envoy, and AWS API Gateway** generate millions of structured access log lines every hour. Observability pipelines (ELK Stack, Datadog Logs, Grafana Loki) must perform two vital jobs at once:

1. **Performance & Reliability Analytics:** Parse raw log text into typed fields to spot HTTP 4xx/5xx error spikes, measure average latency, and pinpoint the slowest API endpoint.
2. **Privacy & Security Compliance (GDPR / POPIA / SOC 2):** Scrub Personally Identifiable Information (PII) like customer email addresses and leaked credentials (`token=...`, `api_key=...`) **before** logs hit searchable dashboards or third-party storage.

In this checkpoint, you will build a clean, resilient Web Access Log Parser & PII Sanitizer.

---

## Problem Statement

Given pipe-delimited web access log lines such as:

```text
2026-11-25 14:22:01 | GET | /api/users | 200 | 42ms | user=alice@mail.com token=tok_live_987
```

build a parsing, PII-masking, and log-summarization module that validates malformed entries, safely masks emails and redacts secrets, and aggregates traffic metrics across an entire log batch without crashing on corrupt lines.

---

## How a Similar Functioning System Was Done (`worked_example.py`)

Study [`worked_example.py`](worked_example.py) — an **App Audit Event Parser & Secret Redactor**.

Microservices emit audit events like:

```text
2026-11-25 09:15:02 | WARN | auth-service | Failed call api_key=sk_live_99812abx44 for tenant=acme
```

### Key Architectural Patterns in `worked_example.py`

1. **Strict Structural Validation (`parse_audit_event`):**
   Splits on `"|"`, verifies the exact expected column count, trims whitespace, normalizes severity to uppercase, and raises `ValueError` on corrupt records.
2. **Token-Aware Secret Redaction (`redact_secrets`):**
   Scans whitespace-separated tokens for sensitive `key=value` pairs (`api_key`, `secret`, `token`), preserves trailing punctuation like `,` or `;`, and replaces the secret portion while leaving non-sensitive metadata untouched.
3. **Fault-Tolerant Batch Summarization (`summarize_audit_events`):**
   Real log streams always contain occasional truncated or malformed lines. Instead of crashing the whole job, the aggregator catches `ValueError` per line and increments `malformed_count` so engineers know data quality dropped.

Run the reference demo:

```bash
python master_projects/checkpoint_07_log_line_parser/worked_example.py
```

---

## Your Project Brief (`project.py`)

Implement the four functions in [`project.py`](project.py).

### Standard Log Line Format
```text
<timestamp> | <METHOD> | <endpoint> | <status_code> | <latency>ms | <metadata>
```
Example:
```text
2026-11-25 14:22:01 | GET | /api/users | 200 | 42ms | user=alice@mail.com
```

### 1. `parse_log_line(line: str) -> dict[str, object]`
- Split `line` by `"|"` and strip whitespace from each part. Must have **exactly 6 fields**; otherwise raise `ValueError`.
- Validate each field (raising `ValueError` on failure):
  - `timestamp`: non-empty string
  - `method`: non-empty string (normalized to uppercase, e.g. `"get"` -> `"GET"`)
  - `endpoint`: non-empty string starting with `"/"`
  - `status_code`: integer in range `100 <= status_code <= 599`
  - `latency_ms`: raw field must end with `"ms"` (case-insensitive) and the numeric part must be an integer `>= 0`
  - `metadata`: stripped string (may be empty `""`)
- Return a dictionary with keys:
  `"timestamp"`, `"method"`, `"endpoint"`, `"status_code"`, `"latency_ms"`, `"metadata"`.

### 2. `mask_email(email: str) -> str`
- Strip surrounding whitespace.
- Validate that `email` contains **exactly one** `"@"`, has a non-empty local part before `"@"`, and a non-empty domain after `"@"` containing at least one `"."` (and not starting or ending with `"."`). Otherwise raise `ValueError`.
- Mask the local part by keeping **only its first character** followed by `"***"` and `"@" + domain`:
  - `"alice@mail.com"` -> `"a***@mail.com"`
  - `"z@co.za"` -> `"z***@co.za"`
  *(Using a fixed `***` instead of matching the exact character count prevents leaking username length!)*

### 3. `sanitize_log_line(line: str) -> str`
- Inspect whitespace-separated tokens across the line (preserving `" "` joining and trailing `,` or `;` punctuation on tokens):
  - Any `key=value` token where `key.lower()` is in `{"token", "api_key", "secret", "password"}` must have its value replaced with `"[REDACTED]"` (e.g. `token=abc123` -> `token=[REDACTED]`).
  - Any `key=value` token whose `value` is a valid email address must have `value` masked using `mask_email` (e.g. `user=alice@mail.com` -> `user=a***@mail.com`).
  - Any standalone token that is a valid email address must be masked using `mask_email` (e.g. `alice@mail.com` -> `a***@mail.com`).
  - All other tokens remain unchanged.

### 4. `summarize_logs(lines: list[str]) -> dict[str, object]`
- Iterate through `lines`:
  - Ignore blank / whitespace-only lines.
  - Parse each non-empty line via `parse_log_line`. If parsing raises `ValueError`, skip it and increment `"malformed_count"`.
- Return a dictionary with exact keys:
  - `"total_requests"` (`int`): count of valid parsed requests
  - `"error_count"` (`int`): count of valid requests with `status_code >= 400`
  - `"avg_latency_ms"` (`float`): mean latency rounded to 2 decimal places (`0.0` if `total_requests == 0`)
  - `"max_latency_ms"` (`int`): highest single-request latency (`0` if `total_requests == 0`)
  - `"slowest_endpoint"` (`str | None`): endpoint of the request with the highest `latency_ms` (if tied, first seen wins; `None` if `total_requests == 0`)
  - `"malformed_count"` (`int`): count of non-empty lines that failed parsing

---

## Running Tests

From the `ExamPrep/` directory:

```bash
python -m unittest master_projects/checkpoint_07_log_line_parser/test_project.py -v
```
