import pytest
from src.black_fennec.structure.map import Map

from src.black_fennec.structure.merge.merged_null import MergedNull
from src.black_fennec.structure.merge.merged_structure import MergedStructure
from src.black_fennec.structure.null import Null
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.string import String
from src.black_fennec.util.parameterized_visitor import ParameterizedVisitor

def test_can_construct():
    t = MergedNull(None, None)
    assert t

@pytest.mark.parametrize(
    "underlay, overlay, expected",
    [
        (Null(), Null(), None),
        (Null(), String("overlay"), "overlay"),
        (String("underlay"), Null(), "underlay"),
        (String("underlay"), String("overlay"), "overlay"),
    ],
)
def test_can_get_simple_value(underlay, overlay, expected):
    t = MergedNull(underlay, overlay)
    assert t.value == expected

@pytest.mark.xfail("merged null is implemented wrong")
def test_can_get_complex_value():
    t = MergedNull(Null(), Map({"foo": Number(1)}))
    assert isinstance(t.value["foo"], MergedStructure)

def test_cannot_set_value():
    t = MergedNull(None, None)
    with pytest.raises(AssertionError):
        t.value = "foo"

@pytest.mark.parametrize(
    "underlay, overlay, visitor",
    [
        (Null(),        Null(),             ParameterizedVisitor(null=True)),
        (Null(),        String("overlay"),  ParameterizedVisitor(string=True)),
        (Number(-1),    Null(),             ParameterizedVisitor(number=True)),
        (Number(-1),    String("overlay"),  ParameterizedVisitor(string=True)),
    ],
)
def test_can_accept_visitor(underlay, overlay, visitor):
    t = MergedNull(underlay, overlay)
    assert t.accept(visitor)

def test_repr():
    t = MergedNull(None, None)
    assert repr(t).startswith("MergedNull")