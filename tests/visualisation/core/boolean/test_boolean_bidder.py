import unittest

from doubles.black_fennec.structure.double_map import MapMock
from doubles.double_dummy import Dummy
from src.black_fennec.interpretation.auction.offer import Offer
from src.black_fennec.structure.boolean import Boolean
from src.visualisation.core.boolean.boolean_bidder import BooleanBidder
from src.black_fennec.structure.type.boolean_type import BooleanType
from src.black_fennec.structure.type.string_type import StringType


class BooleanBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        BooleanBidder()

    def test_offer_greater_than_string_offer(self):
        bidder = BooleanBidder()
        subject = Boolean()
        lesser_offer = Offer(subject, 0, StringType(), Dummy())
        offer = bidder.bid(subject)
        self.assertGreater(offer, lesser_offer)

    def test_offer_equal_boolean_offer(self):
        bidder = BooleanBidder()
        subject = MapMock({})
        expected_offer = Offer(subject, 0, BooleanType(), Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)
