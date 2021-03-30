import unittest

from src.core.number import NumberViewModel

class NumberViewModelTestSuite(unittest.TestCase):
    def test_can_construct(self):
        NumberViewModel({})

    def test_can_get_value(self):
        number_view_model = NumberViewModel({})
        self.assertEqual(number_view_model.value, 0)

    def test_can_set_value(self):
        number_view_model = NumberViewModel({})
        number_view_model.value = 3.141
        self.assertEqual(number_view_model.value, 3.141)
