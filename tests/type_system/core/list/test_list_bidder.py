import unittest

from doubles.double_dummy import Dummy
from doubles.interpretation.double_interpretation_service import InterpretationServiceMock
from src.interpretation.auction import Offer
from src.structure.list import List
from src.type_system.core.list.list_bidder import ListBidder, create_list_template
from src.type_system.core.string.string_bidder import create_string_template


class ListBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        ListBidder(InterpretationServiceMock([]))

    def test_offer_greater_than_string_offer(self):
        bidder = ListBidder(InterpretationServiceMock([]))
        subject = List()
        lesser_offer = Offer(subject, 0, create_string_template(), Dummy())
        offer = bidder.bid(subject)
        self.assertGreater(offer, lesser_offer)

    def test_offer_equal_list_offer(self):
        bidder = ListBidder(InterpretationServiceMock([]))
        subject = {}
        expected_offer = Offer(subject, 0, create_list_template(), Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)
