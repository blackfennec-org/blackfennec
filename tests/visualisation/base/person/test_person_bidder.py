import unittest

from doubles.black_fennec.structure.double_map import MapMock
from doubles.double_dummy import Dummy
from doubles.black_fennec.interpretation.double_interpretation_service import InterpretationServiceMock
from doubles.black_fennec.type_system.double_template_registry import TemplateRegistryMock
from src.visualisation.base.address.address import Address
from src.visualisation.base.image.image import Image
from src.visualisation.base.person.person import Person
from src.visualisation.base.person.person_bidder import PersonBidder
from src.black_fennec.interpretation.auction.offer import Offer
from src.black_fennec.structure.map import Map
from src.visualisation.core.map.map_bidder import MapBidder
from src.black_fennec.structure.string import String


class PersonBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        PersonBidder()

    def test_offer_equal_map_offer(self):
        bidder = PersonBidder()
        subject = MapMock({})
        expected_offer = Offer(subject, 1, Person.TEMPLATE, Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)

    def test_offer_person_like_structure(self):
        map_bidder = MapBidder(
            InterpretationServiceMock([]),
            TemplateRegistryMock())
        person_bidder = PersonBidder()
        subject = Map({
            Person.COURTESY_TITLE_KEY: String(Person.COURTESY_TITLE_KEY),
            Person.FIRST_NAME_KEY: String(Person.FIRST_NAME_KEY),
            Person.MIDDLE_NAME_KEY: String(Person.MIDDLE_NAME_KEY),
            Person.LAST_NAME_KEY: String(Person.LAST_NAME_KEY),
            Person.SUFFIX_KEY: String(Person.SUFFIX_KEY),
            Person.PERSONAL_PHOTO_KEY: Map({
                Image.FILE_PATH_KEY: String(Image.FILE_PATH_KEY),
                Image.FILE_TYPE_KEY: String('image/test')
            }),
            Person.HOME_ADDRESS_KEY: Map({
                Address.FIRST_NAME_KEY: String(Address.FIRST_NAME_KEY),
                Address.LAST_NAME_KEY: String(Address.LAST_NAME_KEY),
                Address.STREET_KEY: String(Address.STREET_KEY),
                Address.STREET_NUMBER_KEY: String(Address.STREET_NUMBER_KEY),
                Address.CITY_KEY: String(Address.CITY_KEY)
            }),
            Person.GENDER_KEY: String(Person.GENDER_KEY),
            Person.SEX_KEY: String(Person.SEX_KEY),
            Person.MARITAL_STATUS_KEY: String(Person.MARITAL_STATUS_KEY),
            Person.NATIONALITY_KEY: String(Person.NATIONALITY_KEY)
        })
        map_offer = map_bidder.bid(subject)
        person_offer = person_bidder.bid(subject)
        self.assertGreater(person_offer, map_offer)
