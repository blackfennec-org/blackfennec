import pytest
from blackfennec.layers.merge.merged_map import MergedMap
from blackfennec.structure.null import Null


def test_can_construct():
    t = MergedMap(None, Null(), Null())
    assert t


def test_cannot_set_value():
    t = MergedMap(None, Null(), Null())
    with pytest.raises(AssertionError):
        t.value = "foo"


def test_can_get_value():
    t = MergedMap(None, Null(), Null())
    assert t.value == {}


def test_repr():
    t = MergedMap(None, Null(), Null())
    assert repr(t).startswith("MergedMap")
