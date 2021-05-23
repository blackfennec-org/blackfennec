import unittest

from doubles.black_fennec.type_system.double_template_registry import TemplateRegistryMock
from doubles.double_dummy import Dummy
from doubles.black_fennec.type_system.double_type_registry import TypeRegistryMock
from src.extension.extension_api import ExtensionApi
from src.visualisation.core import create_extension, destroy_extension


class CoreExtensionTestSuite(unittest.TestCase):
    def setUp(self) -> None:
        self.type_registry = TypeRegistryMock()
        self.template_registry = TemplateRegistryMock()
        self.extension_api = ExtensionApi(
            presenter_registry=Dummy('PresenterRegistry'),
            type_registry=self.type_registry,
            template_registry=self.template_registry,
            interpretation_service=Dummy('InterpretationService')
        )

    def test_create_core_extension(self):
        create_extension(self.extension_api)
        self.assertGreater(self.type_registry.register_type_count, 0)
        self.assertGreater(self.template_registry.register_template_count, 0)

    def test_destroy_core_extension(self):
        destroy_extension(self.extension_api)
        self.assertGreater(self.type_registry.deregister_type_count, 0)
        self.assertGreater(self.template_registry.deregister_template_count, 0)

    def test_everything_created_is_destroyed(self):
        create_extension(self.extension_api)
        destroy_extension(self.extension_api)
        self.assertEqual(
            self.type_registry.register_type_count,
            self.type_registry.deregister_type_count
        )
        self.assertEqual(
            self.template_registry.register_template_count,
            self.template_registry.deregister_template_count
        )
