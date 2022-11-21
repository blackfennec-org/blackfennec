import pytest

from blackfennec.structure.map import Map
from blackfennec.structure.list import List
from blackfennec.layers.merge.merged_layer import MergedLayer
from blackfennec.layers.merge.merged_structure import MergedStructure
from blackfennec.structure.null import Null
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
    merged = MergedLayer().apply(underlay, overlay)
    assert merged.value["foo"].value is None


@pytest.mark.parametrize(
    "underlay, overlay",
    [
        (MergedStructure(None, String("foo"), Null()), MergedStructure(None, String("foo"), Null())),
        (MergedStructure(None, Null(), String("foo")), MergedStructure(None, String("foo"), Null())),
        (MergedStructure(None, String("foo"), Null()), MergedStructure(None, Null(), String("foo"))),
        (MergedStructure(None, Null(), String("foo")), MergedStructure(None, Null(), String("foo"))),
    ]
)
def test_merge_two_merged_maps_with_null_properties(underlay, overlay):
    merged = MergedLayer().apply(underlay, overlay)
    assert merged.value == "foo"


def test_merged_parent_is_self():
    divinetype = Map({
        "super": Map({
            "super": Null(),
        })
    })

    merged = MergedLayer().apply(divinetype.value["super"], divinetype)
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
    merged = MergedLayer().apply(underlay, overlay)
    actual = merged.parent.value["layer"].value
    assert actual == expected


def test_can_get_parent_if_no_parent():
    merged = MergedStructure(None, Null(), Null())
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
    merged = MergedLayer().apply(underlay, overlay)
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
    merged = MergedStructure(None, underlay, overlay)
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
    merged = MergedStructure(None, underlay, overlay)
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
    merged = MergedStructure(None, underlay, overlay)
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
        MergedLayer().apply(underlay, overlay)
    elif isinstance(underlay, Null) or isinstance(overlay, Null):
        MergedLayer().apply(underlay, overlay)
    else:
        with pytest.raises(TypeError):
            MergedLayer().apply(underlay, overlay)


@pytest.mark.parametrize(
    "underlay, overlay, expected",
    [
        (Null(), Map({"foo": String("bar")}), ("foo", "bar")),
        (Map(), Map({"foo": String("bar")}), ("foo", "bar")),
        (Map({"foo": String("bar")}), Null(), ("foo", "bar")),
        (Map({"foo": String("bar")}), Map(), ("foo", "bar")),
        (Map({"foo": String("bar")}), Map(
            {"foo": String("baz")}), ("foo", "baz")),
        (Map({"foo": String("foz")}), Map(
            {"bar": String("baz")}), ("foo", "foz")),
        (Map({"foo": String("foz")}), Map(
            {"bar": String("baz")}), ("bar", "baz")),
    ]
)
def test_can_get_merged_children(underlay, overlay, expected):
    t = MergedLayer().apply(underlay, overlay)
    assert t.value[expected[0]].value == expected[1]



@pytest.mark.parametrize(
    "underlay, overlay, expected",
    [
        (Null(), List([String("foo")]), (0, "foo")),
        (List(), List([String("foo")]), (0, "foo")),
        (List([String("foo")]), Null(), (0, "foo")),
        (List([String("foo")]), List(), (0, "foo")),
        (List([String("foo")]), List([String("bar")]), (0, "foo")),
        (List([String("foo")]), List([String("bar")]), (1, "bar")),
    ]
)
def test_can_get_merged_children(underlay, overlay, expected):
    t = MergedLayer().apply(underlay, overlay)
    assert t.value[expected[0]].value == expected[1]
