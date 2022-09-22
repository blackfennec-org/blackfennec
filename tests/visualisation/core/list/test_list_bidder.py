import unittest

from doubles.black_fennec.structure.double_map import MapMock
from doubles.black_fennec.type_system.double_type_registry import TypeRegistryMock
from doubles.double_dummy import Dummy
from doubles.black_fennec.interpretation.double_interpretation_service import InterpretationServiceMock
from src.black_fennec.interpretation.auction.offer import Offer
from src.black_fennec.structure.list import List
from src.visualisation.core.list.list_bidder import ListBidder
from src.black_fennec.structure.type.list_type import ListType
from src.black_fennec.structure.type.string_type import StringType


class ListBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        ListBidder(
            InterpretationServiceMock([]),
            TypeRegistryMock()
        )

    def test_offer_greater_than_string_offer(self):
        bidder = ListBidder(
            InterpretationServiceMock([]),
            TypeRegistryMock()
        )
        subject = List()
        lesser_offer = Offer(subject, 0, StringType(), Dummy())
        offer = bidder.bid(subject)
        self.assertGreater(offer, lesser_offer)

    def test_offer_equal_list_offer(self):
        bidder = ListBidder(
            InterpretationServiceMock([]),
            TypeRegistryMock()
        )
        subject = MapMock({})
        expected_offer = Offer(subject, 0, ListType(), Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)
