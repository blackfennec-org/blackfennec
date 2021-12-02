import unittest

from doubles.black_fennec.structure.double_structure import StructureMock
from doubles.black_fennec.structure.double_root import RootMock
from doubles.black_fennec.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from src.black_fennec.structure.root import Root


class RootTestSuite(unittest.TestCase):
    def test_can_construct(self):
        root = Root()
        self.assertEqual(root.root, root)

    def test_get_uri(self):
        uri = 'test'
        root = Root(uri=uri)
        self.assertEqual(root.uri, uri)

    def test_set_uri(self):
        uri = 'test'
        root = Root()
        root.uri = uri
        self.assertEqual(root.uri, uri)

    def test_get_mime_type(self):
        mime_type = 'test'
        root = Root(mime_type=mime_type)
        self.assertEqual(root.mime_type, mime_type)

    def test_set_mime_type(self):
        mime_type = 'test'
        root = Root()
        root.mime_type = mime_type
        self.assertEqual(root.mime_type, mime_type)

    def test_get_value(self):
        child = StructureMock()
        root = Root(child)
        self.assertEqual(child, root.value)

    def test_set_value(self):
        child = StructureMock()
        root = Root()
        root.value = child
        self.assertEqual(root.value, child)

    def test_can_not_change_parent(self):
        new_parent = RootMock()
        root = Root()

        def set_parent(structure, new_parent):
            structure.parent = new_parent

        self.assertRaises(AssertionError,
            lambda: set_parent(root, new_parent))

    def test_can_get_parent(self):
        root = Root()
        self.assertEqual(root.parent, root)

    def test_can_get_root(self):
        root = Root()
        self.assertEqual(root.root, root)

    def test_accept(self):
        visitor = FactoryBaseVisitorMock()
        root = Root()
        root.accept(visitor)
        self.assertEqual(visitor.root, root)
        self.assertEqual(visitor.visit_root_count, 1)