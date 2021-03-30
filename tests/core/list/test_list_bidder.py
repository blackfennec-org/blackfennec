import unittest

from src.core.list import List, ListBidder

class ListBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        ListBidder()

    def test_returns_true_on_bid_for_list(self):
        bidder = ListBidder()
        self.assertTrue(bidder.bid(List()))

    def test_returns_false_on_bid_for_not_list(self):
        bidder = ListBidder()
        not_list = {}
        self.assertFalse(bidder.bid(not_list))
    