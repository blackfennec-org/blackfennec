import unittest

from src.core.string import String, StringTypeBidder

class StringTypeBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        StringTypeBidder()

    def test_returns_true_on_bid_for_string(self):
        bidder = StringTypeBidder()
        self.assertTrue(bidder.bid(String()))

    def test_returns_false_on_bid_for_not_string(self):
        bidder = StringTypeBidder()
        not_string = {}
        self.assertFalse(bidder.bid(not_string))
    