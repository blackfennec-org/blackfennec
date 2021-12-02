# -*- coding: utf-8 -*-
import unittest

from doubles.black_fennec.structure.double_root import RootMock
from doubles.black_fennec.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from src.black_fennec.structure.boolean import Boolean


class BooleanTestSuite(unittest.TestCase):
    def test_can_construct(self):
        boolean = Boolean(True)
        self.assertIsNotNone(boolean)

    def test_can_default_construct(self):
        boolean = Boolean()
        self.assertIsNotNone(boolean)

    def test_can_get_value(self):
        boolean = Boolean(True)
        self.assertEqual(boolean.value, True)

    def test_can_set_value(self):
        boolean = Boolean()
        boolean.value = True
        self.assertEqual(boolean.value, True)

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

    def test_representation(self):
        actual = Boolean(True)
        expected = 'Boolean(%s)' % actual.value
        self.assertEqual(actual.__repr__(), expected)

    def test_accept(self):
        visitor = FactoryBaseVisitorMock()
        boolean = Boolean()
        boolean.accept(visitor)
        self.assertEqual(visitor.boolean, boolean)
        self.assertEqual(visitor.visit_boolean_count, 1)
