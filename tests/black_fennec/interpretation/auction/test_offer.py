# -*- coding: utf-8 -*-
import unittest

from doubles.black_fennec.structure.double_structure import StructureMock
from doubles.double_dummy import Dummy
from src.black_fennec.interpretation.auction.coverage import Coverage
from src.black_fennec.interpretation.auction.offer import Offer
from src.black_fennec.structure.template.template_factory_visitor import TemplateFactoryVisitor


class OfferTestSuite(unittest.TestCase):
    def setUp(self) -> None:
        self.template_factory = TemplateFactoryVisitor()

    def tearDown(self) -> None:
        self.template_factory = None

    def test_can_create_offer(self):
        subject = StructureMock('Structure')
        specificity = 1
        template = StructureMock('Structure').accept(self.template_factory)
        view_factory = Dummy('ViewFactory')
        offer = Offer(subject, specificity, template, view_factory)
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
            offer.template,
            template,
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
        template = StructureMock('Structure').accept(self.template_factory)
        view_factory = Dummy('ViewFactory')
        offer = Offer(subject, specificity, template, view_factory)
        self.assertEqual(
            offer.subject,
            subject,
            msg='Offer has not initialized ' +
                'subject correctly'
        )

    def test_specificity_getter(self):
        subject = StructureMock('Structure')
        specificity = 1
        template = StructureMock('Structure').accept(self.template_factory)
        view_factory = Dummy('ViewFactory')
        offer = Offer(subject, specificity, template, view_factory)
        self.assertEqual(
            offer.specificity,
            specificity,
            msg='Offer has not initialized ' +
                'specificity correctly'
        )

    def test_template_getter(self):
        subject = StructureMock('Structure')
        specificity = 1
        template = StructureMock('Structure').accept(self.template_factory)
        view_factory = Dummy('ViewFactory')
        offer = Offer(subject, specificity, template, view_factory)
        self.assertEqual(
            offer.template,
            template,
            msg='Offer has not initialized ' +
                'template correctly'
        )

    def test_view_factory_getter(self):
        subject = StructureMock('Structure')
        specificity = 1
        template = StructureMock('Structure').accept(self.template_factory)
        view_factory = Dummy('ViewFactory')
        offer = Offer(subject, specificity, template, view_factory)
        self.assertEqual(
            offer.view_factory,
            view_factory,
            msg='Offer has not initialized ' +
                'view_factory correctly'
        )

    def test_coverage_getter_simple(self):
        subject = StructureMock('Structure')
        specificity = 1
        template = StructureMock('Structure').accept(self.template_factory)
        view_factory = Dummy('ViewFactory')
        offer = Offer(subject, specificity, template, view_factory)
        self.assertEqual(
            offer.coverage,
            Coverage.COVERED
        )

    def test_equal_offers_equality(self):
        subject = StructureMock('Structure')
        template = subject.accept(self.template_factory)
        offer = Offer(
            subject,
            specificity=1,
            template=template,
            type_view_factory=Dummy('StructureFactory')
        )
        other_offer = Offer(
            subject,
            specificity=1,
            template=template,
            type_view_factory=Dummy('StructureFactory')
        )
        self.assertTrue(
            offer == other_offer,
            msg='Equal offers are not equal'
        )

    def test_not_equal_offers_equality(self):
        subject = StructureMock('Structure')
        template = subject.accept(self.template_factory)
        offer = Offer(
            subject,
            specificity=1,
            template=template,
            type_view_factory=Dummy('StructureFactory')
        )
        other_offer = Offer(
            subject,
            specificity=2,
            template=template,
            type_view_factory=Dummy('StructureFactory')
        )
        self.assertFalse(
            offer == other_offer,
            msg='Not equal offers are equal'
        )

    def test_lower_than_equal(self):
        subject = StructureMock('Structure')
        template = subject.accept(self.template_factory)
        offer = Offer(
            subject,
            specificity=0,
            template=template,
            type_view_factory=Dummy('StructureFactory')
        )
        other_offer = Offer(
            subject,
            specificity=0,
            template=template,
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
        template = subject.accept(self.template_factory)
        greater_offer = Offer(
            subject,
            specificity=0,
            template=template,
            type_view_factory=Dummy('StructureFactory')
        )
        lower_offer = Offer(
            subject,
            specificity=1,
            template=template,
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
        template = subject.accept(self.template_factory)
        other_subject = StructureMock('Structure2')
        offer = Offer(
            subject,
            specificity=1,
            template=template,
            type_view_factory=Dummy('StructureFactory')
        )
        other_offer = Offer(
            other_subject,
            specificity=1,
            template=template,
            type_view_factory=Dummy('StructureFactory')
        )
        with self.assertRaises(
                ValueError,
                msg='Comparison of offers with different subject does ' +
                    'not throw ValueError'
        ):
            offer < other_offer # pylint: disable=pointless-statement

    def test_hash_unequal_values(self):
        subject = StructureMock('Structure')
        template = subject.accept(self.template_factory)
        other_subject = StructureMock('Structure2')
        offer = Offer(
            subject,
            specificity=1,
            template=template,
            type_view_factory=Dummy('StructureFactory')
        )
        other_offer = Offer(
            other_subject,
            specificity=2,
            template=template,
            type_view_factory=Dummy('StructureFactory')
        )
        self.assertNotEqual(hash(offer), hash(other_offer))

    def test_hash_equal_values(self):
        subject = StructureMock('Structure')
        template = subject.accept(self.template_factory)
        offer = Offer(
            subject,
            specificity=1,
            template=template,
            type_view_factory=Dummy('StructureFactory'))
        other_offer = Offer(
            subject,
            specificity=1,
            template=template,
            type_view_factory=Dummy('StructureFactory'))
        self.assertEqual(hash(offer), hash(other_offer))

    def test_representation(self):
        factory = Dummy('StructureFactory')
        subject = StructureMock('Structure')
        template = subject.accept(self.template_factory)
        offer = Offer(
            subject,
            specificity=1,
            template=template,
            type_view_factory=factory)
        representation = repr(offer)
        factory_representation = repr(factory)
        self.assertIn(factory_representation, representation)
