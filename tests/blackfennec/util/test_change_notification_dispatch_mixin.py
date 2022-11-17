import pytest

from blackfennec.util.change_notification import ChangeNotification
from blackfennec.util.change_notification_dispatch_mixin import ChangeNotificationDispatchMixin
from blackfennec_doubles.double_dummy import Dummy
from tests.test_utils.observer import Observer


@pytest.fixture
def change_notification_dispatch_mixin():
    return ChangeNotificationDispatchMixin()


def test_can_construct(change_notification_dispatch_mixin):
    assert isinstance(change_notification_dispatch_mixin, ChangeNotificationDispatchMixin)


def test_dispatch_change_notification(change_notification_dispatch_mixin):
    observer = Observer()
    change_notification_dispatch_mixin.bind(changed=observer.endpoint)

    sender = Dummy('sender')
    notification = ChangeNotification('old', 'new')

    change_notification_dispatch_mixin._dispatch_change_notification(sender, notification)

    assert observer.last_call[0][0] == sender
    assert observer.last_call[0][1] == notification


def test_skip_unnecessary_dispatch_of_change_notification(change_notification_dispatch_mixin):
    observer = Observer()
    change_notification_dispatch_mixin.bind(changed=observer.endpoint)

    sender = Dummy('sender')
    notification = ChangeNotification('old', 'old')

    change_notification_dispatch_mixin._dispatch_change_notification(sender, notification)

    assert len(observer.last_call) == 0
