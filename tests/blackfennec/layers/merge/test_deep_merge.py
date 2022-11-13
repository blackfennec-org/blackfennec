import json
import pytest

from blackfennec_doubles.document_system.mime_type.json.double_json_reference_serializer import \
    JsonReferenceSerializerMock
from blackfennec.structure.structure_serializer import StructureSerializer
from blackfennec.layers.merge.deep_merge import DeepMerge
from blackfennec.structure.null import Null
from blackfennec.layers.merge.merged_null import MergedNull
from blackfennec.layers.overlay.overlay_factory_visitor import OverlayFactoryVisitor

from blackfennec.structure.map import Map
from blackfennec.structure.reference import Reference
from blackfennec.structure.string import String

from blackfennec.structure.reference_navigation.parent_navigator import ParentNavigator
from blackfennec.structure.reference_navigation.child_navigator import ChildNavigator


@pytest.fixture
def parser():
    structure_serializer = StructureSerializer(JsonReferenceSerializerMock())
    return structure_serializer.deserialize


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


def test_merges_properties(parser):
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


def test_can_access_super_super(merged):
    assert merged.value["a"].value["a"].value == "super.super.a.a"


def test_can_access_super(merged):
    assert merged.value["b"].value["b"].value == "super.b.b"


def test_can_merge_merged_structure(merged):
    assert merged.value["c"].value["c"].value == "c.c"


def test_merge_super_first_level(parser):
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


def test_merge_super_second_level(parser):
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
        "a": Reference([ParentNavigator(), ChildNavigator("b")]),
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
        "a": Reference([ParentNavigator(), ChildNavigator("b")]),
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
        "a": Reference([ParentNavigator(), ChildNavigator("b")]),
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
    assert merged.value["1"].parent.value["2"].value == "overlay"


def test_can_access_parent():
    b = Map({"1": String("underlay")})
    c = Map({})
    merged = DeepMerge.merge(underlay=b, overlay=c)
    assert merged.value["1"].parent.structure == merged.structure


def test_navigation_in_phantom_parents():
    a = Map({"1": Map({"2": String("underlay")})})
    b = Map({"2": String("overlay")})
    merged = DeepMerge.merge(underlay=a.value["1"], overlay=b)
    assert merged.parent.structure == a.structure


def test_can_compare_merged_objects():
    a = Map({"1": String("underlay")})
    b = Map({})
    one = DeepMerge.merge(underlay=a, overlay=b)
    two = DeepMerge.merge(underlay=a, overlay=b)

    assert one.structure == two.structure


def test_cannot_compare_merged_objects_with_different_values():
    a = Map({"1": String("underlay")})
    b = Map({})
    c = Map({"1": String("underlay")})
    d = Map({})
    one = DeepMerge.merge(underlay=a, overlay=b)
    two = DeepMerge.merge(underlay=c, overlay=d)

    assert one.structure != two.structure


def test_cannot_compare_merged_objects_with_standard_objects():
    a = Map({"1": String("underlay")})
    b = Map({})
    one = DeepMerge.merge(underlay=a, overlay=b)
    two = Map({"1": String("underlay")})

    assert one.structure != two.structure


def test_can_recover_from_null_merge():
    a = Map({"1": String("underlay")})
    b = Null()
    c = Map({"1": String("overlay")})
    one = DeepMerge.merge(underlay=a, overlay=b)
    two = DeepMerge.merge(underlay=one, overlay=c)

    assert not isinstance(two, MergedNull)


def test_can_recover_from_null_merge_2():
    a = Null()
    b = Map({"1": String("underlay")})
    c = Map({"1": String("overlay")})
    one = DeepMerge.merge(underlay=a, overlay=b)
    two = DeepMerge.merge(underlay=one, overlay=c)

    assert not isinstance(two, MergedNull)


def test_cannot_compare_merged():
    b = Map({"1": String("underlay")})
    c = Map({})
    merged = DeepMerge.merge(underlay=b, overlay=c)
    assert merged.value["1"].parent != merged
