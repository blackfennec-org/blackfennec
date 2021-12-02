import unittest

from doubles.black_fennec.interpretation.double_interpretation_service import InterpretationServiceMock
from doubles.black_fennec.type_system.double_template_registry import TemplateRegistryMock
from src.black_fennec.interpretation.auction.auctioneer import Auctioneer
from src.black_fennec.interpretation.specification import Specification
from src.black_fennec.structure.boolean import Boolean
from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.string import String
from src.visualisation.core.boolean.boolean_bidder import BooleanBidder
from src.visualisation.core.boolean.boolean_view_factory import BooleanViewFactory
from src.visualisation.core.list.list_bidder import ListBidder
from src.visualisation.core.list.list_view_factory import ListViewFactory
from src.visualisation.core.map.map_bidder import MapBidder
from src.visualisation.core.map.map_view_factory import MapViewFactory
from src.visualisation.core.number.number_bidder import NumberBidder
from src.visualisation.core.number.number_view_factory import NumberViewFactory
from src.visualisation.core.string.string_bidder import StringBidder
from src.visualisation.core.string.string_view_factory import StringViewFactory
from src.black_fennec.type_system.type_registry import TypeRegistry


class AuctionOfCoreTypesTestSuite(unittest.TestCase):

    def setUp(self):
        registry = TypeRegistry()
        interpretation_service = InterpretationServiceMock([])
        template_registry = TemplateRegistryMock()
        registry.register_type(BooleanBidder())
        registry.register_type(NumberBidder())
        registry.register_type(StringBidder())
        registry.register_type(
            ListBidder(interpretation_service, template_registry))
        registry.register_type(
            MapBidder(interpretation_service, template_registry))
        self.registry = registry
        self.auctioneer = Auctioneer(registry)

    def tearDown(self) -> None:
        self.registry = None
        self.auctioneer = None

    def test_auction_boolean(self):
        result = self.auctioneer.auction(Boolean(), Specification())
        self.assertIsInstance(result[0], BooleanViewFactory)

    def test_auction_number(self):
        result = self.auctioneer.auction(Number(), Specification())
        self.assertIsInstance(result[0], NumberViewFactory)

    def test_auction_list(self):
        result = self.auctioneer.auction(List(), Specification())
        self.assertIsInstance(result[0], ListViewFactory)

    def test_auction_map(self):
        result = self.auctioneer.auction(Map(), Specification())
        self.assertIsInstance(result[0], MapViewFactory)

    def test_auction_string(self):
        result = self.auctioneer.auction(String(), Specification())
        self.assertIsInstance(result[0], StringViewFactory)
