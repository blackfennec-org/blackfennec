import unittest

from doubles.double_dummy import Dummy
from src.black_fennec.interpretation.auction.offer import Offer
from src.black_fennec.structure.string import String
from src.visualisation.core.number.number_bidder import create_number_template
from src.visualisation.core.string.string_bidder import StringBidder, create_string_template


class StringBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        StringBidder()

    def test_offer_greater_than_number_offer(self):
        bidder = StringBidder()
        subject = String()
        lesser_offer = Offer(subject, 0, create_number_template(), Dummy())
        offer = bidder.bid(subject)
        self.assertGreater(offer, lesser_offer)

    def test_offer_equal_string_offer(self):
        bidder = StringBidder()
        subject = {}
        expected_offer = Offer(subject, 0, create_string_template(), Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)
