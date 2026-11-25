"""Master Project (Checkpoint 13): Production Config Schema Validator.

Implement the three functions below according to the specification in README.md.
Run tests from ExamPrep/ with:
    python -m unittest master_projects/checkpoint_13_config_schema_validator/test_project.py -v
"""

from __future__ import annotations


def validate_field(name: str, value: object, rule: dict) -> list[str]:
    """Validate a single configuration field against its schema rule.

    Supported rule keys:
        - ``"type"``: Expected Python type. Note that ``bool`` values MUST be
          rejected when ``int`` or ``float`` is expected! When ``float`` is
          expected, non-bool ``int`` and ``float`` values are accepted.
        - ``"min"``: Inclusive lower bound (for numeric values).
        - ``"max"``: Inclusive upper bound (for numeric values).
        - ``"choices"``: Collection of permitted values.

    If the ``"type"`` check fails, return immediately with the type error so
    downstream bound checks do not raise ``TypeError``. Every returned error
    message must include ``name``.

    Args:
        name: Configuration field name.
        value: Value supplied for the field.
        rule: Dictionary of validation constraints.

    Returns:
        List of human-readable error strings (empty if valid).
    """
    pass


def apply_defaults(config: dict, schema: dict[str, dict]) -> dict:
    """Return a new config dictionary populated with missing schema defaults.

    Existing keys in ``config`` (even falsy ones like ``0``, ``False``, ``""``,
    or ``None``) are preserved untouched. Neither ``config`` nor ``schema``
    may be mutated.

    Args:
        config: Raw configuration dictionary.
        schema: Mapping of field name -> rule dictionary.

    Returns:
        A new dictionary combining ``config`` with defaults for missing keys.
    """
    pass


def validate_config(
    config: dict,
    schema: dict[str, dict],
    allow_unknown: bool = False,
) -> dict:
    """Validate an entire configuration dictionary against ``schema``.

    Steps:
        1. Resolve defaults via ``apply_defaults(config, schema)`` without
           mutating inputs.
        2. Check required fields and run ``validate_field`` on present fields.
        3. If ``allow_unknown`` is ``False``, report every key in ``resolved``
           that is not defined in ``schema`` (in sorted order).

    Args:
        config: Raw configuration dictionary.
        schema: Mapping of field name -> rule dictionary.
        allow_unknown: Whether keys absent from ``schema`` are permitted.

    Returns:
        Dictionary ``{"valid": bool, "errors": list[str], "resolved": dict}``.
    """
    pass
