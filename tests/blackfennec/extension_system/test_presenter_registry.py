"""presenter-registrydef setUp(self):
        self.structure_type_name = 'Boolean'
        self.default_value = False
        self.alternative_value = True

    def create_structure(self, value):
        return Boolean(value) Tests.

This module contains the unit-tests of the presenter-registry."""

import unittest

from blackfennec_doubles.double_dummy import Dummy
from blackfennec.presentation_system.presenter_registry import PresenterRegistry


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
        presenter_registry.deregister_presenter(Dummy)

        self.assertNotIn(presenter_bidder, presenter_registry.presenters)
