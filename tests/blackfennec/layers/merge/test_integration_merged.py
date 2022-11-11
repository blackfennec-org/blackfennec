import pytest

from blackfennec_doubles.structure.double_reference import ReferenceMock
from blackfennec.structure.map import Map
from blackfennec.layers.merge.deep_merge import DeepMerge
from blackfennec.layers.merge.merged_structure import MergedStructure
from blackfennec.structure.null import Null
from blackfennec.layers.overlay.overlay_factory_visitor import OverlayFactoryVisitor
from blackfennec.structure.reference import Reference
from blackfennec.structure.string import String
from tests.test_utils.parameterize import CORE_STRUCTURES

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
    root = merged.root or Null()
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
    actual = merged.root
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
    root = merged.root
    if root:
        actual = root.value["layer"].value
    else:
        actual = Null()
    assert actual == expected


@pytest.mark.parametrize(
    "underlay",
    CORE_STRUCTURES,
    ids=lambda x: x.__class__.__name__,
)
@pytest.mark.parametrize(
    "overlay",
    CORE_STRUCTURES,
    ids=lambda x: x.__class__.__name__,
)
def test_only_merge_with_same_type(underlay, overlay):
    if isinstance(underlay, Reference) or isinstance(overlay, Reference):
        pytest.skip("Reference not implemented yet")
    elif type(underlay) is type(overlay):
        DeepMerge.merge(underlay, overlay)
    elif isinstance(underlay, Null) or isinstance(overlay, Null):
        DeepMerge.merge(underlay, overlay)
    else:
        with pytest.raises(TypeError):
            DeepMerge.merge(underlay, overlay)
