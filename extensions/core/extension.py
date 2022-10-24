from blackfennec.extension.extension_api import ExtensionApi
from blackfennec.structure.type.boolean_type import BooleanType
from core.boolean.boolean_view_factory import BooleanViewFactory
from blackfennec.structure.type.list_type import ListType
from core.list.list_view_factory import ListViewFactory
from blackfennec.structure.type.map_type import MapType
from core.map.map_view_factory import MapViewFactory
from blackfennec.structure.type.number_type import NumberType
from core.number.number_view_factory import NumberViewFactory
from blackfennec.structure.type.reference_type import ReferenceType
from core.reference.reference_view_factory import ReferenceViewFactory
from blackfennec.structure.type.string_type import StringType
from core.string.string_view_factory import StringViewFactory
from blackfennec.interpretation.specification import Specification

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
    types = _types(extension_api)

    for type, unused_factories in types:
        extension_api.type_registry.deregister_type(type)
        extension_api.view_factory_registry.deregister_view_factory(
            type, Specification())
        extension_api.view_factory_registry.deregister_view_factory(
            type, Specification(True))
