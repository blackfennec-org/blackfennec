import unittest

from doubles.double_dummy import Dummy
from src.black_fennec.interpretation.auction.offer import Offer
from src.black_fennec.structure.reference import Reference
from src.visualisation.core.reference.reference_bidder import ReferenceBidder, create_reference_template
from src.visualisation.core.string.string_bidder import create_string_template


class ReferenceBidderTestSuite(unittest.TestCase):
    def test_can_construct(self):
        ReferenceBidder()

    def test_offer_for_reference(self):
        bidder = ReferenceBidder()
        subject = Reference(Dummy())
        lesser_offer = Offer(subject, 0, create_reference_template(), Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, lesser_offer)

    def test_offer_greater_than_string_offer(self):
        bidder = ReferenceBidder()
        subject = Reference(Dummy())
        lesser_offer = Offer(subject, 0, create_string_template(), Dummy())
        offer = bidder.bid(subject)
        print(f'string_offer: cov({lesser_offer.coverage}), spec({lesser_offer.specificity})')
        print(f'reference_offer: cov({offer.coverage}), spec({offer.specificity})')
        self.assertGreater(offer, lesser_offer)

    def test_offer_equal_map_offer(self):
        bidder = ReferenceBidder()
        subject = Reference(Dummy())
        expected_offer = Offer(subject, 0, create_reference_template(), Dummy())
        offer = bidder.bid(subject)
        self.assertEqual(offer, expected_offer)
