import unittest

from doubles.double_dummy import Dummy
from src.interpretation.auction import Offer
from src.structure.number import Number
from src.type_system.core.number.number_bidder import NumberBidder, create_number_template
from src.type_system.core.string.string_bidder import create_string_template


class NumberBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        NumberBidder()

    def test_offer_greater_than_string_offer(self):
        bidder = NumberBidder()
        subject = Number()
        lesser_offer = Offer(subject, 0, create_string_template(), Dummy())
        offer = bidder.bid(subject)
        self.assertGreater(offer, lesser_offer)

    def test_offer_equal_number_offer(self):
        bidder = NumberBidder()
        subject = {}
        expected_offer = Offer(subject, 0, create_number_template(), Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)
