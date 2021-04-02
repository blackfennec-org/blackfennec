import unittest

from src.core.auction import Offer
from src.core.boolean import Boolean, BooleanBidder

class BooleanBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        BooleanBidder()

    def test_returns_true_on_bid_for_boolean(self):
        bidder = BooleanBidder()
        subject = Boolean()
        lesser_offer = Offer(subject, 0, 0)
        offer = bidder.bid(subject)
        self.assertGreater(offer, lesser_offer)

    def test_returns_false_on_bid_for_not_boolean(self):
        bidder = BooleanBidder()
        subject = {}
        expected_offer = Offer(subject, 0, 0)
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)
