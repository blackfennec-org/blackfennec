import unittest
import logging

from doubles.black_fennec.structure.double_structure import StructureMock
from doubles.black_fennec.structure.double_root import RootMock
from doubles.black_fennec.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from src.black_fennec.structure.map import Map

class MapTestSuite(unittest.TestCase):
    def test_can_construct(self):
        m = Map()
        self.assertEqual(m, {})

    def test_can_construct_from_dict(self):
        data = {'a': StructureMock(), 'b': StructureMock()}
        structure = Map(data)
        self.assertEqual(structure, data)
        self.assertEqual(data['a'].parent, structure)

    def test_can_add_item(self):
        m = Map()
        key = 'Key'
        value = StructureMock()
        m[key] = value
        self.assertIn(key, m)

    def test_does_set_parent(self):
        m = Map()
        key = 'Key'
        value = StructureMock()
        m[key] = value
        self.assertEqual(value.parent, m)

    def test_throws_on_parent_not_none(self):
        m = Map()
        key = 'Key'
        value = RootMock()

        with self.assertRaises(ValueError):
            m[key] = value

    def test_logs_on_parent_not_none(self):
        m = Map()
        key = 'Key'
        value = RootMock()

        with self.assertLogs(None, logging.ERROR):
            try:
                m[key] = value
            except ValueError:
                pass

    def test_can_delete_item(self):
        m = Map()
        key = 'Key'
        value = StructureMock()
        m[key] = value
        del m[key]
        self.assertNotIn(key, m)

    def test_does_unset_parent(self):
        m = Map()
        key = 'Key'
        value = StructureMock()
        m[key] = value
        del m[key]
        self.assertEqual(value.parent, None)

    def test_throws_on_delete_of_not_existing_item(self):
        m = Map()
        not_key = 'Not in Map'

        with self.assertRaises(KeyError):
            del m[not_key]

    def test_logs_on_delete_of_not_existing_item(self):
        m = Map()
        not_key = 'Not in Map'
        with self.assertLogs(None, logging.ERROR):
            try:
                del m[not_key]
            except KeyError:
                pass

    def test_can_get_value(self):
        key = 'key'
        value = StructureMock('value')
        structure_map = Map({key: value})
        self.assertEqual(value, structure_map.value[key])

    def test_can_set_value(self):
        key = 'key'
        value = StructureMock('value')
        structure_map = Map()
        structure_map.value = {key: value}
        self.assertEqual(value, structure_map.value[key])

    def test_accept(self):
        visitor = FactoryBaseVisitorMock()
        structure_map = Map()
        structure_map.accept(visitor)
        self.assertEqual(visitor.map, structure_map)
        self.assertEqual(visitor.visit_map_count, 1)
