import pytest

from blackfennec.layers.overlay.overlay import Overlay

from blackfennec.structure.map import Map
from blackfennec.structure.reference import Reference
from blackfennec.structure.string import String

from blackfennec.structure.reference_navigation.parent_navigator import ParentNavigator
from blackfennec.structure.reference_navigation.child_navigator import ChildNavigator

@pytest.fixture
def layer():
    return Overlay()

def test_can_resolve_double_reference(layer):
    map = Map({
        "a": Reference([ ParentNavigator(), ChildNavigator("b"), ChildNavigator("c") ]),
        "b": Map({
            "c": Reference([ ParentNavigator(), ChildNavigator("d") ]),
            "d": String("value"),
        })
    })
    overlay = layer.apply(map)

    assert overlay.value["a"].value == "value"
