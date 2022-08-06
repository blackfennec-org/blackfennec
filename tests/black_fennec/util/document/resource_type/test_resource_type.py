# -*- coding: utf-8 -*-
import unittest

from src.black_fennec.util.document.resource_type.resource_type import ResourceType


class ResourceTypeTestSuite(unittest.TestCase):

    def test_determine_resource_type_of_https(self):
        uri = 'https://test.com/test#test'
        resource_type = 'https'
        actual_resource_type = ResourceType.try_determine_resource_type(uri)
        self.assertEqual(actual_resource_type, resource_type)

    def test_determine_resource_type_of_http(self):
        uri = 'http://test.com/test#test'
        resource_type = 'http'
        actual_resource_type = ResourceType.try_determine_resource_type(uri)
        self.assertEqual(actual_resource_type, resource_type)

    def test_determine_resource_type_of_file(self):
        uri = '/test/test.json'
        resource_type = 'file'
        actual_resource_type = ResourceType.try_determine_resource_type(uri)
        self.assertEqual(actual_resource_type, resource_type)
