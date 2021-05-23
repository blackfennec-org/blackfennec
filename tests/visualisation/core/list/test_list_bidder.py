import unittest

from doubles.black_fennec.structure.double_map import MapMock
from doubles.double_dummy import Dummy
from doubles.black_fennec.interpretation.double_interpretation_service import InterpretationServiceMock
from src.black_fennec.interpretation.auction.offer import Offer
from src.black_fennec.structure.list import List
from src.visualisation.core.list.list_bidder import ListBidder
from src.visualisation.core.list.list_template import ListTemplate
from src.visualisation.core.string.string_template import StringTemplate


class ListBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        ListBidder(InterpretationServiceMock([]))

    def test_offer_greater_than_string_offer(self):
        bidder = ListBidder(InterpretationServiceMock([]))
        subject = List()
        lesser_offer = Offer(subject, 0, StringTemplate(), Dummy())
        offer = bidder.bid(subject)
        self.assertGreater(offer, lesser_offer)

    def test_offer_equal_list_offer(self):
        bidder = ListBidder(InterpretationServiceMock([]))
        subject = MapMock({})
        expected_offer = Offer(subject, 0, ListTemplate(), Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)
