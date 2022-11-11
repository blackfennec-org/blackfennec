import pytest
from blackfennec.structure.list import List
from blackfennec.layers.merge.merged_list import MergedList
from blackfennec.structure.null import Null
from blackfennec.structure.string import String


def test_can_construct():
    t = MergedList(Null(), Null())
    assert t

def test_cannot_set_value():
    t = MergedList(Null(), Null())
    with pytest.raises(AssertionError):
        t.value = "foo"

def test_can_get_value():
    t = MergedList(Null(), Null())
    assert t.value == []

@pytest.mark.parametrize(
    "underlay, overlay, expected",
    [
        (Null(), List([String("foo")]), (0, "foo")),
        (List(), List([String("foo")]), (0, "foo")),
        (List([String("foo")]), Null(), (0, "foo")),
        (List([String("foo")]), List(), (0, "foo")),
        (List([String("foo")]), List([String("bar")]), (0, "foo")),
        (List([String("foo")]), List([String("bar")]), (1, "bar")),
    ]
)
def test_can_get_merged_children(underlay, overlay, expected):
    t = MergedList(underlay, overlay)
    assert t.value[expected[0]].value == expected[1]

def test_repr():
    t = MergedList(Null(), Null())
    assert repr(t).startswith("MergedList(")
