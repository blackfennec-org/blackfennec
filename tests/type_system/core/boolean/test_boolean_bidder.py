import unittest

from doubles.double_dummy import Dummy
from src.interpretation.auction import Offer
from src.structure.boolean import Boolean
from src.type_system.core.boolean.boolean_bidder import BooleanBidder, create_boolean_template
from src.type_system.core.string.string_bidder import create_string_template


class BooleanBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        BooleanBidder()

    def test_offer_greater_than_string_offer(self):
        bidder = BooleanBidder()
        subject = Boolean()
        lesser_offer = Offer(subject, 0, create_string_template(), Dummy())
        offer = bidder.bid(subject)
        self.assertGreater(offer, lesser_offer)

    def test_offer_equal_boolean_offer(self):
        bidder = BooleanBidder()
        subject = {}
        expected_offer = Offer(subject, 0, create_boolean_template(), Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)
