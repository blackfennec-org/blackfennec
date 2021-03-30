import unittest
from doubles.core import RootMock
from src.core.info import Info

class InfoTestSuite(unittest.TestCase):
    def test_can_construct(self):
        parent = RootMock()
        info = Info(parent)
        self.assertEqual(info.parent, parent)

    def test_can_change_parent(self):
        original_parent = RootMock()
        new_parent = RootMock()
        info = Info(original_parent)
        info.parent = new_parent

        self.assertEqual(info.parent, new_parent)

    def test_can_get_root(self):
        root = RootMock()
        info = Info(root)
        self.assertEqual(info.root, root)
