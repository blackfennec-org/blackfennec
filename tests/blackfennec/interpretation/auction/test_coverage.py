# -*- coding: utf-8 -*-
import unittest

from blackfennec.interpretation.auction.coverage import Coverage


class CoverageTestSuite(unittest.TestCase):

    def test_can_construct_not_covered(self):
        Coverage(1, 0)

    def test_is_covered_true(self):
        coverage = Coverage(1, 1)
        self.assertTrue(coverage.is_covered())

    def test_is_covered_false(self):
        coverage = Coverage(1, 0)
        self.assertFalse(coverage.is_covered())

    def test_equal_coverages_equality(self):
        coverage = Coverage(1, 1)
        other_coverage = Coverage(2, 2)
        self.assertTrue(
            coverage == other_coverage,
            msg='Equal coverages are not equal'
        )

    def test_not_equal_coverages_equality(self):
        coverage = Coverage(1, 1)
        other_coverage = Coverage(2, 1)
        self.assertFalse(
            coverage == other_coverage,
            msg='Not equal coverages are equal'
        )

    def test_lower_than_equal(self):
        coverage = Coverage(1, 1)
        other_coverage = Coverage(2, 2)
        self.assertFalse(
            coverage < other_coverage,
            msg='One coverage lower than equal coverage'
        )
        self.assertFalse(
            other_coverage < coverage,
            msg='One Coverage lower than equal coverage'
        )

    def test_lower_than_lower_and_greater(self):
        greater_coverage = Coverage(1, 1)
        lower_coverage = Coverage(2, 1)
        self.assertFalse(
            greater_coverage < lower_coverage,
            msg='Lower coverage not lower than greater coverage'
        )
        self.assertTrue(
            lower_coverage < greater_coverage,
            msg='Greater Coverage lower than lower coverage'
        )
