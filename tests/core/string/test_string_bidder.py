import unittest

from doubles.dummy import Dummy
from src.core.auction import Offer
from src.core.string import String
from src.core.string.string_bidder import StringBidder


class StringBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        StringBidder()

    def test_returns_true_on_bid_for_string(self):
        bidder = StringBidder()
        subject = String()
        lesser_offer = Offer(subject, 0, 0, Dummy())
        offer = bidder.bid(subject)
        self.assertGreater(offer, lesser_offer)

    def test_returns_false_on_bid_for_not_string(self):
        bidder = StringBidder()
        subject = {}
        expected_offer = Offer(subject, 0, 0, Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)
