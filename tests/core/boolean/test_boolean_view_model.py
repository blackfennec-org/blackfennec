import unittest

from src.core.boolean import BooleanViewModel

class BooleanViewModelTestSuite(unittest.TestCase):
    def test_can_construct(self):
        BooleanViewModel({})

    def test_can_get_value(self):
        boolean_view_model = BooleanViewModel({})
        self.assertEqual(boolean_view_model.value, 0)

    def test_can_set_value(self):
        boolean_view_model = BooleanViewModel({})
        boolean_view_model.value = 3.141
        self.assertEqual(boolean_view_model.value, 3.141)
