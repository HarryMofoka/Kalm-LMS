# Master Projects — 20 Real-World Checkpoints

Welcome to **Layer 2** of Kalm-LMS! Every ~6–7 activities in [`../activities/`](../activities/README.md), you unlock a **Checkpoint**.

Each Master Project mirrors a **real, functioning software system** — the kind of backend engine, CLI tool, validator, parser, scheduler, or simulation module you can genuinely contribute to in open-source repos and production engineering teams.

## How Each Checkpoint Works

Inside every `checkpoint_XX_*` folder you will find:
1. **`README.md`** — Real-world context, problem statement, a detailed walkthrough of how a similar functioning system was built, and your project specification.
2. **`worked_example.py`** — A complete, clean, runnable sibling system you can read and execute (`python worked_example.py`) to see good structure in action.
3. **`project.py`** — Your starter file with docstrings, type hints, and empty stubs for you to build.
4. **`test_project.py`** — Automated tests split into:
   - `TestWorkedExample` (passing right out of the box so you can trust the reference!)
   - `TestMasterProject` (red until you implement `project.py` — true Test-Driven Development!)

## All 20 Checkpoints (Click Any Project to Open)

| Checkpoint | Unlocked After | Project Folder | System You Will Build | Core Concepts |
|---|---|---|---|---|
| **CP 01** | Activity 006 | [checkpoint_01_split_bill_calculator](./checkpoint_01_split_bill_calculator/README.md) | Restaurant Bill, Tax & Tip Splitter | Variables, arithmetic, rounding |
| **CP 02** | Activity 012 | [checkpoint_02_transit_timetable_clock](./checkpoint_02_transit_timetable_clock/README.md) | Bus/Train Wrap-Around Timetable Engine | `//`, `%`, formatting |
| **CP 03** | Activity 018 | [checkpoint_03_smart_tariff_calculator](./checkpoint_03_smart_tariff_calculator/README.md) | Progressive Electricity Tiered Billing | Conditionals, tiered brackets |
| **CP 04** | Activity 024 | [checkpoint_04_password_policy_auditor](./checkpoint_04_password_policy_auditor/README.md) | Production Auth Password Policy Auditor | Logic, guards, validation errors |
| **CP 05** | Activity 030 | [checkpoint_05_loan_amortization_simulator](./checkpoint_05_loan_amortization_simulator/README.md) | Micro-Loan Payoff & Interest Simulator | `while`/`for` loops, running state |
| **CP 06** | Activity 036 | [checkpoint_06_server_uptime_monitor](./checkpoint_06_server_uptime_monitor/README.md) | SRE Heartbeat & SLA Outage Analyzer | Loops, streaks, percentages |
| **CP 07** | Activity 042 | [checkpoint_07_log_line_parser](./checkpoint_07_log_line_parser/README.md) | Web Server Access Log Parser & PII Masker | Strings, parsing, masking |
| **CP 08** | Activity 048 | [checkpoint_08_markdown_mini_renderer](./checkpoint_08_markdown_mini_renderer/README.md) | Mini Markdown & `{{var}}` Template Engine | String pipelines, formatting |
| **CP 09** | Activity 054 | [checkpoint_09_playlist_queue_engine](./checkpoint_09_playlist_queue_engine/README.md) | Music Streaming Queue & Smart Shuffle | Lists, slicing, dedup, rotation |
| **CP 10** | Activity 060 | [checkpoint_10_cinema_seat_booking](./checkpoint_10_cinema_seat_booking/README.md) | 2D Cinema Seat Grid & Group Allocator | 2D lists, coordinates, grids |
| **CP 11** | Activity 066 | [checkpoint_11_inventory_ledger](./checkpoint_11_inventory_ledger/README.md) | Multi-Warehouse Stock & Reorder System | Dictionaries, merging, alerts |
| **CP 12** | Activity 072 | [checkpoint_12_tag_search_indexer](./checkpoint_12_tag_search_indexer/README.md) | Inverted Index & Mini Full-Text Search | Dicts + sets, set intersections |
| **CP 13** | Activity 078 | [checkpoint_13_config_schema_validator](./checkpoint_13_config_schema_validator/README.md) | Production Config Schema Validator | Functions, validation contracts |
| **CP 14** | Activity 084 | [checkpoint_14_leaderboard_ranking_engine](./checkpoint_14_leaderboard_ranking_engine/README.md) | Esports Tournament Ranking & Tie-Breaker | Custom sort keys, decomposition |
| **CP 15** | Activity 090 | [checkpoint_15_code_linter_bracket_checker](./checkpoint_15_code_linter_bracket_checker/README.md) | Source Code Bracket & Line/Col Linter | Stacks, scanning algorithms |
| **CP 16** | Activity 096 | [checkpoint_16_text_diff_engine](./checkpoint_16_text_diff_engine/README.md) | Mini `git diff` Line-Comparison Engine | Dynamic programming (LCS) |
| **CP 17** | Activity 102 | [checkpoint_17_terminal_chart_dashboard](./checkpoint_17_terminal_chart_dashboard/README.md) | DevOps CLI Metrics & Bar-Chart Dashboard | ASCII layouts, zero trailing spaces |
| **CP 18** | Activity 114 | [checkpoint_18_perimeter_patrol_scheduler](./checkpoint_18_perimeter_patrol_scheduler/README.md) | Drone Factory Perimeter Patrol Planner | Halo rules, clockwise walks, modulo |
| **CP 19** | Activity 120 | [checkpoint_19_retro_snake_board_engine](./checkpoint_19_retro_snake_board_engine/README.md) | Retro Arcade Multi-Runner Board Engine | 2D grid simulation, collisions |
| **CP 20** | Activity 132 | [checkpoint_20_mini_bank_ledger_system](./checkpoint_20_mini_bank_ledger_system/README.md) | OOP Digital Wallet & Double-Entry Ledger | Classes, invariants, audit trails |

## Running Tests

```bash
# From the repository root:
python progress.py

# Or run a single checkpoint:
python -m unittest master_projects/checkpoint_01_split_bill_calculator/test_project.py -v
```
