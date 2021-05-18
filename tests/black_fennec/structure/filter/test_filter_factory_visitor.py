# -*- coding: utf-8 -*-
import unittest
from typing import Optional

from doubles.black_fennec.structure.double_info import InfoInstanceMock
from doubles.black_fennec.structure.double_list import ListInstanceMock
from doubles.black_fennec.structure.double_map import MapInstanceMock
from src.black_fennec.structure.filter.filter_factory_visitor import FilterFactoryVisitor
from src.black_fennec.structure.filter.list_filter import ListFilter
from src.black_fennec.structure.filter.map_filter import MapFilter
from src.black_fennec.structure.filter.filter_base import FilterBase


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

    def test_can_visit_info(self):
        info = InfoInstanceMock()
        info_filter = self.visitor.visit_info(info)
        self.assertIsInstance(info_filter, FilterBase)

    def test_can_visit_list(self):
        info_list = ListInstanceMock()
        list_filter = self.visitor.visit_list(info_list)
        self.assertIsInstance(list_filter, ListFilter)

    def test_can_visit_map(self):
        info_map = MapInstanceMock()
        map_filter = self.visitor.visit_map(info_map)
        self.assertIsInstance(map_filter, MapFilter)

    def test_visit_caches_class(self):
        info = InfoInstanceMock()
        info_filter_type = type(self.visitor.visit_info(info))
        self.assertIsInstance(self.visitor.visit_info(info), info_filter_type)

    def test_generic_filter_subject(self):
        info = InfoInstanceMock()
        info_filter = self.visitor.visit_info(info).subject
        # checking a property type is not possible thus,
        # only the existence is checked:
        # https://stackoverflow.com/questions/52201094/check-underlying-type-of-a-property-in-python
        self.assertIsNotNone(info_filter)