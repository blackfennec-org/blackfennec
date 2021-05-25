import unittest

from doubles.black_fennec.structure.double_map import MapMock
from doubles.double_dummy import Dummy
from doubles.black_fennec.interpretation.double_interpretation_service import InterpretationServiceMock
from doubles.black_fennec.type_system.double_template_registry import TemplateRegistryMock
from src.black_fennec.interpretation.auction.offer import Offer
from src.black_fennec.structure.map import Map
from src.visualisation.core.map.map_bidder import MapBidder
from src.visualisation.core.map.map_template import MapTemplate
from src.visualisation.core.string.string_template import StringTemplate


class MapBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        bidder = MapBidder(
            InterpretationServiceMock([]),
            TemplateRegistryMock())
        self.assertIsNotNone(bidder)

    def test_offer_greater_than_string_offer(self):
        bidder = MapBidder(
            InterpretationServiceMock([]),
            TemplateRegistryMock())
        subject = Map()
        lesser_offer = Offer(subject, 0, StringTemplate(), Dummy())
        offer = bidder.bid(subject)
        self.assertGreater(offer, lesser_offer)

    def test_offer_equal_map_offer(self):
        bidder = MapBidder(
            InterpretationServiceMock([]),
            TemplateRegistryMock())
        subject = MapMock({})
        expected_offer = Offer(subject, 0, MapTemplate(), Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)
