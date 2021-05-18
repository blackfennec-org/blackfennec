import unittest
from enum import Enum

from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.root import Root
from src.black_fennec.structure.string import String
from src.black_fennec.util.json.json_pointer import JsonPointer, JsonPointerType, is_relative_json_pointer, is_absolute_json_pointer


class JsonPointerTestSuite(unittest.TestCase):
    def test_can_construct(self):
        JsonPointer('0', JsonPointerType.RELATIVE_JSON_POINTER)
        JsonPointer('', JsonPointerType.ABSOLUTE_JSON_POINTER)

    def test_get_path(self):
        pointer = JsonPointer('/test/test', JsonPointerType.ABSOLUTE_JSON_POINTER)
        hierarchy = pointer.path
        self.assertEqual(3, len(hierarchy))

    def test_set_path(self):
        pointer = JsonPointer('/test/test', JsonPointerType.ABSOLUTE_JSON_POINTER)
        pointer.path = ('/test', JsonPointerType.ABSOLUTE_JSON_POINTER)
        self.assertEqual(2, len(pointer.path))

    def test_resolve_pointer_without_source(self):
        pointer = JsonPointer('0/key', JsonPointerType.RELATIVE_JSON_POINTER)
        with self.assertRaises(ValueError):
            pointer.resolve_from(None)

    def test_resolve_pointer_of_type_not_implemented(self):
        data = {
            'key': String('value')
        }
        map = Map(data)

        class NotImplementedJsonPointerType(Enum):
            NEW_JSON_POINTER = 2

        pointer = JsonPointer('0/key', NotImplementedJsonPointerType.NEW_JSON_POINTER)
        with self.assertRaises(NotImplementedError):
            pointer.resolve_from(map)

    def test_resolve_relative_pointer_level_zero(self):
        data = {
            'key': String('value')
        }
        map = Map(data)
        pointer = JsonPointer('0/key', JsonPointerType.RELATIVE_JSON_POINTER)
        result = pointer.resolve_from(map)
        self.assertEqual(data['key'], result)

    def test_resolve_relative_pointer_parent_level(self):
        data = {
            'key': String('value')
        }
        map = Map(data)
        pointer = JsonPointer('1/key', JsonPointerType.RELATIVE_JSON_POINTER)
        result = pointer.resolve_from(data['key'])
        self.assertEqual(data['key'], result)

    def test_resolve_relative_pointer_invalid_level_navigation(self):
        data = [
            String('value1'),
            String('value2')
        ]
        List(data)
        pointer = JsonPointer('a', JsonPointerType.RELATIVE_JSON_POINTER)
        with self.assertRaises(ValueError):
            pointer.resolve_from(data[0])

    def test_resolve_relative_pointer_list_preceeding_sibling(self):
        data = [
            String('value1'),
            String('value2')
        ]
        List(data)
        pointer = JsonPointer('0-1', JsonPointerType.RELATIVE_JSON_POINTER)
        result = pointer.resolve_from(data[1])
        self.assertEqual(data[0], result)

    def test_resolve_relative_pointer_list_succeeding_sibling(self):
        data = [
            String('value1'),
            String('value2')
        ]
        List(data)
        pointer = JsonPointer('0+1', JsonPointerType.RELATIVE_JSON_POINTER)
        result = pointer.resolve_from(data[0])
        self.assertEqual(data[1], result)

    def test_resolve_relative_pointer_list_invalid_index_decrement(self):
        data = [
            String('value1'),
            String('value2')
        ]
        List(data)
        pointer = JsonPointer('0-a', JsonPointerType.RELATIVE_JSON_POINTER)
        with self.assertRaises(ValueError):
            pointer.resolve_from(data[0])

    def test_resolve_relative_pointer_list_index_increment_not_in_list(self):
        data = {
            'key': String('value')
        }
        map = Map(data)
        pointer = JsonPointer('0-1', JsonPointerType.RELATIVE_JSON_POINTER)
        with self.assertRaises(TypeError):
            pointer.resolve_from(data['key'])

    def test_resolve_relative_pointer_list_invalid_index_increment(self):
        data = [
            String('value1'),
            String('value2')
        ]
        List(data)
        pointer = JsonPointer('0+a', JsonPointerType.RELATIVE_JSON_POINTER)
        with self.assertRaises(ValueError):
            pointer.resolve_from(data[0])

    def test_resolve_relative_pointer_key(self):
        data = {
            'key': String('value')
        }
        Map(data)
        pointer = JsonPointer('0#', JsonPointerType.RELATIVE_JSON_POINTER)
        result = pointer.resolve_from(data['key'])
        self.assertEqual('key', result)

    def test_resolve_relative_pointer_key_in_list_instead_of_map(self):
        data = [
            String('value1'),
            String('value2')
        ]
        list = List(data)
        list.parent = Root(child=list)
        pointer = JsonPointer('0#', JsonPointerType.RELATIVE_JSON_POINTER)
        with self.assertRaises(TypeError):
            pointer.resolve_from(data[0])


    def test_resolve_absolute_pointer_map_navigation(self):
        data = {
            'key': String('value')
        }
        map = Map(data)
        map.parent = Root(child=map)
        pointer = JsonPointer('key', JsonPointerType.ABSOLUTE_JSON_POINTER)
        result = pointer.resolve_from(map)
        self.assertEqual(data['key'], result)

    def test_resolve_absolute_pointer_map_navigation_invalid_key(self):
        data = {
            'key': String('value')
        }
        map = Map(data)
        map.parent = Root(child=map)
        pointer = JsonPointer('non-existent-key', JsonPointerType.ABSOLUTE_JSON_POINTER)
        with self.assertRaises(KeyError):
            pointer.resolve_from(map)

    def test_resolve_absolute_pointer_list_navigation(self):
        data = [
            String('value1'),
            String('value2')
        ]
        list = List(data)
        list.parent = Root(child=list)
        pointer = JsonPointer('1', JsonPointerType.ABSOLUTE_JSON_POINTER)
        result = pointer.resolve_from(data[0])
        self.assertEqual(data[1], result)

    def test_resolve_absolute_pointer_list_navigation_non_decimal_index(self):
        data = [
            String('value1'),
            String('value2')
        ]
        list = List(data)
        list.parent = Root(child=list)
        pointer = JsonPointer('key', JsonPointerType.ABSOLUTE_JSON_POINTER)
        with self.assertRaises(ValueError):
            pointer.resolve_from(data[0])

    def test_resolve_absolute_pointer_list_navigation_index_out_of_bounds(self):
        data = [
            String('value1'),
            String('value2')
        ]
        list = List(data)
        list.parent = Root(child=list)
        pointer = JsonPointer('2', JsonPointerType.ABSOLUTE_JSON_POINTER)
        with self.assertRaises(IndexError):
            pointer.resolve_from(data[0])

    def test_resolve_absolute_pointer_string_navigation(self):
        string = String('value1')
        string.parent = Root(child=string)
        pointer = JsonPointer('1', JsonPointerType.ABSOLUTE_JSON_POINTER)
        with self.assertRaises(TypeError):
            pointer.resolve_from(string)

    def test_is_relative_json_pointer(self):
        self.assertTrue(is_relative_json_pointer('0/a'))
        self.assertTrue(is_relative_json_pointer('0-1/a'))
        self.assertTrue(is_relative_json_pointer('0+1/a'))
        self.assertTrue(is_relative_json_pointer('0'))
        self.assertFalse(is_relative_json_pointer('a'))
        self.assertFalse(is_relative_json_pointer('0-a'))

    def test_is_absolute_json_pointer(self):
        self.assertTrue(is_absolute_json_pointer('/a'))
        self.assertTrue(is_absolute_json_pointer('/a/a'))
        self.assertTrue(is_absolute_json_pointer(''))
        self.assertTrue(is_absolute_json_pointer('/'))
        self.assertTrue(is_absolute_json_pointer('~0'))
        self.assertTrue(is_absolute_json_pointer('~1'))
        self.assertFalse(is_absolute_json_pointer('~'))
        self.assertFalse(is_absolute_json_pointer('~2'))