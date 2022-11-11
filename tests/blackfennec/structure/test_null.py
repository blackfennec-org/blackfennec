# -*- coding: utf-8 -*-
import unittest
from tests.blackfennec.structure.test_structure import StructureTestMixin
from blackfennec_doubles.structure.double_root import RootMock
from blackfennec_doubles.layers.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from blackfennec.structure.null import Null


class NullTestSuite(StructureTestMixin, unittest.TestCase):
    def setUp(self):
        self.structure_type_name = 'Null'
        self.default_value = None
        self.alternative_value = None

    def create_instance(self, value=None):
        return Null()

    def test_can_construct(self):
        null = self.create_instance()
        self.assertIsNotNone(null)

    def test_can_default_construct(self):
        null = Null()
        self.assertIsNotNone(null)
