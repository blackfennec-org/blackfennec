import pytest
from src.black_fennec.structure.list import List
from src.black_fennec.structure.merge.merged_list import MergedList
from src.black_fennec.structure.string import String


def test_can_construct():
    t = MergedList(None, None)
    assert t

def test_cannot_set_value():
    t = MergedList(None, None)
    with pytest.raises(AssertionError):
        t.value = "foo"

def test_can_get_value():
    t = MergedList(None, None)
    assert t.value == []

@pytest.mark.parametrize(
    "underlay, overlay, expected",
    [
        (List(), List([String("foo")]), (0, "foo")),
        (List([String("foo")]), List(), (0, "foo")),
        (List([String("foo")]), List([String("bar")]), (0, "foo")),
        (List([String("foo")]), List([String("bar")]), (1, "bar")),
    ]
)
def test_can_get_merged_children(underlay, overlay, expected):
    t = MergedList(underlay, overlay)
    assert t.value[expected[0]].value == expected[1]

def test_repr():
    t = MergedList(None, None)
    assert repr(t).startswith("MergedList(")
