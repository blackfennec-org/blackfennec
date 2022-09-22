# -*- coding: utf-8 -*-
import unittest

from doubles.black_fennec.structure.double_structure import StructureMock, StructureTypeMock
from doubles.double_dummy import Dummy
from src.black_fennec.interpretation.auction.coverage import Coverage
from src.black_fennec.interpretation.auction.offer import Offer


class OfferTestSuite(unittest.TestCase):

    def tearDown(self) -> None:
        self.type_factory = None

    def test_can_create_offer(self):
        subject = StructureMock('Structure')
        specificity = 1
        type = StructureTypeMock('StructureType')
        view_factory = Dummy('ViewFactory')
        offer = Offer(subject, specificity, type, view_factory)
        self.assertEqual(
            offer.subject,
            subject,
            msg='Offer has not initialized ' +
                'subject correctly'
        )
        self.assertEqual(
            offer.specificity,
            specificity,
            msg='Offer has not initialized ' +
                'specificity correctly'
        )
        self.assertEqual(
            offer.type,
            type,
            msg='Offer has not initialized ' +
                'coverage correctly'
        )
        self.assertEqual(
            offer.view_factory,
            view_factory,
            msg='Offer has not initialized ' +
                'view_factory correctly'
        )

    def test_subject_getter(self):
        subject = StructureMock('Structure')
        specificity = 1
        type = StructureTypeMock('StructureType')
        view_factory = Dummy('ViewFactory')
        offer = Offer(subject, specificity, type, view_factory)
        self.assertEqual(
            offer.subject,
            subject,
            msg='Offer has not initialized ' +
                'subject correctly'
        )

    def test_specificity_getter(self):
        subject = StructureMock('Structure')
        specificity = 1
        type = StructureTypeMock('StructureType')
        view_factory = Dummy('ViewFactory')
        offer = Offer(subject, specificity, type, view_factory)
        self.assertEqual(
            offer.specificity,
            specificity,
            msg='Offer has not initialized ' +
                'specificity correctly'
        )

    def test_type_getter(self):
        subject = StructureMock('Structure')
        specificity = 1
        type = StructureTypeMock('StructureType')
        view_factory = Dummy('ViewFactory')
        offer = Offer(subject, specificity, type, view_factory)
        self.assertEqual(
            offer.type,
            type,
            msg='Offer has not initialized ' +
                'type correctly'
        )

    def test_view_factory_getter(self):
        subject = StructureMock('Structure')
        specificity = 1
        type = StructureTypeMock('StructureType')
        view_factory = Dummy('ViewFactory')
        offer = Offer(subject, specificity, type, view_factory)
        self.assertEqual(
            offer.view_factory,
            view_factory,
            msg='Offer has not initialized ' +
                'view_factory correctly'
        )

    def test_coverage_getter_simple(self):
        subject = StructureMock('Structure')
        specificity = 1
        type = StructureTypeMock('StructureType', Coverage.COVERED)
        view_factory = Dummy('ViewFactory')
        offer = Offer(subject, specificity, type, view_factory)
        self.assertEqual(
            offer.coverage,
            Coverage.COVERED
        )

    def test_equal_offers_equality(self):
        subject = StructureMock('Structure')
        type = StructureTypeMock('StructureType', Coverage.COVERED)
        offer = Offer(
            subject,
            specificity=1,
            type=type,
            type_view_factory=Dummy('StructureFactory')
        )
        other_offer = Offer(
            subject,
            specificity=1,
            type=type,
            type_view_factory=Dummy('StructureFactory')
        )
        self.assertTrue(
            offer == other_offer,
            msg='Equal offers are not equal'
        )

    def test_not_equal_offers_equality(self):
        subject = StructureMock('Structure')
        type = StructureTypeMock('StructureType', Coverage.COVERED)
        offer = Offer(
            subject,
            specificity=1,
            type=type,
            type_view_factory=Dummy('StructureFactory')
        )
        other_offer = Offer(
            subject,
            specificity=2,
            type=type,
            type_view_factory=Dummy('StructureFactory')
        )
        self.assertFalse(
            offer == other_offer,
            msg='Not equal offers are equal'
        )

    def test_lower_than_equal(self):
        subject = StructureMock('Structure')
        type = StructureTypeMock('StructureType')
        offer = Offer(
            subject,
            specificity=0,
            type=type,
            type_view_factory=Dummy('StructureFactory')
        )
        other_offer = Offer(
            subject,
            specificity=0,
            type=type,
            type_view_factory=Dummy('StructureFactory')
        )
        self.assertFalse(
            offer < other_offer,
            msg='One offer lower than equal offer'
        )
        self.assertFalse(
            other_offer < offer,
            msg='One Offer lower than equal offer'
        )

    def test_lower_than_lower_and_greater(self):
        subject = StructureMock('Structure')
        type = StructureTypeMock('StructureType')
        greater_offer = Offer(
            subject,
            specificity=0,
            type=type,
            type_view_factory=Dummy('StructureFactory')
        )
        lower_offer = Offer(
            subject,
            specificity=1,
            type=type,
            type_view_factory=Dummy('StructureFactory')
        )
        self.assertFalse(
            greater_offer < lower_offer,
            msg='Lower offer not lower than greater offer'
        )
        self.assertTrue(
            lower_offer < greater_offer,
            msg='Greater Offer lower than lower offer'
        )

    def test_lower_than_with_different_subject(self):
        subject = StructureMock('Structure')
        type = StructureTypeMock('StructureType')
        other_subject = StructureMock('Structure2')
        offer = Offer(
            subject,
            specificity=1,
            type=type,
            type_view_factory=Dummy('StructureFactory')
        )
        other_offer = Offer(
            other_subject,
            specificity=1,
            type=type,
            type_view_factory=Dummy('StructureFactory')
        )
        with self.assertRaises(
                ValueError,
                msg='Comparison of offers with different subject does ' +
                    'not throw ValueError'
        ):
            offer < other_offer  # pylint: disable=pointless-statement

    def test_representation(self):
        factory = Dummy('StructureFactory')
        subject = StructureMock('Structure')
        type = StructureTypeMock('StructureType')
        offer = Offer(
            subject,
            specificity=1,
            type=type,
            type_view_factory=factory)
        representation = repr(offer)
        factory_representation = repr(factory)
        self.assertIn(factory_representation, representation)
