import unittest

from doubles.black_fennec.structure.double_map import MapMock
from doubles.double_dummy import Dummy
from src.black_fennec.interpretation.auction.offer import Offer
from src.black_fennec.structure.number import Number
from src.visualisation.core.number.number_bidder import NumberBidder
from src.visualisation.core.number.number_template import NumberTemplate
from src.visualisation.core.string.string_template import StringTemplate


class NumberBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        NumberBidder()

    def test_offer_greater_than_string_offer(self):
        bidder = NumberBidder()
        subject = Number()
        lesser_offer = Offer(subject, 0, StringTemplate(), Dummy())
        offer = bidder.bid(subject)
        self.assertGreater(offer, lesser_offer)

    def test_offer_equal_number_offer(self):
        bidder = NumberBidder()
        subject = MapMock({})
        expected_offer = Offer(subject, 0, NumberTemplate(), Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)
