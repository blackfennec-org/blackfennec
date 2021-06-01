"""template-registry Tests.

This module contains the unit-tests of the template-registry."""
import logging
import unittest

from doubles.double_dummy import Dummy
from src.black_fennec.type_system.template_registry import TemplateRegistry


class TemplateRegistryTestSuite(unittest.TestCase):
    def test_create_template_registry(self):
        template_registry = TemplateRegistry()
        self.assertIsInstance(template_registry.templates, set)

    def test_register_template(self):
        template_registry = TemplateRegistry()
        template = Dummy()
        template_registry.register_template(template)

        self.assertIn(template, template_registry.templates)

    def test_deregister_template(self):
        template_registry = TemplateRegistry()
        template = Dummy()
        template_registry.register_template(template)
        template_registry.deregister_template(Dummy)

        self.assertNotIn(template, template_registry.templates)

    def test_deregister_inexistent_throws(self):
        template_registry = TemplateRegistry()
        with self.assertRaises(KeyError):
            template_registry.deregister_template(Dummy)

    def test_deregister_inexistent_logs(self):
        template_registry = TemplateRegistry()
        with self.assertLogs(None, logging.ERROR):
            try:
                template_registry.deregister_template(Dummy)
            except KeyError:
                pass
