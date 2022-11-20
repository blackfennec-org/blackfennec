from typing import Optional

import pytest

from blackfennec.layers.encapsulation_base.base_factory_visitor import \
    _create_generic_class
from blackfennec.layers.encapsulation_base.encapsulation_base import \
    EncapsulationBase
from blackfennec.layers.encapsulation_base.list_encapsulation_base import \
    ListEncapsulationBase
from blackfennec.structure.list import List
from blackfennec_doubles.layers.encapsulation_base.double_factory_base_visitor \
    import FactoryBaseVisitorMock
from blackfennec_doubles.structure.double_string import StringMock
from tests.test_utils.observer import Observer


@pytest.fixture
def visitor():
    return FactoryBaseVisitorMock()


@pytest.fixture
def subject():
    return List()


@pytest.fixture
def list_encapsulation_base(visitor, subject) -> ListEncapsulationBase:
    return ListEncapsulationBase(visitor, subject)


def test_can_construct(list_encapsulation_base):
    assert isinstance(list_encapsulation_base, ListEncapsulationBase)


def test_subject_getter(list_encapsulation_base, subject):
    assert list_encapsulation_base.subject == subject


def test_add_item_item(list_encapsulation_base):
    value = StringMock('test_value')
    list_encapsulation_base.add_item(value)
    assert value in list_encapsulation_base.subject.value


def test_add_item_item_already_encapsulated(list_encapsulation_base, visitor):
    value = StringMock('test_value')
    type_class = _create_generic_class(EncapsulationBase)
    encapsulated = type_class(visitor, value)
    list_encapsulation_base.add_item(encapsulated)
    assert value in list_encapsulation_base.subject.value


def test_get_value(visitor):
    subject_content = StringMock('test')
    subject = List([subject_content])
    list_encapsulation_base = ListEncapsulationBase(
        visitor,
        subject
    )
    value = list_encapsulation_base.value
    assert subject_content == value[0]


def test_can_get_value_empty(list_encapsulation_base):
    assert isinstance(list_encapsulation_base.value, list)


def test_set_value(list_encapsulation_base):
    value = StringMock('test')
    list_encapsulation_base.value = [value]
    assert value in list_encapsulation_base.subject.value


def test_remove_item(visitor):
    value = StringMock('test_value')
    subject = List([value])
    list_type: Optional[ListEncapsulationBase] = ListEncapsulationBase(
        visitor,
        subject
    )
    list_type.remove_item(value)
    assert len(subject.value) == 0


def test_remove_encapsulated_item(visitor):
    value = StringMock('test_value')
    subject = List([value])
    list_type = ListEncapsulationBase(
        visitor,
        subject
    )
    type_class = _create_generic_class(EncapsulationBase)
    encapsulated = type_class(visitor, value)
    list_type.remove_item(encapsulated)
    assert len(subject.value) == 0


def test_dispatch_change_notification(
        list_encapsulation_base,
        visitor,
        subject
):
    observer = Observer()
    list_encapsulation_base.bind(changed=observer.endpoint)

    list_encapsulation_base.add_item(StringMock('test'))

    assert observer.last_call[0][0] == subject
    assert visitor.visit_string_count == 1


def test_can_get_repr(list_encapsulation_base):
    representation: str = list_encapsulation_base.__repr__()
    assert representation.startswith('ListEncapsulationBase(')
