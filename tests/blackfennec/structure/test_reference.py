import pytest

from blackfennec_doubles.structure.double_structure import StructureMock
from blackfennec_doubles.structure.reference_navigation.double_navigation import NavigatorMock
from blackfennec.structure.reference import Reference


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
