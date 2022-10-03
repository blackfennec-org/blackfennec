from typing import Union, Type

import pytest

from src.black_fennec.document_system.mime_type.types.json.json_pointer_serializer import JsonPointerSerializer
from src.black_fennec.structure.reference_navigation.child_navigator import ChildNavigator
from src.black_fennec.structure.reference_navigation.index_of_navigator import IndexOfNavigator
from src.black_fennec.structure.reference_navigation.navigator import Navigator
from src.black_fennec.structure.reference_navigation.parent_navigator import ParentNavigator
from src.black_fennec.structure.reference_navigation.root_navigator import RootNavigator
from src.black_fennec.structure.reference_navigation.sibling_offset_navigator import SiblingOffsetNavigator


@pytest.mark.parametrize("relative_pointer_str, expected", [
    ('0/key', [ChildNavigator('key')]),
    ('1/key', [ParentNavigator(), ChildNavigator('key')]),
    ('3/key', [ParentNavigator(), ParentNavigator(), ParentNavigator(), ChildNavigator('key')]),
    ('0/key/1', [ChildNavigator('key'), ChildNavigator('1')]),
    ('a', ValueError),
    ('0-1', [SiblingOffsetNavigator(-1)]),
    ('0-0', []),
    ('0-3', [SiblingOffsetNavigator(-3)]),
    ('1-1', [ParentNavigator(), SiblingOffsetNavigator(-1)]),
    ('3-1', [ParentNavigator(), ParentNavigator(), ParentNavigator(), SiblingOffsetNavigator(-1)]),
    ('0+1', [SiblingOffsetNavigator(1)]),
    ('0+0', []),
    ('0+3', [SiblingOffsetNavigator(3)]),
    ('1+1', [ParentNavigator(), SiblingOffsetNavigator(1)]),
    ('3+1', [ParentNavigator(), ParentNavigator(), ParentNavigator(), SiblingOffsetNavigator(1)]),
    ('0-a', ValueError),
    ('0+a', ValueError),
    ('0#', [IndexOfNavigator()]),
    ('0/key#', [ChildNavigator('key'), IndexOfNavigator()]),
    ('0/0/0#', [ChildNavigator('0'), ChildNavigator('0'), IndexOfNavigator()]),
    ('-1', ValueError),
])
def test_parse_relative_pointer(relative_pointer_str: str, expected: Union[list[Navigator], Type[Exception]]):
    if type(expected) == type and issubclass(expected, Exception):
        with pytest.raises(expected):
            JsonPointerSerializer.deserialize_relative_pointer(relative_pointer_str)
    else:
        relative_pointer = JsonPointerSerializer.deserialize_relative_pointer(relative_pointer_str)
        assert relative_pointer == expected


@pytest.mark.parametrize("absolute_pointer_str, expected", [
    ('key', [RootNavigator(), ChildNavigator('key')]),
    ('0', [RootNavigator(), ChildNavigator('0')]),
    ('0/key', [RootNavigator(), ChildNavigator('0'), ChildNavigator('key')]),
    ('', [RootNavigator()]),
    ('/', [RootNavigator(), ChildNavigator('')]),
    ('~0', [RootNavigator(), ChildNavigator('~')]),
    ('~1', [RootNavigator(), ChildNavigator('/')]),
    ('~01', [RootNavigator(), ChildNavigator('~1')]),
    ('~', [RootNavigator(), ChildNavigator('~')]),
    ('~2', [RootNavigator(), ChildNavigator('~2')]),
])
def test_parse_absolute_pointer(absolute_pointer_str: str, expected: Union[list[Navigator], Type[Exception]]):
    if type(expected) == type and issubclass(expected, Exception):
        with pytest.raises(expected):
            JsonPointerSerializer.deserialize_absolute_pointer(absolute_pointer_str)
            return
    else:
        relative_pointer = JsonPointerSerializer.deserialize_absolute_pointer(absolute_pointer_str)
        assert relative_pointer == expected


@pytest.mark.parametrize("json_pointer, expected", [
    ('0/a', True),
    ('0-1/a', True),
    ('0+1/a', True),
    ('0', True),
    ('a', False),
    ('0-a', False)
])
def test_is_relative_json_pointer(json_pointer: str, expected: bool):
    assert JsonPointerSerializer.is_relative_json_pointer(json_pointer) is expected


@pytest.mark.parametrize("json_pointer, expected", [
    ('/a', True),
    ('/a/a', True),
    ('', True),
    ('/', True),
    ('~0', True),
    ('~1', True),
    ('~', False),
    ('~2', False),
])
def test_is_absolute_json_pointer(json_pointer: str, expected: bool):
    assert JsonPointerSerializer.is_absolute_json_pointer(json_pointer) is expected
