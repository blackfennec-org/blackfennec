import unittest

from src.core import \
    BooleanBidder, BooleanViewFactory, Boolean, \
    NumberBidder, NumberViewFactory, Number, \
    StringViewFactory, StringBidder, String, \
    ListBidder, ListViewFactory, List, \
    MapBidder, MapViewFactory, Map, \
    Auctioneer
from src.extension.type_registry import TypeRegistry


class AuctionOfCoreTypesTestSuite(unittest.TestCase):

    def setUp(self):
        registry = TypeRegistry()
        registry.register_type(BooleanBidder(), BooleanViewFactory())
        registry.register_type(NumberBidder(), NumberViewFactory())
        registry.register_type(StringBidder(), StringViewFactory())
        registry.register_type(ListBidder(), ListViewFactory())
        registry.register_type(MapBidder(), MapViewFactory())
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
