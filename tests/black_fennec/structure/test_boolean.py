# -*- coding: utf-8 -*-
import unittest
from tests.black_fennec.structure.test_structure import StructureTestMixin
from doubles.black_fennec.structure.double_root import RootMock
from doubles.black_fennec.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from src.black_fennec.structure.boolean import Boolean


class BooleanTestSuite(StructureTestMixin, unittest.TestCase):
    def setUp(self):
        self.structure_type_name = 'Boolean'
        self.default_value = False
        self.alternative_value = True

    def create_instance(self, value):
        return Boolean(value)

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
