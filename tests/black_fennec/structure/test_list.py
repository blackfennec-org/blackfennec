import unittest
import logging
from doubles.black_fennec.structure.double_structure import StructureMock
from doubles.black_fennec.structure.double_root import RootMock
from doubles.black_fennec.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from src.black_fennec.structure.list import List


class ListTestSuite(unittest.TestCase):
    def test_can_construct(self):
        test_list = List()
        self.assertEqual(test_list.value, [])

    def test_can_construct_from_list(self):
        test_list = List([StructureMock()])
        self.assertEqual(len(test_list.value), 1)
        self.assertEqual(test_list.value[0].parent, test_list)

    def test_can_add_item_item(self):
        test_list = List()
        value = StructureMock()
        test_list.add_item(value)
        self.assertIn(value, test_list.value)

    def test_add_item_does_set_parent(self):
        test_list = List()
        value = StructureMock()
        test_list.add_item(value)
        self.assertEqual(value.parent, test_list)

    def test_add_item_throws_on_parent_not_none(self):
        test_list = List()
        value = RootMock()

        with self.assertRaises(AssertionError):
            test_list.add_item(value)

    def test_add_item_logs_on_parent_not_none(self):
        test_list = List()
        value = RootMock()

        with self.assertRaises(AssertionError):
            test_list.add_item(value)

    def test_can_remove_item_item(self):
        test_list = List()
        value = StructureMock()
        test_list.add_item(value)
        test_list.remove_item(value)
        self.assertNotIn(value, test_list.value)

    def test_remove_item_does_unset_parent(self):
        test_list = List()
        value = StructureMock()
        test_list.add_item(value)
        test_list.remove_item(value)
        self.assertEqual(value.parent, None)

    def test_remove_item_throws_on_delete_of_not_existing_item(self):
        test_list = List()
        not_value = StructureMock()

        with self.assertRaises(ValueError):
            test_list.remove_item(not_value)

    def test_can_get_value(self):
        value = StructureMock('value')
        structure_list = List([value])
        self.assertIn(value, structure_list.value)

    def test_can_set_value(self):
        value = StructureMock('value')
        structure_list = List()
        structure_list.value = [value]
        self.assertIn(value, structure_list.value)

    def test_accept(self):
        visitor = FactoryBaseVisitorMock()
        structure_list = List()
        structure_list.accept(visitor)
        self.assertEqual(visitor.list, structure_list)
        self.assertEqual(visitor.visit_list_count, 1)
