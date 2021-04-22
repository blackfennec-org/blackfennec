import unittest

from doubles.dummy import Dummy
from doubles.interpretation.interpretation_service import InterpretationServiceMock
from src.interpretation.auction import Offer
from src.structure.map import Map
from src.structure.string import String
from src.type_system.base.address.address_bidder import AddressBidder
from src.type_system.core.map.map_bidder import MapBidder


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
        map_bidder = MapBidder(InterpretationServiceMock([]))
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
