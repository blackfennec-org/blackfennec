import unittest

from doubles.black_fennec.structure.double_map import MapMock
from doubles.double_dummy import Dummy
from doubles.black_fennec.interpretation.double_interpretation_service import InterpretationServiceMock
from src.black_fennec.interpretation.auction.offer import Offer
from src.black_fennec.structure.map import Map
from src.visualisation.core.map.map_bidder import MapBidder, create_map_template
from src.visualisation.core.string.string_bidder import create_string_template


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
        subject = MapMock({})
        expected_offer = Offer(subject, 0, create_map_template(), Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)