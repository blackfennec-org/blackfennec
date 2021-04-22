import unittest
from collections import deque
from doubles.dummy import Dummy
from doubles.interpretation.interpretation import InterpretationMock
from doubles.interpretation.interpretation_service import InterpretationServiceMock
from doubles.structure.info import InfoMock
from doubles.structure.map import MapMock
from src.type_system.core.map.map_view_model import MapViewModel


class MapViewModelTestSuite(unittest.TestCase):
    def test_can_construct(self):
        interpretation = InterpretationMock(MapMock())
        interpretation_service = Dummy('interpretation service')
        view_model = MapViewModel(interpretation, interpretation_service)
        self.assertIsNotNone(view_model)

    def test_can_get_value(self):
        interpretation = InterpretationMock(MapMock())
        interpretation_service = Dummy('interpretation service')
        view_model = MapViewModel(interpretation, interpretation_service)
        self.assertEqual(view_model.value, {})

    def test_can_add_item(self):
        interpretation = InterpretationMock(MapMock())
        interpretation_service = Dummy('interpretation service')
        view_model = MapViewModel(interpretation, interpretation_service)
        key = 'Key'
        value = InfoMock()
        view_model.add_item(key, value)
        self.assertIn(key, view_model.value)

    def test_can_delete_item(self):
        interpretation = InterpretationMock(MapMock())
        interpretation_service = Dummy('interpretation service')
        view_model = MapViewModel(interpretation, interpretation_service)
        key = 'Key'
        value = InfoMock()
        view_model.add_item(key, value)
        view_model.delete_item(key)
        self.assertNotIn(key, view_model.value)

    def test_can_forward_navigation_request(self):
        interpretation = InterpretationMock(MapMock())
        interpretation_service = Dummy('interpretation service')
        view_model = MapViewModel(interpretation, interpretation_service)
        route_target = InfoMock()
        view_model.navigate_to(route_target)
        self.assertListEqual(
            interpretation.navigation_requests,
            [route_target])

    def test_can_create_preview(self):
        interpretation = InterpretationMock(MapMock())
        interpretation_service = InterpretationServiceMock(deque([
            InterpretationMock()]))
        view_model = MapViewModel(interpretation, interpretation_service)
        preview = view_model.create_preview(InfoMock())
        self.assertTrue(
            interpretation_service.last_specification.is_request_for_preview)
        self.assertIsNotNone(preview.navigation_service)

