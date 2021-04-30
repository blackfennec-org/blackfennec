import unittest

from doubles.structure.double_info import InfoMock
from doubles.structure.double_root import RootMock
from src.structure.root import Root


class RootTestSuite(unittest.TestCase):
    def test_can_construct(self):
        root = Root()
        self.assertEqual(root.parent, root)

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

    def test_get_child(self):
        child = InfoMock()
        root = Root(child)
        self.assertEqual(child, root.child)

    def test_set_child(self):
        child = InfoMock()
        root = Root()
        root.child = child
        self.assertEqual(root.child, child)

    def test_get_children(self):
        child = InfoMock()
        root = Root(child)
        self.assertIn(child, root.children)

    def test_can_not_change_parent(self):
        new_parent = RootMock()
        root = Root()

        def set_parent(info, new_parent):
            info.parent = new_parent

        self.assertRaises(TypeError,
            lambda: set_parent(root, new_parent))

    def test_can_get_root(self):
        root = Root()
        self.assertEqual(root.root, root)
