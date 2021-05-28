import unittest
from collections import deque
from doubles.double_dummy import Dummy
from doubles.black_fennec.interpretation.double_interpretation import InterpretationMock
from doubles.black_fennec.interpretation.double_interpretation_service import InterpretationServiceMock
from doubles.black_fennec.type_system.double_template_registry import TemplateRegistryMock
from doubles.visualisation.double_info_template import InfoTemplate \
as InfoTemplateMock
from doubles.black_fennec.structure.double_info import InfoMock
from doubles.black_fennec.structure.double_map import MapInstanceMock
from src.visualisation.core.map.map_view_model import MapViewModel


class MapViewModelTestSuite(unittest.TestCase):
    def setUp(self):
        self.interpretation = InterpretationMock(MapInstanceMock())
        self.interpretation_service = InterpretationServiceMock(
            deque([self.interpretation]))
        self.template_registry = TemplateRegistryMock([
            InfoTemplateMock(Dummy('info'))
        ])
        self.view_model = MapViewModel(
            self.interpretation,
            self.interpretation_service,
            self.template_registry)

    def test_can_construct(self):
        self.assertIsNotNone(self.view_model)

    def test_can_get_value(self):
        self.assertEqual(self.view_model.value, {})

    def test_can_add_item(self):
        key = 'Key'
        value = InfoMock()
        self.view_model.add_item(key, value)
        self.assertIn(key, self.view_model.value)

    def test_can_delete_item(self):
        key = 'Key'
        value = InfoMock()
        self.view_model.add_item(key, value)
        self.view_model.delete_item(key)
        self.assertNotIn(key, self.view_model.value)

    def test_can_forward_navigation_request(self):
        route_target = InfoMock()
        self.view_model.navigate_to(route_target)
        self.assertListEqual(
            self.interpretation.navigation_requests,
            [route_target])

    def test_can_create_preview(self):
        preview = self.view_model.create_preview(InfoMock())
        last_spec = self.interpretation_service.last_specification
        self.assertTrue(last_spec.is_request_for_preview)
        self.assertIsNotNone(preview.navigation_service)

    def test_can_rename_key(self):
        self.view_model.add_item('old_key', InfoMock())
        self.view_model.rename_key('old_key', 'new_key')
        self.assertIn('new_key', self.view_model.value.value)
        self.assertNotIn('old_key', self.view_model.value.value)        

    def test_can_add_by_template(self):
        key = 'key'
        info = InfoMock(value='info')
        template = InfoTemplateMock(info)
        self.view_model.add_by_template(key, template)
        self.assertEqual(self.view_model.value[key], info)

    def test_can_get_templates(self):
        templates = self.view_model.get_templates()
        self.assertEqual(templates, self.template_registry.templates)
