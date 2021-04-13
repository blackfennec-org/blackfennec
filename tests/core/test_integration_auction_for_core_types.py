import unittest

from src.core import Auctioneer
from src.core.boolean import BooleanViewFactory, Boolean
from src.core.boolean.boolean_bidder import BooleanBidder
from src.core.list import ListViewFactory, List
from src.core.list.list_bidder import ListBidder
from src.core.map import MapViewFactory, Map
from src.core.map.map_bidder import MapBidder
from src.core.number import NumberViewFactory, Number
from src.core.number.number_bidder import NumberBidder
from src.core.string import StringViewFactory, String
from src.core.string.string_bidder import StringBidder
from src.extension.type_registry import TypeRegistry


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
