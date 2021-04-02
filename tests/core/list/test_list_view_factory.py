import unittest

from src.core.list import ListViewFactory, ListView

class MapViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        ListViewFactory()

    def test_can_create_list_view(self):
        factory = ListViewFactory()
        view = factory.create({})
        self.assertIsInstance(view, ListView)
