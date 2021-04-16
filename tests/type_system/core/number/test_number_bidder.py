import unittest

from doubles.dummy import Dummy
from src.interpretation.auction import Offer
from src.structure.number import Number
from src.type_system.core.number.number_bidder import NumberBidder


class NumberBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        NumberBidder()

    def test_offer_greater_than_dummy_offer(self):
        bidder = NumberBidder()
        subject = Number()
        lesser_offer = Offer(subject, 0, Dummy(), Dummy())
        offer = bidder.bid(subject)
        self.assertGreater(offer, lesser_offer)

    def test_offer_equal_number_offer(self):
        bidder = NumberBidder()
        subject = {}
        expected_offer = Offer(subject, 0, Number(), Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)
