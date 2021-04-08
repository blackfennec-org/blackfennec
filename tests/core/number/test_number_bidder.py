import unittest

from doubles.dummy import Dummy
from src.core.auction import Offer
from src.core.number import Number
from src.core.number.number_bidder import NumberBidder


class NumberBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        NumberBidder()

    def test_returns_true_on_bid_for_number(self):
        bidder = NumberBidder()
        subject = Number()
        lesser_offer = Offer(subject, 0, 0, Dummy())
        offer = bidder.bid(subject)
        self.assertGreater(offer, lesser_offer)

    def test_returns_false_on_bid_for_not_number(self):
        bidder = NumberBidder()
        subject = {}
        expected_offer = Offer(subject, 0, 0, Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)
