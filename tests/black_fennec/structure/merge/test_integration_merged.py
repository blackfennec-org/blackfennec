import pytest
from doubles.black_fennec.structure.double_reference import ReferenceMock
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.merge.deep_merge import DeepMerge
from src.black_fennec.structure.merge.merged_structure import MergedStructure

from src.black_fennec.structure.null import Null
from src.black_fennec.structure.overlay.overlay_factory_visitor import OverlayFactoryVisitor
from src.black_fennec.structure.string import String
from src.black_fennec.structure.type.map_type import MapType
from src.black_fennec.structure.type.type_parser import TypeParser

pytestmark = pytest.mark.integration

@pytest.mark.parametrize(
    "underlay, overlay",
    [
        (Map(), Map({"foo": Null()})),
        (Map({"foo": Null()}), Map()),
        (Map({"foo": Null()}), Map({"foo": Null()})),
    ]
)
def test_merged_map_null_property(underlay, overlay):
    merged = DeepMerge.merge(underlay, overlay)
    assert merged.value["foo"].value is None

def test_unknown_error():
    visitor = OverlayFactoryVisitor()

    divinetype = Map({
        "super": Map({
            "super": Null(),
        })
    })

    divinetype_merged = DeepMerge.merge(divinetype.value["super"], divinetype)
    
    supertype = Map({
        "super": ReferenceMock(resolve_return=divinetype_merged),
    })

    supertype_overlay = supertype.accept(visitor)

    divinetype = supertype_overlay.value["super"]
    maptype = divinetype.value["super"]
    divinetype_merged = DeepMerge.merge(underlay=maptype, overlay=divinetype)
    supertype_merged = DeepMerge.merge(
        underlay=divinetype_merged, overlay=supertype_overlay)

    assert supertype_merged.value["super"].value["super"].value["super"].value is None

@pytest.mark.parametrize(
    "underlay, overlay",
    [
        (MergedStructure(String("foo"), Null()), MergedStructure(String("foo"), Null())),
        (MergedStructure(Null(), String("foo")), MergedStructure(String("foo"), Null())),
        (MergedStructure(String("foo"), Null()), MergedStructure(Null(), String("foo"))),
        (MergedStructure(Null(), String("foo")), MergedStructure(Null(), String("foo"))),
    ]
)
def test_merge_two_merged_maps_with_null_properties(underlay, overlay):
    merged = DeepMerge.merge(underlay, overlay)
    assert merged.value == "foo"

def test_merged_parent_is_self():
    divinetype = Map({
        "super": Map({
            "super": Null(),
        })
    })

    merged = DeepMerge.merge(divinetype.value["super"], divinetype)
    assert merged.parent.structure is merged.structure


def map_chain(layer, depth):
    innermost = Map({"layer": String(layer)})
    top = innermost
    for i in range(depth):
        top = Map({
            "layer": String(layer),
            "child": top})
    return innermost


@pytest.mark.parametrize(
    "underlay, overlay, expected",
    [
        (map_chain("underlay", 0), map_chain("overlay", 1), "overlay"),
        (map_chain("underlay", 1), map_chain("overlay", 0), "underlay"),
        (map_chain("underlay", 1), map_chain("overlay", 1), "overlay"),

    ],
)
def test_can_get_parent(underlay, overlay, expected):
    merged = MergedStructure(underlay, overlay)
    actual = merged.parent.value["layer"].value
    assert actual == expected

def test_can_get_parent_if_no_parent():
    merged = MergedStructure(Null(), Null())
    assert merged.parent is None


@pytest.mark.parametrize(
    "underlay, overlay, expected_type",
    [
        (map_chain("underlay", 0), map_chain("overlay", 0), Null),
        (map_chain("underlay", 0), map_chain("overlay", 1), MergedStructure),
        (map_chain("underlay", 1), map_chain("overlay", 0), MergedStructure),
        (map_chain("underlay", 1), map_chain("overlay", 1), MergedStructure),

    ],
)
def test_parent_returns_merged_structure(underlay, overlay, expected_type):
    merged = MergedStructure(underlay, overlay)
    root = merged.parent or Null()
    assert isinstance(root, expected_type)


@pytest.mark.xfail(
    reason="get_root not implemented correctly, tracked with issue #38")
@pytest.mark.parametrize(
    "underlay, overlay",
    [
        (map_chain("underlay", 0), map_chain("overlay", 0)),
        (map_chain("underlay", 0), map_chain("overlay", 1)),
        (map_chain("underlay", 1), map_chain("overlay", 0)),
        (map_chain("underlay", 1), map_chain("overlay", 1)),

    ],
)
def test_get_root_returns_merged_structure(underlay, overlay):
    merged = MergedStructure(underlay, overlay)
    root = merged.get_root() or Null()
    assert isinstance(root, MergedStructure)


@pytest.mark.xfail(
    reason="get_root not implemented correctly, tracked with issue #38")
@pytest.mark.parametrize(
    "underlay, overlay, diff, expected",
    [
        (map_chain("underlay", 3), map_chain("overlay", 3), 0, "overlay"),
        (map_chain("underlay", 3), map_chain("overlay", 2), 1, "overlay"),
        (map_chain("underlay", 3), map_chain("overlay", 1), 2, "overlay"),
        (map_chain("underlay", 3), map_chain("overlay", 0), 3, "overlay"),
    ],
)
def test_can_get_child_of_root(underlay, overlay, diff, expected):
    merged = MergedStructure(underlay, overlay)
    actual = merged.get_root()
    for i in range(diff):
        actual = actual.value["child"]
    actual = actual.value["layer"].value
    assert actual == expected


@pytest.mark.xfail(
    reason="get_root not implemented correctly, tracked with issue #38")
@pytest.mark.parametrize(
    "underlay, overlay, expected",
    [
        (map_chain("underlay", 0), map_chain("overlay", 0), "overlay"),
        (map_chain("underlay", 0), map_chain("overlay", 1), "overlay"),
        (map_chain("underlay", 1), map_chain("overlay", 0), "underlay"),
        (map_chain("underlay", 1), map_chain("overlay", 1), "overlay"),

    ],
)
def test_can_get_root(underlay, overlay, expected):
    merged = MergedStructure(underlay, overlay)
    root = merged.get_root()
    if root:
        actual = root.value["layer"].value
    else:
        actual = Null()
    assert actual == expected