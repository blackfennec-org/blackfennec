import unittest

from doubles.black_fennec.type_system.double_template_registry import TemplateRegistryMock
from doubles.black_fennec.structure.double_map import MapMock
from doubles.double_dummy import Dummy
from doubles.black_fennec.interpretation.double_interpretation_service import InterpretationServiceMock
from src.black_fennec.interpretation.auction.offer import Offer
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.string import String
from src.visualisation.base.address.address import Address
from src.visualisation.base.address.address_bidder import AddressBidder
from src.visualisation.core.map.map_bidder import MapBidder


class AddressBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        AddressBidder()

    def test_offer_equal_address_offer(self):
        bidder = AddressBidder()
        subject = MapMock({})
        expected_offer = Offer(subject, 1, Address.TEMPLATE, Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)

    def test_offer_address_like_structure(self):
        map_bidder = MapBidder(
            InterpretationServiceMock([]),
            TemplateRegistryMock())
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
