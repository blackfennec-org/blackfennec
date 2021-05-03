# -*- coding: utf-8 -*-
import unittest
from typing import Optional

from doubles.structure.double_info import InfoInstanceMock, InfoMock
from doubles.structure.double_list import ListInstanceMock
from doubles.structure.double_map import MapInstanceMock
from src.structure.filter.list_filter import ListFilter
from src.structure.filter.map_filter import MapFilter
from src.structure.filter.filter_base import FilterBase
from src.structure.filter.filter_factory import FilterFactory


class FilterFactoryTestSuite(unittest.TestCase):
    def setUp(self):
        self.factory: Optional[FilterFactory] = FilterFactory()

    def tearDown(self) -> None:
        self.factory: Optional[FilterFactory] = None

    def test_can_construct(self):
        pass

    def test_can_create(self):
        info = InfoInstanceMock()
        info_filter = self.factory.create(info)
        self.assertIsInstance(info_filter, FilterBase)

    def test_can_create_list(self):
        info_list = ListInstanceMock()
        list_filter = self.factory.create(info_list)
        self.assertIsInstance(list_filter, ListFilter)

    def test_can_create_map(self):
        info_map = MapInstanceMock()
        map_filter = self.factory.create(info_map)
        self.assertIsInstance(map_filter, MapFilter)

    def test_create_caches_class(self):
        info = InfoInstanceMock()
        info_filter_type = type(self.factory.create(info))
        self.assertIsInstance(self.factory.create(info), info_filter_type)

    def test_create_with_wrong_class(self):
        info = InfoMock()
        with self.assertRaises(TypeError):
            self.factory.create(info)

    def test_generic_filter_subject(self):
        info = InfoInstanceMock()
        info_filter = self.factory.create(info).subject
        # checking a property type is not possible thus,
        # only the existence is checked:
        # https://stackoverflow.com/questions/52201094/check-underlying-type-of-a-property-in-python
        self.assertIsNotNone(info_filter)
