import unittest

from doubles.black_fennec.structure.double_map import MapMock
from doubles.double_dummy import Dummy
from src.black_fennec.interpretation.auction.offer import Offer
from src.black_fennec.structure.number import Number
from src.visualisation.core.number.number_bidder import NumberBidder
from src.black_fennec.structure.type.number_type import NumberType
from src.black_fennec.structure.type.string_type import StringType


class NumberBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        NumberBidder()

    def test_offer_greater_than_string_offer(self):
        bidder = NumberBidder()
        subject = Number()
        lesser_offer = Offer(subject, 0, StringType(), Dummy())
        offer = bidder.bid(subject)
        self.assertGreater(offer, lesser_offer)

    def test_offer_equal_number_offer(self):
        bidder = NumberBidder()
        subject = MapMock({})
        expected_offer = Offer(subject, 0, NumberType(), Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)
