import pytest
from blackfennec.structure.list import List
from blackfennec.layers.merge.merged_list import MergedList
from blackfennec.structure.null import Null
from blackfennec.structure.string import String


def test_can_construct():
    t = MergedList(None, Null(), Null())
    assert t


def test_cannot_set_value():
    t = MergedList(None, Null(), Null())
    with pytest.raises(AssertionError):
        t.value = "foo"


def test_can_get_value():
    t = MergedList(None, Null(), Null())
    assert t.value == []


def test_repr():
    t = MergedList(None, Null(), Null())
    assert repr(t).startswith("MergedList(")
