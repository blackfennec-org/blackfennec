import pytest

from blackfennec.facade.ui_service.message import Message


@pytest.fixture
def message():
    return Message(
        'text',
        action_name='action_name',
        action_target='action_target',
    )


def test_can_construct(message):
    assert isinstance(message, Message)


def test_can_get_text(message):
    assert message.text == 'text'


def test_can_get_action_name(message):
    assert message.action_name == 'action_name'


def test_can_get_action_target(message):
    assert message.action_target == 'action_target'


def test_can_get_timeout(message):
    assert message.timeout > 0.5
