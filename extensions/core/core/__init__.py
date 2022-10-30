from blackfennec.extension.extension_api import ExtensionApi
from blackfennec.interpretation.specification import Specification
from blackfennec.structure.type.boolean_type import BooleanType
from blackfennec.structure.type.list_type import ListType
from blackfennec.structure.type.map_type import MapType
from blackfennec.structure.type.number_type import NumberType
from blackfennec.structure.type.reference_type import ReferenceType
from blackfennec.structure.type.string_type import StringType

from core.boolean.boolean_view_factory import BooleanViewFactory
from core.column_based_presenter.column_based_presenter_view_factory import \
    ColumnBasedPresenterViewFactory
from core.list.list_view_factory import ListViewFactory
from core.map.map_view_factory import MapViewFactory
from core.number.number_view_factory import NumberViewFactory
from core.reference.reference_view_factory import ReferenceViewFactory
from core.string.string_view_factory import StringViewFactory

__types = []

def _types(extension_api):
    global __types
    if not __types:
        __types = [
            (BooleanType(), BooleanViewFactory()),
            (NumberType(), NumberViewFactory()),
            (StringType(), StringViewFactory()),
            (
                ListType(),
                ListViewFactory(
                    extension_api.interpretation_service, extension_api.type_registry,
                    extension_api.view_factory
                )
            ),
            (
                MapType(),
                MapViewFactory(
                    extension_api.interpretation_service, extension_api.type_registry,
                    extension_api.view_factory
                )
            ),
            (ReferenceType(), ReferenceViewFactory()),
        ]
    return __types

def create_extension(extension_api: ExtensionApi):
    """Registers all core types in black-fennec

    Args:
        extension_api (ExtensionApi): contains constructor injection
            parameters.
    """
    extension_api.presenter_registry.register_presenter(
        ColumnBasedPresenterViewFactory(
            extension_api.interpretation_service,
            extension_api.view_factory))
    
    types = _types(extension_api)

    for type, factory in types:
        extension_api.type_registry.register_type(type)
        extension_api.view_factory_registry.register_view_factory(
            type, Specification(), factory)
        extension_api.view_factory_registry.register_view_factory(
            type, Specification(True), factory)


def destroy_extension(extension_api: ExtensionApi):
    """Deregisters all core types from black-fennec

    Args:
        extension_api (ExtensionApi): contains constructor injection
            parameters
    """
    extension_api.presenter_registry.deregister_presenter(
        ColumnBasedPresenterViewFactory
    )
    types = _types(extension_api)

    for type, unused_factories in types:
        extension_api.type_registry.deregister_type(type)
        extension_api.view_factory_registry.deregister_view_factory(
            type, Specification())
        extension_api.view_factory_registry.deregister_view_factory(
            type, Specification(True))
