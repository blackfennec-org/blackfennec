"""
def test_resolve_absolute_pointer_map_navigation_invalid_key(self):
    data = {
        'key': String('value')
    }
    map = Map(data)
    RootFactory.make_root(map)
    pointer = JsonPointerParser('non-existent-key', JsonPointerType.ABSOLUTE_JSON_POINTER)
    with self.assertRaises(KeyError):
        pointer.resolve_from(map)


def test_resolve_absolute_pointer_list_navigation(self):
    data = [
        String('value1'),
        String('value2')
    ]
    list = List(data)
    RootFactory.make_root(list)
    pointer = JsonPointerParser('1', JsonPointerType.ABSOLUTE_JSON_POINTER)
    result = pointer.resolve_from(data[0])
    self.assertEqual(data[1], result)


def test_resolve_absolute_pointer_list_navigation_non_decimal_index(self):
    data = [
        String('value1'),
        String('value2')
    ]
    list = List(data)
    RootFactory.make_root(list)
    pointer = JsonPointerParser('key', JsonPointerType.ABSOLUTE_JSON_POINTER)
    with self.assertRaises(ValueError):
        pointer.resolve_from(data[0])


def test_resolve_absolute_pointer_list_navigation_index_out_of_bounds(self):
    data = [
        String('value1'),
        String('value2')
    ]
    list = List(data)
    RootFactory.make_root(list)
    pointer = JsonPointerParser('2', JsonPointerType.ABSOLUTE_JSON_POINTER)
    with self.assertRaises(IndexError):
        pointer.resolve_from(data[0])


def test_resolve_absolute_pointer_string_navigation(self):
    string = String('value1')
    RootFactory.make_root(string)
    pointer = JsonPointerParser('1', JsonPointerType.ABSOLUTE_JSON_POINTER)
    with self.assertRaises(TypeError):
        pointer.resolve_from(string)
"""
