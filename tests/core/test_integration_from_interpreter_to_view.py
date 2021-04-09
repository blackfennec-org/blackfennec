import unittest


from doubles.dummy import Dummy
from src.core import BooleanViewFactory, NumberViewFactory, StringViewFactory, \
    ListViewFactory, MapViewFactory, \
    Map, List, Interpreter, Boolean, BooleanView, \
    ListView, MapView, Number, NumberView, String, StringView


class IntegrationFromInterpreterToViewTestSuite(unittest.TestCase):

    def test_boolean_interpreter_results_in_boolean_view(self):
        factories = [BooleanViewFactory()]
        interpreter = Interpreter(Dummy('navigation service'), factories)
        interpretation = interpreter.interpret(Boolean())
        view = interpretation.view
        self.assertIsInstance(view, BooleanView)

    def test_list_interpreter_results_in_list_view(self):
        factories = [ListViewFactory()]
        interpreter = Interpreter(Dummy('navigation service'), factories)
        interpretation = interpreter.interpret(List())
        view = interpretation.view
        self.assertIsInstance(view, ListView)

    def test_map_interpreter_results_in_map_view(self):
        factories = [MapViewFactory()]
        interpreter = Interpreter(Dummy('navigation service'), factories)
        interpretation = interpreter.interpret(Map())
        view = interpretation.view
        self.assertIsInstance(view, MapView)

    def test_number_interpreter_results_in_number_view(self):
        factories = [NumberViewFactory()]
        interpreter = Interpreter(Dummy('navigation service'), factories)
        interpretation = interpreter.interpret(Number())
        view = interpretation.view
        self.assertIsInstance(view, NumberView)

    def test_string_interpreter_results_in_string_view(self):
        factories = [StringViewFactory()]
        interpreter = Interpreter(Dummy('navigation service'), factories)
        interpretation = interpreter.interpret(String())
        view = interpretation.view
        self.assertIsInstance(view, StringView)





