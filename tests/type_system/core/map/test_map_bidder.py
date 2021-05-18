import unittest

from doubles.double_dummy import Dummy
from doubles.interpretation.double_interpretation_service import InterpretationServiceMock
from src.interpretation.auction import Offer
from src.structure.map import Map
from src.type_system.core.map.map_bidder import MapBidder, create_map_template
from src.type_system.core.string.string_bidder import create_string_template


class MapBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        MapBidder(InterpretationServiceMock([]))

    def test_offer_greater_than_string_offer(self):
        bidder = MapBidder(InterpretationServiceMock([]))
        subject = Map()
        lesser_offer = Offer(subject, 0, create_string_template(), Dummy())
        offer = bidder.bid(subject)
        self.assertGreater(offer, lesser_offer)

    def test_offer_equal_map_offer(self):
        bidder = MapBidder(InterpretationServiceMock([]))
        subject = {}
        expected_offer = Offer(subject, 0, create_map_template(), Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)
