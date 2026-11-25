#!/usr/bin/env python3
"""Interactive progress dashboard for Kalm-LMS.

Usage:
    python progress.py                   # Full dashboard (activities, master projects, refactoring)
    python progress.py -v                # Also list failing student test names
    python progress.py --verify-examples # Verify 100% of worked examples & refactoring safety nets pass
"""

from __future__ import annotations

import importlib
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

BAR_WIDTH = 20


def _bar(passed: int, total: int) -> str:
    filled = round(BAR_WIDTH * passed / total) if total else 0
    return f"[{'#' * filled}{'-' * (BAR_WIDTH - filled)}]"


def _run_testcase_class(module_name: str, class_name: str) -> tuple[int, int, list[str], list[str]]:
    """Run a single unittest.TestCase class and return (passed, total, failures, errors)."""
    mod = importlib.import_module(module_name)
    cls = getattr(mod, class_name)
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(cls)
    result = unittest.TestResult()
    suite.run(result)
    total = suite.countTestCases()
    failures = sorted({t.id().split(" ")[0].split(".")[-1] for t, _ in result.failures})
    errors = sorted({t.id().split(" ")[0].split(".")[-1] for t, _ in result.errors})
    bad_count = len(set(failures) | set(errors))
    passed = total - bad_count
    return passed, total, failures, errors


def _discover_activity_modules() -> list[tuple[str, str]]:
    base = ROOT / "activities"
    modules = []
    if not base.exists():
        return modules
    for folder in sorted(base.iterdir()):
        if folder.is_dir() and folder.name[0].isdigit():
            test_file = folder / f"test_{folder.name}.py"
            if test_file.exists():
                modules.append((folder.name, f"activities.{folder.name}.test_{folder.name}"))
    return modules


def _discover_master_projects() -> list[tuple[str, str]]:
    base = ROOT / "master_projects"
    projects = []
    if not base.exists():
        return projects
    for folder in sorted(base.iterdir()):
        if folder.is_dir() and folder.name.startswith("checkpoint_"):
            if (folder / "test_project.py").exists():
                projects.append((folder.name, f"master_projects.{folder.name}.test_project"))
    return projects


def _discover_refactoring_projects() -> list[tuple[str, str]]:
    base = ROOT / "refactoring_projects"
    projects = []
    if not base.exists():
        return projects
    for folder in sorted(base.iterdir()):
        if folder.is_dir() and folder.name.startswith("refactor_"):
            if (folder / "test_refactor.py").exists():
                projects.append((folder.name, f"refactoring_projects.{folder.name}.test_refactor"))
    return projects


def verify_examples() -> int:
    """Verify every worked example and every refactoring behavioral safety net passes 100%."""
    all_ok = True
    print("\n=== Kalm-LMS Integrity Check (Worked Examples & Safety Nets) ===\n")

    ex_pass = ex_tot = 0
    for name, mod_name in _discover_activity_modules():
        p, t, fails, errs = _run_testcase_class(mod_name, "TestWorkedExamples")
        ex_pass += p
        ex_tot += t
        if p != t:
            all_ok = False
            print(f"  [FAIL] activities/{name} WorkedExamples: {p}/{t} (fails={fails}, errs={errs})")
    print(f"  Activity Worked Examples : {ex_pass}/{ex_tot} passing")

    mp_pass = mp_tot = 0
    for name, mod_name in _discover_master_projects():
        p, t, fails, errs = _run_testcase_class(mod_name, "TestWorkedExample")
        mp_pass += p
        mp_tot += t
        if p != t:
            all_ok = False
            print(f"  [FAIL] master_projects/{name} WorkedExample: {p}/{t} (fails={fails}, errs={errs})")
    print(f"  Master Worked Examples   : {mp_pass}/{mp_tot} passing")

    rf_ex_pass = rf_ex_tot = 0
    rf_safe_pass = rf_safe_tot = 0
    for name, mod_name in _discover_refactoring_projects():
        p1, t1, f1, e1 = _run_testcase_class(mod_name, "TestWorkedExample")
        p2, t2, f2, e2 = _run_testcase_class(mod_name, "TestBehaviorSafetyNet")
        rf_ex_pass += p1
        rf_ex_tot += t1
        rf_safe_pass += p2
        rf_safe_tot += t2
        if p1 != t1:
            all_ok = False
            print(f"  [FAIL] refactoring_projects/{name} WorkedExample: {p1}/{t1} (fails={f1}, errs={e1})")
        if p2 != t2:
            all_ok = False
            print(f"  [FAIL] refactoring_projects/{name} SafetyNet: {p2}/{t2} (fails={f2}, errs={e2})")
    print(f"  Refactor Worked Examples : {rf_ex_pass}/{rf_ex_tot} passing")
    print(f"  Refactor Safety Nets     : {rf_safe_pass}/{rf_safe_tot} passing")

    print()
    if all_ok:
        print("  ALL worked examples and baseline safety nets are 100% GREEN!\n")
        return 0
    print("  Some worked examples or safety nets failed. See details above.\n")
    return 1


