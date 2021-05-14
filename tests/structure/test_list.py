import unittest
import logging
from doubles.structure.double_info import InfoMock
from doubles.structure.double_root import RootMock
from doubles.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from src.structure.list import List

class ListTestSuite(unittest.TestCase):
    def test_can_construct(self):
        l = List()
        self.assertEqual(l, [])

    def test_can_construct_from_list(self):
        l = List([InfoMock()])
        self.assertEqual(len(l), 1)
        self.assertEqual(l[0].parent, l)

    def test_can_get_children(self):
        data = [InfoMock(), InfoMock()]
        info = List(data)
        children = info.children
        self.assertListEqual(children, data)

    def test_can_append_item(self):
        l = List()
        value = InfoMock()
        l.append(value)
        self.assertIn(value, l)

    def test_append_does_set_parent(self):
        l = List()
        value = InfoMock()
        l.append(value)
        self.assertEqual(value.parent, l)

    def test_append_throws_on_parent_not_none(self):
        l = List()
        value = RootMock()

        with self.assertRaises(ValueError):
            l.append(value)

    def test_append_logs_on_parent_not_none(self):
        l = List()
        value = RootMock()

        with self.assertLogs(None, logging.ERROR):
            try:
                l.append(value)
            except ValueError:
                pass

    def test_can_set_item(self):
        l = List()
        l.append(InfoMock())
        value = InfoMock()
        l[0] = value
        self.assertIn(value, l)

    def test_set_does_set_parent(self):
        l = List()
        l.append(InfoMock())
        value = InfoMock()
        l[0] = value
        self.assertEqual(value.parent, l)

    def test_set_does_unset_parent(self):
        l = List()
        value = InfoMock()
        l.append(value)
        l[0] = InfoMock()
        self.assertEqual(value.parent, None)

    def test_set_throws_on_parent_not_none(self):
        l = List()
        l.append(InfoMock())
        value = RootMock()
        with self.assertRaises(ValueError):
            l[0] = value

    def test_set_logs_on_parent_not_none(self):
        l = List()
        l.append(InfoMock())
        value = RootMock()
        with self.assertLogs(None, logging.ERROR):
            try:
                l[0] = value
            except ValueError:
                pass

    def test_can_remove_item(self):
        l = List()
        value = InfoMock()
        l.append(value)
        l.remove(value)
        self.assertNotIn(value, l)

    def test_remove_does_unset_parent(self):
        l = List()
        value = InfoMock()
        l.append(value)
        l.remove(value)
        self.assertEqual(value.parent, None)

    def test_remove_throws_on_delete_of_not_existing_item(self):
        l = List()
        not_value = InfoMock()

        with self.assertRaises(KeyError):
            l.remove(not_value)

    def test_remove_logs_on_delete_of_not_existing_item(self):
        l = List()
        not_value = InfoMock()

        with self.assertLogs(None, logging.ERROR):
            try:
                l.remove(not_value)
            except KeyError:
                pass

    def test_can_delete_item(self):
        l = List()
        value = InfoMock()
        l.append(value)
        del l[0]
        self.assertNotIn(value, l)

    def test_delete_does_unset_parent(self):
        l = List()
        value = InfoMock()
        l.append(value)
        del l[0]
        self.assertEqual(value.parent, None)

    def test_delete_throws_on_delete_of_not_existing_item(self):
        l = List()
        with self.assertRaises(KeyError):
            del l[0]

    def test_delete_logs_on_delete_of_not_existing_item(self):
        l = List()

        with self.assertLogs(None, logging.ERROR):
            try:
                del l[0]
            except KeyError:
                pass

    def test_can_get_value(self):
        value = InfoMock('value')
        info_list = List([value])
        self.assertIn(value, info_list.value)

    def test_can_set_value(self):
        value = InfoMock('value')
        info_list = List()
        info_list.value = [value]
        self.assertIn(value, info_list.value)

    def test_accept(self):
        visitor = FactoryBaseVisitorMock()
        info_list = List()
        info_list.accept(visitor)
        self.assertEqual(visitor.list, info_list)
        self.assertEqual(visitor.visit_list_count, 1)
