import unittest

from blackfennec_doubles.structure.double_structure import StructureMock
from blackfennec_doubles.structure.double_string import StringMock
from blackfennec.structure.encapsulation_base.base_factory_visitor import _create_generic_class
from blackfennec.structure.filter.filter_base import FilterBase
from blackfennec.structure.filter.filter_factory_visitor import FilterFactoryVisitor
from blackfennec.structure.map import Map
from blackfennec.structure.filter.map_filter import MapFilter
from blackfennec.structure.structure import Structure


class MapFilterTestSuite(unittest.TestCase):
    def setUp(self):
        self.visitor = FilterFactoryVisitor()
        self.subject = Map()
        self.map_filter = MapFilter(self.visitor, self.subject)

    def tearDown(self) -> None:
        self.visitor = None
        self.subject = None
        self.map_filter = None

    def test_can_construct(self):
        self.assertIsNotNone(self.map_filter)

    def test_set_item_already_encapsulated(self):
        key = 'test'
        value = StringMock('test_value')
        type_class = _create_generic_class(FilterBase)
        encapsulated = type_class(self.visitor, value)
        self.map_filter.add_item(key, encapsulated)
        self.assertEqual(value, self.map_filter.value[key].subject)

    def test_set_item_map_already_encapsulated(self):
        key = 'test'
        value = Map()
        encapsulated = MapFilter(self.visitor, value)
        self.map_filter.add_item(key, encapsulated)
        self.assertEqual(value, self.map_filter.value[key].subject)

    def test_can_get_repr(self):
        representation: str = self.map_filter.__repr__()
        self.assertTrue(representation.startswith('MapFilter('))
