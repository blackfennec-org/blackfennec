import unittest

from src.core.boolean import Boolean, BooleanBidder

class BooleanBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        BooleanBidder()

    def test_returns_true_on_bid_for_boolean(self):
        bidder = BooleanBidder()
        self.assertTrue(bidder.bid(Boolean()))

    def test_returns_false_on_bid_for_not_boolean(self):
        bidder = BooleanBidder()
        not_boolean = {}
        self.assertFalse(bidder.bid(not_boolean))
    