import unittest
from doubles.structure.double_root import RootMock
from doubles.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from src.structure.info import Info


class InfoTestSuite(unittest.TestCase):
    def test_can_construct(self):
        parent = RootMock()
        info = Info(parent=parent)
        self.assertEqual(info.parent, parent)

    def test_can_change_parent(self):
        original_parent = RootMock()
        new_parent = RootMock()
        info = Info(parent=original_parent)
        info.parent = new_parent

        self.assertEqual(info.parent, new_parent)

    def test_can_get_root(self):
        root = RootMock()
        info = Info(parent=root)
        self.assertEqual(info.root, root)

    def test_can_get_children(self):
        info = Info()
        children = info.children
        self.assertEqual(children, [])

    def test_can_get_value(self):
        value = 'value'
        info = Info(value)
        self.assertEqual(value, info.value)

    def test_can_set_value(self):
        value = 'value'
        info = Info()
        info.value = value
        self.assertEqual(value, info.value)

    def test_accept(self):
        visitor = FactoryBaseVisitorMock()
        info = Info()
        info.accept(visitor)
        self.assertEqual(visitor.info, info)
        self.assertEqual(visitor.visit_info_count, 1)
