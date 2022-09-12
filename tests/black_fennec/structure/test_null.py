# -*- coding: utf-8 -*-
import unittest
from tests.black_fennec.structure.test_structure import StructureTestMixin
from doubles.black_fennec.structure.double_root import RootMock
from doubles.black_fennec.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from src.black_fennec.structure.null import Null


class NullTestSuite(StructureTestMixin, unittest.TestCase):
    def setUp(self):
        self.structure_type_name = 'Null'
        self.default_value = None
        self.alternative_value = None

    def create_structure(self, value=None):
        return Null()

    def test_can_construct(self):
        null = self.create_structure()
        self.assertIsNotNone(null)

    def test_can_default_construct(self):
        null = Null()
        self.assertIsNotNone(null)
