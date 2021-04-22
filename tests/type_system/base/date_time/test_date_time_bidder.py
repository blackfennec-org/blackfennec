import unittest
from datetime import datetime

from doubles.dummy import Dummy
from doubles.interpretation.interpretation_service import InterpretationServiceMock
from src.interpretation.auction import Offer
from src.structure.map import Map
from src.structure.string import String
from src.type_system.base.date_time.date_time import DateTime
from src.type_system.base.date_time.date_time_bidder import DateTimeBidder
from src.type_system.core.map.map_bidder import MapBidder


class DateTimeBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        DateTimeBidder()

    def test_offer_equal_map_offer(self):
        bidder = DateTimeBidder()
        subject = {}
        expected_offer = Offer(subject, 1, Map(), Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)

    def test_offer_date_time_like_structure(self):
        map_bidder = MapBidder(InterpretationServiceMock([]))
        date_time_bidder = DateTimeBidder()
        subject = Map({
            DateTime.DATE_TIME_KEY: String(datetime.now().isoformat())
        })
        map_offer = map_bidder.bid(subject)
        date_time_offer = date_time_bidder.bid(subject)
        self.assertGreater(date_time_offer, map_offer)
