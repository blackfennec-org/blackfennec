"""type-registry Tests.

This module contains the unit-tests of the type-registry."""

import unittest

from blackfennec_doubles.double_dummy import Dummy
from blackfennec.type_system.type_registry import TypeRegistry


class TypeRegistryTestSuite(unittest.TestCase):
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
        type = Dummy()
        type_registry._types.append(type)
        type_registry.deregister_type(type)

        self.assertNotIn(type, type_registry.types)

    def test_returns_copy_of_internal_list(self):
        type_registry = TypeRegistry()
        type = Dummy()
        type_registry.types.append(type)

        self.assertNotIn(type, type_registry.types)
