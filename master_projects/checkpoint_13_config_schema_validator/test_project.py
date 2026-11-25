"""Unit tests for Checkpoint 13: Production Config Schema Validator."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from master_projects.checkpoint_13_config_schema_validator import project, worked_example


class TestWorkedExample(unittest.TestCase):
    """Verify the Environment Variable Preflight Checker reference implementation."""

    def test_parse_env_value_handles_supported_types(self) -> None:
        self.assertEqual(worked_example.parse_env_value(" 8080 ", int), 8080)
        self.assertEqual(worked_example.parse_env_value("2.5", float), 2.5)
        self.assertIs(worked_example.parse_env_value("TRUE", bool), True)
        self.assertIs(worked_example.parse_env_value("0", bool), False)
        self.assertEqual(worked_example.parse_env_value("hello", str), "hello")

    def test_parse_env_value_rejects_invalid_literals(self) -> None:
        with self.assertRaises(ValueError):
            worked_example.parse_env_value("abc", int)
        with self.assertRaises(ValueError):
            worked_example.parse_env_value("maybe", bool)

    def test_check_env_var_required_default_and_choices(self) -> None:
        val, err = worked_example.check_env_var("PORT", None, {"type": int, "default": 8000})
        self.assertEqual(val, 8000)
        self.assertIsNone(err)

        val, err = worked_example.check_env_var("SECRET", "", {"type": str, "required": True})
        self.assertIsNone(val)
        self.assertIn("SECRET", err or "")

        val, err = worked_example.check_env_var(
            "MODE", "qa", {"type": str, "choices": ["dev", "prod"]}
        )
        self.assertIsNone(val)
        self.assertIn("MODE", err or "")

    def test_preflight_check_valid_config(self) -> None:
        specs = {
            "ENV": {"type": str, "required": True, "choices": ["dev", "prod"]},
            "PORT": {"type": int, "default": 8000},
            "DEBUG": {"type": bool, "default": False},
        }
        env = {"ENV": "prod", "PORT": "9000"}
        report = worked_example.preflight_check(env, specs)
        self.assertIs(report["ok"], True)
        self.assertEqual(report["errors"], [])
        self.assertEqual(report["config"], {"ENV": "prod", "PORT": 9000, "DEBUG": False})
        self.assertEqual(env, {"ENV": "prod", "PORT": "9000"})

    def test_preflight_check_collects_multiple_errors(self) -> None:
        specs = {
            "ENV": {"type": str, "required": True, "choices": ["dev", "prod"]},
            "PORT": {"type": int, "required": True},
            "TOKEN": {"type": str, "required": True},
        }
        report = worked_example.preflight_check({"ENV": "qa", "PORT": "bad"}, specs)
        self.assertIs(report["ok"], False)
        self.assertEqual(len(report["errors"]), 3)


class TestMasterProject(unittest.TestCase):
    """Tests for the student's Production Config Schema Validator."""

    def test_validate_field_valid_and_rejects_bool_for_int_or_float(self) -> None:
        self.assertEqual(
            project.validate_field("port", 8080, {"type": int, "min": 1024, "max": 65535}),
            [],
        )
        self.assertEqual(
            project.validate_field("timeout", 30, {"type": float, "min": 0.5}),
            [],
        )
        self.assertEqual(
            project.validate_field("debug", False, {"type": bool}),
            [],
        )

        # Python gotcha: isinstance(True, int) is True, but bool must be rejected!
        bool_as_int_errors = project.validate_field("workers", True, {"type": int, "min": 1})
        self.assertIsInstance(bool_as_int_errors, list)
        self.assertGreaterEqual(len(bool_as_int_errors), 1)
        self.assertTrue(any("workers" in msg for msg in bool_as_int_errors))

        bool_as_float_errors = project.validate_field("ratio", False, {"type": float})
        self.assertIsInstance(bool_as_float_errors, list)
        self.assertGreaterEqual(len(bool_as_float_errors), 1)
        self.assertTrue(any("ratio" in msg for msg in bool_as_float_errors))

    def test_validate_field_min_max_choices_and_early_type_exit(self) -> None:
        # Exact boundaries are valid
        self.assertEqual(project.validate_field("retries", 0, {"type": int, "min": 0, "max": 5}), [])
        self.assertEqual(project.validate_field("retries", 5, {"type": int, "min": 0, "max": 5}), [])

        below_min = project.validate_field("retries", -1, {"type": int, "min": 0, "max": 5})
        self.assertIsInstance(below_min, list)
        self.assertEqual(len(below_min), 1)
        self.assertIn("retries", below_min[0])

        above_max = project.validate_field("retries", 6, {"type": int, "min": 0, "max": 5})
        self.assertIsInstance(above_max, list)
        self.assertEqual(len(above_max), 1)
        self.assertIn("retries", above_max[0])

        bad_choice = project.validate_field(
            "log_level", "VERBOSE", {"type": str, "choices": ["DEBUG", "INFO", "ERROR"]}
        )
        self.assertIsInstance(bad_choice, list)
        self.assertEqual(len(bad_choice), 1)
        self.assertIn("log_level", bad_choice[0])

        # Wrong type with numeric bounds must not raise TypeError
        wrong_type = project.validate_field("port", "8080", {"type": int, "min": 1, "max": 65535})
        self.assertIsInstance(wrong_type, list)
        self.assertEqual(len(wrong_type), 1)
        self.assertIn("port", wrong_type[0])

    def test_apply_defaults_fills_missing_preserves_falsy_and_does_not_mutate(self) -> None:
        schema = {
            "host": {"type": str, "default": "0.0.0.0"},
            "port": {"type": int, "default": 8080},
            "retries": {"type": int, "default": 3},
            "debug": {"type": bool, "default": True},
            "prefix": {"type": str, "default": "/api"},
        }
        raw = {"retries": 0, "debug": False, "prefix": ""}
        resolved = project.apply_defaults(raw, schema)

        self.assertEqual(
            resolved,
            {
                "host": "0.0.0.0",
                "port": 8080,
                "retries": 0,
                "debug": False,
                "prefix": "",
            },
        )
        # Ensure original config was NOT mutated
        self.assertEqual(raw, {"retries": 0, "debug": False, "prefix": ""})

    def test_validate_config_valid_with_defaults_resolved(self) -> None:
        schema = {
            "service_name": {"type": str, "required": True},
            "port": {"type": int, "default": 8080, "min": 1024, "max": 65535},
            "env": {"type": str, "default": "dev", "choices": ["dev", "staging", "prod"]},
            "optional_note": {"type": str},
        }
        cfg = {"service_name": "billing-api"}
        result = project.validate_config(cfg, schema)

        self.assertIsInstance(result, dict)
        self.assertIs(result["valid"], True)
        self.assertEqual(result["errors"], [])
        self.assertEqual(
            result["resolved"],
            {"service_name": "billing-api", "port": 8080, "env": "dev"},
        )
        self.assertEqual(cfg, {"service_name": "billing-api"})

    def test_validate_config_collects_required_type_and_range_errors(self) -> None:
        schema = {
            "api_key": {"type": str, "required": True},
            "workers": {"type": int, "required": True, "min": 1, "max": 64},
            "env": {"type": str, "required": True, "choices": ["dev", "prod"]},
        }
        cfg = {"workers": True, "env": "sandbox"}
        result = project.validate_config(cfg, schema)

        self.assertIsInstance(result, dict)
        self.assertIs(result["valid"], False)
        self.assertEqual(len(result["errors"]), 3)
        joined = " | ".join(result["errors"])
        self.assertIn("api_key", joined)
        self.assertIn("workers", joined)
        self.assertIn("env", joined)

    def test_validate_config_unknown_fields_policy(self) -> None:
        schema = {
            "port": {"type": int, "default": 8000},
        }
        cfg = {"port": 9000, "extra_flag": True, "mystery": 42}

        strict = project.validate_config(cfg, schema, allow_unknown=False)
        self.assertIsInstance(strict, dict)
        self.assertIs(strict["valid"], False)
        self.assertEqual(len(strict["errors"]), 2)
        self.assertIn("extra_flag", strict["errors"][0])
        self.assertIn("mystery", strict["errors"][1])

        permissive = project.validate_config(cfg, schema, allow_unknown=True)
        self.assertIsInstance(permissive, dict)
        self.assertIs(permissive["valid"], True)
        self.assertEqual(permissive["errors"], [])
        self.assertEqual(
            permissive["resolved"],
            {"port": 9000, "extra_flag": True, "mystery": 42},
        )


if __name__ == "__main__":
    unittest.main()
