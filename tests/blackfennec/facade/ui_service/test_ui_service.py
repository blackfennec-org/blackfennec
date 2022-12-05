import pytest

from blackfennec.facade.ui_service.ui_service import UiService
from blackfennec_doubles.facade.ui_service.double_message import MessageMock
from tests.test_utils.observer import Observer


@pytest.fixture
def message():
    return MessageMock('message')


@pytest.fixture
def ui_service():
    return UiService()


def test_can_construct(ui_service):
    assert isinstance(ui_service, UiService)


def test_can_show_simple_message(ui_service, message):
    observer = Observer()

    ui_service.bind(message=observer.endpoint)
    ui_service.show_message(message)

    toast = observer.last_call[0][1]
    assert toast.get_title() == message.text


def test_can_show_action_message(ui_service, message):
    message.action_name = 'action'
    message.action_target = 'target'

    observer = Observer()

    ui_service.bind(message=observer.endpoint)
    ui_service.show_message(message)

    toast = observer.last_call[0][1]
    assert toast.get_title() == message.text
    assert toast.get_button_label() == message.action_name
    assert toast.get_action_name() == message.action_target


def test_can_copy(ui_service):
    copy = ui_service.copy()
    assert isinstance(copy, UiService)
    assert copy != ui_service
