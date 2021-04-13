import unittest

from doubles.dummy import Dummy
from src.base.types.address.address_bidder import AddressBidder
from src.core.auction import Offer
from src.core.map import Map
from src.core.map.map_bidder import MapBidder
from src.core.string import String


class AddressBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        AddressBidder()

    def test_offer_equal_map_offer(self):
        bidder = AddressBidder()
        subject = {}
        expected_offer = Offer(subject, 1, Map(), Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)

    def test_offer_address_like_structure(self):
        map_bidder = MapBidder()
        address_bidder = AddressBidder()
        subject = Map({
            'first_name': String('first_name'),
            'last_name': String('last_name'),
            'street': String('street'),
            'street_nr': String('street_nr'),
            'city': String('city')
        })
        map_offer = map_bidder.bid(subject)
        address_offer = address_bidder.bid(subject)
        self.assertGreater(address_offer, map_offer)
