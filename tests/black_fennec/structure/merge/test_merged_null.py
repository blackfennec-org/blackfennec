import pytest
from src.black_fennec.structure.map import Map

from src.black_fennec.structure.merge.merged_null import MergedNull
from src.black_fennec.structure.merge.merged_structure import MergedStructure
from src.black_fennec.structure.null import Null
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.string import String
from src.black_fennec.util.parameterized_visitor import ParameterizedVisitor

def test_can_construct():
    t = MergedNull(Null(), Null())
    assert t

def test_can_get_value():
    t = MergedNull(Null(), Null())
    assert t.value is None

def test_can_get_subject():
    t = MergedNull(Null(), Null())
    assert isinstance(t.subject, Null)

def test_cannot_set_value():
    t = MergedNull(Null(), Null())
    with pytest.raises(AssertionError):
        t.value = "foo"

@pytest.mark.parametrize(
    "underlay, overlay",
    [
        (Null(), String()),
        (String(), Null()),
        (String(), String()),
    ]
)
def test_cannot_construct_with_none_null(underlay, overlay):
    with pytest.raises(AssertionError):
        MergedNull(underlay, overlay)


def test_can_accept_visitor():
    t = MergedNull(Null(), Null())
    assert t.accept(ParameterizedVisitor(null=True))

def test_repr():
    t = MergedNull(Null(), Null())
    assert repr(t).startswith("MergedNull")