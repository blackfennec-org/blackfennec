import unittest

from doubles.core import InfoMock, InterprationMock
from src.core.map import MapViewModel

class MapViewModelTestSuite(unittest.TestCase):
    def test_can_construct(self):
        MapViewModel({})

    def test_can_get_value(self):
        map_view_model = MapViewModel({})
        self.assertEqual(map_view_model.value, {})

    def test_can_add_item(self):
        map_view_model = MapViewModel({})
        key = 'Key'
        value = InfoMock()
        map_view_model.add_item(key, value)
        self.assertIn(key, map_view_model.value)

    def test_can_delete_item(self):
        map_view_model = MapViewModel({})
        key = 'Key'
        value = InfoMock()
        map_view_model.add_item(key, value)
        map_view_model.delete_item(key)
        self.assertNotIn(key, map_view_model.value)

    def test_can_forward_navigation_request(self):
        interpretation = InterprationMock()
        route_target = InfoMock()
        map_view_model = MapViewModel(interpretation)
        map_view_model.navigate_to(route_target)
        self.assertListEqual(
            interpretation.navigation_requests,
            [route_target])
