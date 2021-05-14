import unittest
from doubles.structure.double_root import RootMock
from doubles.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
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

    def test_accept(self):
        visitor = FactoryBaseVisitorMock()
        string = String()
        string.accept(visitor)
        self.assertEqual(visitor.string, string)
        self.assertEqual(visitor.visit_string_count, 1)