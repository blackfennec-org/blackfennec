import unittest

from doubles.dummy import Dummy
from src.base.types.person.person_bidder import PersonBidder
from src.core.auction import Offer
from src.core.map import Map
from src.core.map.map_bidder import MapBidder
from src.core.string import String


class PersonBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        PersonBidder()

    def test_offer_equal_map_offer(self):
        bidder = PersonBidder()
        subject = {}
        expected_offer = Offer(subject, 1, Map(), Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)

    def test_offer_person_like_structure(self):
        map_bidder = MapBidder()
        person_bidder = PersonBidder()
        subject = Map({
            'courtesy_title': String('courtesy_title'),
            'first_name': String('first_name'),
            'middle_name': String('middle_name'),
            'last_name': String('last_name'),
            'suffix': String('suffix'),
            'gender': String('gender'),
            'sex': String('sex'),
            'marital_status': String('marital_status'),
            'nationality': String('nationality')
        })
        map_offer = map_bidder.bid(subject)
        person_offer = person_bidder.bid(subject)
        self.assertGreater(person_offer, map_offer)
