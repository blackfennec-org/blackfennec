"""extension_source-registry Tests.

This module contains the unit-tests of the extension_source-registry."""

import unittest

from doubles.double_dummy import Dummy
from src.extension.extension_source_registry import ExtensionSourceRegistry


class ExtensionSourceRegistryTestSuite(unittest.TestCase):
    def test_create_extension_source_registry(self):
        extension_source_registry = ExtensionSourceRegistry()
        self.assertIsInstance(extension_source_registry.extension_sources, set)

    def test_register_extension_source(self):
        extension_source_registry = ExtensionSourceRegistry()
        extension_source = Dummy()
        extension_source_registry.register_extension_source(extension_source)

        self.assertIn(extension_source, extension_source_registry.extension_sources)

    def test_deregister_extension_source(self):
        extension_source_registry = ExtensionSourceRegistry()
        extension_source = Dummy()
        extension_source_registry.register_extension_source(extension_source)
        extension_source_registry.deregister_extension_source(extension_source)

        self.assertNotIn(extension_source, extension_source_registry.extension_sources)
