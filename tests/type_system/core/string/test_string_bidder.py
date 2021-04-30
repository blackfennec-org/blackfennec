import unittest

from doubles.double_dummy import Dummy
from src.interpretation.auction import Offer
from src.structure.string import String
from src.type_system.core.string.string_bidder import StringBidder


class StringBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        StringBidder()

    def test_offer_greater_than_dummy_offer(self):
        bidder = StringBidder()
        subject = String()
        lesser_offer = Offer(subject, 0, Dummy(), Dummy())
        offer = bidder.bid(subject)
        self.assertGreater(offer, lesser_offer)

    def test_offer_equal_string_offer(self):
        bidder = StringBidder()
        subject = {}
        expected_offer = Offer(subject, 0, String(), Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)