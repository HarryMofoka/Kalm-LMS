"""Worked Example: App Audit Event Parser & Secret Redactor.

Demonstrates pipe-delimited event parsing, secret key-value redaction using
pure string operations, and fault-tolerant severity summarization.
"""

from __future__ import annotations

SENSITIVE_KEYS = {"api_key", "secret", "token"}
VALID_SEVERITIES = {"INFO", "WARN", "ERROR"}


def parse_audit_event(line: str) -> dict[str, str]:
    """Parse a pipe-delimited audit event line into structured fields.

    Expected format:
        timestamp | SEVERITY | service | message
    """
    parts = [part.strip() for part in line.split("|")]
    if len(parts) != 4:
        raise ValueError(f"Expected 4 pipe-delimited fields, got {len(parts)}")

    timestamp, severity, service, message = parts
    severity = severity.upper()

    if not timestamp:
        raise ValueError("Missing timestamp")
    if severity not in VALID_SEVERITIES:
        raise ValueError(f"Unsupported severity: {severity!r}")
    if not service:
        raise ValueError("Missing service name")

    return {
        "timestamp": timestamp,
        "severity": severity,
        "service": service,
        "message": message,
    }


def redact_secrets(text: str) -> str:
    """Redact api_key/secret/token key=value pairs in text, preserving last 4 chars."""
    tokens = text.split(" ")
    sanitized_tokens: list[str] = []

    for token in tokens:
        trailing = ""
        core = token
        while core and core[-1] in ",;":
            trailing = core[-1] + trailing
            core = core[:-1]

        if "=" in core:
            key, value = core.split("=", 1)
            if key.lower() in SENSITIVE_KEYS:
                if len(value) > 4:
                    redacted_val = "***" + value[-4:]
                else:
                    redacted_val = "****"
                sanitized_tokens.append(f"{key}={redacted_val}{trailing}")
                continue

        sanitized_tokens.append(token)

    return " ".join(sanitized_tokens)


def sanitize_audit_event(line: str) -> str:
    """Parse an audit event and return a clean line with secrets redacted."""
    event = parse_audit_event(line)
    clean_message = redact_secrets(event["message"])
    return (
        f"{event['timestamp']} | {event['severity']} | "
        f"{event['service']} | {clean_message}"
    )


def summarize_audit_events(lines: list[str]) -> dict[str, object]:
    """Summarize valid audit events by severity and track malformed lines."""
    by_severity = {"INFO": 0, "WARN": 0, "ERROR": 0}
    services: list[str] = []
    valid_count = 0
    malformed_count = 0

    for raw_line in lines:
        if not raw_line.strip():
            continue
        try:
            event = parse_audit_event(raw_line)
        except ValueError:
            malformed_count += 1
            continue

        valid_count += 1
        by_severity[event["severity"]] += 1
        if event["service"] not in services:
            services.append(event["service"])

    return {
        "total_events": valid_count,
        "by_severity": by_severity,
        "services": services,
        "malformed_count": malformed_count,
    }


if __name__ == "__main__":
    sample_events = [
        "2026-11-25 09:15:02 | INFO | billing | Charge ok api_key=sk_live_99812abx44",
        "2026-11-25 09:16:10 | WARN | auth | Retry limit hit token=tok_8821zz99,",
        "2026-11-25 09:17:44 | ERROR | payments | Gateway timeout secret=abcd",
        "corrupted line without pipes",
    ]
    print("=== Sanitized Audit Events ===")
    for event_line in sample_events[:3]:
        print(" ", sanitize_audit_event(event_line))
    print("\n=== Summary ===")
    print(" ", summarize_audit_events(sample_events))
