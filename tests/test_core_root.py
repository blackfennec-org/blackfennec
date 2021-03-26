import unittest
from tests.doubles.doubles import InfoMock

from src.core.root import Root

class InfoTestSuite(unittest.TestCase):
    def test_can_construct(self):
        root = Root()
        self.assertEqual(root.parent, root)

    def test_can_not_change_parent(self):
        new_parent = InfoMock()
        root = Root()

        def set_parent(info, new_parent):
            info.parent = new_parent

        self.assertRaises(TypeError,
            lambda: set_parent(root, new_parent))

    def test_can_get_root(self):
        root = Root()
        self.assertEqual(root.root, root)
