import unittest
from typing import Optional

from doubles.black_fennec.structure.double_structure import StructureMock
from doubles.black_fennec.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from src.black_fennec.structure.encapsulation_base.encapsulation_base import EncapsulationBase
from src.black_fennec.structure.encapsulation_base.base_factory_visitor import _create_generic_class
from src.black_fennec.structure.structure import Structure
from src.black_fennec.structure.list import List
from src.black_fennec.structure.encapsulation_base.list_encapsulation_base import ListEncapsulationBase


class ListEncapsulationBaseTestSuite(unittest.TestCase):
    def setUp(self):
        self.visitor = FactoryBaseVisitorMock()
        self.subject = List()
        self.list_encapsulation_base: Optional[ListEncapsulationBase] = ListEncapsulationBase(self.visitor,
                                                                                              self.subject)

    def tearDown(self) -> None:
        self.visitor = None
        self.subject = None
        self.list_encapsulation_base: Optional[ListEncapsulationBase] = None

    def test_can_create(self):
        pass

    def test_subject_getter(self):
        self.assertEqual(self.list_encapsulation_base.subject, self.subject)

    def test_add_item_item(self):
        value = StructureMock('test_value')
        self.list_encapsulation_base.add_item(value)
        self.assertIn(value, self.list_encapsulation_base.subject.value)

    def test_add_item_item_already_encapsulated(self):
        value = StructureMock('test_value')
        template_class = _create_generic_class(EncapsulationBase)
        encapsulated = template_class(self.visitor, value)
        self.list_encapsulation_base.add_item(encapsulated)
        self.assertIn(value, self.list_encapsulation_base.subject.value)

    def test_get_value(self):
        subject_content = StructureMock('test')
        subject = List([subject_content])
        list_encapsulation_base = ListEncapsulationBase(
            self.visitor,
            subject
        )
        value = list_encapsulation_base.value
        self.assertEqual(subject_content, value[0])

    def test_can_get_value_empty(self):
        value = self.list_encapsulation_base.value
        self.assertIsInstance(value, list)

    def test_set_value(self):
        value = StructureMock('test')
        self.list_encapsulation_base.value = [value]
        self.assertIn(value, self.list_encapsulation_base.subject.value)

    def test_remove_item(self):
        value = StructureMock('test_value')
        subject = List([value])
        list_template: Optional[ListEncapsulationBase] = ListEncapsulationBase(
            self.visitor,
            subject
        )
        list_template.remove_item(value)
        self.assertEqual(len(self.subject.value), 0)

    def test_remove_encapsulated_item(self):
        value = StructureMock('test_value')
        subject = List([value])
        list_template: Optional[ListEncapsulationBase] = ListEncapsulationBase(
            self.visitor,
            subject
        )
        template_class = _create_generic_class(EncapsulationBase)
        encapsulated = template_class(self.visitor, value)
        list_template.remove_item(encapsulated)
        self.assertEqual(len(self.subject.value), 0)

    def test_remove_item_not_in_list(self):
        value = StructureMock('test_value')
        with self.assertRaises(KeyError):
            self.list_encapsulation_base.remove_item(value)

    def test_can_get_repr(self):
        representation: str = self.list_encapsulation_base.__repr__()
        self.assertTrue(representation.startswith('ListEncapsulationBase('))
