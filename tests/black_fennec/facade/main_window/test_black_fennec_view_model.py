import unittest
import logging
from uri import URI

from doubles.double_dummy import Dummy
from doubles.black_fennec.interpretation.double_interpretation_service import InterpretationServiceMock
from doubles.extension.double_extension_source_registry import ExtensionSourceRegistryMock
from doubles.presentation.double_presenter_factory import PresenterFactoryMock
from doubles.black_fennec.util.uri.double_uri_import_service import UriImportServiceMock
from src.black_fennec.facade.extension_store.extension_store_view_model import ExtensionStoreViewModel
from src.black_fennec.facade.main_window.black_fennec_view_model import BlackFennecViewModel


class BlackFennecViewModelTestSuite(unittest.TestCase):
    def setUp(self) -> None:
        self.presenter_factory = PresenterFactoryMock()
        self.interpretation_service = InterpretationServiceMock(Dummy())
        self.uri_import_service = UriImportServiceMock()
        self.extension_api = Dummy()
        self.extension_source_registry = ExtensionSourceRegistryMock()
        self.view_model = BlackFennecViewModel(
            self.presenter_factory,
            self.interpretation_service,
            self.uri_import_service,
            self.extension_api,
            self.extension_source_registry)

    def test_can_open_file(self):
        self.view_model.open(URI('/examples/black_fennec.json'))
        self.assertEqual(1, self.presenter_factory.create_call_count)
        self.assertEqual(1, self.uri_import_service.load_count)

    def test_can_create_new_file(self):
        with self.assertLogs(None, logging.WARNING):
            self.view_model.new()

    def test_can_quit_application(self):
        with self.assertLogs(None, logging.WARNING):
            self.view_model.quit()

    def test_can_save_file(self):
        with self.assertLogs(None, logging.WARNING):
            self.view_model.save()

    def test_can_save_as_file(self):
        with self.assertLogs(None, logging.WARNING):
            self.view_model.save_as()

    def test_can_create_extension_store(self):
        extension_store_view_model = self.view_model.create_extension_store()
        self.assertIsInstance(extension_store_view_model, ExtensionStoreViewModel)

    def test_can_go_to_about_and_help(self):
        with self.assertLogs(None, logging.WARNING):
            self.view_model.about_and_help()

    def test_presenter_getter(self):
        self.assertEqual(
            self.view_model._presenter_factory,
            self.presenter_factory
        )
