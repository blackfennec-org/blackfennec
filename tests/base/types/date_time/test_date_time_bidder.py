import unittest
from datetime import datetime

from doubles.dummy import Dummy
from src.base.types.date_time.date_time import DateTime
from src.base.types.date_time.date_time_bidder import DateTimeBidder
from src.core.auction import Offer
from src.core.types.map import Map
from src.core.types.map.map_bidder import MapBidder
from src.core.types.string import String


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
        map_bidder = MapBidder()
        date_time_bidder = DateTimeBidder()
        subject = Map({
            DateTime.DATE_TIME_KEY: String(datetime.now().isoformat())
        })
        map_offer = map_bidder.bid(subject)
        date_time_offer = date_time_bidder.bid(subject)
        self.assertGreater(date_time_offer, map_offer)
