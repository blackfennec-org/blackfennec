import unittest

from doubles.double_dummy import Dummy
from doubles.interpretation.double_interpretation_service import InterpretationServiceMock
from src.interpretation.auction import Offer
from src.structure.reference import Reference
from src.type_system.core.reference.reference_bidder import ReferenceBidder


class ReferenceBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        ReferenceBidder()

    def test_offer_greater_than_dummy_offer(self):
        bidder = ReferenceBidder()
        subject = Reference(Dummy())
        lesser_offer = Offer(subject, 0, Dummy(), Dummy())
        offer = bidder.bid(subject)
        self.assertGreater(offer, lesser_offer)

    def test_offer_equal_map_offer(self):
        bidder = ReferenceBidder()
        subject = Reference(Dummy())
        expected_offer = Offer(subject, 0, Reference(Dummy()), Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)
