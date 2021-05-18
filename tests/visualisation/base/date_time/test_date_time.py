import unittest
from datetime import datetime

from doubles.black_fennec.structure.double_map import MapMock
from doubles.black_fennec.structure.double_string import StringMock
from src.visualisation.base.date_time.date_time import DateTime

class DateTimeTestSuite(unittest.TestCase):
    def test_can_default_construct(self):
        date_time = DateTime()
        self.assertEqual(date_time.date_time, datetime.min)

    def test_can_construct_with_map(self):
        data = dict()
        data[DateTime.DATE_TIME_KEY] = StringMock(datetime.now().isoformat())

        data_map = MapMock(data)
        DateTime(data_map)
        self.assertIn(DateTime.DATE_TIME_KEY, data_map)

    def test_date_time_getter(self):
        data = dict()
        data[DateTime.DATE_TIME_KEY] = StringMock(datetime.now().isoformat())

        data_map = MapMock(data)
        date_time = DateTime(data_map)
        date_time_string = date_time.date_time.isoformat()
        self.assertEqual(date_time_string, data[DateTime.DATE_TIME_KEY].value)

    def test_date_time_getter_wrong_datetime_format(self):
        data = dict()
        data[DateTime.DATE_TIME_KEY] = StringMock('16.04.2021')

        data_map = MapMock(data)
        date_time = DateTime(data_map)
        date_time_string = date_time.date_time
        self.assertEqual(date_time_string, datetime.min)

    def test_date_time_setter(self):
        date_time_value = datetime.now()
        date_time = DateTime()
        date_time.date_time = date_time_value
        self.assertEqual(date_time.date_time, date_time_value)
