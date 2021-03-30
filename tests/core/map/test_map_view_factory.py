import unittest

from src.core.map import MapViewFactory, MapView

class MapViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        MapViewFactory()

    def test_can_create_map_view(self):
        factory = MapViewFactory()
        view = factory.create({})
        self.assertIsInstance(view, MapView)
