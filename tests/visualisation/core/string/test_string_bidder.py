import unittest

from doubles.black_fennec.structure.double_map import MapMock
from doubles.double_dummy import Dummy
from src.black_fennec.interpretation.auction.offer import Offer
from src.black_fennec.structure.string import String
from src.black_fennec.structure.type.number_type import NumberType
from src.visualisation.core.string.string_bidder import StringBidder
from src.black_fennec.structure.type.string_type import StringType


class StringBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        StringBidder()

    def test_offer_greater_than_number_offer(self):
        bidder = StringBidder()
        subject = String()
        lesser_offer = Offer(subject, 0, NumberType(), Dummy())
        offer = bidder.bid(subject)
        self.assertGreater(offer, lesser_offer)

    def test_offer_equal_string_offer(self):
        bidder = StringBidder()
        subject = MapMock({})
        expected_offer = Offer(subject, 0, StringType(), Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)
