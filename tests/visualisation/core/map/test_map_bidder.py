import unittest

from doubles.black_fennec.structure.double_map import MapMock
from doubles.double_dummy import Dummy
from doubles.black_fennec.interpretation.double_interpretation_service import InterpretationServiceMock
from doubles.black_fennec.type_system.double_type_registry import TypeRegistryMock
from src.black_fennec.interpretation.auction.offer import Offer
from src.black_fennec.structure.map import Map
from src.visualisation.core.map.map_bidder import MapBidder
from src.black_fennec.structure.type.map_type import MapType
from src.black_fennec.structure.type.string_type import StringType


class MapBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        bidder = MapBidder(
            InterpretationServiceMock([]),
            TypeRegistryMock())
        self.assertIsNotNone(bidder)

    def test_offer_greater_than_string_offer(self):
        bidder = MapBidder(
            InterpretationServiceMock([]),
            TypeRegistryMock())
        subject = Map()
        lesser_offer = Offer(subject, 0, StringType(), Dummy())
        offer = bidder.bid(subject)
        self.assertGreater(offer, lesser_offer)

    def test_offer_equal_map_offer(self):
        bidder = MapBidder(
            InterpretationServiceMock([]),
            TypeRegistryMock())
        subject = MapMock({})
        expected_offer = Offer(subject, 0, MapType(), Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)
