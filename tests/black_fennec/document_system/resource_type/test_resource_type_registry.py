# -*- coding: utf-8 -*-
import unittest

from doubles.double_dummy import Dummy
from src.black_fennec.document_system.resource_type.resource_type_registry import ResourceTypeRegistry


class ResourceTypeRegistryTestSuite(unittest.TestCase):
    def test_create_resource_type_registry(self):
        resource_type_registry = ResourceTypeRegistry()
        self.assertIsInstance(resource_type_registry.resource_types, dict)

    def test_register_resource_type(self):
        resource_type_registry = ResourceTypeRegistry()
        resource_type_id = 'resource_type'
        resource_type = Dummy()
        resource_type_registry.register_resource_type(resource_type_id, resource_type)

        self.assertIn(resource_type_id, resource_type_registry.resource_types)
        self.assertEqual(resource_type, resource_type_registry.resource_types[resource_type_id])

    def test_deregister_resource_type(self):
        resource_type_registry = ResourceTypeRegistry()
        resource_type_id = 'resource_type'
        resource_type = Dummy()
        resource_type_registry.register_resource_type(resource_type_id, resource_type)
        resource_type_registry.deregister_resource_type(resource_type_id)

        self.assertNotIn(resource_type_id, resource_type_registry.resource_types)
