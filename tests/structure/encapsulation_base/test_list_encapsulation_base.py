import unittest
from typing import Optional

from doubles.structure.double_info import InfoMock
from doubles.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from doubles.structure.template.double_template_factory import TemplateFactoryMock
from src.structure.encapsulation_base.encapsulation_base import EncapsulationBase
from src.structure.encapsulation_base.base_factory_visitor import _create_generic_class
from src.structure.info import Info
from src.structure.list import List
from src.structure.root import Root
from src.structure.template.list_template import ListEncapsulationBase


class ListEncapsulationBaseTestSuite(unittest.TestCase):
    def setUp(self):
        self.visitor = FactoryBaseVisitorMock()
        self.subject = List()
        self.subject.parent = Root(self.subject)
        self.list_encapsulation_base: Optional[ListEncapsulationBase] = ListEncapsulationBase(self.visitor, self.subject)

    def tearDown(self) -> None:
        self.visitor = None
        self.subject = None
        self.list_encapsulation_base: Optional[ListEncapsulationBase] = None

    def test_can_create(self):
        pass

    def test_subject_getter(self):
        self.assertEqual(self.list_encapsulation_base.subject, self.subject)

    def test_get_item(self):
        value = InfoMock('test_value')
        subject = List([value])
        list_template: Optional[ListEncapsulationBase] = ListEncapsulationBase(
            self.visitor,
            subject
        )
        get = list_template[0]
        self. assertEqual(get, value)
        self.assertEqual(self.visitor.info, value)
        self.assertEqual(self.visitor.visit_info_count, 1)

    def test_set_item(self):
        value = InfoMock('test_value')
        subject = List([value])
        list_template: Optional[ListEncapsulationBase] = ListEncapsulationBase(
            self.visitor,
            subject
        )
        new_value = InfoMock('new_value')
        list_template[0] = new_value
        self.assertNotIn(value, list_template.subject)
        self.assertIn(new_value, list_template.subject)

    def test_append_item(self):
        value = InfoMock('test_value')
        self.list_encapsulation_base.append(value)
        self.assertIn(value, self.list_encapsulation_base.subject.children)

    def test_append_item_already_encapsulated(self):
        value = InfoMock('test_value')
        template_class = _create_generic_class(EncapsulationBase, Info)
        encapsulated = template_class(self.visitor, value)
        self.list_encapsulation_base.append(encapsulated)
        self.assertIn(value, self.list_encapsulation_base.subject.children)

    def test_get_children(self):
        value = InfoMock('test_value')
        subject = List([value])
        list_template: Optional[ListEncapsulationBase] = ListEncapsulationBase(
            self.visitor,
            subject
        )
        children = list_template.children
        self.assertEqual(len(children), 1)
        self.assertEqual(self.visitor.info, value)
        self.assertEqual(self.visitor.visit_info_count, 1)

    def test_get_empty_children(self):
        children = self.list_encapsulation_base.children
        self.assertEqual(len(children), 0)
        self.assertEqual(self.visitor.visit_info_count, 0)

    def test_remove_item(self):
        value = InfoMock('test_value')
        subject = List([value])
        list_template: Optional[ListEncapsulationBase] = ListEncapsulationBase(
            self.visitor,
            subject
        )
        list_template.remove(value)
        self.assertEqual(len(self.subject), 0)

    def test_remove_encapsulated_item(self):
        value = InfoMock('test_value')
        subject = List([value])
        list_template: Optional[ListEncapsulationBase] = ListEncapsulationBase(
            self.visitor,
            subject
        )
        template_class = _create_generic_class(EncapsulationBase, Info)
        encapsulated = template_class(self.visitor, value)
        list_template.remove(encapsulated)
        self.assertEqual(len(self.subject), 0)

    def test_remove_item_not_in_list(self):
        value = InfoMock('test_value')
        subject = List([value])
        with self.assertRaises(KeyError):
            self.list_encapsulation_base.remove(value)

    def test_can_get_repr(self):
        representation: str = self.list_encapsulation_base.__repr__()
        self.assertTrue(representation.startswith('ListEncapsulationBase('))
