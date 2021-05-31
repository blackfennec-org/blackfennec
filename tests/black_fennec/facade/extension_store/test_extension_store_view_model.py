import unittest

from doubles.double_dummy import Dummy
from doubles.extension.double_extension_source import ExtensionSourceMock
from doubles.extension.double_extension_source_registry import ExtensionSourceRegistryMock
from src.black_fennec.facade.extension_store.extension_store_view_model import ExtensionStoreViewModel


class ExtensionStoreViewModelTestSuite(unittest.TestCase):
    def setUp(self) -> None:
        self.extension_source_registry = ExtensionSourceRegistryMock()
        self.extension = Dummy('Extension')
        self.extension_source = ExtensionSourceMock({self.extension})
        self.extension_source_registry.extension_sources.add(
            self.extension_source
        )

        self.extension_api = Dummy()

        self.view_model: ExtensionStoreViewModel = ExtensionStoreViewModel(
            self.extension_source_registry,
            self.extension_api
        )

    def tearDown(self) -> None:
        self.extension_source_registry = None
        self.extension_api = None
        self.view_model: ExtensionStoreViewModel = None

    def test_can_construct(self):
        self.assertIsNotNone(self.view_model)

    def test_extension_api_getter(self):
        self.assertEqual(self.view_model.extension_api, self.extension_api)

    def test_extensions_getter(self):
        self.assertIn(self.extension, self.view_model.extensions)

    def test_reload(self):
        self.view_model.reload_extensions()
        self.assertEqual(len(self.view_model.extensions), 1)

    def test_reload_extension_from_source(self):
        self.view_model.reload_extension_from_source()
        self.assertEqual(self.extension_source.refresh_extensions_count, 1)
