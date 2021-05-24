import unittest
from doubles.black_fennec.structure.double_root import RootMock
from doubles.black_fennec.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from src.black_fennec.structure.structure import Structure


class StructureTestSuite(unittest.TestCase):
    def test_can_construct(self):
        parent = RootMock()
        structure = Structure(parent=parent)
        self.assertEqual(structure.parent, parent)

    def test_can_change_parent(self):
        original_parent = RootMock()
        new_parent = RootMock()
        structure = Structure(parent=original_parent)
        structure.parent = new_parent

        self.assertEqual(structure.parent, new_parent)

    def test_can_get_root(self):
        root = RootMock()
        structure = Structure(parent=root)
        self.assertEqual(structure.root, root)

    def test_can_get_children(self):
        structure = Structure()
        children = structure.children
        self.assertEqual(children, [])

    def test_can_get_value(self):
        value = 'value'
        structure = Structure(value)
        self.assertEqual(value, structure.value)

    def test_can_set_value(self):
        value = 'value'
        structure = Structure()
        structure.value = value
        self.assertEqual(value, structure.value)

    def test_accept(self):
        visitor = FactoryBaseVisitorMock()
        structure = Structure()
        structure.accept(visitor)
        self.assertEqual(visitor.structure, structure)
        self.assertEqual(visitor.visit_structure_count, 1)
