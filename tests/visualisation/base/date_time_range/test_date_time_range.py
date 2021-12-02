import unittest
from datetime import datetime

from doubles.black_fennec.structure.double_map import MapMock
from doubles.black_fennec.structure.double_string import StringMock
from src.visualisation.base.date_time_range.date_time_range import DateTimeRange


class DateTimeRangeTestSuite(unittest.TestCase):
    def test_can_default_construct(self):
        date_time = DateTimeRange()
        self.assertEqual(date_time.date_time_start, datetime.min)
        self.assertEqual(date_time.date_time_end, datetime.max)

    def test_can_construct_with_map(self):
        data = dict()
        data[DateTimeRange.START_KEY] = StringMock(datetime.now().isoformat())
        data[DateTimeRange.END_KEY] = StringMock(datetime.now().isoformat())

        data_map = MapMock(data)
        DateTimeRange(data_map)
        self.assertIn(DateTimeRange.START_KEY, data_map.value)
        self.assertIn(DateTimeRange.END_KEY, data_map.value)

    def test_date_time_start_getter(self):
        data = dict()
        data[DateTimeRange.START_KEY] = StringMock(datetime.now().isoformat())

        data_map = MapMock(data)
        date_time = DateTimeRange(data_map)
        date_time_start_string = date_time.date_time_start.isoformat()
        self.assertEqual(date_time_start_string,
                         data[DateTimeRange.START_KEY].value)

    def test_date_start_time_getter_wrong_datetime_format(self):
        data = dict()
        data[DateTimeRange.START_KEY] = StringMock('16.04.2021')

        data_map = MapMock(data)
        date_time = DateTimeRange(data_map)
        date_time_string = date_time.date_time_start
        self.assertEqual(date_time_string, datetime.min)

    def test_date_time_start_setter(self):
        date_time_value = datetime.now()
        date_time = DateTimeRange()
        date_time.date_time_start = date_time_value
        self.assertEqual(date_time.date_time_start, date_time_value)

    def test_date_time_end_getter(self):
        data = dict()
        data[DateTimeRange.END_KEY] = StringMock(datetime.now().isoformat())

        data_map = MapMock(data)
        date_time = DateTimeRange(data_map)
        date_time_end_string = \
            date_time.date_time_end.isoformat()
        self.assertEqual(date_time_end_string,
                         data[DateTimeRange.END_KEY].value)

    def test_date_end_time_getter_wrong_datetime_format(self):
        data = dict()
        data[DateTimeRange.END_KEY] = StringMock('16.04.2021')

        data_map = MapMock(data)
        date_time = DateTimeRange(data_map)
        date_time_string = date_time.date_time_end
        self.assertEqual(date_time_string, datetime.max)

    def test_date_time_end_setter(self):
        date_time_value = datetime.now()
        date_time = DateTimeRange()
        date_time.date_time_end = date_time_value
        self.assertEqual(date_time.date_time_end, date_time_value)
