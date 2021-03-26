"""type-registry Tests.

This module contains the unit-tests of the type-registry."""

import unittest

from doubles.dummy import Dummy
from src.extension.type_registry import TypeRegistry


class ExtensionApiTestSuite(unittest.TestCase):
    def test_create_type_registry(self):
        type_registry = TypeRegistry()
        self.assertIsInstance(type_registry.types, dict)


    def test_register_view(self):
        type_registry = TypeRegistry()
        type_bidder = Dummy()
        type_view_factory = Dummy()
        type_registry.register_type(type_bidder, type_view_factory)

        self.assertIn(type_bidder, type_registry.types)
        self.assertEqual(type_registry.types[type_bidder], type_view_factory)

    def test_deregister_view(self):
        type_registry = TypeRegistry()
        type_bidder = Dummy()
        type_view_factory = Dummy()
        type_registry.types[type_bidder] = type_view_factory
        type_registry.deregister_type(type_bidder)

        self.assertNotIn(type_bidder, type_registry.types)
