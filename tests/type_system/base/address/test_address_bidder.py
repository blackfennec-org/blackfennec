import unittest

from doubles.double_dummy import Dummy
from doubles.interpretation.double_interpretation_service import InterpretationServiceMock
from src.interpretation.auction import Offer
from src.structure.map import Map
from src.structure.string import String
from src.type_system.base.address.address import Address
from src.type_system.base.address.address_bidder import AddressBidder
from src.type_system.core.map.map_bidder import MapBidder


class AddressBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        AddressBidder()

    def test_offer_equal_address_offer(self):
        bidder = AddressBidder()
        subject = {}
        expected_offer = Offer(subject, 1, Address.TEMPLATE, Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)

    def test_offer_address_like_structure(self):
        map_bidder = MapBidder(InterpretationServiceMock([]))
        address_bidder = AddressBidder()
        subject = Map({
            Address.FIRST_NAME_KEY: String(Address.FIRST_NAME_KEY),
            Address.LAST_NAME_KEY: String(Address.LAST_NAME_KEY),
            Address.STREET_KEY: String(Address.STREET_KEY),
            Address.STREET_NUMBER_KEY: String(Address.STREET_NUMBER_KEY),
            Address.CITY_KEY: String(Address.CITY_KEY)
        })
        map_offer = map_bidder.bid(subject)
        address_offer = address_bidder.bid(subject)
        self.assertGreater(address_offer, map_offer)
