import unittest
from doubles.structure.double_root import RootMock
from src.structure.string import String


class StringTestSuite(unittest.TestCase):
    def test_can_construct(self):
        string = String("Black Fennec")
        self.assertEqual(string, "Black Fennec")

    def test_can_get_value(self):
        string = String("Black Fennec")
        self.assertEqual(string.value, "Black Fennec")

    def test_can_set_value(self):
        string = String("Tiny Fennec")
        string.value = "Black Fennec"
        self.assertEqual(string, "Black Fennec")

    def test_can_change_parent(self):
        new_parent = RootMock()
        string = String("Black Fennec")
        string.parent = new_parent
        self.assertEqual(string.parent, new_parent)

    def test_can_get_root(self):
        root = RootMock()
        string = String("Black Fennec")
        string.parent = root
        self.assertEqual(string.root, root)
