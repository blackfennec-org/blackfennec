# -*- coding: utf-8 -*-
import unittest
import pytest

from doubles.black_fennec.document_system.double_document import DocumentMock
from src.black_fennec.document_system.resource_type.protocols.https_resource_type import HttpsResourceType
from tests.test_utils.connection import has_internet_connection

pytestmark = pytest.mark.integration

class HttpsResourceTypeTestSuite(unittest.TestCase):

    def setUp(self) -> None:
        self.uri = 'https://jsonplaceholder.typicode.com/posts/1'
        self.content = '''{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\\nsuscipit recusandae consequuntur expedita et cum\\nreprehenderit molestiae ut ut quas totam\\nnostrum rerum est autem sunt rem eveniet architecto"
}'''

    @pytest.mark.skipif(not has_internet_connection(), reason="test requires internet")
    def test_load_resource(self):
        document = DocumentMock(uri=self.uri)

        with HttpsResourceType().load_resource(document, "r") as data:
            content = data.read()

        self.assertEqual(self.content, content)

    @pytest.mark.skipif(not has_internet_connection(), reason="test requires internet")
    def test_determine_mimetype_online(self):
        uri = 'https://jsonplaceholder.typicode.com/posts/1'
        resource_type = 'https'
        actual_mime_type = HttpsResourceType().guess_mime_type(uri)
        self.assertEqual(actual_mime_type, 'application/json')