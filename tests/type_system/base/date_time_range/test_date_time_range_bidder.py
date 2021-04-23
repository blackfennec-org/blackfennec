import unittest
from datetime import datetime

from doubles.dummy import Dummy
from doubles.interpretation.interpretation_service import InterpretationServiceMock
from src.interpretation.auction import Offer
from src.structure.map import Map
from src.structure.string import String
from src.type_system.base.date_time_range.date_time_range import DateTimeRange
from src.type_system.base.date_time_range.date_time_range_bidder import DateTimeRangeBidder
from src.type_system.core.map.map_bidder import MapBidder


class DateTimeRangeBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        DateTimeRangeBidder()

    def test_offer_equal_map_offer(self):
        bidder = DateTimeRangeBidder()
        subject = {}
        expected_offer = Offer(subject, 1, Map(), Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)

    def test_offer_date_time_range_like_structure(self):
        map_bidder = MapBidder(InterpretationServiceMock([]))
        date_time_range_bidder = DateTimeRangeBidder()
        subject = Map({
            DateTimeRange.START_KEY: String(datetime.now().isoformat()),
            DateTimeRange.END_KEY: String(datetime.now().isoformat())
        })
        map_offer = map_bidder.bid(subject)
        date_time_range_offer = date_time_range_bidder.bid(subject)
        self.assertGreater(date_time_range_offer, map_offer)

    def test_invalid_date_time_range_structure(self):
        map_bidder = MapBidder(InterpretationServiceMock([]))
        date_time_range_bidder = DateTimeRangeBidder()
        subject = Map({
            DateTimeRange.START_KEY: String('9999-12-31T23:59:5'),
            DateTimeRange.END_KEY: String('9999-12-31 23:59:50')
        })
        map_offer = map_bidder.bid(subject)
        date_time_range_offer = date_time_range_bidder.bid(subject)
        self.assertGreater(map_offer, date_time_range_offer)
