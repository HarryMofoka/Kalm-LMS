"""Unit tests for Module 11: Classes & Object-Oriented Programming (Activities 121-132).

Run from ExamPrep/:
    python -m unittest activities/11_classes_and_oop/test_11_classes_and_oop.py -v
"""
from __future__ import annotations

import importlib
import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

_PKG = "activities.11_classes_and_oop"

_m121 = importlib.import_module(f"{_PKG}.activity_121_first_class_and_init")
_m122 = importlib.import_module(f"{_PKG}.activity_122_str_repr_and_display")
_m123 = importlib.import_module(f"{_PKG}.activity_123_stateful_objects_and_invariants")
_m124 = importlib.import_module(f"{_PKG}.activity_124_mutating_vs_new_objects")
_m125 = importlib.import_module(f"{_PKG}.activity_125_validation_and_properties")
_m126 = importlib.import_module(f"{_PKG}.activity_126_utility_and_solver_classes")
_m127 = importlib.import_module(f"{_PKG}.activity_127_composition_objects_holding_objects")
_m128 = importlib.import_module(f"{_PKG}.activity_128_reusable_grid_canvas")
_m129 = importlib.import_module(f"{_PKG}.activity_129_inheritance_and_base_class")
_m130 = importlib.import_module(f"{_PKG}.activity_130_oop_halo_runner_simulation")
_m131 = importlib.import_module(f"{_PKG}.activity_131_dunder_methods_protocol")
_m132 = importlib.import_module(f"{_PKG}.activity_132_mini_state_machine")

ExampleBook = _m121.ExampleBook
MovieTicket = _m121.MovieTicket

ExamplePoint = _m122.ExamplePoint
Temperature = _m122.Temperature

ExampleCounter = _m123.ExampleCounter
FuelTank = _m123.FuelTank

ExampleVector2D = _m124.ExampleVector2D
GridCursor = _m124.GridCursor

ExampleProduct = _m125.ExampleProduct
BankAccount = _m125.BankAccount

ExampleTextAnalyzer = _m126.ExampleTextAnalyzer
MiniProblemSolver = _m126.MiniProblemSolver

ExampleSong = _m127.ExampleSong
ExamplePlaylist = _m127.ExamplePlaylist
CartItem = _m127.CartItem
ShoppingCart = _m127.ShoppingCart

ExampleBoard = _m128.ExampleBoard
GridCanvas = _m128.GridCanvas

ExampleAnimal = _m129.ExampleAnimal
ExampleDog = _m129.ExampleDog
ExampleCat = _m129.ExampleCat
Shape = _m129.Shape
SquareHaloShape = _m129.SquareHaloShape
RectangleHaloShape = _m129.RectangleHaloShape

ExampleClock = _m130.ExampleClock
HaloRunner = _m130.HaloRunner

ExampleBag = _m131.ExampleBag
Scoreboard = _m131.Scoreboard

ExampleTrafficLight = _m132.ExampleTrafficLight
OrderWorkflow = _m132.OrderWorkflow


