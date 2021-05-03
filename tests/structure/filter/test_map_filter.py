import unittest
from typing import Optional

from doubles.structure.double_info import InfoMock
from doubles.structure.filter.double_filter_factory import FilterFactoryMock
from src.structure.info import Info
from src.structure.map import Map
from src.structure.root import Root
from src.structure.filter.map_filter import MapFilter
from src.structure.filter.filter_factory import _get_filter_class


class MapFilterTestSuite(unittest.TestCase):
    def setUp(self):
        self.property_storage = dict()
        self.factory = FilterFactoryMock()
        self.subject = Map()
        self.subject.parent = Root(self.subject)
        self.map_filter: Optional[MapFilter] = MapFilter(self.subject, self.factory, self.property_storage)

    def tearDown(self) -> None:
        self.property_storage = None
        self.factory = None
        self.subject = None
        self.map_filter: Optional[MapFilter] = None

    def test_can_create(self):
        pass

    def test_subject_getter(self):
        self.assertEqual(self.map_filter.subject, self.subject)

    def test_get_item(self):
        key = 'test'
        value = InfoMock('test_value')
        self.subject[key] = value
        self.factory._create_return = value
        map_filter: Optional[MapFilter] = MapFilter(self.subject, self.factory, self.property_storage)
        get = map_filter[key]
        self.assertEqual(get, value)
        self.assertEqual(self.factory._subject, value)
        self.assertEqual(self.factory._create_calls, 1)

    def test_set_item(self):
        key = 'test'
        value = InfoMock('test_value')
        self.factory._create_return = value
        self.map_filter[key] = value
        self.assertEqual(value, self.map_filter[key])

    def test_set_item_already_encapsulated(self):
        key = 'test'
        value = InfoMock('test_value')
        filter_class = _get_filter_class(Info)
        encapsulated = filter_class(value, self.factory, None)
        self.factory._create_return = encapsulated
        self.factory._create_return = value
        self.map_filter[key] = encapsulated
        self.assertEqual(value, self.map_filter[key])

    def test_get_children(self):
        key = 'test'
        value = InfoMock('test_value')
        self.subject[key] = value
        self.factory._create_return = value
        map_filter: Optional[MapFilter] = MapFilter(self.subject, self.factory, self.property_storage)
        children = map_filter.children
        self.assertEqual(len(children), 1)
        self.assertEqual(self.factory._subject, value)
        self.assertEqual(self.factory._create_calls, 1)

    def test_get_empty_children(self):
        children = self.map_filter.children
        self.assertEqual(len(children), 0)
        self.assertEqual(self.factory._create_calls, 0)

    def test_can_get_repr(self):
        representation: str = self.map_filter.__repr__()
        self.assertTrue(representation.startswith('MapFilter('))
