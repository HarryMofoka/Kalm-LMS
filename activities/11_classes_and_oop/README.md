# Module 11: Classes & Object-Oriented Programming (Activities 121–132)

Transition smoothly from standalone functions to clean, reliable, real-world Python **classes**!

Every activity pairs a worked `Example<Name>` class ("I Do") with a distinct real-world `<Name>` class ("You Do"), building progressively from `__init__` and `__str__` through stateful invariants, properties, composition, reusable grid canvases, inheritance, OOP halo-runner simulations, Python's dunder protocols (`len`, `in`, `==`, `iter`), and finite-state workflows.

## Learning Goals

- Design classes with clear constructors (`__init__`), instance attributes, and readable `__str__` / `__repr__` representations.
- Protect object invariants using validation, `@property` getters/setters, and `ValueError` guards.
- Distinguish mutating methods from methods that return fresh objects, and compose complex objects from smaller classes.
- Build solver/utility classes (aligned with `ProblemSolver`), reusable `GridCanvas` renderers, class hierarchies with `super()`, dunder-protocol containers, and finite-state machines.

## Activities

| Activity | File | Worked Example ("I Do") | Your Turn ("You Do") | Difficulty |
|---|---|---|---|---|
| 121 | `activity_121_first_class_and_init.py` | `ExampleBook` (`title`, `author`, `summary`) | `MovieTicket` (`movie`, `price`, `apply_discount(pct)`) | 121 / 132 |
| 122 | `activity_122_str_repr_and_display.py` | `ExamplePoint` (`__str__`, `__repr__`) | `Temperature` (Celsius/Fahrenheit, clean `__str__` & `__repr__`) | 122 / 132 |
| 123 | `activity_123_stateful_objects_and_invariants.py` | `ExampleCounter` (`increment`, `reset`, bounds) | `FuelTank` (`0 <= fuel <= capacity`, `ValueError` guards) | 123 / 132 |
| 124 | `activity_124_mutating_vs_new_objects.py` | `ExampleVector2D` (immutable `add`, `scale`) | `GridCursor` (clamped `move`, `history`, non-mutating `preview_move`) | 124 / 132 |
| 125 | `activity_125_validation_and_properties.py` | `ExampleProduct` (`@property` validated price) | `BankAccount` (`deposit`, `withdraw`, overdraft guard, `transactions`) | 125 / 132 |
| 126 | `activity_126_utility_and_solver_classes.py` | `ExampleTextAnalyzer` (stateful call counter) | `MiniProblemSolver` (`call_count` + 3 algorithm methods) | 126 / 132 |
| 127 | `activity_127_composition_objects_holding_objects.py` | `ExamplePlaylist` holding `ExampleSong`s | `ShoppingCart` holding `CartItem`s (`subtotal`, tax, `remove_by_name`) | 127 / 132 |
| 128 | `activity_128_reusable_grid_canvas.py` | `ExampleBoard` (`place`, `get`, `render`) | `GridCanvas(width, height)` (`set_cell`, `draw_border`, `render`) | 128 / 132 |
| 129 | `activity_129_inheritance_and_base_class.py` | `ExampleAnimal` (`ExampleDog`, `ExampleCat`) | `Shape` (`SquareHaloShape`, `RectangleHaloShape`) | 129 / 132 |
| 130 | `activity_130_oop_halo_runner_simulation.py` | `ExampleClock` (`tick`, `days_elapsed`, `reset`) | `HaloRunner(path)` (`step`, `position`, `laps_completed`, `reset`) | 130 / 132 |
| 131 | `activity_131_dunder_methods_protocol.py` | `ExampleBag` (`__len__`, `__contains__`, `__eq__`, `__iter__`) | `Scoreboard` (`len`, `in`, `==`, `iter`, `top(n)`) | 131 / 132 |
| 132 | `activity_132_mini_state_machine.py` | `ExampleTrafficLight` (state cycle & history) | `OrderWorkflow` (`DRAFT -> PAID -> SHIPPED -> DELIVERED` / `CANCELLED`) | 132 / 132 |

## Checkpoints Unlocked

- **Checkpoint 20 (FINAL CHECKPOINT!)** — Unlocked upon completing **Activity 132** (complete mastery of Python OOP: encapsulation, properties, composition, inheritance, Python data model dunders, and state machines!).

## Running Tests

From the `ExamPrep/` directory, run:

```bash
python -m unittest activities/11_classes_and_oop/test_11_classes_and_oop.py -v
```

Or run only the worked examples or only your activities:

```bash
python -m unittest activities.11_classes_and_oop.test_11_classes_and_oop.TestWorkedExamples -v
python -m unittest activities.11_classes_and_oop.test_11_classes_and_oop.TestYourActivities -v
```
