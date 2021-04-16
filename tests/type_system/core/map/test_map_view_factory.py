import unittest

from doubles.interpretation.interpretation import InterpretationMock
from doubles.structure.map import MapMock
from src.type_system.core.map.map_view import MapView
from src.type_system.core.map.map_view_factory import MapViewFactory


class MapViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        MapViewFactory()

    def test_can_create_map_view(self):
        factory = MapViewFactory()
        view = factory.create(InterpretationMock(MapMock()))
        self.assertIsInstance(view, MapView)
