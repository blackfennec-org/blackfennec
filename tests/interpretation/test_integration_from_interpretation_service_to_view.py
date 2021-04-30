import unittest

from doubles.interpretation.double_interpretation_service import InterpretationServiceMock
from src.interpretation.auction.auctioneer import Auctioneer
from src.structure.boolean import Boolean
from src.structure.list import List
from src.structure.map import Map
from src.structure.number import Number
from src.structure.string import String
from src.type_system.core.boolean.boolean_bidder import BooleanBidder
from src.type_system.core.boolean.boolean_view import BooleanView
from src.type_system.core.list.list_bidder import ListBidder
from src.type_system.core.list.list_view import ListView
from src.type_system.core.map.map_bidder import MapBidder
from src.type_system.core.map.map_view import MapView
from src.type_system.core.number.number_bidder import NumberBidder
from src.interpretation.interpretation_service import InterpretationService
from src.type_system.core.number.number_view import NumberView
from src.type_system.core.string.string_bidder import StringBidder
from src.type_system.core.string.string_view import StringView
from src.type_system.type_registry import TypeRegistry


class IntegrationFromInterpretationServiceToViewTestSuite(unittest.TestCase):

    def setUp(self):
        registry = TypeRegistry()
        interpretation_service = InterpretationServiceMock([])
        registry.register_type(BooleanBidder())
        registry.register_type(NumberBidder())
        registry.register_type(StringBidder())
        registry.register_type(ListBidder())
        registry.register_type(MapBidder(interpretation_service))
        auctioneer = Auctioneer(registry)
        self.interpreter = InterpretationService(auctioneer)

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
