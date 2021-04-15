import unittest

from doubles.dummy import Dummy
from src.core import Auctioneer
from src.core.types.boolean import Boolean, BooleanView
from src.core.types.boolean.boolean_bidder import BooleanBidder
from src.core.types.list import List, ListView
from src.core.types.list.list_bidder import ListBidder
from src.core.types.map import Map, MapView
from src.core.types.map.map_bidder import MapBidder
from src.core.types.number import Number, NumberView
from src.core.types.number.number_bidder import NumberBidder
from src.core.types.string import String, StringView
from src.core.interpretation_service import InterpretationService
from src.core.types.string.string_bidder import StringBidder
from src.extension.type_registry import TypeRegistry


class IntegrationFromInterpretationServiceToViewTestSuite(unittest.TestCase):

    def setUp(self):
        registry = TypeRegistry()
        registry.register_type(BooleanBidder())
        registry.register_type(NumberBidder())
        registry.register_type(StringBidder())
        registry.register_type(ListBidder())
        registry.register_type(MapBidder())
        auctioneer = Auctioneer(registry)
        self.interpreter = InterpretationService(
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
