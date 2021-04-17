# -*- coding: utf-8 -*-
import unittest

from src.interpretation.specification import Specification


class SpecificationTestSuite(unittest.TestCase):
    def test_can_default_create(self):
        specification = Specification()
        self.assertFalse(specification.is_request_for_preview)

    def test_can_request_preview(self):
        specification = Specification(request_preview=True)
        self.assertTrue(specification.is_request_for_preview)
