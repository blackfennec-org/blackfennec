import unittest
from tests.doubles.doubles import InfoMock
from src.core.map import Map

class InfoTestSuite(unittest.TestCase):
    def test_can_construct(self):
        Map()

    #def test_can_construct_from_dict?

    def test_can_add_item(self):
        m = Map()
        key = 'Key'
        value = InfoMock()
        m[key] = value
        self.assertIn(key, m)
