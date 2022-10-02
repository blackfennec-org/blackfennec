import unittest
from collections import deque
from typing import Optional

from doubles.black_fennec.interpretation.double_interpretation import \
    InterpretationMock
from doubles.black_fennec.interpretation.double_interpretation_service import \
    InterpretationServiceMock
from doubles.black_fennec.structure.double_list import (ListInstanceMock,
                                                        ListMock)
from doubles.black_fennec.structure.double_structure import StructureMock
from doubles.black_fennec.type_system.double_type_registry import TypeRegistryMock
from doubles.black_fennec.structure.type.double_type import TypeMock
from src.visualisation.core.list.list_view_model import ListViewModel


class ListViewModelTestSuite(unittest.TestCase):
    def setUp(self) -> None:
        self.interpretation = InterpretationMock(ListInstanceMock())
        self.interpretation_service = InterpretationServiceMock(
            deque([InterpretationMock()])
        )
        self.type_registry = TypeRegistryMock()
        self.view_model: Optional[ListViewModel] = ListViewModel(
            self.interpretation,
            self.interpretation_service,
            self.type_registry
        )

    def test_can_construct(self):
        self.assertIsNotNone(self.view_model)

    def test_can_get_value(self):
        self.assertEqual(self.view_model.value.value, [])

    def test_can_add_item(self):
        item = StructureMock()
        self.view_model.add_item(item)
        self.assertIn(item, self.view_model.value.value)

    def test_can_delete_item(self):
        item = StructureMock()
        self.view_model.add_item(item)
        self.view_model.delete_item(item)
        self.assertNotIn(item, self.view_model.value.value)

    def test_can_forward_navigation_request(self):
        route_target = StructureMock()
        self.view_model.navigate_to(route_target)
        self.assertListEqual(
            self.interpretation.navigation_requests,
            [route_target])

    def test_can_create_preview(self):
        preview = self.view_model.create_preview(StructureMock())
        self.assertTrue(
            self.interpretation_service.last_specification.is_request_for_preview)
        self.assertIsNotNone(preview.navigation_service)

    def test_can_add_by_template(self):
        subject = StructureMock()
        template = TypeMock(default=subject)
        self.view_model.add_by_template(template)
        self.assertIn(subject, self.view_model.value.value)

    def test_can_get_templates(self):
        subject = StructureMock()
        template = TypeMock(subject)
        self.type_registry.types.append(template)
        templates = self.view_model.get_templates()
        self.assertIn(template, templates)
