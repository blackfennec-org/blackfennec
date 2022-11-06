import pytest
from blackfennec.extension.extension_api import ExtensionApi
from blackfennec.extension.view_factory import ViewFactory
from blackfennec.extension.view_factory_registry import ViewFactoryRegistry
from blackfennec.interpretation.interpretation import Interpretation
from blackfennec.interpretation.specification import Specification
from blackfennec.interpretation.interpretation_service import \
    InterpretationService
from blackfennec.navigation.navigation_service import NavigationService
from blackfennec.structure.boolean import Boolean
from blackfennec.structure.list import List
from blackfennec.structure.map import Map
from blackfennec.structure.number import Number
from blackfennec.structure.reference import Reference
from blackfennec.structure.string import String
from blackfennec.type_system.type_registry import TypeRegistry
from blackfennec_doubles.double_dummy import Dummy
from blackfennec_doubles.extension.double_structure_presenter import \
    StructurePresenterMock
from blackfennec_doubles.extension.double_presenter_registry import PresenterRegistryMock
from blackfennec_doubles.type_system.double_type_registry import \
    TypeRegistryMock
from core.boolean.boolean_view import BooleanView
from core.list.list_view import ListView
from core.list.list_view_model import ListViewModel
from core.map.map_view import MapView
from core.map.map_view_model import MapViewModel
from core.number.number_view import NumberView
from core.string.string_view import StringView
from core import create_extension, destroy_extension

pytestmark = pytest.mark.integration

@pytest.fixture
def view_factory_registry():
    return ViewFactoryRegistry()


@pytest.fixture
def view_factory(view_factory_registry):
    return ViewFactory(view_factory_registry)


@pytest.fixture
def type_registry():
    return TypeRegistry()


@pytest.fixture
def interpreter(type_registry):
    return InterpretationService(type_registry)


@pytest.fixture
def api(type_registry, interpreter, view_factory, view_factory_registry):
    return ExtensionApi(
        presenter_registry=PresenterRegistryMock(),
        type_registry=type_registry,
        interpretation_service=interpreter,
        view_factory=view_factory,
        view_factory_registry=view_factory_registry,
        type_loader=Dummy('TypeLoader'),
    )


@pytest.fixture
def presenter():
    return StructurePresenterMock()

@pytest.fixture
def navigation_service(presenter):
    navigation_service = NavigationService()
    navigation_service.set_presenter(presenter)
    return navigation_service


@pytest.mark.parametrize(
    ["structure", "view_class"],
    [
        (Map(), MapView),
        (List(), ListView),
        # (Reference(Dummy()), ReferenceView),
        (String(), StringView),
        (Number(), NumberView),
        (Boolean(), BooleanView),
        # (Null(), NullView)
    ],
    ids=[
        "map",
        "list",
        # "reference",
        "string",
        "number",
        "boolean",
        # "null"
    ],
)
def test_integration_correct_interpretation(
    api, structure, interpreter, view_factory, view_class
):
    create_extension(api)
    interpretation = interpreter.interpret(structure, Specification())
    view = view_factory.create(interpretation)
    assert isinstance(view, view_class)


def test_map_can_navigate(presenter, navigation_service):
    structure = Map()
    interpretation = Interpretation(
        structure, Dummy('specification'), Dummy('factories'))
    interpretation.set_navigation_service(navigation_service)
    interpretation_service = Dummy('InterpretationService')
    type_registry = TypeRegistryMock()
    map_view_model = MapViewModel(
        interpretation,
        interpretation_service,
        type_registry)
    map_view_model.navigate_to(Map())
    assert presenter.show_count == 1


def test_list_can_navigate(presenter, navigation_service):
    structure = List()
    interpretation = Interpretation(
        structure, Dummy('specification'), Dummy('factories'))
    interpretation.set_navigation_service(navigation_service)
    interpretation_service = Dummy('InterpretationService')
    type_registry = Dummy('TypeRegistry')
    list_view_model = ListViewModel(
        interpretation,
        interpretation_service,
        type_registry
    )
    list_view_model.navigate_to(List())
    assert presenter.show_count == 1
