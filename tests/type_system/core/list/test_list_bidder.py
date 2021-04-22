import unittest

from doubles.double_dummy import Dummy
from src.interpretation.auction import Offer
from src.structure.list import List
from src.type_system.core.list.list_bidder import ListBidder


class ListBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        ListBidder()

    def test_offer_greater_than_dummy_offer(self):
        bidder = ListBidder()
        subject = List()
        lesser_offer = Offer(subject, 0, Dummy(), Dummy())
        offer = bidder.bid(subject)
        self.assertGreater(offer, lesser_offer)

    def test_offer_equal_list_offer(self):
        bidder = ListBidder()
        subject = {}
        expected_offer = Offer(subject, 0, List(), Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)
