# -*- coding: utf-8 -*-
import unittest
import pytest

from src.black_fennec.document_system.mime_type.mime_type import MimeType


class MimeTypeTestSuite(unittest.TestCase):

    def setUp(self):
        self.expected_mime_type = 'application/json'

    def test_determine_mimetype_of_file(self):
        uri = '/test/test.json'
        resource_type = 'file'
        actual_mime_type = MimeType.try_determine_mime_type(uri, resource_type)
        self.assertEqual(actual_mime_type, self.expected_mime_type)

    def test_determine_mimetype_of_unknown(self):
        uri = '/test/test'
        class ResourceTypeMock:
            def guess_mime_type(self, uri):
                return None

        with self.assertRaises(ValueError):
            MimeType.try_determine_mime_type(uri, ResourceTypeMock())
