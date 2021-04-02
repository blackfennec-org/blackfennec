import unittest

from src.core.auction import Offer
from src.core.list import List, ListBidder

class ListBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        ListBidder()

    def test_returns_true_on_bid_for_list(self):
        bidder = ListBidder()
        subject = List()
        lesser_offer = Offer(subject, 0, 0)
        offer = bidder.bid(subject)
        self.assertGreater(offer, lesser_offer)

    def test_returns_false_on_bid_for_not_list(self):
        bidder = ListBidder()
        subject = {}
        expected_offer = Offer(subject, 0, 0)
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)
