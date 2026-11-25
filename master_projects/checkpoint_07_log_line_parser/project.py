"""Master Project — Checkpoint 07: Web Access Log Parser & PII Sanitizer.

Implement the web access log parsing, email masking, PII/secret redaction,
and batch summarization functions below according to README.md.
"""

from __future__ import annotations

SENSITIVE_KEYS = {"token", "api_key", "secret", "password"}


def parse_log_line(line: str) -> dict[str, object]:
    """Parse a pipe-delimited web access log line into a typed dictionary.

    Expected format:
        "2026-11-25 14:22:01 | GET | /api/users | 200 | 42ms | user=alice@mail.com"

    Args:
        line: Raw access log line.

    Returns:
        Dictionary with keys:
            - "timestamp" (str)
            - "method" (str, uppercase)
            - "endpoint" (str, starts with "/")
            - "status_code" (int, 100..599)
            - "latency_ms" (int, >= 0)
            - "metadata" (str)

    Raises:
        ValueError: If the line does not have 6 valid pipe-delimited fields.
    """
    pass


def mask_email(email: str) -> str:
    """Mask an email's local part, keeping only its first character and domain.

    Example:
        "alice@mail.com" -> "a***@mail.com"
        "z@co.za"        -> "z***@co.za"

    Args:
        email: Email address string to mask.

    Returns:
        Masked email string in the format "<first_char>***@<domain>".

    Raises:
        ValueError: If email is malformed (missing '@', empty local/domain,
            multiple '@', or domain missing a valid '.').
    """
    pass


def sanitize_log_line(line: str) -> str:
    """Mask embedded email addresses and redact sensitive tokens in a log line.

    Rules:
        - Tokens of the form key=value where key.lower() is in SENSITIVE_KEYS
          ("token", "api_key", "secret", "password") become "key=[REDACTED]".
        - Tokens of the form key=email have the email portion masked via mask_email.
        - Standalone email tokens are masked via mask_email.
        - Trailing ',' or ';' punctuation on tokens is preserved.

    Args:
        line: Raw log line containing potential PII or secrets.

    Returns:
        Sanitized log line string.
    """
    pass


def summarize_logs(lines: list[str]) -> dict[str, object]:
    """Parse a batch of access log lines and return traffic & error metrics.

    Blank/whitespace-only lines are ignored. Non-empty malformed lines are
    skipped and tallied in "malformed_count".

    Args:
        lines: List of raw access log lines.

    Returns:
        Dictionary with keys:
            - "total_requests" (int)
            - "error_count" (int): requests with status_code >= 400
            - "avg_latency_ms" (float): rounded to 2 decimal places (0.0 if none)
            - "max_latency_ms" (int): highest latency (0 if none)
            - "slowest_endpoint" (str | None): endpoint with highest latency
                (first seen wins ties; None if total_requests == 0)
            - "malformed_count" (int): count of non-empty malformed lines
    """
    pass
