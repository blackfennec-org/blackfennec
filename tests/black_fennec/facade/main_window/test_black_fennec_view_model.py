import unittest
import logging
from uri import URI

from doubles.double_dummy import Dummy
from doubles.black_fennec.interpretation.double_interpretation_service import InterpretationServiceMock
from doubles.presentation.double_presenter_factory import PresenterFactoryMock
from doubles.black_fennec.util.uri.double_uri_import_service import UriImportServiceMock
from src.black_fennec.facade.main_window.black_fennec_view_model import BlackFennecViewModel


class BlackFennecViewModelTestSuite(unittest.TestCase):
    def test_can_open_file(self):
        presenter_factory = PresenterFactoryMock()
        interpretation_service = InterpretationServiceMock(Dummy())
        uri_import_service = UriImportServiceMock()
        view_model = BlackFennecViewModel(
            presenter_factory, interpretation_service, uri_import_service)
        view_model.open(URI('/examples/black_fennec.json'))
        self.assertEqual(1, presenter_factory.create_call_count)
        self.assertEqual(1, uri_import_service.load_count)

    def test_can_create_new_file(self):
        view_model = BlackFennecViewModel(Dummy(), Dummy(), Dummy())
        with self.assertLogs(None, logging.WARNING):
            view_model.new()

    def test_can_quit_application(self):
        view_model = BlackFennecViewModel(Dummy(), Dummy(), Dummy())
        with self.assertLogs(None, logging.WARNING):
            view_model.quit()

    def test_can_save_file(self):
        view_model = BlackFennecViewModel(Dummy(), Dummy(), Dummy())
        view_model.save()

    def test_can_save_as_file(self):
        view_model = BlackFennecViewModel(Dummy(), Dummy(), Dummy())
        with self.assertLogs(None, logging.WARNING):
            view_model.save_as()

    def test_can_go_to_store(self):
        view_model = BlackFennecViewModel(Dummy(), Dummy(), Dummy())
        with self.assertLogs(None, logging.WARNING):
            view_model.go_to_store()

    def test_can_go_to_about_and_help(self):
        view_model = BlackFennecViewModel(Dummy(), Dummy(), Dummy())
        with self.assertLogs(None, logging.WARNING):
            view_model.about_and_help()

    def test_presenter_getter(self):
        presenter_factory = Dummy('Presenter')
        view_model = BlackFennecViewModel(presenter_factory, Dummy(), Dummy())
        self.assertEqual(
            view_model._presenter_factory,
            presenter_factory
        )
