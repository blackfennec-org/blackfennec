"""type-registry Tests.

This module contains the unit-tests of the type-registry."""

import unittest

from doubles.dummy import Dummy
from src.type_system.type_registry import TypeRegistry


class ExtensionApiTestSuite(unittest.TestCase):
    def test_create_type_registry(self):
        type_registry = TypeRegistry()
        self.assertIsInstance(type_registry.types, list)

    def test_register_view(self):
        type_registry = TypeRegistry()
        type_bidder = Dummy()
        type_registry.register_type(type_bidder)

        self.assertIn(type_bidder, type_registry.types)

    def test_deregister_view(self):
        type_registry = TypeRegistry()
        type_bidder = Dummy()
        type_registry.types.append(type_bidder)
        type_registry.deregister_type(type_bidder)

        self.assertNotIn(type_bidder, type_registry.types)