class TestWorkedExamples(unittest.TestCase):
    """Tests for the 12 worked OOP examples ('I Do') — all should PASS out of the box."""

    def test_example_121(self) -> None:
        book = ExampleBook("Dune", "Frank Herbert", 412)
        self.assertEqual(book.title, "Dune")
        self.assertEqual(book.author, "Frank Herbert")
        self.assertEqual(book.summary(), "'Dune' by Frank Herbert (412 pages)")
        self.assertTrue(book.is_long())
        short = ExampleBook("Animal Farm", "George Orwell", 112)
        self.assertFalse(short.is_long())

    def test_example_122(self) -> None:
        p = ExamplePoint(3, 4)
        self.assertEqual(str(p), "(3, 4)")
        self.assertEqual(repr(p), "ExamplePoint(x=3, y=4)")
        self.assertEqual(p.distance_to_origin(), 5.0)

    def test_example_123(self) -> None:
        c = ExampleCounter(start=1, max_value=5)
        self.assertEqual(c.increment(), 2)
        self.assertEqual(c.increment(3), 5)
        with self.assertRaises(ValueError):
            c.increment(1)
        self.assertEqual(c.value, 5)
        c.reset()
        self.assertEqual(c.value, 0)
        with self.assertRaises(ValueError):
            ExampleCounter(start=-1)

    def test_example_124(self) -> None:
        v1 = ExampleVector2D(2, 3)
        v2 = v1.add(ExampleVector2D(-1, 4))
        v3 = v1.scale(3)
        self.assertEqual(v1.as_tuple(), (2, 3))
        self.assertEqual(v2.as_tuple(), (1, 7))
        self.assertEqual(v3.as_tuple(), (6, 9))

    def test_example_125(self) -> None:
        p = ExampleProduct("  Mouse  ", 50)
        self.assertEqual(p.name, "Mouse")
        self.assertEqual(p.price, 50.0)
        self.assertEqual(p.price_with_tax(0.1), 55.0)
        p.price = 80
        self.assertEqual(p.price, 80.0)
        with self.assertRaises(ValueError):
            p.price = -1
        with self.assertRaises(ValueError):
            ExampleProduct("   ", 10)

    def test_example_126(self) -> None:
        ta = ExampleTextAnalyzer()
        self.assertEqual(ta.calls, 0)
        self.assertEqual(ta.word_count("hello world from python"), 4)
        self.assertEqual(ta.char_frequency("Aa b"), {"a": 2, "b": 1})
        self.assertTrue(ta.is_palindrome("Race car!"))
        self.assertFalse(ta.is_palindrome("Python"))
        self.assertEqual(ta.calls, 4)

    def test_example_127(self) -> None:
        pl = ExamplePlaylist("Chill")
        pl.add_song(ExampleSong("Track 1", "Artist A", 120))
        pl.add_song(ExampleSong("Track 2", "Artist B", 180))
        self.assertEqual(pl.total_duration(), 300)
        self.assertEqual(pl.titles(), ["Track 1", "Track 2"])
        self.assertTrue(pl.remove_by_title("Track 1"))
        self.assertFalse(pl.remove_by_title("Missing"))
        self.assertEqual(pl.titles(), ["Track 2"])

    def test_example_128(self) -> None:
        b = ExampleBoard(3, fill=".")
        b.place(0, 0, "X")
        b.place(1, 2, "O")
        self.assertEqual(b.get(1, 2), "O")
        self.assertEqual(b.render(), "X . .\n. . O\n. . .")
        with self.assertRaises(ValueError):
            b.place(3, 0, "X")
        with self.assertRaises(ValueError):
            ExampleBoard(0)

    def test_example_129(self) -> None:
        dog = ExampleDog("Rex")
        cat = ExampleCat("Luna")
        self.assertIsInstance(dog, ExampleAnimal)
        self.assertEqual(dog.describe(), "Rex says 'Woof!'")
        self.assertEqual(cat.describe(), "Luna says 'Meow!'")
        with self.assertRaises(NotImplementedError):
            ExampleAnimal("Unknown").speak()

    def test_example_130(self) -> None:
        clk = ExampleClock(23, 50)
        self.assertEqual(clk.formatted(), "23:50")
        self.assertEqual(clk.days_elapsed, 0)
        self.assertEqual(clk.tick(20), "00:10")
        self.assertEqual(clk.days_elapsed, 1)
        clk.reset()
        self.assertEqual(clk.formatted(), "00:00")
        self.assertEqual(clk.days_elapsed, 0)

    def test_example_131(self) -> None:
        b1 = ExampleBag()
        b1.add("pear", 2)
        b1.add("apple", 1)
        b2 = ExampleBag()
        b2.add("apple", 1)
        b2.add("pear", 2)
        self.assertEqual(len(b1), 3)
        self.assertIn("apple", b1)
        self.assertNotIn("grape", b1)
        self.assertEqual(b1, b2)
        self.assertNotEqual(b1, "not a bag")
        self.assertEqual(list(b1), ["apple", "pear"])

    def test_example_132(self) -> None:
        light = ExampleTrafficLight()
        self.assertFalse(light.can_go())
        self.assertEqual(light.advance(), "GREEN")
        self.assertTrue(light.can_go())
        self.assertEqual(light.advance(), "YELLOW")
        self.assertEqual(light.advance(), "RED")
        self.assertEqual(light.history, ["RED", "GREEN", "YELLOW", "RED"])
        with self.assertRaises(ValueError):
            ExampleTrafficLight("BLUE")


