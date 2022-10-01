import unittest

from doubles.double_dummy import Dummy
from doubles.black_fennec.type_system.double_type_registry import TypeRegistryMock
from doubles.visualisation.double_view_factory_registry import ViewFactoryRegistryMock
from src.extension.extension_api import ExtensionApi
from src.visualisation.base import create_extension, destroy_extension


class BaseExtensionTestSuite(unittest.TestCase):
    def setUp(self) -> None:
        self.type_registry = TypeRegistryMock()
        self.view_factory_registry = ViewFactoryRegistryMock()
        self.extension_api = ExtensionApi(
            presenter_registry=Dummy('PresenterRegistry'),
            type_registry=self.type_registry,
            template_registry=Dummy('TemplateRegistry'),
            interpretation_service=Dummy('InterpretationService'),
            view_factory=Dummy('ViewFactory'),
            view_factory_registry=self.view_factory_registry
        )

    def test_create_base_extension(self):
        create_extension(self.extension_api)
        self.assertGreater(self.type_registry.register_type_count, 0)

    def test_destroy_base_extension(self):
        destroy_extension(self.extension_api)
        self.assertGreater(self.type_registry.deregister_type_count, 0)

    def test_everything_created_is_destroyed(self):
        create_extension(self.extension_api)
        destroy_extension(self.extension_api)
        self.assertEqual(
            self.type_registry.register_type_count,
            self.type_registry.deregister_type_count
        )
