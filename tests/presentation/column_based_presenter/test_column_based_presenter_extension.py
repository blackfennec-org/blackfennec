import unittest

from doubles.double_dummy import Dummy
from doubles.presentation.double_presenter_registry import PresenterRegistryMock
from src.extension.extension_api import ExtensionApi
from src.presentation.column_based_presenter import create_extension, destroy_extension


class Column_based_presenterExtensionTestSuite(unittest.TestCase):
    def setUp(self) -> None:
        self.presenter_registry = PresenterRegistryMock()
        self.extension_api = ExtensionApi(
            type_registry=Dummy('typeRegistry'),
            presenter_registry=self.presenter_registry,
            interpretation_service=Dummy('InterpretationService')
        )

    def test_create_column_based_presenter_extension(self):
        create_extension(self.extension_api)
        self.assertGreater(self.presenter_registry.register_presenter_count, 0)

    def test_destroy_column_based_presenter_extension(self):
        destroy_extension(self.extension_api)
        self.assertGreater(self.presenter_registry.deregister_presenter_count, 0)

    def test_everything_created_is_destroyed(self):
        create_extension(self.extension_api)
        destroy_extension(self.extension_api)
        self.assertEqual(
            self.presenter_registry.register_presenter_count,
            self.presenter_registry.deregister_presenter_count
        )