class TestYourActivities(unittest.TestCase):
    """Tests for your 12 student OOP activities ('You Do') — make every single one green!"""

    def _get(self, obj: object, attr: str) -> object:
        """Read an expected attribute, failing cleanly if not yet initialized."""
        if not hasattr(obj, attr):
            self.fail(f"{type(obj).__name__} is missing attribute {attr!r}")
        return getattr(obj, attr)

    def _eval(self, func, *args, **kwargs):
        """Invoke a built-in/dunder operation, failing cleanly if stub returns None."""
        try:
            return func(*args, **kwargs)
        except (AttributeError, TypeError) as exc:
            self.fail(f"Incomplete implementation: {exc}")

    def test_activity_121(self) -> None:
        ticket = MovieTicket("Dune", 120.0)
        self.assertEqual(self._get(ticket, "movie"), "Dune")
        self.assertEqual(self._get(ticket, "price"), 120.0)
        self.assertEqual(ticket.label(), "Dune - $120.00")

        self.assertEqual(ticket.apply_discount(25), 90.0)
        self.assertEqual(self._get(ticket, "price"), 90.0)
        self.assertEqual(ticket.label(), "Dune - $90.00")

        self.assertEqual(ticket.apply_discount(0), 90.0)
        self.assertEqual(ticket.apply_discount(100), 0.0)

        with self.assertRaises(ValueError):
            MovieTicket("Bad Price", -5)
        with self.assertRaises(ValueError):
            ticket.apply_discount(-1)
        with self.assertRaises(ValueError):
            ticket.apply_discount(101)

    def test_activity_122(self) -> None:
        freezing = Temperature(0)
        self.assertEqual(self._get(freezing, "celsius"), 0.0)
        self.assertEqual(freezing.to_fahrenheit(), 32.0)
        self.assertEqual(self._eval(str, freezing), "0.0°C (32.0°F)")
        self.assertEqual(self._eval(repr, freezing), "Temperature(celsius=0.0)")

        same = Temperature(-40)
        self.assertEqual(same.to_fahrenheit(), -40.0)
        self.assertEqual(self._eval(str, same), "-40.0°C (-40.0°F)")

        boiling = Temperature.from_fahrenheit(212)
        self.assertIsInstance(boiling, Temperature)
        self.assertEqual(self._get(boiling, "celsius"), 100.0)
        self.assertEqual(self._eval(str, boiling), "100.0°C (212.0°F)")

    def test_activity_123(self) -> None:
        tank = FuelTank(50, fuel=10)
        self.assertEqual(self._get(tank, "capacity"), 50.0)
        self.assertEqual(self._get(tank, "fuel"), 10.0)
        self.assertEqual(tank.refuel(15), 25.0)
        self.assertEqual(tank.percent_full(), 50.0)
        self.assertEqual(tank.drive(5), 20.0)
        self.assertEqual(tank.refuel(30), 50.0)  # exact capacity allowed
        self.assertEqual(tank.drive(50), 0.0)    # exact empty allowed

        with self.assertRaises(ValueError):
            tank.refuel(0)
        with self.assertRaises(ValueError):
            tank.refuel(51)
        with self.assertRaises(ValueError):
            tank.drive(0)
        with self.assertRaises(ValueError):
            tank.drive(1)
        with self.assertRaises(ValueError):
            FuelTank(0)
        with self.assertRaises(ValueError):
            FuelTank(40, fuel=45)
        with self.assertRaises(ValueError):
            FuelTank(40, fuel=-1)

    def test_activity_124(self) -> None:
        cur = GridCursor(3, 4)
        self.assertEqual(cur.position(), (0, 0))
        self.assertEqual(self._get(cur, "history"), [(0, 0)])

        self.assertEqual(cur.move(1, 2), (1, 2))
        self.assertEqual(cur.move(10, -5), (2, 0))
        self.assertEqual(cur.move(-10, 10), (0, 3))
        self.assertEqual(self._get(cur, "history"), [(0, 0), (1, 2), (2, 0), (0, 3)])

        ghost = cur.preview_move(2, -1)
        self.assertIsInstance(ghost, GridCursor)
        self.assertEqual(ghost.position(), (2, 2))
        self.assertEqual(self._get(ghost, "history"), [(2, 2)])
        # Original cursor untouched!
        self.assertEqual(cur.position(), (0, 3))
        self.assertEqual(self._get(cur, "history"), [(0, 0), (1, 2), (2, 0), (0, 3)])

        with self.assertRaises(ValueError):
            GridCursor(0, 4)
        with self.assertRaises(ValueError):
            GridCursor(3, 4, row=3, col=0)

    def test_activity_125(self) -> None:
        acct = BankAccount("  Ada  ", 100.0)
        self.assertEqual(self._get(acct, "owner"), "Ada")
        self.assertEqual(acct.balance, 100.0)
        self.assertEqual(acct.transactions, [])

        self.assertEqual(acct.deposit(50), 150.0)
        self.assertEqual(acct.withdraw(40), 110.0)
        self.assertEqual(acct.balance, 110.0)
        self.assertEqual(acct.transactions, [("DEPOSIT", 50.0), ("WITHDRAW", 40.0)])

        # Defensive copy check on transactions
        log_copy = acct.transactions
        log_copy.append(("FAKE", 9999.0))
        self.assertEqual(len(acct.transactions), 2)

        # Read-only balance property
        with self.assertRaises(AttributeError):
            acct.balance = 999.0  # type: ignore[misc]

        # Overdraft & validation guards
        with self.assertRaises(ValueError):
            acct.withdraw(200)
        self.assertEqual(acct.balance, 110.0)
        with self.assertRaises(ValueError):
            acct.deposit(0)
        with self.assertRaises(ValueError):
            acct.withdraw(-5)
        with self.assertRaises(ValueError):
            BankAccount("   ", 10)
        with self.assertRaises(ValueError):
            BankAccount("Ada", -1)

    def test_activity_126(self) -> None:
        solver = MiniProblemSolver()
        self.assertEqual(self._get(solver, "call_count"), 0)

        self.assertEqual(solver.sum_even_positives([-4, 0, 2, 3, 6]), 8)
        self.assertEqual(solver.sum_even_positives([]), 0)

        raw = [3, 1, 3, 2, 1, 4]
        self.assertEqual(solver.remove_duplicates_preserve_order(raw), [3, 1, 2, 4])
        self.assertEqual(raw, [3, 1, 3, 2, 1, 4])  # did not mutate input

        self.assertEqual(solver.longest_word("Cat, dog! Fox?"), "Fox")
        self.assertEqual(solver.longest_word("Python rocks!!"), "Python")
        self.assertEqual(solver.longest_word("... !!!"), "")

        self.assertEqual(self._get(solver, "call_count"), 6)

    def test_activity_127(self) -> None:
        cart = ShoppingCart(tax_rate=0.15)
        self.assertEqual(cart.subtotal(), 0.0)
        self.assertEqual(cart.tax_amount(), 0.0)
        self.assertEqual(cart.total(), 0.0)

        notebook = CartItem("Notebook", 25.0, quantity=2)
        pen = CartItem("Pen", 5.0, quantity=4)
        self.assertEqual(notebook.line_total(), 50.0)

        cart.add_item(notebook)
        cart.add_item(pen)
        self.assertEqual(cart.subtotal(), 70.0)
        self.assertEqual(cart.tax_amount(), 10.5)
        self.assertEqual(cart.total(), 80.5)

        self.assertTrue(cart.remove_by_name("Pen"))
        self.assertFalse(cart.remove_by_name("Pen"))
        self.assertEqual(cart.subtotal(), 50.0)

        with self.assertRaises(ValueError):
            CartItem("", 10.0)
        with self.assertRaises(ValueError):
            CartItem("Glue", -1.0)
        with self.assertRaises(ValueError):
            CartItem("Glue", 2.0, quantity=0)
        with self.assertRaises(ValueError):
            ShoppingCart(tax_rate=1.5)

    def test_activity_128(self) -> None:
        canvas = GridCanvas(5, 3)
        canvas.draw_border("#")
        canvas.set_cell(1, 2, "@")
        self.assertEqual(canvas.get_cell(1, 2), "@")
        self.assertEqual(canvas.get_cell(0, 0), "#")
        rendered = canvas.render()
        self.assertEqual(rendered, "# # # # #\n#   @   #\n# # # # #")
        for line in rendered.splitlines():
            self.assertEqual(line, line.rstrip(" "))

        thin_h = GridCanvas(4, 1)
        thin_h.draw_border("*")
        self.assertEqual(thin_h.render(), "* * * *")

        thin_v = GridCanvas(1, 3)
        thin_v.draw_border("+")
        self.assertEqual(thin_v.render(), "+\n+\n+")

        with self.assertRaises(ValueError):
            GridCanvas(0, 3)
        with self.assertRaises(ValueError):
            canvas.set_cell(3, 0, "X")
        with self.assertRaises(ValueError):
            canvas.get_cell(0, 5)

    def test_activity_129(self) -> None:
        self.assertTrue(issubclass(SquareHaloShape, Shape))
        self.assertTrue(issubclass(RectangleHaloShape, Shape))

        sq = SquareHaloShape(3)
        self.assertIsInstance(sq, Shape)
        self.assertEqual(
            sq.border_cells(),
            [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0)],
        )
        self.assertEqual(sq.perimeter_count(), 8)
        self.assertEqual(sq.summary(), "Square(3): 8 border cells")

        rect = RectangleHaloShape(4, 3)
        self.assertEqual(rect.perimeter_count(), 10)
        self.assertEqual(rect.summary(), "Rectangle(4x3): 10 border cells")

        thin = RectangleHaloShape(4, 1)
        self.assertEqual(thin.border_cells(), [(0, 0), (0, 1), (0, 2), (0, 3)])
        self.assertEqual(thin.perimeter_count(), 4)

        with self.assertRaises(NotImplementedError):
            Shape("Base").border_cells()
        with self.assertRaises(ValueError):
            SquareHaloShape(0)
        with self.assertRaises(ValueError):
            RectangleHaloShape(3, 0)

    def test_activity_130(self) -> None:
        track = [(0, 0), (0, 1), (1, 1), (1, 0)]
        runner = HaloRunner(track)
        # Mutating caller list must not corrupt runner's track
        track.clear()

        self.assertEqual(runner.position, (0, 0))
        self.assertEqual(runner.index, 0)
        self.assertEqual(runner.laps_completed, 0)

        self.assertEqual(runner.step(), (0, 1))
        self.assertEqual(runner.step(4), (0, 1))
        self.assertEqual(runner.index, 1)
        self.assertEqual(runner.laps_completed, 1)

        runner.reset()
        self.assertEqual(runner.position, (0, 0))
        self.assertEqual(runner.laps_completed, 0)

        # Negative counter-clockwise steps
        self.assertEqual(runner.step(-1), (1, 0))
        self.assertEqual(runner.index, 3)
        self.assertEqual(runner.laps_completed, 0)
        self.assertEqual(runner.step(-3), (0, 0))
        self.assertEqual(runner.laps_completed, 1)

        with self.assertRaises(ValueError):
            HaloRunner([])

    def test_activity_131(self) -> None:
        initial = {"Zara": 100, "Alex": 100, "Maya": 150}
        sb = Scoreboard(initial)
        initial["Hacker"] = 9999  # must not mutate scoreboard

        self.assertEqual(self._eval(len, sb), 3)
        self.assertTrue(self._eval(lambda s: "Maya" in s, sb))
        self.assertFalse(self._eval(lambda s: "Hacker" in s, sb))
        self.assertEqual(sb.score_of("Maya"), 150)
        self.assertEqual(sb.score_of("Unknown"), 0)

        self.assertEqual(sb.top(2), [("Maya", 150), ("Alex", 100)])
        self.assertEqual(sb.top(0), [])
        self.assertEqual(self._eval(list, sb), ["Maya", "Alex", "Zara"])

        self.assertEqual(sb.record("Alex", 50), 150)
        self.assertEqual(sb.record("Nova", 20), 20)
        self.assertEqual(sb.top(2), [("Alex", 150), ("Maya", 150)])

        other = Scoreboard({"Nova": 20, "Maya": 150, "Alex": 150, "Zara": 100})
        self.assertTrue(self._eval(lambda a, b: a == b, sb, other))
        self.assertFalse(self._eval(lambda a, b: a == b, sb, {"Maya": 150}))

    def test_activity_132(self) -> None:
        order = OrderWorkflow("  ORD-1001  ")
        self.assertEqual(self._get(order, "order_id"), "ORD-1001")
        self.assertEqual(self._get(order, "state"), "DRAFT")
        self.assertEqual(self._get(order, "history"), ["DRAFT"])
        self.assertFalse(order.is_terminal())

        self.assertTrue(order.can_transition_to("PAID"))
        self.assertTrue(order.can_transition_to("CANCELLED"))
        self.assertFalse(order.can_transition_to("SHIPPED"))
        self.assertFalse(order.can_transition_to("REFUNDED"))

        self.assertEqual(order.transition_to("PAID"), "PAID")
        self.assertEqual(order.transition_to("SHIPPED"), "SHIPPED")
        self.assertFalse(order.can_transition_to("CANCELLED"))

        # Cannot cancel after shipping!
        with self.assertRaises(ValueError):
            order.transition_to("CANCELLED")
        self.assertEqual(self._get(order, "state"), "SHIPPED")

        self.assertEqual(order.transition_to("DELIVERED"), "DELIVERED")
        self.assertTrue(order.is_terminal())
        self.assertEqual(
            self._get(order, "history"),
            ["DRAFT", "PAID", "SHIPPED", "DELIVERED"],
        )

        # Terminal state rejects any further transition
        with self.assertRaises(ValueError):
            order.transition_to("CANCELLED")

        # Cancel flow from DRAFT
        cancelled = OrderWorkflow("ORD-1002")
        self.assertEqual(cancelled.transition_to("CANCELLED"), "CANCELLED")
        self.assertTrue(cancelled.is_terminal())
        with self.assertRaises(ValueError):
            cancelled.transition_to("PAID")

        with self.assertRaises(ValueError):
            OrderWorkflow("   ")


if __name__ == "__main__":
    unittest.main()
