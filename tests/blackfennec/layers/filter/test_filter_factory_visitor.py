# -*- coding: utf-8 -*-
import unittest
from typing import Optional

from blackfennec_doubles.structure.double_structure import StructureInstanceMock
from blackfennec_doubles.structure.double_list import ListInstanceMock
from blackfennec_doubles.structure.double_map import MapInstanceMock
from blackfennec.layers.filter.filter_factory_visitor import FilterFactoryVisitor
from blackfennec.layers.filter.list_filter import ListFilter
from blackfennec.layers.filter.map_filter import MapFilter
from blackfennec.layers.filter.filter_base import FilterBase


class FilterFactoryVisitorTestSuite(unittest.TestCase):
    def setUp(self):
        self.visitor: Optional[FilterFactoryVisitor] = FilterFactoryVisitor()

    def tearDown(self) -> None:
        self.visitor: Optional[FilterFactoryVisitor] = None

    def test_can_construct(self):
        pass

    def test_can_get_metadata_storage(self):
        metadata = self.visitor.metadata_storage
        self.assertIsInstance(metadata, dict)

    def test_can_visit_structure(self):
        structure = StructureInstanceMock()
        structure_filter = self.visitor.visit_structure(structure)
        self.assertIsInstance(structure_filter, FilterBase)

    def test_can_visit_list(self):
        structure_list = ListInstanceMock()
        list_filter = self.visitor.visit_list(structure_list)
        self.assertIsInstance(list_filter, ListFilter)

    def test_can_visit_map(self):
        structure_map = MapInstanceMock()
        map_filter = self.visitor.visit_map(structure_map)
        self.assertIsInstance(map_filter, MapFilter)

    def test_visit_caches_class(self):
        structure = StructureInstanceMock()
        structure_filter_type = type(self.visitor.visit_structure(structure))
        self.assertIsInstance(self.visitor.visit_structure(structure), structure_filter_type)

    def test_generic_filter_subject(self):
        structure = StructureInstanceMock()
        structure_filter = self.visitor.visit_structure(structure).subject
        # checking a property type is not possible thus,
        # only the existence is checked:
        # https://stackoverflow.com/questions/52201094/check-underlying-type-of-a-property-in-python
        self.assertIsNotNone(structure_filter)