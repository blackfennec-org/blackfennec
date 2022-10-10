import unittest
from doubles.double_dummy import Dummy
from doubles.visualisation.double_view_factory_registry import ViewFactoryRegistryMock
from doubles.black_fennec.type_system.double_type_registry import TypeRegistryMock

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


class CoreExtensionTestSuite(unittest.TestCase):
    def setUp(self) -> None:
        self.type_registry = TypeRegistryMock()
        self.view_factory_registry = ViewFactoryRegistryMock()
        self.extension_api = ExtensionApi(
            presenter_registry=Dummy("PresenterRegistry"),
            type_registry=self.type_registry,
            interpretation_service=Dummy("InterpretationService"),
            view_factory=Dummy("ViewFactory"),
            view_factory_registry=self.view_factory_registry,
            type_loader=Dummy('TypeLoader'),
        )

    def test_create_core_extension(self):
        create_extension(self.extension_api)
        self.assertGreater(self.type_registry.register_type_count, 0)

    def test_destroy_core_extension(self):
        destroy_extension(self.extension_api)
        self.assertGreater(self.type_registry.deregister_type_count, 0)

    def test_everything_created_is_destroyed(self):
        create_extension(self.extension_api)
        destroy_extension(self.extension_api)
        self.assertEqual(
            self.type_registry.register_type_count,
            self.type_registry.deregister_type_count,
        )