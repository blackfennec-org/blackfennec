import unittest
from ddt import ddt, data

from tests.test_utils.parameterize import MOCK_CORE_STRUCTURES
from tests.test_utils.what_the_farmer_does_not_eat_visitor_factory import WhatTheFarmerDoesNotEatVisitorFactory
from blackfennec_doubles.structure.double_boolean import BooleanMock
from blackfennec_doubles.structure.double_structure import StructureInstanceMock, StructureMock
from blackfennec_doubles.structure.double_list import ListMock
from blackfennec_doubles.structure.double_map import MapMock
from blackfennec_doubles.structure.double_number import NumberMock
from blackfennec_doubles.structure.double_reference import ReferenceMock
from blackfennec_doubles.structure.double_string import StringMock
from blackfennec.layers.encapsulation_base.base_factory_visitor import BaseFactoryVisitor
from blackfennec.layers.encapsulation_base.encapsulation_base import EncapsulationBase
from blackfennec.layers.encapsulation_base.list_encapsulation_base import ListEncapsulationBase
from blackfennec.layers.encapsulation_base.map_encapsulation_base import MapEncapsulationBase


@ddt
class BaseFactoryVisitorTestSuite(unittest.TestCase):
    def setUp(self):
        self.visitor = BaseFactoryVisitor(None, EncapsulationBase)

    def test_can_construct(self):
        pass

    def test_can_visit_structure(self):
        structure = StructureMock()
        structure_filter = self.visitor.visit_structure(structure)
        self.assertIsInstance(structure_filter, EncapsulationBase)

    def test_can_visit_string(self):
        string = StringMock()
        string_filter = self.visitor.visit_string(string)
        self.assertIsInstance(string_filter, EncapsulationBase)

    def test_can_visit_number(self):
        number = NumberMock()
        number_filter = self.visitor.visit_number(number)
        self.assertIsInstance(number_filter, EncapsulationBase)

    def test_can_visit_boolean(self):
        boolean = BooleanMock()
        boolean_filter = self.visitor.visit_boolean(boolean)
        self.assertIsInstance(boolean_filter, EncapsulationBase)

    def test_can_visit_reference(self):
        reference = ReferenceMock()
        reference_filter = self.visitor.visit_reference(reference)
        self.assertIsInstance(reference_filter, EncapsulationBase)

    def test_can_visit_list(self):
        structure_list = ListMock()
        list_filter = self.visitor.visit_list(structure_list)
        self.assertIsInstance(list_filter, ListEncapsulationBase)

    def test_can_visit_map(self):
        structure_map = MapMock()
        map_filter = self.visitor.visit_map(structure_map)
        self.assertIsInstance(map_filter, MapEncapsulationBase)

    def test_visit_caches_class(self):
        structure = StructureInstanceMock()
        structure_encapsulation_type = type(self.visitor.visit_structure(structure))
        self.assertIsInstance(self.visitor.visit_structure(structure), structure_encapsulation_type)

    @data(*MOCK_CORE_STRUCTURES)
    def test_double_encapsulation(self, core_object):
        string = StringMock()
        encapsulated = core_object.accept(self.visitor)
        double_encapsulation = encapsulated.accept(self.visitor)
        self.assertIsInstance(double_encapsulation, EncapsulationBase)

    @data(*MOCK_CORE_STRUCTURES)
    def test_encapsulated_can_visit(self, core_object):
        mock_visitor = core_object.accept(WhatTheFarmerDoesNotEatVisitorFactory())
        encapsulated = core_object.accept(self.visitor)
        self.assertTrue(encapsulated.accept(mock_visitor))
