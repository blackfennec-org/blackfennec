import unittest

from src.interpretation.auction.auctioneer import Auctioneer
from src.structure.boolean import Boolean
from src.structure.list import List
from src.structure.map import Map
from src.structure.number import Number
from src.structure.string import String
from src.type_system.core.boolean.boolean_bidder import BooleanBidder
from src.type_system.core.boolean.boolean_view_factory import BooleanViewFactory
from src.type_system.core.list.list_bidder import ListBidder
from src.type_system.core.list.list_view_factory import ListViewFactory
from src.type_system.core.map.map_bidder import MapBidder
from src.type_system.core.map.map_view_factory import MapViewFactory
from src.type_system.core.number.number_bidder import NumberBidder
from src.type_system.core.number.number_view_factory import NumberViewFactory
from src.type_system.core.string.string_bidder import StringBidder
from src.type_system.core.string.string_view_factory import StringViewFactory
from src.type_system.type_registry import TypeRegistry


class AuctionOfCoreTypesTestSuite(unittest.TestCase):

    def setUp(self):
        registry = TypeRegistry()
        registry.register_type(BooleanBidder())
        registry.register_type(NumberBidder())
        registry.register_type(StringBidder())
        registry.register_type(ListBidder())
        registry.register_type(MapBidder())
        self.registry = registry
        self.auctioneer = Auctioneer(registry)

    def tearDown(self) -> None:
        self.registry = None
        self.auctioneer = None

    def test_auction_boolean(self):
        result = self.auctioneer.auction(Boolean())
        self.assertIsInstance(result[0], BooleanViewFactory)

    def test_auction_number(self):
        result = self.auctioneer.auction(Number())
        self.assertIsInstance(result[0], NumberViewFactory)

    def test_auction_list(self):
        result = self.auctioneer.auction(List())
        self.assertIsInstance(result[0], ListViewFactory)

    def test_auction_map(self):
        result = self.auctioneer.auction(Map())
        self.assertIsInstance(result[0], MapViewFactory)

    def test_auction_string(self):
        result = self.auctioneer.auction(String())
        self.assertIsInstance(result[0], StringViewFactory)
