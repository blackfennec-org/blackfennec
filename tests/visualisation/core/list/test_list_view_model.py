import unittest

from collections import deque
from doubles.double_dummy import Dummy
from doubles.black_fennec.interpretation.double_interpretation import InterpretationMock
from doubles.black_fennec.interpretation.double_interpretation_service import InterpretationServiceMock
from doubles.black_fennec.structure.double_info import InfoMock
from doubles.black_fennec.structure.double_list import ListMock
from src.visualisation.core.list.list_view_model import ListViewModel


class ListViewModelTestSuite(unittest.TestCase):
    def test_can_construct(self):
        interpretation = InterpretationMock(ListMock())
        interpretation_service = Dummy('interpretation service')
        view_model = ListViewModel(interpretation, interpretation_service)
        self.assertIsNotNone(view_model)

    def test_can_get_value(self):
        interpretation = InterpretationMock(ListMock())
        interpretation_service = Dummy('interpretation service')
        view_model = ListViewModel(interpretation, interpretation_service)
        self.assertEqual(view_model.value, [])

    def test_can_add_item(self):
        interpretation_service = InterpretationServiceMock([])
        list_view_model = ListViewModel(InterpretationMock(ListMock()),
                                        interpretation_service)
        item = InfoMock()
        list_view_model.add_item(item)
        self.assertIn(item, list_view_model.value)

    def test_can_delete_item(self):
        interpretation_service = InterpretationServiceMock([])
        list_view_model = ListViewModel(InterpretationMock(ListMock()),
                                        interpretation_service)
        item = InfoMock()
        list_view_model.add_item(item)
        list_view_model.delete_item(item)
        self.assertNotIn(item, list_view_model.value)

    def test_can_forward_navigation_request(self):
        interpretation = InterpretationMock(ListMock())
        interpretation_service = InterpretationServiceMock([])
        route_target = InfoMock()
        list_view_model = ListViewModel(interpretation, interpretation_service)
        list_view_model.navigate_to(route_target)
        self.assertListEqual(
            interpretation.navigation_requests,
            [route_target])

    def test_can_create_preview(self):
        interpretation = InterpretationMock(ListMock())
        interpretation_service = InterpretationServiceMock(deque([
            InterpretationMock()]))
        view_model = ListViewModel(interpretation, interpretation_service)
        preview = view_model.create_preview(InfoMock())
        self.assertTrue(
            interpretation_service.last_specification.is_request_for_preview)
        self.assertIsNotNone(preview.navigation_service)
