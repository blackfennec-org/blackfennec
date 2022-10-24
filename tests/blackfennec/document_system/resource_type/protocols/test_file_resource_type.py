# -*- coding: utf-8 -*-
import tempfile
import unittest

from blackfennec_doubles.document_system.double_document import DocumentMock
from blackfennec.document_system.resource_type.protocols.file_resource_type import FileResourceType


class FileResourceTypeTestSuite(unittest.TestCase):

    def setUp(self) -> None:
        self.tmp_file = tempfile.NamedTemporaryFile()
        self.tmp_file_content = 'content'
        self.tmp_file.write(bytes(self.tmp_file_content, encoding='utf8'))
        self.tmp_file.seek(0)
        self.tmp_file_path = self.tmp_file.name
        self.tmp_file_location = '/'.join(self.tmp_file_path.split('/', 2)[:2]) + '/'
        self.tmp_file_uri = self.tmp_file_path.split('/')[2]

    def tearDown(self) -> None:
        self.tmp_file.close()
        self.tmp_file = None
        self.tmp_file_path = None
        self.tmp_file_location = None
        self.tmp_file_uri = None

    def test_load_resource_relative_path(self):
        document = DocumentMock(uri=self.tmp_file_uri, location=self.tmp_file_location)

        with FileResourceType().load_resource(document, "r") as data:
            content = data.read()

        self.assertEqual('content', content)

    def test_load_resource_absolute_path(self):
        document = DocumentMock(uri=self.tmp_file_path, location=self.tmp_file_location)

        with FileResourceType().load_resource(document, "r") as data:
            content = data.read()

        self.assertEqual('content', content)
