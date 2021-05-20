import unittest
from datetime import datetime

from doubles.black_fennec.interpretation.double_interpretation import InterpretationMock
from doubles.black_fennec.structure.double_map import MapMock
from doubles.black_fennec.structure.double_string import StringMock
from src.visualisation.base.date_time_range.date_time_range import DateTimeRange
from src.visualisation.base.date_time_range.date_time_range_view_model import DateTimeRangeViewModel


class DateTimeRangeViewModelTestSuite(unittest.TestCase):
    def test_can_construct(self):
        DateTimeRangeViewModel(InterpretationMock(MapMock()))

    def test_can_get_date_time(self):
        view_model = DateTimeRangeViewModel(InterpretationMock(MapMock()))
        self.assertEqual(datetime.min, view_model.date_time_start)
        self.assertEqual(datetime.max, view_model.date_time_end)

    def test_date_time_start_getter(self):
        data = dict()
        data[DateTimeRange.START_KEY] = StringMock(datetime.now().isoformat())

        data_map = MapMock(data)
        view_model = DateTimeRangeViewModel(InterpretationMock(data_map))
        date_time_start = \
            datetime.fromisoformat(data[DateTimeRange.START_KEY].value)
        self.assertEqual(view_model.date_time_start, date_time_start)

    def test_date_time_start_setter(self):
        date_time_start = datetime.now()
        view_model = DateTimeRangeViewModel(InterpretationMock(MapMock()))
        view_model.date_time_start = date_time_start
        self.assertEqual(view_model.date_time_start, date_time_start)

    def test_date_time_end_getter(self):
        data = dict()
        data[DateTimeRange.END_KEY] = StringMock(datetime.now().isoformat())

        data_map = MapMock(data)
        view_model = \
            DateTimeRangeViewModel(InterpretationMock(data_map))
        date_time_end = \
            datetime.fromisoformat(data[DateTimeRange.END_KEY].value)
        self.assertEqual(view_model.date_time_end, date_time_end)

    def test_date_time_end_setter(self):
        date_time_end = datetime.now()
        view_model = DateTimeRangeViewModel(InterpretationMock(MapMock()))
        view_model.date_time_end = date_time_end
        self.assertEqual(view_model.date_time_end, date_time_end)
