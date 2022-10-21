import pytest
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.merge.merged_map import MergedMap
from src.black_fennec.structure.null import Null
from src.black_fennec.structure.string import String



def test_can_construct():
    t = MergedMap(None, None)
    assert t

def test_cannot_set_value():
    t = MergedMap(None, None)
    with pytest.raises(AssertionError):
        t.value = "foo"

def test_can_get_value():
    t = MergedMap(None, None)
    assert t.value == {}

@pytest.mark.parametrize(
    "underlay, overlay, expected",
    [
        (Map(), Map({"foo": String("bar")}), ("foo", "bar")),
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
    t = MergedMap(None, None)
    assert repr(t).startswith("MergedMap")
