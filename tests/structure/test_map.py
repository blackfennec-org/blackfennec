import unittest
import logging

from doubles.structure.double_info import InfoMock
from doubles.structure.double_root import RootMock
from src.structure.map import Map

class MapTestSuite(unittest.TestCase):
    def test_can_construct(self):
        m = Map()
        self.assertEqual(m, {})

    def test_can_construct_from_dict(self):
        data = {'a': InfoMock(), 'b': InfoMock()}
        info = Map(data)
        self.assertEqual(info, data)
        self.assertEqual(data['a'].parent, info)

    def test_can_get_children(self):
        data = {'a': InfoMock(), 'b': InfoMock()}
        info = Map(data)
        children = info.children
        self.assertListEqual(children, list(data.values()))

    def test_can_add_item(self):
        m = Map()
        key = 'Key'
        value = InfoMock()
        m[key] = value
        self.assertIn(key, m)

    def test_does_set_parent(self):
        m = Map()
        key = 'Key'
        value = InfoMock()
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
        value = InfoMock()
        m[key] = value
        del m[key]
        self.assertNotIn(key, m)

    def test_does_unset_parent(self):
        m = Map()
        key = 'Key'
        value = InfoMock()
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
