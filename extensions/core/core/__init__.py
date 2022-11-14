from blackfennec.extension.extension_api import ExtensionApi
from blackfennec.interpretation.specification import Specification
from blackfennec.type_system.boolean_type import BooleanType
from blackfennec.type_system.list_type import ListType
from blackfennec.type_system.map_type import MapType
from blackfennec.type_system.number_type import NumberType
from blackfennec.type_system.reference_type import ReferenceType
from blackfennec.type_system.string_type import StringType

import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from core.boolean.boolean_view_factory import BooleanViewFactory
from core.column_based_presenter.column_based_presenter_view_factory import \
    ColumnBasedPresenterViewFactory
from core.list.list_view_factory import ListViewFactory
from core.map.map_view_factory import MapViewFactory
from core.number.number_view_factory import NumberViewFactory
from core.reference.reference_view_factory import ReferenceViewFactory
from core.string.string_view_factory import StringViewFactory


class CoreTypes:
    """Contains all core types in black-fennec

    Attributes:
        boolean (BooleanType): boolean type
        number (NumberType): number type
        string (StringType): string type
        list (ListType): list type
        map (MapType): map type
        reference (ReferenceType): reference type
    """
    boolean = BooleanType()
    number = NumberType()
    string = StringType()
    list = ListType()
    map = MapType()
    reference = ReferenceType()

    def register(self, type_registry):
        type_registry.register_type(self.boolean)
        type_registry.register_type(self.number)
        type_registry.register_type(self.string)
        type_registry.register_type(self.list)
        type_registry.register_type(self.map)
        type_registry.register_type(self.reference)

    def deregister(self, type_registry):
        type_registry.deregister_type(self.boolean)
        type_registry.deregister_type(self.number)
        type_registry.deregister_type(self.string)
        type_registry.deregister_type(self.list)
        type_registry.deregister_type(self.map)
        type_registry.deregister_type(self.reference)


class CoreExtension:
    def __init__(self):
        self._is_setup = False
        self._is_registered = False
        self.types = CoreTypes()
        self.view_factories = dict()
        self.actions = []

    def setup(self, extension_api: ExtensionApi):
        self.view_factories = {
            self.types.boolean: BooleanViewFactory(),
            self.types.number: NumberViewFactory(),
            self.types.string: StringViewFactory(),
            self.types.list: ListViewFactory(
                extension_api.interpretation_service,
                extension_api.type_registry,
                extension_api.action_registry,
                extension_api.view_factory
            ),
            self.types.map: MapViewFactory(
                extension_api.interpretation_service,
                extension_api.type_registry,
                extension_api.action_registry,
                extension_api.view_factory,
            ),
            self.types.reference: ReferenceViewFactory(),
        }

        from core.string.actions.to_upper import ToUpperAction
        from core.string.actions.to_lower import ToLowerAction
        from core.number.actions.to_integer import ToIntegerAction
        from core.map.actions.delete_items import DeleteMapItemsAction
        self.actions = [
            ToUpperAction(),
            ToLowerAction(),
            ToIntegerAction(),
            DeleteMapItemsAction(),
        ]

    def register(self, extension_api: ExtensionApi):
        self.setup(extension_api)

        self.types.register(extension_api.type_registry)

        extension_api.presenter_registry.register_presenter(
            ColumnBasedPresenterViewFactory(
                extension_api.interpretation_service,
                extension_api.view_factory))

        for type, factory in self.view_factories.items():
            extension_api.view_factory_registry.register_view_factory(
                type, Specification(), factory)
            extension_api.view_factory_registry.register_view_factory(
                type, Specification(True), factory)

        for action in self.actions:
            extension_api.action_registry.register_action(action)

    def deregister(self, extension_api: ExtensionApi):
        self.types.deregister(extension_api.type_registry)

        extension_api.presenter_registry.deregister_presenter(
            ColumnBasedPresenterViewFactory
        )

        for type, _ in self.view_factories.items():
            extension_api.view_factory_registry.deregister_view_factory(
                type, Specification())
            extension_api.view_factory_registry.deregister_view_factory(
                type, Specification(True))

        for action in self.actions:
            extension_api.action_registry.deregister_action(action)


CORE_EXTENSION = CoreExtension()


def create_extension(extension_api: ExtensionApi):
    """Registers all core types in black-fennec

    Args:
        extension_api (ExtensionApi): contains constructor injection
            parameters.
    """
    CORE_EXTENSION.register(extension_api)


def destroy_extension(extension_api: ExtensionApi):
    """Deregisters all core types from black-fennec

    Args:
        extension_api (ExtensionApi): contains constructor injection
            parameters
    """
    CORE_EXTENSION.deregister(extension_api)
