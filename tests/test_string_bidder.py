import unittest

from src.core.string import String, StringBidder

class StringBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        StringBidder()

    def test_returns_true_on_bid_for_string(self):
        bidder = StringBidder()
        self.assertTrue(bidder.bid(String()))

    def test_returns_false_on_bid_for_not_string(self):
        bidder = StringBidder()
        not_string = {}
        self.assertFalse(bidder.bid(not_string))
    