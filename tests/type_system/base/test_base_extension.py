import unittest

from doubles.double_dummy import Dummy
from doubles.type_system.double_type_registry import TypeRegistryMock
from src.extension.extension_api import ExtensionApi
from src.type_system.base import create_extension, destroy_extension


class BaseExtensionTestSuite(unittest.TestCase):
    def setUp(self) -> None:
        self.type_registry = TypeRegistryMock()
        self.extension_api = ExtensionApi(
            type_registry=self.type_registry,
            presenter_registry=Dummy('PresenterRegistry'),
            interpretation_service=Dummy('InterpretationService'),
            navigation_service=Dummy('NavigationService')
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
