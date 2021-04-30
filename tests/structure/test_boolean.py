# -*- coding: utf-8 -*-
import unittest

from doubles.structure.double_root import RootMock
from src.structure.boolean import Boolean


class BooleanTestSuite(unittest.TestCase):
    def test_can_construct(self):
        boolean = Boolean(True)
        self.assertEqual(boolean, True)

    def test_can_default_construct(self):
        boolean = Boolean()
        self.assertEqual(boolean, False)

    def test_can_get_value(self):
        boolean = Boolean(True)
        self.assertEqual(boolean.value, True)

    def test_can_set_value(self):
        boolean = Boolean()
        boolean.value = True
        self.assertEqual(boolean, True)

    def test_can_change_parent(self):
        new_parent = RootMock()
        boolean = Boolean()
        boolean.parent = new_parent
        self.assertEqual(boolean.parent, new_parent)

    def test_can_get_root(self):
        root = RootMock()
        boolean = Boolean()
        boolean.parent = root
        self.assertEqual(boolean.root, root)

    def test_is_boolish(self):
        true = Boolean(True)
        false = Boolean(False)
        self.assertEqual(true, not false)

    def test_can_convert_to_string(self):
        self.assertEqual(str(Boolean(3.141)), '3.141')

    def test_representation(self):
        actual = Boolean(True)
        expected = 'Boolean(%s)' % actual.value
        self.assertEqual(actual.__repr__(), expected)

    def test_equal_equal_elements(self):
        comp = Boolean(True)
        equal_comp = Boolean(True)
        self.assertTrue(
            comp == equal_comp,
            msg='Equal elements are not equal'
        )

    def test_equal_unequal_elements(self):
        comp = Boolean(True)
        other_comp = Boolean(False)
        self.assertFalse(
            comp == other_comp,
            msg='Unequal elements are equal'
        )

    def test_not_equal_equal_elements(self):
        comp = Boolean(True)
        equal_comp = Boolean(True)
        self.assertFalse(
            comp != equal_comp,
            msg='Equal elements are not equal'
        )

    def test_not_equal_unequal_elements(self):
        comp = Boolean(True)
        other_comp = Boolean(False)
        self.assertTrue(
            comp != other_comp,
            msg='Unequal elements are equal'
        )