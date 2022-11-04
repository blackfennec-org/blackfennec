import unittest
from datetime import datetime

from blackfennec_doubles.interpretation.double_interpretation import InterpretationMock
from blackfennec_doubles.structure.double_map import MapMock
from blackfennec_doubles.structure.double_string import StringMock
from base.date_time.date_time import DateTime
from base.date_time.date_time_view_model import DateTimeViewModel


class DateTimeViewModelTestSuite(unittest.TestCase):
    def test_can_construct(self):
        DateTimeViewModel(InterpretationMock(MapMock()))

    def test_can_get_date_time(self):
        view_model = DateTimeViewModel(InterpretationMock(MapMock()))
        self.assertEqual(datetime.min, view_model.date_time)

    def test_date_time_getter(self):
        data = dict()
        data[DateTime.DATE_TIME_KEY] = StringMock(datetime.now().isoformat())

        data_map = MapMock(data)
        view_model = DateTimeViewModel(InterpretationMock(data_map))
        date_time = datetime.fromisoformat(data[DateTime.DATE_TIME_KEY].value)
        self.assertEqual(view_model.date_time, date_time)

    def test_date_time_setter(self):
        date_time = datetime.now()
        view_model = DateTimeViewModel(InterpretationMock(MapMock()))
        view_model.date_time = date_time
        self.assertEqual(view_model.date_time, date_time)