import unittest
import logging

from doubles.dummy import Dummy
from src.black_fennec_view_model import BlackFennecViewModel


class BlackFennecViewModelTestSuite(unittest.TestCase):
    def test_can_open_file(self):
        view_model = BlackFennecViewModel(Dummy())
        with self.assertLogs(None, logging.WARNING):
            view_model.open()

    def test_can_create_new_file(self):
        view_model = BlackFennecViewModel(Dummy())
        with self.assertLogs(None, logging.WARNING):
            view_model.new()

    def test_can_quit_application(self):
        view_model = BlackFennecViewModel(Dummy())
        with self.assertLogs(None, logging.WARNING):
            view_model.quit()

    def test_can_save_file(self):
        view_model = BlackFennecViewModel(Dummy())
        with self.assertLogs(None, logging.WARNING):
            view_model.save()

    def test_can_save_as_file(self):
        view_model = BlackFennecViewModel(Dummy())
        with self.assertLogs(None, logging.WARNING):
            view_model.save_as()

    def test_can_go_to_store(self):
        view_model = BlackFennecViewModel(Dummy())
        with self.assertLogs(None, logging.WARNING):
            view_model.go_to_store()

    def test_can_go_to_about_and_help(self):
        view_model = BlackFennecViewModel(Dummy())
        with self.assertLogs(None, logging.WARNING):
            view_model.about_and_help()




