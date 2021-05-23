"""template-registry Tests.

This module contains the unit-tests of the template-registry."""

import unittest

from doubles.double_dummy import Dummy
from src.black_fennec.type_system.template_registry import TemplateRegistry


class TemplateRegistryTestSuite(unittest.TestCase):
    def test_create_template_registry(self):
        template_registry = TemplateRegistry()
        self.assertIsInstance(template_registry.templates, set)

    def test_register_view(self):
        template_registry = TemplateRegistry()
        template = Dummy()
        template_registry.register_template(template)

        self.assertIn(template, template_registry.templates)

    def test_deregister_view(self):
        template_registry = TemplateRegistry()
        template = Dummy()
        template_registry.templates.add(template)
        template_registry.deregister_template(Dummy)

        self.assertNotIn(template, template_registry.templates)
