from src.extension.extension_api import ExtensionApi
from src.black_fennec.structure.type.boolean_type import BooleanType
from src.visualisation.core.boolean.boolean_view_factory import BooleanViewFactory
from src.black_fennec.structure.type.list_type import ListType
from src.visualisation.core.list.list_view_factory import ListViewFactory
from src.black_fennec.structure.type.map_type import MapType
from src.visualisation.core.map.map_view_factory import MapViewFactory
from src.black_fennec.structure.type.number_type import NumberType
from src.visualisation.core.number.number_view_factory import NumberViewFactory
from src.black_fennec.structure.type.reference_type import ReferenceType
from src.visualisation.core.reference.reference_view_factory import ReferenceViewFactory
from src.black_fennec.structure.type.string_type import StringType
from src.visualisation.core.string.string_view_factory import StringViewFactory
from src.black_fennec.interpretation.specification import Specification

types = []


def create_extension(extension_api: ExtensionApi):
    """
    Registers all core types in black-fennec
    Args:
        extension_api (ExtensionApi): contains constructor injection
            parameters.
    """
    global types
    types = [
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

    for type, factory in types:
        extension_api.type_registry.register_type(type)
        extension_api.view_factory_registry.register_view_factory(
            type, Specification(), factory)
        extension_api.view_factory_registry.register_view_factory(
            type, Specification(True), factory)


def destroy_extension(extension_api: ExtensionApi):
    """
    Deregisters all core types from black-fennec
    Args:
        extension_api (ExtensionApi): contains constructor injection
            parameters
    """

    for type, unused_factories in types:
        extension_api.type_registry.deregister_type(type)
        extension_api.view_factory_registry.deregister_view_factory(
            type, Specification())
        extension_api.view_factory_registry.deregister_view_factory(
            type, Specification(True))
