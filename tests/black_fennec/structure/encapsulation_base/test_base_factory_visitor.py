import unittest
from typing import Optional

from doubles.black_fennec.structure.double_boolean import BooleanMock
from doubles.black_fennec.structure.double_info import InfoInstanceMock, InfoMock
from doubles.black_fennec.structure.double_list import ListMock
from doubles.black_fennec.structure.double_map import MapMock
from doubles.black_fennec.structure.double_number import NumberMock
from doubles.black_fennec.structure.double_reference import ReferenceMock
from doubles.black_fennec.structure.double_root import RootMock
from doubles.black_fennec.structure.double_string import StringMock
from src.black_fennec.structure.encapsulation_base.base_factory_visitor import BaseFactoryVisitor
from src.black_fennec.structure.encapsulation_base.encapsulation_base import EncapsulationBase
from src.black_fennec.structure.encapsulation_base.list_encapsulation_base import ListEncapsulationBase
from src.black_fennec.structure.encapsulation_base.map_encapsulation_base import MapEncapsulationBase


class BaseFactoryVisitorTestSuite(unittest.TestCase):
    def setUp(self):
        self.visitor: Optional[BaseFactoryVisitor] = BaseFactoryVisitor(EncapsulationBase)

    def tearDown(self) -> None:
        self.visitor: Optional[BaseFactoryVisitor] = None

    def test_can_construct(self):
        pass

    def test_can_visit_info(self):
        info = InfoMock()
        info_filter = self.visitor.visit_info(info)
        self.assertIsInstance(info_filter, EncapsulationBase)
        
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
        
    def test_can_visit_root(self):
        root = RootMock()
        root_filter = self.visitor.visit_root(root)
        self.assertIsInstance(root_filter, EncapsulationBase)
        
    def test_can_visit_reference(self):
        reference = ReferenceMock()
        reference_filter = self.visitor.visit_reference(reference)
        self.assertIsInstance(reference_filter, EncapsulationBase)

    def test_can_visit_list(self):
        info_list = ListMock()
        list_filter = self.visitor.visit_list(info_list)
        self.assertIsInstance(list_filter, ListEncapsulationBase)

    def test_can_visit_map(self):
        info_map = MapMock()
        map_filter = self.visitor.visit_map(info_map)
        self.assertIsInstance(map_filter, MapEncapsulationBase)

    def test_visit_caches_class(self):
        info = InfoInstanceMock()
        info_encapsulation_type = type(self.visitor.visit_info(info))
        self.assertIsInstance(self.visitor.visit_info(info), info_encapsulation_type)
