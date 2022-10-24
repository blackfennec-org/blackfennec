# -*- coding: utf-8 -*-
import unittest

from blackfennec_doubles.util.double_comparable import ComparableMock


class ComparableTestSuite(unittest.TestCase):
    def test_not_equal_equal_elements(self):
        comp = ComparableMock(1)
        equal_comp = ComparableMock(1)
        self.assertFalse(
            comp != equal_comp,
            msg = 'Equal elements are not equal'
        )

    def test_not_equal_unequal_elements(self):
        comp = ComparableMock(1)
        other_comp = ComparableMock(2)
        self.assertTrue(
            comp != other_comp,
            msg='Unequal elements are equal'
        )

    def test_lower_equal_lower_element(self):
        comp = ComparableMock(1)
        greater_comp = ComparableMock(2)
        self.assertTrue(
            comp <= greater_comp,
            msg='Lower element greater than greater element'
        )

    def test_lower_equal_equal_elements(self):
        comp = ComparableMock(1)
        equal_comp = ComparableMock(1)
        self.assertTrue(
            comp <= equal_comp,
            msg='Equal element greater than equal element'
        )

    def test_lower_equal_greater_element(self):
        comp = ComparableMock(1)
        greater_comp= ComparableMock(2)
        self.assertFalse(
            greater_comp <= comp,
            msg='Greater element lower equal lower element'
        )

    def test_greater_than_lower_element(self):
        comp = ComparableMock(1)
        greater_comp = ComparableMock(2)
        self.assertTrue(
            greater_comp > comp,
            msg='Greater element lower than lower element'
        )

    def test_greater_than_equal_elements(self):
        comp = ComparableMock(1)
        equal_comp = ComparableMock(1)
        self.assertFalse(
            comp > equal_comp,
            msg='Equal element lower than equal element'
        )

    def test_greater_than_greater_element(self):
        comp = ComparableMock(1)
        greater_comp = ComparableMock(2)
        self.assertFalse(
            comp > greater_comp,
            msg='Lower element greater than greater element'
        )

    def test_greater_equal_lower_element(self):
        comp = ComparableMock(1)
        greater_comp = ComparableMock(2)
        self.assertFalse(
            comp >= greater_comp,
            msg='Greater element lower than lower element'
        )

    def test_greater_equal_equal_elements(self):
        comp = ComparableMock(1)
        equal_comp = ComparableMock(1)
        self.assertTrue(
            comp >= equal_comp,
            msg='Equal element lower than equal element'
        )

    def test_greater_equal_greater_element(self):
        comp = ComparableMock(1)
        greater_comp= ComparableMock(2)
        self.assertTrue(
            greater_comp >= comp,
            msg='Lower element greater than greater element'
        )