def show_dashboard(verbose: bool = False) -> int:
    print("\n======================================================================")
    print("                    Kalm-LMS Python Progress Board")
    print("======================================================================\n")

    # 1. Activities
    print("--- 1. PROGRESSIVE ACTIVITIES (11 Modules) ---")
    act_passed = act_total = 0
    next_activity_hint = None
    for name, mod_name in _discover_activity_modules():
        p, t, fails, errs = _run_testcase_class(mod_name, "TestYourActivities")
        act_passed += p
        act_total += t
        mark = "OK" if p == t and t > 0 else "  "
        print(f"  [{mark}] {name:<36} {_bar(p, t)} {p:>2}/{t}")
        if next_activity_hint is None and (fails or errs):
            first = (fails + errs)[0]
            next_activity_hint = f"activities/{name} ({first})"
        if verbose:
            for item in fails:
                print(f"         x {item}")
            for item in errs:
                print(f"         ! {item} (error)")

    # 2. Master Projects
    print("\n--- 2. MASTER PROJECTS (20 Checkpoints) ---")
    mp_done = 0
    mp_count = 0
    for name, mod_name in _discover_master_projects():
        mp_count += 1
        p, t, fails, errs = _run_testcase_class(mod_name, "TestMasterProject")
        if p == t and t > 0:
            mp_done += 1
            mark = "OK"
        else:
            mark = "  "
        print(f"  [{mark}] {name:<44} {_bar(p, t)} {p:>2}/{t}")
        if verbose:
            for item in fails:
                print(f"         x {item}")
            for item in errs:
                print(f"         ! {item} (error)")

    # 3. Refactoring Projects
    print("\n--- 3. REFACTORING MISSIONS (20 Legacy Rescues) ---")
    rf_done = 0
    rf_count = 0
    for name, mod_name in _discover_refactoring_projects():
        rf_count += 1
        sp, st, sf, se = _run_testcase_class(mod_name, "TestBehaviorSafetyNet")
        gp, gt, gf, ge = _run_testcase_class(mod_name, "TestRefactorGoals")
        safe_ok = sp == st and st > 0
        goals_ok = gp == gt and gt > 0
        if safe_ok and goals_ok:
            rf_done += 1
            mark = "OK"
        elif not safe_ok:
            mark = "!!"
        else:
            mark = "  "
        safe_str = f"safe {sp}/{st}"
        print(f"  [{mark}] {name:<38} ({safe_str:<10}) goals {_bar(gp, gt)} {gp:>2}/{gt}")
        if verbose:
            for item in sf + se:
                print(f"         !! SAFETY NET BROKEN: {item}")
            for item in gf:
                print(f"         x goal: {item}")
            for item in ge:
                print(f"         ! goal error: {item}")

    print("\n======================================================================")
    print(f"  Activities Completed    : {act_passed}/{act_total}")
    print(f"  Master Projects Done    : {mp_done}/{mp_count}")
    print(f"  Refactoring Rescues Done: {rf_done}/{rf_count}")
    if next_activity_hint:
        print(f"  Next Recommended Step   : {next_activity_hint}")
    print("======================================================================\n")
    return 0


def main() -> int:
    args = set(sys.argv[1:])
    if "--verify-examples" in args:
        return verify_examples()
    return show_dashboard(verbose="-v" in args)


if __name__ == "__main__":
    sys.exit(main())
