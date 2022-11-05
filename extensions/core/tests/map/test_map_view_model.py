import unittest
from collections import deque

import pytest

from blackfennec_doubles.interpretation.double_interpretation import \
    InterpretationMock
from blackfennec_doubles.interpretation.double_interpretation_service import \
    InterpretationServiceMock
from blackfennec_doubles.structure.double_structure import StructureMock
from blackfennec_doubles.structure.double_map import MapInstanceMock, MapMock
from blackfennec_doubles.structure.double_structure import StructureMock
from blackfennec_doubles.type_system.double_type_registry import TypeRegistryMock
from blackfennec_doubles.double_dummy import Dummy
from blackfennec_doubles.type_system.double_type import TypeMock
from blackfennec.structure.root_factory import RootFactory
from core.map.map_view_model import MapViewModel


class MapViewModelTestSuite(unittest.TestCase):
    def setUp(self):
        structure = MapInstanceMock()
        RootFactory.make_root(structure)
        self.interpretation = InterpretationMock(structure)
        self.interpretation_service = InterpretationServiceMock(
            deque([self.interpretation]))
        self.type_registry = TypeRegistryMock([
            TypeMock(Dummy('structure'))
        ])
        self.view_model = MapViewModel(
            self.interpretation,
            self.interpretation_service,
            self.type_registry)

    def test_can_construct(self):
        self.assertIsNotNone(self.view_model)

    def test_can_get_value(self):
        self.assertEqual(self.view_model.value.value, {})

    def test_can_add_item(self):
        key = 'Key'
        value = StructureMock()
        self.view_model.add_item(key, value)
        self.assertIn(key, self.view_model.value.value)

    def test_can_delete_item(self):
        key = 'Key'
        value = StructureMock()
        self.view_model.add_item(key, value)
        self.view_model.delete_item(key)
        self.assertNotIn(key, self.view_model.value.value)

    def test_can_forward_navigation_request(self):
        route_target = StructureMock()
        self.view_model.navigate_to(route_target)
        self.assertListEqual(
            self.interpretation.navigation_requests,
            [route_target])

    def test_can_create_preview(self):
        preview = self.view_model.create_preview(StructureMock())
        last_spec = self.interpretation_service.last_specification
        self.assertTrue(last_spec.is_request_for_preview)
        self.assertIsNotNone(preview.navigation_service)

    def test_can_rename_key(self):
        self.view_model.add_item('old_key', StructureMock())
        self.view_model.rename_key('old_key', 'new_key')
        self.assertIn('new_key', self.view_model.value.value)
        self.assertNotIn('old_key', self.view_model.value.value)

    def test_can_add_by_template(self):
        key = 'key'
        structure = StructureMock(value='structure')
        template = TypeMock(default=structure)
        self.view_model.add_by_template(key, template)
        self.assertEqual(self.view_model.value.value[key], structure)

    def test_can_get_templates(self):
        templates = self.view_model.get_templates()
        self.assertEqual(templates, self.type_registry.types)
