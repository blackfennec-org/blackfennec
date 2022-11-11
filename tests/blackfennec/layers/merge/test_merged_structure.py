from ctypes import Structure
from typing import Optional
import pytest
from blackfennec_doubles.structure.double_structure import StructureMock
from blackfennec.structure.map import Map
from blackfennec.layers.merge.merged_structure import MergedStructure
from blackfennec.structure.null import Null
from blackfennec.structure.string import String
from blackfennec.util.parameterized_visitor import ParameterizedVisitor

@pytest.mark.parametrize(
    "underlay, overlay, expected",
    [
        (Null(), String("overlay"), "overlay"),
        (String("underlay"), Null(), "underlay"),
        (String("underlay"), String("overlay"), "overlay"),
    ],
)
def test_can_get_value(underlay, overlay, expected):
    t = MergedStructure(underlay, overlay)
    assert t.value == expected

def test_cannot_set_value():
    t = MergedStructure(Null(), Null())
    with pytest.raises(AssertionError):
        t.value = "foo"

def test_cannot_set_parent():
    t = MergedStructure(Null(), Null())
    with pytest.raises(AssertionError):
        t.parent = t

@pytest.mark.parametrize(
    "merged",
    [
        MergedStructure(Null(), String("foo")),
        MergedStructure(String("foo"), Null()),
        MergedStructure(String("foo"), String("bar")),
    ],
)
def test_can_accept_correctly(merged):
    visitor = ParameterizedVisitor(string=True)
    assert merged.accept(visitor) == True

def can_get_parent_parameters():
    def create_mock(**kwargs):
        return StructureMock(
            value = "value",
            accept_strategy=lambda s, v: v.visit_string(s),
            **kwargs)
        
    parent = create_mock()
    valid_valid = (
        create_mock(parent=create_mock()), 
        create_mock(parent=parent),
        parent)
    none_valid = (
        create_mock(parent=None),
        create_mock(parent=parent),
        parent)
    valid_none = (
        create_mock(parent=parent),
        create_mock(parent=None),
        parent)
    none_none = (
        create_mock(parent=None),
        create_mock(parent=None),
        None)
    return [valid_valid, none_valid, valid_none, none_none]
@pytest.mark.parametrize(
    "underlay, overlay, expected",
    can_get_parent_parameters(),
    ids=["valid_valid", "none_valid", "valid_none", "none_none"],
)
def test_can_get_parent(underlay, overlay, expected):
    merged = MergedStructure(underlay, overlay)
    parent = merged.parent.structure if merged.parent else merged.parent
    assert parent == expected
    

def can_get_structure_parameters():
    structure = StructureMock(value=True)
    valid_valid = (
        StructureMock(value=None), 
        structure,
        structure)
    none_valid = (
        StructureMock(value=None),
        structure,
        structure)
    valid_none = (
        structure,
        StructureMock(value=None),
        structure)
    return [valid_valid, none_valid, valid_none]
@pytest.mark.parametrize(
    "underlay, overlay, expected",
    can_get_structure_parameters(),
    ids=["valid_valid", "none_valid", "valid_none"],
)
def test_can_get_structure(underlay, overlay, expected):
    merged = MergedStructure(underlay, overlay)
    assert merged.structure == expected
