# -*- coding: utf-8 -*-
import unittest

from doubles.dummy import Dummy
from src.core.offer import Offer


class InterpreterTestSuite(unittest.TestCase):
    def test_create_offer(self):
        subject = Dummy('Info')
        specificity = 1
        coverage = 1
        offer = Offer(subject, specificity, coverage)
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
            offer.coverage,
            coverage,
            msg='Offer has not initialized ' +
                'coverage correctly'
        )

    def test_create_invalid_offer_negative_coverage(self):
        subject = Dummy('Info')
        specificity = 1
        coverage = -0.01
        with self.assertRaises(
            ValueError,
            msg='Coverage is negative but Offer did not raise Value Error'
        ):
            Offer(subject, specificity, coverage)

    def test_create_invalid_offer_coverage_over_one(self):
        subject = Dummy('Info')
        specificity = 1
        coverage = 1.01
        with self.assertRaises(
            ValueError,
            msg='Coverage is over 1 but Offer did not raise Value Error'
        ):
            Offer(subject, specificity, coverage)

    def test_equal_offers_equality(self):
        subject = Dummy('Info')
        offer = Offer(subject, specificity = 1, coverage = 1)
        other_offer = Offer(subject, specificity = 1, coverage = 1)
        self.assertTrue(
            offer == other_offer,
            msg='Equal offers are not equal'
        )

    def test_not_equal_offers_equality(self):
        subject = Dummy('Info')
        offer = Offer(subject, specificity=1, coverage=1)
        other_offer = Offer(subject, specificity=2, coverage=1)
        self.assertFalse(
            offer == other_offer,
            msg='Not equal offers are equal'
        )

    def test_lower_than_equal(self):
        subject = Dummy('Info')
        offer = Offer(subject, specificity=1, coverage=1)
        other_offer = Offer(subject, specificity=2, coverage=1)
        self.assertFalse(
            offer < other_offer,
            msg='Lower offer lower than equal offer'
        )
        self.assertFalse(
            other_offer < offer,
            msg='Greater Offer lower than equal offer'
        )

    def test_lower_than(self):
        subject = Dummy('Info')
        offer = Offer(subject, specificity=1, coverage=0.5)
        other_offer = Offer(subject, specificity=1, coverage=0.49)
        self.assertFalse(
            offer < other_offer,
            msg='Lower offer not lower than greater offer'
        )
        self.assertTrue(
            other_offer < offer,
            msg='Greater Offer lower than lower offer'
        )

    def test_lower_than_with_different_subject(self):
        subject = Dummy('Info')
        other_subject = Dummy('Info2')
        offer = Offer(subject, specificity=1, coverage=1)
        other_offer = Offer(other_subject, specificity=1, coverage=1)
        with self.assertRaises(
                ValueError,
                msg='Comparison of offers with different subject does ' +
                    'not throw ValueError'
        ):
            offer < other_offer
