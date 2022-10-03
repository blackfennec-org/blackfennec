import pytest

from doubles.black_fennec.interpretation.double_interpretation import InterpretationMock
from doubles.black_fennec.structure.double_reference import ReferenceMock, ReferenceInstanceMock
from doubles.black_fennec.structure.double_structure import StructureMock
from doubles.black_fennec.structure.reference_navigation.double_navigation import NavigatorMock
from src.visualisation.core.reference.reference_view_model import ReferenceViewModel


@pytest.fixture()
def structure():
    return StructureMock()


@pytest.fixture()
def interpretation(structure):
    return InterpretationMock(
        ReferenceInstanceMock(
            [NavigatorMock(navigate_return=structure)]
        )
    )


@pytest.fixture()
def reference_view_model(interpretation):
    return ReferenceViewModel(interpretation)


def test_can_construct(reference_view_model):
    assert isinstance(reference_view_model, ReferenceViewModel)


def test_wrong_instance_in_interpretation(reference_view_model):
    interpretation = InterpretationMock(ReferenceMock())
    with pytest.raises(TypeError):
        ReferenceViewModel(interpretation)


def test_can_get_reference(reference_view_model, interpretation):
    assert reference_view_model.reference == interpretation.structure


def test_can_forward_navigation_request(reference_view_model, interpretation, structure):
    reference_view_model.navigate_to_reference()
    assert interpretation.navigation_requests == [structure]
