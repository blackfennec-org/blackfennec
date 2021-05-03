import unittest
from typing import Optional

from doubles.structure.double_info import InfoMock
from doubles.structure.filter.double_filter_factory import FilterFactoryMock
from src.structure.info import Info
from src.structure.list import List
from src.structure.root import Root
from src.structure.filter.list_filter import ListFilter
from src.structure.filter.filter_factory import _get_filter_class


class ListFilterTestSuite(unittest.TestCase):
    def setUp(self):
        self.property_storage = dict()
        self.factory = FilterFactoryMock()
        self.subject = List()
        self.subject.parent = Root(self.subject)
        self.list_filter: Optional[ListFilter] = ListFilter(self.subject, self.factory, self.property_storage)

    def tearDown(self) -> None:
        self.property_storage = None
        self.factory = None
        self.subject = None
        self.list_filter: Optional[ListFilter] = None

    def test_can_create(self):
        pass

    def test_subject_getter(self):
        self.assertEqual(self.list_filter.subject, self.subject)

    def test_get_item(self):
        value = InfoMock('test_value')
        subject = List([value])
        self.factory._create_return = value
        list_filter: Optional[ListFilter] = ListFilter(
            subject,
            self.factory,
            self.property_storage
        )
        get = list_filter[0]
        self.assertEqual(self.factory._subject, value)
        self.assertEqual(self.factory._create_calls, 1)

    def test_set_item(self):
        value = InfoMock('test_value')
        subject = List([value])
        self.factory._create_return = value
        list_filter: Optional[ListFilter] = ListFilter(
            subject,
            self.factory,
            self.property_storage
        )
        new_value = InfoMock('new_value')
        list_filter[0] = new_value
        self.assertNotIn(value, list_filter.subject)
        self.assertIn(new_value, list_filter.subject)


    def test_append_item(self):
        value = InfoMock('test_value')
        self.factory._create_return = value
        self.list_filter.append(value)
        self.assertIn(value, self.list_filter.children)

    def test_append_item_already_encapsulated(self):
        value = InfoMock('test_value')
        filter_class = _get_filter_class(Info)
        encapsulated = filter_class(value, self.factory, None)
        self.factory._create_return = encapsulated
        self.list_filter.append(encapsulated)
        self.assertIn(value, self.list_filter.subject.children)

    def test_get_children(self):
        value = InfoMock('test_value')
        subject = List([value])
        self.factory._create_return = value
        list_filter: Optional[ListFilter] = ListFilter(
            subject,
            self.factory,
            self.property_storage
        )
        children = list_filter.children
        self.assertEqual(len(children), 1)
        self.assertEqual(self.factory._subject, value)
        self.assertEqual(self.factory._create_calls, 1)

    def test_get_empty_children(self):
        children = self.list_filter.children
        self.assertEqual(len(children), 0)
        self.assertEqual(self.factory._create_calls, 0)

    def test_remove_item(self):
        value = InfoMock('test_value')
        subject = List([value])
        self.factory._create_return = value
        list_filter: Optional[ListFilter] = ListFilter(
            subject,
            self.factory,
            self.property_storage
        )
        list_filter.remove(value)
        self.assertEqual(len(self.subject), 0)

    def test_remove_encapsulated_item(self):
        value = InfoMock('test_value')
        subject = List([value])
        self.factory._create_return = value
        list_filter: Optional[ListFilter] = ListFilter(
            subject,
            self.factory,
            self.property_storage
        )
        filter_class = _get_filter_class(Info)
        encapsulated = filter_class(value, self.factory, None)
        list_filter.remove(encapsulated)
        self.assertEqual(len(self.subject), 0)

    def test_remove_item_not_in_list(self):
        value = InfoMock('test_value')
        subject = List([value])
        self.factory._create_return = value
        with self.assertRaises(KeyError):
            self.list_filter.remove(value)

    def test_can_get_repr(self):
        representation: str = self.list_filter.__repr__()
        self.assertTrue(representation.startswith('ListFilter('))
