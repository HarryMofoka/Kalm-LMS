"""Worked Example (Checkpoint 13): Environment Variable Preflight Checker.

A sibling reference system demonstrating strict parsing, structured per-field
validation, and error aggregation before booting a backend server.
"""

from __future__ import annotations


def parse_env_value(raw: str, expected_type: type) -> object:
    """Parse a raw environment variable string into ``expected_type``.

    Supports ``str``, ``int``, ``float``, and ``bool``.

    Raises:
        ValueError: If ``raw`` cannot be parsed into ``expected_type`` or
            ``expected_type`` is unsupported.
    """
    if expected_type is str:
        return raw

    cleaned = raw.strip()
    if expected_type is bool:
        lowered = cleaned.lower()
        if lowered in {"true", "1", "yes"}:
            return True
        if lowered in {"false", "0", "no"}:
            return False
        raise ValueError(f"cannot parse {raw!r} as bool")

    if expected_type is int:
        try:
            return int(cleaned)
        except ValueError as exc:
            raise ValueError(f"cannot parse {raw!r} as int") from exc

    if expected_type is float:
        try:
            return float(cleaned)
        except ValueError as exc:
            raise ValueError(f"cannot parse {raw!r} as float") from exc

    raise ValueError(f"unsupported env type: {expected_type.__name__}")


def check_env_var(
    name: str,
    raw: str | None,
    spec: dict,
) -> tuple[object | None, str | None]:
    """Validate and parse a single environment variable against ``spec``.

    Returns ``(parsed_value, error_message)``. When valid, ``error_message``
    is ``None``.
    """
    if raw is None or raw == "":
        if "default" in spec:
            return spec["default"], None
        if spec.get("required", False):
            return None, f"{name}: missing required environment variable"
        return None, None

    expected_type = spec.get("type", str)
    try:
        parsed = parse_env_value(raw, expected_type)
    except ValueError as exc:
        return None, f"{name}: {exc}"

    choices = spec.get("choices")
    if choices is not None and parsed not in choices:
        return None, f"{name}: value {parsed!r} not in allowed choices {list(choices)}"

    return parsed, None


def preflight_check(
    env: dict[str, str],
    specs: dict[str, dict],
) -> dict:
    """Validate all environment variable specs and aggregate every error.

    Does not mutate ``env`` or ``specs``.

    Returns:
        ``{"ok": bool, "errors": list[str], "config": dict}``
    """
    errors: list[str] = []
    config: dict[str, object] = {}

    for name in sorted(specs):
        spec = specs[name]
        raw = env.get(name)
        value, err = check_env_var(name, raw, spec)
        if err is not None:
            errors.append(err)
        elif value is not None or name in env or "default" in spec:
            config[name] = value

    return {
        "ok": len(errors) == 0,
        "errors": errors,
        "config": config,
    }


if __name__ == "__main__":
    server_specs = {
        "APP_ENV": {"type": str, "required": True, "choices": ["dev", "staging", "prod"]},
        "PORT": {"type": int, "default": 8000},
        "DEBUG": {"type": bool, "default": False},
        "DATABASE_URL": {"type": str, "required": True},
    }

    broken_env = {"APP_ENV": "qa", "PORT": "not-a-number", "DEBUG": "maybe"}
    healthy_env = {
        "APP_ENV": "prod",
        "PORT": "8080",
        "DEBUG": "false",
        "DATABASE_URL": "postgres://db.internal:5432/app",
    }

    print("=== Environment Variable Preflight Checker ===")
    print("Broken env check: ", preflight_check(broken_env, server_specs))
    print("Healthy env check:", preflight_check(healthy_env, server_specs))
