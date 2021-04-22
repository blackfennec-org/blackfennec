import unittest
import logging

from doubles.double_dummy import Dummy
from doubles.navigation.double_navigation_service import NavigationServiceMock
from src.visualisation.main_window.black_fennec_view_model import BlackFennecViewModel


class BlackFennecViewModelTestSuite(unittest.TestCase):
    def test_can_open_file(self):
        navigation_service = NavigationServiceMock()
        view_model = BlackFennecViewModel(Dummy(), navigation_service)
        view_model.open('examples/black_fennec.json')
        self.assertEqual(1, navigation_service.navigation_count)

    def test_can_create_new_file(self):
        view_model = BlackFennecViewModel(Dummy(), Dummy())
        with self.assertLogs(None, logging.WARNING):
            view_model.new()

    def test_can_quit_application(self):
        view_model = BlackFennecViewModel(Dummy(), Dummy())
        with self.assertLogs(None, logging.WARNING):
            view_model.quit()

    def test_can_save_file(self):
        view_model = BlackFennecViewModel(Dummy(), Dummy())
        with self.assertLogs(None, logging.WARNING):
            view_model.save()

    def test_can_save_as_file(self):
        view_model = BlackFennecViewModel(Dummy(), Dummy())
        with self.assertLogs(None, logging.WARNING):
            view_model.save_as()

    def test_can_go_to_store(self):
        view_model = BlackFennecViewModel(Dummy(), Dummy())
        with self.assertLogs(None, logging.WARNING):
            view_model.go_to_store()

    def test_can_go_to_about_and_help(self):
        view_model = BlackFennecViewModel(Dummy(), Dummy())
        with self.assertLogs(None, logging.WARNING):
            view_model.about_and_help()

    def test_presenter_getter(self):
        presenter = Dummy('Presenter')
        view_model = BlackFennecViewModel(presenter, Dummy())
        self.assertEqual(
            view_model.presenter,
            presenter
        )
