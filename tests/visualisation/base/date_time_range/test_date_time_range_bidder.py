import unittest
from datetime import datetime

from doubles.black_fennec.type_system.double_type_registry import TypeRegistryMock
from doubles.black_fennec.structure.double_map import MapMock
from doubles.double_dummy import Dummy
from doubles.black_fennec.interpretation.double_interpretation_service import InterpretationServiceMock
from src.black_fennec.interpretation.auction.offer import Offer
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.string import String
from src.visualisation.base.date_time_range.date_time_range import DateTimeRange
from src.visualisation.base.date_time_range.date_time_range_bidder import DateTimeRangeBidder
from src.visualisation.core.map.map_bidder import MapBidder


class DateTimeRangeBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        DateTimeRangeBidder()

    def test_offer_equal_map_offer(self):
        bidder = DateTimeRangeBidder()
        subject = MapMock({})
        expected_offer = Offer(subject, 1, DateTimeRange.TYPE, Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)

    def test_offer_date_time_range_like_structure(self):
        map_bidder = MapBidder(
            InterpretationServiceMock([]),
            TypeRegistryMock())
        date_time_range_bidder = DateTimeRangeBidder()
        subject = Map({
            DateTimeRange.START_KEY: String(datetime.now().isoformat()),
            DateTimeRange.END_KEY: String(datetime.now().isoformat())
        })
        map_offer = map_bidder.bid(subject)
        date_time_range_offer = date_time_range_bidder.bid(subject)
        self.assertGreater(date_time_range_offer, map_offer)

    def test_invalid_date_time_range_structure(self):
        map_bidder = MapBidder(
            InterpretationServiceMock([]),
            TypeRegistryMock())
        date_time_range_bidder = DateTimeRangeBidder()
        subject = Map({
            DateTimeRange.START_KEY: String('9999-12-31T23:59:5'),
            DateTimeRange.END_KEY: String('9999-12-31 23:59:50')
        })
        map_offer = map_bidder.bid(subject)
        date_time_range_offer = date_time_range_bidder.bid(subject)
        self.assertGreater(map_offer, date_time_range_offer)
