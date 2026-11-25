# Kalm-LMS — Progressive Python Mastery Curriculum

> **Learn Python calmly, one tiny step at a time.**
> Zero fluff. Zero setup headaches. **172 hands-on Python challenges** with worked examples, plain-English explanations, real-world projects, legacy-code rescues, and instant automated feedback.

---

## Table of Contents

1. [What Is Kalm-LMS?](#what-is-kalm-lms)
2. [How the Curriculum Is Layered](#how-the-curriculum-is-layered)
3. [Repository Map (What Every Folder Does)](#repository-map-what-every-folder-does)
4. [Quick Start for Complete Beginners](#quick-start-for-complete-beginners)
5. [Walkthrough: Complete Your Very First Activity in 5 Minutes](#walkthrough-complete-your-very-first-activity-in-5-minutes)
6. [Complete Learning Roadmap & Checkpoints](#complete-learning-roadmap--checkpoints)
7. [How Master Projects & Refactoring Missions Work](#how-master-projects--refactoring-missions-work)
8. [Command Cheat Sheet](#command-cheat-sheet)
9. [Beginner FAQ & Troubleshooting](#beginner-faq--troubleshooting)

---

## What Is Kalm-LMS?

**Kalm-LMS** is a self-paced, test-driven Python curriculum built to take you smoothly from printing your very first string all the way to **grid geometry & Halo Patterns**, **classic algorithms**, **Classes & OOP**, **real-world systems**, and **refactoring messy code**.

Every single topic follows the **"I Do → You Do → Prove It"** loop:
1. **Read & run a Worked Example ("I Do")** — a clean, explained solution to a closely related problem.
2. **Solve Your Turn ("You Do")** — a companion problem that raises the difficulty by just a notch.
3. **Run the automated tests ("Prove It")** — instant red-to-green feedback, just like real software engineering!

**Zero third-party libraries required:** Everything runs using Python's built-in standard library (`unittest`). You only need **Python 3.9+**.

---

## How the Curriculum Is Layered

Kalm-LMS is organized into **three reinforcing layers** so you never get stuck in tutorial hell and never hit a sudden difficulty cliff:

| Layer | Folder | Count | Difficulty | Purpose |
|---|---|---|---|---|
| **Layer 1: Guided Activities** | [`activities/`](./activities/README.md) | **132 activities** (11 modules × 12) | Gentle ramp (1 → 132) | Master one concept at a time with a worked example + explanation right above your exercise. |
| **Layer 2: Master Projects** | [`master_projects/`](./master_projects/README.md) | **20 Checkpoints** | Unlocked every ~6 activities | Build **real-world functioning systems** (billing engines, log sanitizers, search indexes, mini `git diff`, drone perimeter patrol, digital bank ledger). Includes a completed similar system + walkthrough. |
| **Layer 3: Refactoring Missions** | [`refactoring_projects/`](./refactoring_projects/README.md) | **20 Legacy Rescues** | Paired with Checkpoints 01–20 | Read and clean up **someone else's working-but-messy code** without breaking its passing behavioral safety net! |

```text
  Activities 001–006 ──► CHECKPOINT 01 (Master Project 01 + Refactoring Mission 01)
  Activities 007–012 ──► CHECKPOINT 02 (Master Project 02 + Refactoring Mission 02)
         ...                            ...
  Activities 109–114 ──► CHECKPOINT 18 (Drone Perimeter Patrol + Halo Refactor 18)
  Activities 115–120 ──► CHECKPOINT 19 (Retro Arcade Board + Game Loop Refactor 19)
  Activities 121–132 ──► CHECKPOINT 20 (OOP Bank Ledger + Procedural-to-OOP Refactor 20)
```

---

## Repository Map (What Every Folder Does)

```text
Kalm-LMS/
├── README.md                  ← You are here! Complete beginner guide & roadmap
├── progress.py                ← Run `python progress.py` to see your live progress bars
├── pyproject.toml             ← Optional pytest configuration
├── requirements.txt           ← Optional pytest dependency (not required to run tests!)
│
├── activities/                ← LAYER 1: 132 progressive Python activities
│   ├── README.md              ← Index of all 11 topic modules
│   ├── 01_variables_and_math/       (Activities 001–012 + tests)
│   ├── 02_conditionals_and_logic/   (Activities 013–024 + tests)
│   ├── 03_loops_fundamentals/       (Activities 025–036 + tests)
│   ├── 04_strings_and_text/         (Activities 037–048 + tests)
│   ├── 05_lists_and_tuples/         (Activities 049–060 + tests)
│   ├── 06_dictionaries_and_sets/    (Activities 061–072 + tests)
│   ├── 07_functions_validation_and_tdd/   (Activities 073–084 + tests)
│   ├── 08_algorithms_and_problem_solving/ (Activities 085–096 + tests)
│   ├── 09_shapes_and_ascii_patterns/      (Activities 097–108 + tests)
│   ├── 10_halo_patterns_and_grid_walks/   (Activities 109–120 + tests)
│   └── 11_classes_and_oop/                (Activities 121–132 + tests)
│
├── master_projects/           ← LAYER 2: 20 real-world functioning systems
│   ├── README.md              ← Index of all 20 Checkpoints
│   ├── checkpoint_01_split_bill_calculator/
│   │   ├── README.md          ← Problem statement + walkthrough of similar system
│   │   ├── worked_example.py  ← Complete working sibling system (run it!)
│   │   ├── project.py         ← Starter file where YOU build the system
│   │   └── test_project.py    ← Automated tests for example + your project
│   └── ... (through checkpoint_20_mini_bank_ledger_system/)
│
└── refactoring_projects/      ← LAYER 3: 20 progressive legacy-code rescues
    ├── README.md              ← Index of all 20 Refactoring Missions
    ├── refactor_01_messy_receipt_math/
    │   ├── README.md          ← Backstory, smells checklist & Before→After walkthrough
    │   ├── worked_example.py  ← Sibling `before_*` vs `after_*` refactoring
    │   ├── messy_code.py      ← Someone else's working-but-messy code for YOU to clean
    │   └── test_refactor.py   ← Safety net (GREEN) + refactoring goals (RED → GREEN)
    └── ... (through refactor_20_procedural_to_oop_rescue/)
```

---

## Quick Start for Complete Beginners

### Step 1: Check that Python 3.9+ is installed
Open a terminal (**PowerShell** on Windows, or **Terminal** on macOS/Linux) and run:

```bash
python --version
# (On macOS/Linux, use `python3 --version` if `python` is not found)
```

If you see `Python 3.9` or higher (e.g. `Python 3.12.x` or `Python 3.14.x`), you are ready! If not, download Python from [python.org/downloads](https://www.python.org/downloads/) (on Windows, tick **"Add Python to PATH"** during installation).

### Step 2: Clone the repository and enter the folder

```bash
git clone https://github.com/HarryMofoka/Kalm-LMS.git
cd Kalm-LMS
```

### Step 3: Check your live progress board

```bash
python progress.py
```

You will see your personal dashboard starting cleanly at `0/132` activities, `0/20` master projects, and `0/20` refactoring missions — plus a **Next Recommended Step** pointing straight to Activity 001!

### Step 4: Verify everything works out of the box (optional sanity check)

```bash
python progress.py --verify-examples
```

You should see:
```text
  Activity Worked Examples : 132/132 passing
  Master Worked Examples   : 96/96 passing
  Refactor Worked Examples : 33/33 passing
  Refactor Safety Nets     : 75/75 passing

  ALL worked examples and baseline safety nets are 100% GREEN!
```

*(Optional: if you like using `pytest`, run `pip install -r requirements.txt` inside a virtual environment — otherwise Python's built-in `unittest` works everywhere with zero installs!)*

---

## Walkthrough: Complete Your Very First Activity in 5 Minutes

Let's walk through **Activity 001** step by step so you feel 100% comfortable:

1. **Open the file** [`activities/01_variables_and_math/activity_001_fstring_greeting.py`](./activities/01_variables_and_math/activity_001_fstring_greeting.py) in VS Code (or any editor).
2. **Read `PART 1: WORKED EXAMPLE ("I DO")`** at the top of the file and study `example_welcome_banner`.
3. **Run the file directly** to see the worked example in action:
   ```bash
   python activities/01_variables_and_math/activity_001_fstring_greeting.py
   ```
4. **Run the test for Activity 001 BEFORE coding** (seeing it fail first proves the test works!):
   ```bash
   python -m unittest activities.01_variables_and_math.test_01_variables_and_math.TestYourActivities.test_activity_001 -v
   ```
   It fails because `solve_gamer_badge` currently just has `pass`.
5. **Read `PART 2: YOUR TURN ("YOU DO")`** and replace `pass` inside `solve_gamer_badge` with your solution.
6. **Re-run the test** until it says `ok`! Then run `python progress.py` and watch Module 01 jump to `1/12`!

> **Golden Rule for Shapes, Loops & Halos (Modules 09–10):**
> **DRAW → INDEX `(row, col)` → RULE → TEST → CODE.**
> Never guess `+1` or `-1` until something "looks right" — draw a tiny 3×3 or 4×3 grid on paper first!

---

## Complete Learning Roadmap & Checkpoints

Work top-to-bottom. Whenever you hit a **Checkpoint**, pause the activity ladder, build the **Master Project**, and complete the matching **Refactoring Mission** before continuing.

| Module | Activities | Topic | Checkpoints Unlocked |
|---|---|---|---|
| **01** | `001 – 012` | [Variables & Math](./activities/01_variables_and_math/README.md) | **CP 01** (after 006): [Bill Splitter](./master_projects/checkpoint_01_split_bill_calculator/README.md) · [RF 01](./refactoring_projects/refactor_01_messy_receipt_math/README.md)<br>**CP 02** (after 012): [Transit Timetable](./master_projects/checkpoint_02_transit_timetable_clock/README.md) · [RF 02](./refactoring_projects/refactor_02_time_converter_spaghetti/README.md) |
| **02** | `013 – 024` | [Conditionals & Logic](./activities/02_conditionals_and_logic/README.md) | **CP 03** (after 018): [Electricity Tariff](./master_projects/checkpoint_03_smart_tariff_calculator/README.md) · [RF 03](./refactoring_projects/refactor_03_nested_if_pyramid/README.md)<br>**CP 04** (after 024): [Password Auditor](./master_projects/checkpoint_04_password_policy_auditor/README.md) · [RF 04](./refactoring_projects/refactor_04_boolean_soup/README.md) |
| **03** | `025 – 036` | [Loops Fundamentals](./activities/03_loops_fundamentals/README.md) | **CP 05** (after 030): [Loan Simulator](./master_projects/checkpoint_05_loan_amortization_simulator/README.md) · [RF 05](./refactoring_projects/refactor_05_copy_paste_loops/README.md)<br>**CP 06** (after 036): [Server Uptime Monitor](./master_projects/checkpoint_06_server_uptime_monitor/README.md) · [RF 06](./refactoring_projects/refactor_06_while_loop_traps/README.md) |
| **04** | `037 – 048` | [Strings & Text](./activities/04_strings_and_text/README.md) | **CP 07** (after 042): [Web Log Parser](./master_projects/checkpoint_07_log_line_parser/README.md) · [RF 07](./refactoring_projects/refactor_07_string_concat_chaos/README.md)<br>**CP 08** (after 048): [Mini Markdown Engine](./master_projects/checkpoint_08_markdown_mini_renderer/README.md) · [RF 08](./refactoring_projects/refactor_08_messy_text_cleaner/README.md) |
| **05** | `049 – 060` | [Lists & Tuples](./activities/05_lists_and_tuples/README.md) | **CP 09** (after 054): [Playlist Queue](./master_projects/checkpoint_09_playlist_queue_engine/README.md) · [RF 09](./refactoring_projects/refactor_09_mutating_inputs_bug/README.md)<br>**CP 10** (after 060): [Cinema Seat Booking](./master_projects/checkpoint_10_cinema_seat_booking/README.md) · [RF 10](./refactoring_projects/refactor_10_grid_aliasing_disaster/README.md) |
| **06** | `061 – 072` | [Dictionaries & Sets](./activities/06_dictionaries_and_sets/README.md) | **CP 11** (after 066): [Inventory Ledger](./master_projects/checkpoint_11_inventory_ledger/README.md) · [RF 11](./refactoring_projects/refactor_11_parallel_lists_to_dicts/README.md)<br>**CP 12** (after 072): [Tag Search Indexer](./master_projects/checkpoint_12_tag_search_indexer/README.md) · [RF 12](./refactoring_projects/refactor_12_quadratic_lookup_rescue/README.md) |
| **07** | `073 – 084` | [Functions, Validation & TDD](./activities/07_functions_validation_and_tdd/README.md) | **CP 13** (after 078): [Config Validator](./master_projects/checkpoint_13_config_schema_validator/README.md) · [RF 13](./refactoring_projects/refactor_13_print_coupled_logic/README.md)<br>**CP 14** (after 084): [Esports Leaderboard](./master_projects/checkpoint_14_leaderboard_ranking_engine/README.md) · [RF 14](./refactoring_projects/refactor_14_god_function_breakup/README.md) |
| **08** | `085 – 096` | [Algorithms & Problem Solving](./activities/08_algorithms_and_problem_solving/README.md) | **CP 15** (after 090): [Code Bracket Linter](./master_projects/checkpoint_15_code_linter_bracket_checker/README.md) · [RF 15](./refactoring_projects/refactor_15_brittle_manual_parser/README.md)<br>**CP 16** (after 096): [Mini `git diff` Engine](./master_projects/checkpoint_16_text_diff_engine/README.md) · [RF 16](./refactoring_projects/refactor_16_slow_naive_algorithms/README.md) |
| **09** | `097 – 108` | [Shapes & ASCII Patterns](./activities/09_shapes_and_ascii_patterns/README.md) | **CP 17** (after 102): [Terminal Dashboard](./master_projects/checkpoint_17_terminal_chart_dashboard/README.md) · [RF 17](./refactoring_projects/refactor_17_fragile_ascii_printer/README.md) |
| **10** | `109 – 120` | [Halo Patterns & Grid Walks](./activities/10_halo_patterns_and_grid_walks/README.md) | **CP 18** (after 114): [Drone Perimeter Patrol](./master_projects/checkpoint_18_perimeter_patrol_scheduler/README.md) · [RF 18](./refactoring_projects/refactor_18_double_corner_halo_mess/README.md)<br>**CP 19** (after 120): [Retro Arcade Board](./master_projects/checkpoint_19_retro_snake_board_engine/README.md) · [RF 19](./refactoring_projects/refactor_19_spaghetti_game_loop/README.md) |
| **11** | `121 – 132` | [Classes & OOP](./activities/11_classes_and_oop/README.md) | **CP 20** (after 132): [OOP Bank Ledger](./master_projects/checkpoint_20_mini_bank_ledger_system/README.md) · [RF 20](./refactoring_projects/refactor_20_procedural_to_oop_rescue/README.md) |

---

## How Master Projects & Refactoring Missions Work

### Master Projects (`master_projects/`)
Each checkpoint gives you **two** systems side by side:
- **`worked_example.py`** — a complete, production-style sibling system so you can see how helper functions, edge-case guards, and clean data structures fit together.
- **`project.py`** — your project to implement until every test in `TestMasterProject` passes.

### Refactoring Missions (`refactoring_projects/`)
Each refactoring folder has **three** test classes in `test_refactor.py`:
1. **`TestWorkedExample` (GREEN)** — proves the sibling `before_*` and `after_*` functions produce identical outputs.
2. **`TestBehaviorSafetyNet` (GREEN)** — tests the current behavior of `messy_code.py`. **Keep this GREEN at all times while refactoring!**
3. **`TestRefactorGoals` (RED → GREEN)** — verifies your code cleanup (e.g., no cryptic variable names, no deep nested `if` pyramids, no silent input mutation, `O(n)` instead of `O(n²)`, clean helper functions, or clean classes).

---

## Command Cheat Sheet

Run all commands from the root `Kalm-LMS/` folder (use `python3` instead of `python` on macOS/Linux if needed):

```bash
# Live progress dashboard
python progress.py

# Progress dashboard + list every unfinished test name
python progress.py -v

# Verify all worked examples & refactoring safety nets pass
python progress.py --verify-examples

# Run one Activity module's tests
python -m unittest activities/01_variables_and_math/test_01_variables_and_math.py -v

# Run a single Activity test
python -m unittest activities.01_variables_and_math.test_01_variables_and_math.TestYourActivities.test_activity_001 -v

# Run one Master Project's tests
python -m unittest master_projects/checkpoint_01_split_bill_calculator/test_project.py -v

# Run one Refactoring Mission's tests
python -m unittest refactoring_projects/refactor_01_messy_receipt_math/test_refactor.py -v

# Run a worked example demo directly
python master_projects/checkpoint_01_split_bill_calculator/worked_example.py

# Optional pytest equivalents (if pytest is installed)
pytest activities/01_variables_and_math/ -k test_activity_001 -v
pytest master_projects/checkpoint_01_split_bill_calculator/ -v
```

---

## Beginner FAQ & Troubleshooting

<details>
<summary><strong>Why are so many tests failing when I first clone the repo?</strong></summary>

That is completely normal and intentional! The **Worked Examples** (`TestWorkedExamples` / `TestWorkedExample`) and **Refactoring Safety Nets** (`TestBehaviorSafetyNet`) all pass 100% out of the box. Your own exercises (`TestYourActivities`, `TestMasterProject`, and `TestRefactorGoals`) start **RED** because you haven't solved them yet — turning them **GREEN** is how you track mastery!
</details>

<details>
<summary><strong><code>python</code> is not recognized on macOS or Linux</strong></summary>

Use `python3` instead of `python` (e.g., `python3 progress.py`).
</details>

<details>
<summary><strong>Should I edit the test files to make them pass?</strong></summary>

No — treat the test files as the **specification**! Only edit the `solve_*` stubs in `activities/`, `project.py` in `master_projects/`, and `messy_code.py` in `refactoring_projects/`. (Adding extra tests of your own is always welcome!)
</details>

<details>
<summary><strong>I'm stuck on an exercise — what should I do?</strong></summary>

1. Re-read the **Worked Example** in the same file and run it (`python activity_NNN_...py`).
2. Read the exact test failure output — it shows what your function returned vs. what was expected.
3. Grab paper and trace one tiny example by hand (e.g., empty list `[]`, `n = 1`, `n = 3`).
4. Check edge cases: empty input, `0`, negatives, ties, duplicates, and don't mutate input lists/dicts!
</details>

---

Happy coding — stay calm, trust the tests, and enjoy watching `python progress.py` hit **100%**!
