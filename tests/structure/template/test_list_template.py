import unittest
from typing import Optional

from doubles.double_dummy import Dummy
from doubles.structure.double_info import InfoMock
from doubles.structure.double_list import ListMock, ListInstanceMock
from doubles.structure.template.double_template_factory import TemplateFactoryMock
from src.structure.info import Info
from src.structure.list import List
from src.structure.root import Root
from src.structure.template.list_template import ListTemplate
from src.structure.template.template_factory import _get_template_class


class ListTemplateTestSuite(unittest.TestCase):
    def setUp(self):
        self.property_storage = dict()
        self.factory = TemplateFactoryMock()
        self.subject = List()
        self.subject.parent = Root(self.subject)
        self.list_template: Optional[ListTemplate] = ListTemplate(self.subject, self.factory, self.property_storage)

    def tearDown(self) -> None:
        self.property_storage = None
        self.factory = None
        self.subject = None
        self.list_template: Optional[ListTemplate] = None

    def test_can_create(self):
        pass

    def test_subject_getter(self):
        self.assertEqual(self.list_template.subject, self.subject)

    def test_get_item(self):
        value = InfoMock('test_value')
        subject = List([value])
        self.factory._create_return = value
        list_template: Optional[ListTemplate] = ListTemplate(
            subject,
            self.factory,
            self.property_storage
        )
        get = list_template[0]
        self.assertEqual(self.factory._subject, value)
        self.assertEqual(self.factory._create_calls, 1)

    def test_set_item(self):
        value = InfoMock('test_value')
        subject = List([value])
        self.factory._create_return = value
        list_template: Optional[ListTemplate] = ListTemplate(
            subject,
            self.factory,
            self.property_storage
        )
        new_value = InfoMock('new_value')
        list_template[0] = new_value
        self.assertNotIn(value, list_template.subject)
        self.assertIn(new_value, list_template.subject)


    def test_append_item(self):
        value = InfoMock('test_value')
        self.factory._create_return = value
        self.list_template.append(value)
        self.assertIn(value, self.list_template.children)

    def test_append_item_already_encapsulated(self):
        value = InfoMock('test_value')
        template_class = _get_template_class(Info)
        encapsulated = template_class(value, self.factory, None)
        self.factory._create_return = encapsulated
        self.list_template.append(encapsulated)
        self.assertIn(value, self.list_template.subject.children)

    def test_get_children(self):
        value = InfoMock('test_value')
        subject = List([value])
        self.factory._create_return = value
        list_template: Optional[ListTemplate] = ListTemplate(
            subject,
            self.factory,
            self.property_storage
        )
        children = list_template.children
        self.assertEqual(len(children), 1)
        self.assertEqual(self.factory._subject, value)
        self.assertEqual(self.factory._create_calls, 1)

    def test_get_empty_children(self):
        children = self.list_template.children
        self.assertEqual(len(children), 0)
        self.assertEqual(self.factory._create_calls, 0)

    def test_remove_item(self):
        value = InfoMock('test_value')
        subject = List([value])
        self.factory._create_return = value
        list_template: Optional[ListTemplate] = ListTemplate(
            subject,
            self.factory,
            self.property_storage
        )
        list_template.remove(value)
        self.assertEqual(len(self.subject), 0)

    def test_remove_encapsulated_item(self):
        value = InfoMock('test_value')
        subject = List([value])
        self.factory._create_return = value
        list_template: Optional[ListTemplate] = ListTemplate(
            subject,
            self.factory,
            self.property_storage
        )
        template_class = _get_template_class(Info)
        encapsulated = template_class(value, self.factory, None)
        list_template.remove(encapsulated)
        self.assertEqual(len(self.subject), 0)

    def test_remove_item(self):
        value = InfoMock('test_value')
        subject = List([value])
        self.factory._create_return = value
        with self.assertRaises(KeyError):
            self.list_template.remove(value)

    def test_can_get_repr(self):
        representation: str = self.list_template.__repr__()
        self.assertTrue(representation.startswith('ListTemplate('))
