import unittest

from doubles.interpretation.interpretation import InterpretationMock
from doubles.interpretation.interpretation_service import InterpretationServiceMock
from doubles.structure.map import MapMock
from src.interpretation.specification import Specification
from src.type_system.core.map.map_view import MapView
from src.type_system.core.map.map_preview import MapPreview
from src.type_system.core.map.map_view_factory import MapViewFactory


class MapViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        MapViewFactory(InterpretationServiceMock([]))

    def test_can_create_map_view(self):
        factory = MapViewFactory(InterpretationServiceMock([]))
        view = factory.create(InterpretationMock(MapMock()), Specification())
        self.assertIsInstance(view, MapView)

    def test_can_create_map_preview(self):
        factory = MapViewFactory(InterpretationServiceMock([]))
        view = factory.create(InterpretationMock(
            MapMock()), Specification(request_preview=True))
        self.assertIsInstance(view, MapPreview)

    def test_satisfies_default(self):
        factory = MapViewFactory(InterpretationServiceMock([]))
        satisfies = factory.satisfies(Specification())
        self.assertTrue(satisfies)

    def test_does_satisfy_preview(self):
        factory = MapViewFactory(InterpretationServiceMock([]))
        satisfies = factory.satisfies(Specification(request_preview=True))
        self.assertTrue(satisfies)
