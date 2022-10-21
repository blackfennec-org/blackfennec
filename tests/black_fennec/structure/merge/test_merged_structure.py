import pytest
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.merge.merged_structure import MergedStructure
from src.black_fennec.structure.null import Null
from src.black_fennec.structure.string import String


@pytest.mark.parametrize(
    "underlay, overlay, expected",
    [
        (None, String("overlay"), "overlay"),
        (String("underlay"), None, "underlay"),
        (String("underlay"), String("overlay"), "overlay"),
    ],
)
def test_can_get_value(underlay, overlay, expected):
    t = MergedStructure(underlay, overlay)
    assert t.value == expected

def test_cannot_set_value():
    t = MergedStructure(None, None)
    with pytest.raises(AssertionError):
        t.value = "foo"

def test_cannot_set_parent():
    t = MergedStructure(None, None)
    with pytest.raises(AssertionError):
        t.parent = t

def test_repr():
    t = MergedStructure(None, None)
    assert repr(t).startswith("MergedStructure")

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
        (map_chain("underlay", 0), map_chain("overlay", 0), None),
        (map_chain("underlay", 0), map_chain("overlay", 1), "overlay"),
        (map_chain("underlay", 1), map_chain("overlay", 0), "underlay"),
        (map_chain("underlay", 1), map_chain("overlay", 1), "overlay"),

    ],
)
def test_can_get_parent(underlay, overlay, expected):
    merged = MergedStructure(underlay, overlay)
    if merged.parent:
        actual = merged.parent.value["layer"].value
    else:
        actual = None
    assert actual == expected


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
        actual = None
    assert actual == expected