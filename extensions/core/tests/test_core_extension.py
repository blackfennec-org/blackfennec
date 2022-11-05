import unittest
from blackfennec_doubles.double_dummy import Dummy
from blackfennec_doubles.extension.double_view_factory_registry import ViewFactoryRegistryMock
from blackfennec_doubles.extension.double_presenter_registry import PresenterRegistryMock
from blackfennec_doubles.type_system.double_type_registry import TypeRegistryMock
from blackfennec_doubles.actions.double_action_registry import ActionRegistryMock

from blackfennec.extension.extension_api import ExtensionApi
from core import create_extension, destroy_extension



class CoreExtensionTestSuite(unittest.TestCase):
    def setUp(self) -> None:
        self.type_registry = TypeRegistryMock()
        self.view_factory_registry = ViewFactoryRegistryMock()
        self.extension_api = ExtensionApi(
            presenter_registry=PresenterRegistryMock(),
            type_registry=self.type_registry,
            interpretation_service=Dummy("InterpretationService"),
            view_factory=Dummy("ViewFactory"),
            view_factory_registry=self.view_factory_registry,
            type_loader=Dummy('TypeLoader'),
            action_registry=ActionRegistryMock(),
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