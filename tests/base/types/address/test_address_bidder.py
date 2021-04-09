import unittest

from doubles.dummy import Dummy
from src.base.types.address.address_bidder import AddressBidder
from src.core.auction import Offer
from src.core.map import Map


class AddressBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        AddressBidder()

    def test_offer_greater_than_dummy_offer(self):
        bidder = AddressBidder()
        subject = Map()
        lesser_offer = Offer(subject, 1, Dummy(), Dummy())
        offer = bidder.bid(subject)
        self.assertGreater(offer, lesser_offer)

    def test_offer_equal_map_offer(self):
        bidder = AddressBidder()
        subject = {}
        expected_offer = Offer(subject, 1, Map(), Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)
    