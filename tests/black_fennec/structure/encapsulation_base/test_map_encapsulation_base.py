import unittest
from typing import Optional

from doubles.black_fennec.structure.double_structure import StructureMock
from doubles.black_fennec.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from src.black_fennec.structure.encapsulation_base.encapsulation_base import EncapsulationBase
from src.black_fennec.structure.encapsulation_base.map_encapsulation_base import MapEncapsulationBase
from src.black_fennec.structure.encapsulation_base.base_factory_visitor import _create_generic_class
from src.black_fennec.structure.structure import Structure
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.root import Root


class MapEncapsulationBaseTestSuite(unittest.TestCase):
    def setUp(self):
        self.visitor = FactoryBaseVisitorMock()
        self.subject = Map()
        self.subject.parent = Root(self.subject)
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
        value = StructureMock('test_value')
        self.subject[key] = value
        map_encapsulation: Optional[MapEncapsulationBase] = MapEncapsulationBase(self.visitor, self.subject)
        get = map_encapsulation[key]
        self.assertEqual(get, value)
        self.assertEqual(self.visitor.structure, value)
        self.assertEqual(self.visitor.visit_structure_count, 1)

    def test_set_item(self):
        key = 'test'
        value = StructureMock('test_value')
        self.map_encapsulation_base[key] = value
        self.assertEqual(value, self.map_encapsulation_base[key])

    def test_set_item_already_encapsulated(self):
        key = 'test'
        value = StructureMock('test_value')
        template_class = _create_generic_class(EncapsulationBase, Structure)
        encapsulated = template_class(self.visitor, value)
        self.map_encapsulation_base[key] = encapsulated
        self.assertEqual(value, self.map_encapsulation_base[key])

    def test_get_value(self):
        key = 'test'
        subject_content = StructureMock('test')
        subject = Map({key: subject_content})
        subject.parent = Root(subject)
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
        value = StructureMock('test')
        self.map_encapsulation_base.value = {key: value}
        self.assertEqual(value, self.map_encapsulation_base[key])

    def test_can_get_repr(self):
        representation: str = self.map_encapsulation_base.__repr__()
        self.assertTrue(representation.startswith('MapEncapsulationBase('))
