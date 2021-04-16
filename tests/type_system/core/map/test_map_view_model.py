import unittest

from doubles.interpretation.interpretation import InterpretationMock
from doubles.structure.info import InfoMock
from doubles.structure.map import MapMock
from src.type_system.core.map.map_view_model import MapViewModel


class MapViewModelTestSuite(unittest.TestCase):
    def test_can_construct(self):
        MapViewModel(InterpretationMock(MapMock()))

    def test_can_get_value(self):
        map_view_model = MapViewModel(InterpretationMock(MapMock()))
        self.assertEqual(map_view_model.value, {})

    def test_can_add_item(self):
        map_view_model = MapViewModel(InterpretationMock(MapMock()))
        key = 'Key'
        value = InfoMock()
        map_view_model.add_item(key, value)
        self.assertIn(key, map_view_model.value)

    def test_can_delete_item(self):
        map_view_model = MapViewModel(InterpretationMock(MapMock()))
        key = 'Key'
        value = InfoMock()
        map_view_model.add_item(key, value)
        map_view_model.delete_item(key)
        self.assertNotIn(key, map_view_model.value)

    def test_can_forward_navigation_request(self):
        interpretation = InterpretationMock(MapMock())
        route_target = InfoMock()
        map_view_model = MapViewModel(interpretation)
        map_view_model.navigate_to(route_target)
        self.assertListEqual(
            interpretation.navigation_requests,
            [route_target])
