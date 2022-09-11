# -*- coding: utf-8 -*-
import unittest

from doubles.black_fennec.util.document.double_document import DocumentMock
from doubles.double_dummy import Dummy
from src.black_fennec.util.document.document import Document
from src.black_fennec.util.document.resource_type.protocols.https_resource_type import HttpsResourceType


class HttpsResourceTypeTestSuite(unittest.TestCase):

    def setUp(self) -> None:
        self.uri = 'https://jsonplaceholder.typicode.com/posts/1'
        self.content = '''{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\\nsuscipit recusandae consequuntur expedita et cum\\nreprehenderit molestiae ut ut quas totam\\nnostrum rerum est autem sunt rem eveniet architecto"
}'''

    def test_load_resource(self):
        document = DocumentMock(uri=self.uri)

        with HttpsResourceType().load_resource(document) as data:
            content = data.read()

        self.assertEqual(self.content, content)
