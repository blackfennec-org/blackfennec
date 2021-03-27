import unittest

from src.core.map import Map, MapBidder

class StringBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        MapBidder()

    def test_returns_true_on_bid_for_map(self):
        bidder = MapBidder()
        self.assertTrue(bidder.bid(Map()))

    def test_returns_false_on_bid_for_not_map(self):
        bidder = MapBidder()
        not_map = {}
        self.assertFalse(bidder.bid(not_map))
    