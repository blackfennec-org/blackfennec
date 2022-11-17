import pytest

from blackfennec.util.change_notification import ChangeNotification
from blackfennec_doubles.double_dummy import Dummy


@pytest.fixture
def change_notification():
    old_value = 'old'
    new_value = 'new'
    return ChangeNotification(old_value, new_value)


def test_can_construct(change_notification):
    assert isinstance(change_notification, ChangeNotification)


def test_get_old_value(change_notification):
    assert change_notification.old_value == 'old'


def test_get_new_value(change_notification):
    assert change_notification.new_value == 'new'
