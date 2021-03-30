import unittest

from src.core.number import Number, NumberBidder

class NumberBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        NumberBidder()

    def test_returns_true_on_bid_for_number(self):
        bidder = NumberBidder()
        self.assertTrue(bidder.bid(Number()))

    def test_returns_false_on_bid_for_not_number(self):
        bidder = NumberBidder()
        not_number = {}
        self.assertFalse(bidder.bid(not_number))
    