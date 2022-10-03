# -*- coding: utf-8 -*-
import unittest

from doubles.double_dummy import Dummy
from src.black_fennec.document_system.mime_type.mime_type_registry import MimeTypeRegistry


class MimeTypeRegistryTestSuite(unittest.TestCase):
    def test_create_mime_type_registry(self):
        mime_type_registry = MimeTypeRegistry()
        self.assertIsInstance(mime_type_registry.mime_types, dict)

    def test_register_mime_type(self):
        mime_type_registry = MimeTypeRegistry()
        mime_type_id = 'mime_type'
        mime_type = Dummy()
        mime_type_registry.register_mime_type(mime_type_id, mime_type)

        self.assertIn(mime_type_id, mime_type_registry.mime_types)
        self.assertEqual(mime_type, mime_type_registry.mime_types[mime_type_id])

    def test_deregister_mime_type(self):
        mime_type_registry = MimeTypeRegistry()
        mime_type_id = 'mime_type'
        mime_type = Dummy()
        mime_type_registry.register_mime_type(mime_type_id, mime_type)
        mime_type_registry.deregister_mime_type(mime_type_id)

        self.assertNotIn(mime_type_id, mime_type_registry.mime_types)
