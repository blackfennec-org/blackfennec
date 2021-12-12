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

    def create_structure(self, value):
        return Boolean(value)

    def test_can_construct(self):
        boolean = Boolean(True)
        self.assertIsNotNone(boolean)

    def test_can_default_construct(self):
        boolean = Boolean()
        self.assertIsNotNone(boolean)

