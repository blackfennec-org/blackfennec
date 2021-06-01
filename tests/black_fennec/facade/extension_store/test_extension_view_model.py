import unittest

from doubles.double_dummy import Dummy
from doubles.extension.double_extension import ExtensionMock
from src.black_fennec.facade.extension_store.extension_view_model import ExtensionViewModel


class ExtensionViewModelTestSuite(unittest.TestCase):
    def setUp(self) -> None:
        self.name = 'name'
        self.description = 'description'
        self.enabled = True
        self.extension = ExtensionMock()
        self.extension.name = self.name
        self.extension.location = self.description
        self.extension.enabled = self.enabled

        self.extension_api = Dummy()

        self.view_model: ExtensionViewModel = ExtensionViewModel(
            self.extension,
            self.extension_api
        )

    def tearDown(self) -> None:
        self.extension = None
        self.extension_api = None
        self.view_model: ExtensionViewModel = None

    def test_can_construct(self):
        self.assertIsNotNone(self.view_model)

    def test_name_getter(self):
        self.assertEqual(self.name, self.view_model.name)
        
    def test_description_getter(self):
        self.assertEqual(self.description, self.view_model.description)
        
    def test_enabled_getter(self):
        self.assertEqual(self.enabled, self.view_model.enabled)

    def test_enable(self):
        self.view_model.enable()
        self.assertEqual(self.extension.load_count, 1)

    def test_disable(self):
        self.view_model.disable()
        self.assertEqual(self.extension.unload_count, 1)
