"""presenter-registry Tests.

This module contains the unit-tests of the presenter-registry."""

import unittest

from doubles.double_dummy import Dummy
from src.presentation.presenter_registry import PresenterRegistry


class PresenterRegistryTestSuite(unittest.TestCase):
    def test_create_presenter_registry(self):
        presenter_registry = PresenterRegistry()
        self.assertIsInstance(presenter_registry.presenters, list)

    def test_register_view(self):
        presenter_registry = PresenterRegistry()
        presenter_bidder = Dummy()
        presenter_registry.register_presenter(presenter_bidder)

        self.assertIn(presenter_bidder, presenter_registry.presenters)

    def test_deregister_view(self):
        presenter_registry = PresenterRegistry()
        presenter_bidder = Dummy()
        presenter_registry.presenters.append(presenter_bidder)
        presenter_registry.deregister_presenter(presenter_bidder)

        self.assertNotIn(presenter_bidder, presenter_registry.presenters)
