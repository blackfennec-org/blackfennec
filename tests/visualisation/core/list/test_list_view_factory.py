import pytest

from doubles.double_dummy import Dummy
from doubles.black_fennec.interpretation.double_interpretation import InterpretationMock
from doubles.black_fennec.interpretation.double_interpretation_service import InterpretationServiceMock
from doubles.black_fennec.structure.double_list import ListMock, ListInstanceMock
from doubles.black_fennec.type_system.double_template_registry import TemplateRegistryMock
from src.black_fennec.interpretation.specification import Specification
from src.visualisation.core.list.list_preview import ListPreview
from src.visualisation.core.list.list_view import ListView
from src.visualisation.core.list.list_view_factory import ListViewFactory


@pytest.fixture
def factory():
    return ListViewFactory(
        InterpretationServiceMock([]),
        TemplateRegistryMock(),
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
