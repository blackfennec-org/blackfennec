import unittest

from doubles.double_dummy import Dummy
from src.black_fennec.interpretation.auction.offer import Offer
from src.black_fennec.structure.reference import Reference
from src.visualisation.core.reference.reference_bidder import ReferenceBidder
from src.visualisation.core.reference.reference_template import ReferenceTemplate
from src.visualisation.core.string.string_template import StringTemplate


class ReferenceBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        ReferenceBidder()

    def test_offer_for_reference(self):
        bidder = ReferenceBidder()
        subject = Reference(Dummy())
        lesser_offer = Offer(subject, 0, ReferenceTemplate(), Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, lesser_offer)

    def test_offer_greater_than_string_offer(self):
        bidder = ReferenceBidder()
        subject = Reference(Dummy())
        lesser_offer = Offer(subject, 0, StringTemplate(), Dummy())
        offer = bidder.bid(subject)
        self.assertGreater(offer, lesser_offer)

    def test_offer_equal_map_offer(self):
        bidder = ReferenceBidder()
        subject = Reference(Dummy())
        expected_offer = Offer(subject, 0, ReferenceTemplate(), Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)
