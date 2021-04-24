import unittest

from doubles.interpretation.double_interpretation import InterpretationMock
from doubles.structure.double_info import InfoMock
from doubles.structure.double_list import ListMock
from src.type_system.core.list.list_view_model import ListViewModel


class ListViewModelTestSuite(unittest.TestCase):
    def test_can_construct(self):
        ListViewModel(InterpretationMock())

    def test_can_get_value(self):
        list_view_model = ListViewModel(InterpretationMock(ListMock()))
        self.assertEqual(list_view_model.value, [])

    def test_can_add_item(self):
        list_view_model = ListViewModel(InterpretationMock(ListMock()))
        item = InfoMock()
        list_view_model.add_item(item)
        self.assertIn(item, list_view_model.value)

    def test_can_delete_item(self):
        list_view_model = ListViewModel(InterpretationMock(ListMock()))
        item = InfoMock()
        list_view_model.add_item(item)
        list_view_model.delete_item(item)
        self.assertNotIn(item, list_view_model.value)

    def test_can_forward_navigation_request(self):
        interpretation = InterpretationMock(ListMock())
        route_target = InfoMock()
        list_view_model = ListViewModel(interpretation)
        list_view_model.navigate_to(route_target)
        self.assertListEqual(
            interpretation.navigation_requests,
            [route_target])
