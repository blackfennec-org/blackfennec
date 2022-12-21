import logging

import pytest

from blackfennec.presentation_system.ui_service.ui_service import UiService
from blackfennec_doubles.actions.double_context import ContextMock
from blackfennec_doubles.actions.double_ui_context import UiContextMock
from blackfennec_doubles.document_system.mime_type.double_mime_type_registry import \
    MimeTypeRegistryMock
from blackfennec_doubles.presentation_system.ui_service.double_message import MessageMock
from blackfennec_doubles.presentation_system.ui_service.double_message_overlay import \
    MessageOverlayMock


@pytest.fixture
def root():
    return UiContextMock('root')


@pytest.fixture
def context(root):
    return ContextMock(window=root)


@pytest.fixture
def message():
    return MessageMock('message')


@pytest.fixture
def message_overlay(root):
    return MessageOverlayMock(root=root)


@pytest.fixture
def ui_service():
    return UiService(
        MimeTypeRegistryMock(),
    )


def test_can_construct(ui_service):
    assert isinstance(ui_service, UiService)


def test_can_register_message_overlay(ui_service, message_overlay):
    ui_service.register_message_overlay(message_overlay)


def test_can_deregister_message_overlay(ui_service, message_overlay):
    ui_service.register_message_overlay(message_overlay)
    ui_service.deregister_message_overlay(message_overlay)


def test_can_show_simple_message(ui_service, message_overlay, context, message):
    ui_service.register_message_overlay(message_overlay)
    ui_service.show_message(context, message)

    toast = message_overlay.add_toast_parameter
    assert toast.get_title() == message.text


def test_can_show_action_message(ui_service, message_overlay, context, message):
    message.action_name = 'action'
    message.action_target = 'target'

    ui_service.register_message_overlay(message_overlay)
    ui_service.show_message(context, message)
    toast = message_overlay.add_toast_parameter

    assert toast.get_title() == message.text
    assert toast.get_button_label() == message.action_name
    assert toast.get_action_name() == message.action_target
