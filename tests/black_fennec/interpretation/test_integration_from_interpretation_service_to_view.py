import unittest

from doubles.black_fennec.interpretation.double_interpretation_service import InterpretationServiceMock
from doubles.black_fennec.type_system.double_template_registry import TemplateRegistryMock
from src.black_fennec.interpretation.auction.auctioneer import Auctioneer
from src.black_fennec.structure.boolean import Boolean
from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.string import String
from src.visualisation.core.boolean.boolean_bidder import BooleanBidder
from src.visualisation.core.boolean.boolean_view import BooleanView
from src.visualisation.core.list.list_bidder import ListBidder
from src.visualisation.core.list.list_view import ListView
from src.visualisation.core.map.map_bidder import MapBidder
from src.visualisation.core.map.map_view import MapView
from src.visualisation.core.number.number_bidder import NumberBidder
from src.black_fennec.interpretation.interpretation_service import InterpretationService
from src.visualisation.core.number.number_view import NumberView
from src.visualisation.core.string.string_bidder import StringBidder
from src.visualisation.core.string.string_view import StringView
from src.black_fennec.type_system.type_registry import TypeRegistry


class IntegrationFromInterpretationServiceToViewTestSuite(unittest.TestCase):

    def setUp(self):
        registry = TypeRegistry()
        interpretation_service = InterpretationServiceMock([])
        template_registry = TemplateRegistryMock()
        registry.register_type(BooleanBidder())
        registry.register_type(NumberBidder())
        registry.register_type(StringBidder())
        registry.register_type(ListBidder(interpretation_service, template_registry))
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
