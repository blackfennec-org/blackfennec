import json
import pytest

from doubles.black_fennec.document_system.mime_type.types.json.double_json_reference_serializer import JsonReferenceSerializerMock
from src.black_fennec.document_system.mime_type.types.json.structure_serializer import StructureSerializer
from src.black_fennec.structure.merge.deep_merge import DeepMerge
from src.black_fennec.structure.merge.merged import MergedMap, MergedStructure
from src.black_fennec.structure.overlay.overlay_factory_visitor import OverlayFactoryVisitor

from src.black_fennec.structure.map import Map
from src.black_fennec.structure.reference import Reference
from src.black_fennec.structure.string import String

from src.black_fennec.structure.reference_navigation.parent_navigator import ParentNavigator
from src.black_fennec.structure.reference_navigation.child_navigator import ChildNavigator


@pytest.fixture
def parser():
    structure_serializer = StructureSerializer(JsonReferenceSerializerMock())
    return structure_serializer.deserialize
    

def test_merges_properites(parser):
    j = json.loads("""
{
    "super": {
        "a": {
            "b": "super.a.b"
        }
    },
    "a": {
        "c": "a.c"
    }
}
""")
    structure = parser(j)
    merged = DeepMerge.merge(structure.value["super"], structure)

    assert merged.value["a"].value["b"].value == "super.a.b"


@pytest.fixture
def structure(parser):
    j = json.loads("""
    {
        "super": {
            "super": {
                "super": null,
                "a": {
                    "a": "super.super.a.a"
                }
            },
            "b": {
                "b": "super.b.b"
            }
        },
        "c": {
            "c": "c.c"
        }
    }
    """)
    return parser(j)



def _merge_super(structure):
    super = structure.value["super"]
    if super.value is None:
        return structure
    merged_super = _merge_super(super)
    return DeepMerge.merge(underlay=merged_super, overlay=structure)

@pytest.fixture
def merged(structure):
    return _merge_super(structure)
    

def test_can_access_super_super(merged):
    assert merged.value["a"].value["a"].value == "super.super.a.a"

def test_can_access_super(merged):
    assert merged.value["b"].value["b"].value == "super.b.b"

def test_can_merge_merged_structure(merged):
    assert merged.value["c"].value["c"].value == "c.c"

def test_1(parser):
    j = json.loads("""
{
    "super": {
        "super": {
            "super": null
        },
        "b": {
            "value": "super.b.value"
        }
    }
}
""")
    s = parser(j)
    merged = _merge_super(s)
    b = merged.value["b"]
    assert b.value["value"].value == "super.b.value"

def test_2(parser):
    j = json.loads("""
{
    "super": {
        "super": {
            "super": null,
            "a": {
                "value": "super.a.value"
            }
        }
    }
}
""")
    s = parser(j)
    merged = _merge_super(s)
    a = merged.value["a"]
    assert a.value["value"].value == "super.a.value"

def test_merge_with_overlay():
    map = Map({
            "a": Reference([ ParentNavigator(), ChildNavigator("b")]),
            "b": Map({
                "1": String("value"),
            }),
            "c": Map({
                "2": String("value"),
            })
        })
    visitor = OverlayFactoryVisitor()
    overlay = map.accept(visitor)
    merged = DeepMerge.merge(underlay=overlay.value["a"], overlay=overlay.value["c"])
    assert merged.value["1"].value == "value"
    assert merged.value["2"].value == "value"

def test_merge_merged_overlay():
    map = Map({
            "a": Reference([ ParentNavigator(), ChildNavigator("b")]),
            "b": Map({
                "1": String("overlay"),
            }),
            "c": Map({
            })
        })
    visitor = OverlayFactoryVisitor()
    resolved = map.accept(visitor)
    overlay = DeepMerge.merge(underlay=resolved.value["a"], overlay=resolved.value["c"])

    map = Map({
            "a": Reference([ ParentNavigator(), ChildNavigator("b")]),
            "b": Map({
                "1": String("underlay"),
            }),
            "c": Map({
                "2": String("underlay"),
            })
        })
    visitor = OverlayFactoryVisitor()
    resolved = map.accept(visitor)
    underlay = DeepMerge.merge(underlay=resolved.value["a"], overlay=resolved.value["c"])

    merged = DeepMerge.merge(underlay=underlay, overlay=overlay)
    assert merged.value["1"].value == "overlay"
    assert merged.value["2"].value == "underlay"


def test_navigation_in_doubly_merged_object():
    b = Map({"1": String("overlay")})
    c = Map()
    overlay = DeepMerge.merge(underlay=b, overlay=c)

    b = Map({"1": String("underlay")})
    c = Map({"2": String("underlay")})
    underlay = DeepMerge.merge(underlay=b, overlay=c)

    merged = DeepMerge.merge(underlay=underlay, overlay=overlay)
    assert merged.value["1"].parent.value["2"].value == "underlay"

def test_navigation_in_merged_object():
    
    b = Map({"1": String("underlay")})
    c = Map({"2": String("overlay")})
    merged = DeepMerge.merge(underlay=b, overlay=c)
    assert merged.value["1"].value == "underlay"
    assert merged.value["2"].value == "overlay"
    assert merged.value["2"].parent == merged
    assert merged.value["1"].parent == merged
    assert merged.value["1"].parent.value["2"].value == "overlay"

def test_can_access_parent():   
    b = Map({"1": String("underlay")})
    c = Map({})
    merged = DeepMerge.merge(underlay=b, overlay=c)
    assert merged.value["1"].parent == merged
