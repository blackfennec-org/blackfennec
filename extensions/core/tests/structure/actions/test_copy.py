import logging
from io import StringIO

import pytest

from blackfennec_doubles.actions.double_context import ContextMock
from blackfennec_doubles.document_system.double_document import DocumentMock
from blackfennec_doubles.document_system.double_document_registry import \
    DocumentRegistryMock
from blackfennec_doubles.document_system.mime_type.double_mime_type import \
    MimeTypeMock
from blackfennec_doubles.structure.double_string import StringMock
from core.structure.actions.copy import CopyAction
from doubles.double_dummy import Dummy

logger = logging.getLogger(__name__)


@pytest.fixture
def serialized_structure():
    return "serialized_structure"


@pytest.fixture
def mime_type(serialized_structure):
    return MimeTypeMock(exported_structure=serialized_structure)


@pytest.fixture
def document(mime_type):
    return DocumentMock(mime_type=mime_type)


@pytest.fixture
def document_registry(document):
    document_registry = DocumentRegistryMock()
    document_registry.registered_document = document
    return document_registry


@pytest.fixture
def action_type():
    return Dummy('Type')


@pytest.fixture
def clipboard():
    clipboard = StringMock()
    return clipboard


@pytest.fixture
def action(action_type, document_registry, monkeypatch, clipboard):
    action = CopyAction(action_type, document_registry)

    def set_clipboard_text(serialized_structure):
        logger.debug("set_clipboard_text: %s", serialized_structure)
        clipboard.value = serialized_structure

    monkeypatch.setattr(action, '_set_clipboard', set_clipboard_text)
    return action


def test_can_construct(action):
    assert action is not None


def test_can_execute(action, clipboard, serialized_structure):
    context = ContextMock()
    context.structure.value = serialized_structure
    action.execute(context)
    assert clipboard.value == serialized_structure


def test_is_correct_type(action, action_type):
    assert action.type is action_type


def test_has_correct_name(action):
    assert action.name == "copy"


def test_has_correct_description(action):
    assert len(action.description) > 7
