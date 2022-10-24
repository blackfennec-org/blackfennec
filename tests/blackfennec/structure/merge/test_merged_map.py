import pytest
from blackfennec.structure.map import Map
from blackfennec.structure.merge.merged_map import MergedMap
from blackfennec.structure.null import Null
from blackfennec.structure.string import String



def test_can_construct():
    t = MergedMap(Null(), Null())
    assert t

def test_cannot_set_value():
    t = MergedMap(Null(), Null())
    with pytest.raises(AssertionError):
        t.value = "foo"

def test_can_get_value():
    t = MergedMap(Null(), Null())
    assert t.value == {}

@pytest.mark.parametrize(
    "underlay, overlay, expected",
    [
        (Null(), Map({"foo": String("bar")}), ("foo", "bar")),
        (Map(), Map({"foo": String("bar")}), ("foo", "bar")),
        (Map({"foo": String("bar")}), Null(), ("foo", "bar")),
        (Map({"foo": String("bar")}), Map(), ("foo", "bar")),
        (Map({"foo": String("bar")}), Map({"foo": String("baz")}), ("foo", "baz")),
        (Map({"foo": String("foz")}), Map({"bar": String("baz")}), ("foo", "foz")),
        (Map({"foo": String("foz")}), Map({"bar": String("baz")}), ("bar", "baz")),
    ]
)
def test_can_get_merged_children(underlay, overlay, expected):
    t = MergedMap(underlay, overlay)
    assert t.value[expected[0]].value == expected[1]

def test_repr():
    t = MergedMap(Null(), Null())
    assert repr(t).startswith("MergedMap")
