import logging
from io import StringIO

import pytest

from blackfennec.structure.list import List
from blackfennec.structure.map import Map
from blackfennec.structure.number import Number
from blackfennec.structure.string import String
from blackfennec_doubles.actions.double_context import ContextMock
from blackfennec_doubles.document_system.double_document import DocumentMock
from blackfennec_doubles.document_system.double_document_registry import \
    DocumentRegistryMock
from blackfennec_doubles.document_system.mime_type.double_mime_type import \
    MimeTypeMock
from blackfennec_doubles.structure.double_map import MapMock
from blackfennec_doubles.structure.double_string import StringMock
from core.structure.actions.paste import PasteAction
from doubles.double_dummy import Dummy

logger = logging.getLogger(__name__)


@pytest.fixture
def serialized_structure():
    return "serialized_structure"


@pytest.fixture
def structure(serialized_structure):
    return String(serialized_structure)


@pytest.fixture
def mime_type(structure):
    return MimeTypeMock(imported_structure=structure)


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
def action(action_type, document_registry, monkeypatch, structure):
    action = PasteAction(action_type, document_registry)

    def _get_structure_from_clipboard_async(
            mime_type: MimeTypeMock,
            callback: callable,
    ):
        callback(String("value_from_clipboard"))

    monkeypatch.setattr(
        action,
        '_get_structure_from_clipboard_async',
        _get_structure_from_clipboard_async
    )
    return action


def test_can_construct(action):
    assert action is not None


def test_can_execute_with_map_parent(action, structure, serialized_structure):
    context = ContextMock()
    parent_map = Map({"key": structure})
    context.structure = structure
    action.execute(context)
    assert parent_map.value["key"].value == "value_from_clipboard"


def test_can_execute_with_list_parent(action, structure, serialized_structure):
    context = ContextMock()
    parent_list = List([structure])
    context.structure = structure
    action.execute(context)
    assert parent_list.value[0].value == "value_from_clipboard"


def test_can_execute_with_no_parent(action, structure, serialized_structure):
    context = ContextMock()
    context.structure = structure
    action.execute(context)
    assert structure.value == "value_from_clipboard"


def test_can_execute_with_different_structures_with_no_parent(
        action,
        structure,
        serialized_structure
):
    context = ContextMock()
    context.structure = Number(1)
    with pytest.raises(TypeError):
        action.execute(context)


def test_is_correct_type(action, action_type):
    assert action.type is action_type


def test_has_correct_name(action):
    assert action.name == "replace with clipboard"


def test_has_correct_description(action):
    assert len(action.description) > 7
