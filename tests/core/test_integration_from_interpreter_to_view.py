import unittest

from doubles.dummy import Dummy
from src.core import Auctioneer
from src.core.boolean import Boolean, BooleanView
from src.core.boolean.boolean_bidder import BooleanBidder
from src.core.list import List, ListView
from src.core.list.list_bidder import ListBidder
from src.core.map import Map, MapView
from src.core.map.map_bidder import MapBidder
from src.core.number import Number, NumberView
from src.core.number.number_bidder import NumberBidder
from src.core.string import String, StringView
from src.core.interpreter import Interpreter
from src.core.string.string_bidder import StringBidder
from src.extension.type_registry import TypeRegistry


class IntegrationFromInterpreterToViewTestSuite(unittest.TestCase):

    def setUp(self):
        registry = TypeRegistry()
        registry.register_type(BooleanBidder())
        registry.register_type(NumberBidder())
        registry.register_type(StringBidder())
        registry.register_type(ListBidder())
        registry.register_type(MapBidder())
        auctioneer = Auctioneer(registry)
        self.interpreter = Interpreter(
            Dummy('NavigationService'),
            auctioneer
        )

    def tearDown(self) -> None:
        self.interpreter = None

    def test_boolean_interpreter_results_in_boolean_view(self):
        interpretation = self.interpreter.interpret(Boolean())
        view = interpretation.view
        self.assertIsInstance(view, BooleanView)

    def test_list_interpreter_results_in_list_view(self):
        interpretation = self.interpreter.interpret(List())
        view = interpretation.view
        self.assertIsInstance(view, ListView)

    def test_map_interpreter_results_in_map_view(self):
        interpretation = self.interpreter.interpret(Map())
        view = interpretation.view
        self.assertIsInstance(view, MapView)

    def test_number_interpreter_results_in_number_view(self):
        interpretation = self.interpreter.interpret(Number())
        view = interpretation.view
        self.assertIsInstance(view, NumberView)

    def test_string_interpreter_results_in_string_view(self):
        interpretation = self.interpreter.interpret(String())
        view = interpretation.view
        self.assertIsInstance(view, StringView)
