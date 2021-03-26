import unittest
from tests.doubles.doubles import InfoMock

from src.core.info import Info

class InfoTestSuite(unittest.TestCase):
    def test_can_construct(self):
        parent = InfoMock()
        info = Info(parent)
        self.assertEqual(info.parent, parent)

    def test_can_change_parent(self):
        original_parent = InfoMock()
        new_parent = InfoMock()
        info = Info(original_parent)
        info.parent = new_parent

        self.assertEqual(info.parent, new_parent)

    def test_can_get_root(self):
        root = InfoMock()
        info = Info(root)
        self.assertEqual(info.root, root)
