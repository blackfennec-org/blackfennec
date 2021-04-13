import unittest

from src.core.auction import Offer
from src.core.map import Map, MapBidder

class MapBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        MapBidder()

    def test_returns_true_on_bid_for_map(self):
        bidder = MapBidder()
        subject = Map()
        lesser_offer = Offer(subject, 0, 0)
        offer = bidder.bid(subject)
        self.assertGreater(offer, lesser_offer)

    def test_returns_false_on_bid_for_not_map(self):
        bidder = MapBidder()
        subject = {}
        expected_offer = Offer(subject, 0, 0)
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)
    