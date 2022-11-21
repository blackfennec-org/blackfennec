from datetime import datetime

import pytest

from base.date_time.date_time_editor import DateTimeEditor

from doubles.date_time.double_date_time_view_model import DateTimeViewModelMock


@pytest.fixture()
def view_model():
    return DateTimeViewModelMock()


@pytest.fixture()
def date_time_editor(view_model):
    return DateTimeEditor(view_model)


def test_can_construct_date_time_editor(date_time_editor):
    assert isinstance(date_time_editor, DateTimeEditor)


def test_get_hour(date_time_editor):
    assert date_time_editor.hour == 0


def test_set_hour(date_time_editor):
    date_time_editor._hour_entry.set_text('12')
    assert date_time_editor.hour == 12


def test_set_hour_maximal(date_time_editor):
    date_time_editor._hour_entry.set_text('23')
    assert date_time_editor.hour == 23


def test_set_hour_out_of_range(date_time_editor):
    date_time_editor.hour = 24
    assert date_time_editor.hour == 23


def test_get_minute(date_time_editor):
    assert date_time_editor.minute == 0


def test_get_second(date_time_editor):
    assert date_time_editor.second == 0


def test_update_date_time(date_time_editor, view_model):
    now = datetime.now()
    view_model.notify(now, 'date_time')
