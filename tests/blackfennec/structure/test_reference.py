import pytest

from blackfennec_doubles.structure.double_structure import StructureMock
from blackfennec_doubles.structure.reference_navigation.double_navigation import NavigatorMock
from blackfennec.structure.reference import Reference
from tests.test_utils.observer import Observer


@pytest.fixture()
def structure():
    return StructureMock()


@pytest.fixture()
def navigator(structure):
    return NavigatorMock(navigate_return=structure)


@pytest.fixture()
def reference(navigator):
    return Reference([navigator])


def test_can_construct(reference):
    assert isinstance(reference, Reference)


def test_resolve(reference, navigator, structure):
    assert reference.resolve() == structure
    assert navigator.navigate_count == 1
    assert navigator.navigate_parameter_current_structure == reference


def test_can_set_value(reference, navigator):
    reference.value = navigator
    assert reference.value == navigator


def test_notifies_on_value_change(reference, navigator):
    observer = Observer()
    reference.bind(changed=observer.endpoint)
    reference.value = navigator
    assert observer.last_call[0][1].new_value == navigator
    assert observer.last_call[0][1].old_value == [navigator]
