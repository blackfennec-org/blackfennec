import unittest

from doubles.core import InfoMock, ListMock, InterprationMock
from src.core.list import ListViewModel

class ListViewModelTestSuite(unittest.TestCase):
    def test_can_construct(self):
        ListViewModel(InterprationMock())

    def test_can_get_value(self):
        list_view_model = ListViewModel(InterprationMock(ListMock()))
        self.assertEqual(list_view_model.value, [])

    def test_can_add_item(self):
        list_view_model = ListViewModel(InterprationMock(ListMock()))
        item = InfoMock()
        list_view_model.add_item(item)
        self.assertIn(item, list_view_model.value)

    def test_can_delete_item(self):
        list_view_model = ListViewModel(InterprationMock(ListMock()))
        item = InfoMock()
        list_view_model.add_item(item)
        list_view_model.delete_item(item)
        self.assertNotIn(item, list_view_model.value)

    def test_can_forward_navigation_request(self):
        interpretation = InterprationMock(ListMock())
        route_target = InfoMock()
        list_view_model = ListViewModel(interpretation)
        list_view_model.navigate_to(route_target)
        self.assertListEqual(
            interpretation.navigation_requests,
            [route_target])
