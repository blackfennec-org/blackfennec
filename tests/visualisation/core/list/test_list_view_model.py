import unittest

from collections import deque
from typing import Optional

from doubles.black_fennec.type_system.double_template_registry import TemplateRegistryMock
from doubles.black_fennec.interpretation.double_interpretation import InterpretationMock
from doubles.black_fennec.interpretation.double_interpretation_service import InterpretationServiceMock
from doubles.black_fennec.structure.double_info import InfoMock
from doubles.black_fennec.structure.double_list import ListMock, ListInstanceMock
from doubles.visualisation.double_info_template import InfoTemplate
from src.visualisation.core.list.list_view_model import ListViewModel


class ListViewModelTestSuite(unittest.TestCase):
    def setUp(self) -> None:
        self.interpretation = InterpretationMock(ListInstanceMock())
        self.interpretation_service = InterpretationServiceMock(
            deque([InterpretationMock()])
        )
        self.template_registry = TemplateRegistryMock()
        self.view_model: Optional[ListViewModel] = ListViewModel(
            self.interpretation,
            self.interpretation_service,
            self.template_registry
        )

    def tearDown(self) -> None:
        self.interpretation = None
        self.interpretation_service = None
        self.template_registry = None
        self.view_model: Optional[ListViewModel] = None

    def test_can_construct(self):
        self.assertIsNotNone(self.view_model)

    def test_can_get_value(self):
        self.assertEqual(self.view_model.value, [])

    def test_can_add_item(self):
        item = InfoMock()
        self.view_model.add_item(item)
        self.assertIn(item, self.view_model.value)

    def test_can_delete_item(self):
        item = InfoMock()
        self.view_model.add_item(item)
        self.view_model.delete_item(item)
        self.assertNotIn(item, self.view_model.value)

    def test_can_forward_navigation_request(self):
        route_target = InfoMock()
        self.view_model.navigate_to(route_target)
        self.assertListEqual(
            self.interpretation.navigation_requests,
            [route_target])

    def test_can_create_preview(self):
        preview = self.view_model.create_preview(InfoMock())
        self.assertTrue(
            self.interpretation_service.last_specification.is_request_for_preview)
        self.assertIsNotNone(preview.navigation_service)

    def test_can_add_by_template(self):
        subject = InfoMock()
        template = InfoTemplate(subject)
        self.view_model.add_by_template(template)
        self.assertIn(subject, self.view_model.value)

    def test_can_get_templates(self):
        subject = InfoMock()
        template = InfoTemplate(subject)
        self.template_registry.templates.add(template)
        templates = self.view_model.get_templates()
        self.assertIn(template, templates)
