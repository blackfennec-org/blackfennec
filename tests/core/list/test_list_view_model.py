import unittest

from doubles.core import InfoMock, InterprationMock
from src.core.list import ListViewModel

class ListViewModelTestSuite(unittest.TestCase):
    def test_can_construct(self):
        ListViewModel({})

    def test_can_get_value(self):
        list_view_model = ListViewModel({})
        self.assertEqual(list_view_model.value, [])

    def test_can_add_item(self):
        list_view_model = ListViewModel({})
        item = InfoMock()
        list_view_model.add_item(item)
        self.assertIn(item, list_view_model.value)

    def test_can_delete_item(self):
        list_view_model = ListViewModel({})
        item = InfoMock()
        list_view_model.add_item(item)
        list_view_model.delete_item(item)
        self.assertNotIn(item, list_view_model.value)

    def test_can_forward_navigation_request(self):
        interpretation = InterprationMock()
        route_target = InfoMock()
        list_view_model = ListViewModel(interpretation)
        list_view_model.navigate_to(route_target)
        self.assertListEqual(
            interpretation.navigation_requests,
            [route_target])
