import unittest

from doubles.double_dummy import Dummy
from src.interpretation.auction import Offer
from src.structure.boolean import Boolean
from src.type_system.core.boolean.boolean_bidder import BooleanBidder


class BooleanBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        BooleanBidder()

    def test_offer_greater_than_dummy_offer(self):
        bidder = BooleanBidder()
        subject = Boolean()
        lesser_offer = Offer(subject, 0, Dummy(), Dummy())
        offer = bidder.bid(subject)
        self.assertGreater(offer, lesser_offer)

    def test_offer_equal_boolean_offer(self):
        bidder = BooleanBidder()
        subject = {}
        expected_offer = Offer(subject, 0, Boolean(), Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)
