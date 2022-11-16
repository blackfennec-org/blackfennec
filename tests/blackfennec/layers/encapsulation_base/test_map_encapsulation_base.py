import unittest
from typing import Optional

from blackfennec_doubles.structure.double_structure import StructureMock
from blackfennec_doubles.structure.double_string import StringMock
from blackfennec_doubles.layers.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from blackfennec.layers.encapsulation_base.encapsulation_base import EncapsulationBase
from blackfennec.layers.encapsulation_base.map_encapsulation_base import MapEncapsulationBase
from blackfennec.layers.encapsulation_base.base_factory_visitor import _create_generic_class
from blackfennec.structure.structure import Structure
from blackfennec.structure.map import Map


class MapEncapsulationBaseTestSuite(unittest.TestCase):
    def setUp(self):
        self.visitor = FactoryBaseVisitorMock()
        self.subject = Map()
        self.map_encapsulation_base: Optional[MapEncapsulationBase] = MapEncapsulationBase(self.visitor, self.subject)

    def tearDown(self) -> None:
        self.visitor = None
        self.subject = None
        self.map_encapsulation_base: Optional[MapEncapsulationBase] = None

    def test_can_create(self):
        pass

    def test_subject_getter(self):
        self.assertEqual(self.map_encapsulation_base.subject, self.subject)

    def test_get_item(self):
        key = 'test'
        value = StringMock('test_value')
        self.subject.add_item(key, value)
        map_encapsulation = MapEncapsulationBase(self.visitor, self.subject)
        get = map_encapsulation.value[key]
        self.assertEqual(get, value)
        self.assertEqual(self.visitor.string, value)

    def test_set_item(self):
        key = 'test'
        value = StringMock('test_value')
        self.map_encapsulation_base.add_item(key, value)
        self.assertEqual(value, self.map_encapsulation_base.value[key])

    def test_set_item_already_encapsulated(self):
        key = 'test'
        value = StringMock('test_value')
        type_class = _create_generic_class(EncapsulationBase)
        encapsulated = type_class(self.visitor, value)
        self.map_encapsulation_base.add_item(key, encapsulated)
        self.assertEqual(value, self.map_encapsulation_base.value[key])

    def test_get_value(self):
        key = 'test'
        subject_content = StringMock('test')
        subject = Map({key: subject_content})
        map_encapsulation_base = MapEncapsulationBase(
            self.visitor,
            subject
        )
        value = map_encapsulation_base.value
        self.assertEqual(subject_content, value[key])

    def test_can_get_value_empty(self):
        value = self.map_encapsulation_base.value
        self.assertIsInstance(value, dict)

    def test_set_value(self):
        key = 'test'
        value = StringMock('test')
        self.map_encapsulation_base.value = {key: value}
        self.assertEqual(value, self.map_encapsulation_base.value[key])

    def test_can_remove_item(self):
        key = 'test'
        value = StringMock('test')
        self.subject.add_item(key, value)
        self.map_encapsulation_base.remove_item(key)
        self.assertEqual(len(self.map_encapsulation_base.value), 0)

    def test_can_get_repr(self):
        representation: str = self.map_encapsulation_base.__repr__()
        self.assertTrue(representation.startswith('MapEncapsulationBase('))
