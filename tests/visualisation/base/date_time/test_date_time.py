import unittest
from datetime import datetime

from doubles.black_fennec.structure.double_map import MapMock
from doubles.black_fennec.structure.double_string import StringMock
from src.visualisation.base.date_time.date_time import DateTime


def test_can_default_construct():
    date_time = DateTime()
    assert date_time.date_time == datetime.min


def test_can_construct_with_map():
    data = dict()
    data[DateTime.DATE_TIME_KEY] = StringMock(datetime.now().isoformat())

    data_map = MapMock(data)
    DateTime(data_map)
    assert DateTime.DATE_TIME_KEY in data_map.value


def test_date_time_getter():
    data = dict()
    data[DateTime.DATE_TIME_KEY] = StringMock(datetime.now().isoformat())

    data_map = MapMock(data)
    date_time = DateTime(data_map)
    date_time_string = date_time.date_time.isoformat()
    assert date_time_string == data[DateTime.DATE_TIME_KEY].value


def test_date_time_getter_wrong_datetime_format():
    data = dict()
    data[DateTime.DATE_TIME_KEY] = StringMock('16.04.2021')

    data_map = MapMock(data)
    date_time = DateTime(data_map)
    date_time_string = date_time.date_time
    assert date_time_string == datetime.min


def test_date_time_setter():
    date_time_value = datetime.now()
    date_time = DateTime()
    date_time.date_time = date_time_value
    assert date_time.date_time == date_time_value


def test_date_time_repr():
    date_time = DateTime()
    date_time_string = date_time.__repr__()
    assert datetime.min.isoformat() in date_time_string
