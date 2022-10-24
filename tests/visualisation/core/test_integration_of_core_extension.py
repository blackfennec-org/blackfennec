import pytest

from doubles.double_dummy import Dummy

from src.black_fennec.interpretation.interpretation_service import InterpretationService
from src.black_fennec.type_system.type_registry import TypeRegistry
from src.visualisation.view_factory import ViewFactory
from src.visualisation.view_factory_registry import ViewFactoryRegistry
from src.extension.extension_api import ExtensionApi
from src.visualisation.core import create_extension, destroy_extension
from src.black_fennec.structure.boolean import Boolean
from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.reference import Reference
from src.black_fennec.structure.string import String
from src.visualisation.core.boolean.boolean_view import BooleanView
from src.visualisation.core.list.list_view import ListView
from src.visualisation.core.map.map_view import MapView
from src.visualisation.core.number.number_view import NumberView

# from src.visualisation.core.reference.reference_view import ReferenceView
from src.visualisation.core.string.string_view import StringView

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
        presenter_registry=Dummy("PresenterRegistry"),
        type_registry=type_registry,
        interpretation_service=interpreter,
        view_factory=view_factory,
        view_factory_registry=view_factory_registry,
        type_loader=Dummy('TypeLoader'),
    )


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
    interpretation = interpreter.interpret(structure)
    view = view_factory.create(interpretation)
    assert isinstance(view, view_class)
