import pytest

from blackfennec_doubles.double_dummy import Dummy
from blackfennec_doubles.interpretation.double_interpretation import InterpretationMock
from blackfennec_doubles.interpretation.double_interpretation_service import InterpretationServiceMock
from blackfennec_doubles.structure.double_list import ListMock, ListInstanceMock
from blackfennec_doubles.type_system.double_type_registry import TypeRegistryMock
from blackfennec.interpretation.specification import Specification
from core.list.list_preview import ListPreview
from core.list.list_view import ListView
from core.list.list_view_factory import ListViewFactory


@pytest.fixture
def factory():
    return ListViewFactory(
        InterpretationServiceMock([]),
        TypeRegistryMock(),
        Dummy('ViewFactory'))

def test_can_construct(factory):
    assert isinstance(factory, ListViewFactory)

def test_can_create_list_view(factory):
    view = factory.create(
        InterpretationMock(ListInstanceMock()))
    assert isinstance(view, ListView)

def test_can_create_list_preview(factory):
    view = factory.create(
        InterpretationMock(
            ListInstanceMock(), 
            specification=Specification(request_preview=True)))
    assert isinstance(view, ListPreview)

def test_satisfies_default(factory):
    satisfies = factory.satisfies(Specification())
    assert satisfies

def test_does_satisfy_preview(factory):
    satisfies = factory.satisfies(Specification(request_preview=True))
    assert satisfies
