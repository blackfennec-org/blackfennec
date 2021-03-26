"""type-registry Tests.

This module contains the unit-tests of the type-registry."""

import unittest

from doubles.dummy import Dummy
from tests.doubles.extension import TypeBidderStub, RoutingTargetDummy
from black_fennec.src.extension.type_registry import TypeRegistry

class ExtensionApiTestSuite(unittest.TestCase):
    def test_create_type_registry(self):
        type_registry = TypeRegistry()
        self.assertIsInstance(type_registry.types, dict)

    def test_register_view(self):
        type_registry = TypeRegistry()
        type_bidder = TypeBidderStub()
        routing_target = RoutingTargetDummy()
        type_registry.register_type(type_bidder, routing_target)
        self.assertIn(type_bidder, type_registry.types)
        self.assertEqual(type_registry.types[type_bidder], routing_target)

    def test_deregister_view(self):
        type_registry = TypeRegistry()
        type_bidder = TypeBidderStub()
        routing_target = RoutingTargetDummy()
        type_registry.types[type_bidder] = routing_target
        type_registry.deregister_type(type_bidder)
        self.assertNotIn(type_bidder, type_registry.types)
