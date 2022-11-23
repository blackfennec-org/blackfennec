import pytest

from blackfennec_doubles.structure.double_string import StringMock
from blackfennec_doubles.layers.double_layer import LayerMock
from blackfennec.layers.encapsulation_base.encapsulation_base import \
    EncapsulationBase
from blackfennec.layers.encapsulation_base.map_encapsulation_base import \
    MapEncapsulationBase
from blackfennec.layers.encapsulation_base.base_factory_visitor import \
    _create_generic_class
from blackfennec.structure.map import Map
from tests.test_utils.observer import Observer


@pytest.fixture
def layer():
    return LayerMock()


@pytest.fixture
def subject():
    return Map()


@pytest.fixture
def map_encapsulation_base(layer, subject) -> MapEncapsulationBase:
    return MapEncapsulationBase(layer=layer, subject=subject)


def test_can_construct(map_encapsulation_base):
    assert isinstance(map_encapsulation_base, MapEncapsulationBase)


def test_subject_getter(map_encapsulation_base, subject):
    assert map_encapsulation_base.subject == subject


def test_add_item_item(map_encapsulation_base):
    key = 'test'
    value = StringMock('test_value')
    map_encapsulation_base.add_item(key, value)
    assert value == map_encapsulation_base.subject.value[key]


def test_add_item_item_already_encapsulated(map_encapsulation_base, layer):
    key = 'test'
    value = StringMock('test_value')
    type_class = _create_generic_class(EncapsulationBase)
    encapsulated = type_class(layer=layer, subject=value)
    map_encapsulation_base.add_item(key, encapsulated)
    assert value == map_encapsulation_base.subject.value[key]


def test_get_value(layer):
    key = 'test'
    subject = Map({key: StringMock('test')})
    expected = StringMock('test')
    layer.returns = expected
    map_encapsulation_base = MapEncapsulationBase(
        layer=layer,
        subject=subject
    )
    value = map_encapsulation_base.value
    assert {key: expected} == value


def test_can_get_value_empty(map_encapsulation_base):
    assert isinstance(map_encapsulation_base.value, dict)


def test_set_value(map_encapsulation_base):
    key = 'test'
    value = StringMock('test')
    map_encapsulation_base.value = {key: value}
    assert value == map_encapsulation_base.subject.value[key]


def test_remove_item(map_encapsulation_base, subject):
    key = 'test'
    value = StringMock('test')
    subject.add_item(key, value)
    map_encapsulation_base.remove_item(key)
    assert len(subject.value) == 0


def test_remove_item_not_in_map(map_encapsulation_base):
    key = 'test'
    with pytest.raises(KeyError):
        map_encapsulation_base.remove_item(key)


def test_replace_item(map_encapsulation_base):
    key = 'test'
    value = StringMock('test')
    map_encapsulation_base.add_item(key, value)
    new_value = StringMock('new_value')
    map_encapsulation_base.replace_item(key, new_value)
    assert new_value == map_encapsulation_base.subject.value[key]


def test_rename_key(map_encapsulation_base):
    key = 'test'
    new_key = 'new_test'
    value = StringMock('test')
    map_encapsulation_base.add_item(key, value)
    map_encapsulation_base.rename_key(key, new_key)
    assert new_key in map_encapsulation_base.subject.value
    assert key not in map_encapsulation_base.subject.value


def test_dispatch_change_notification(
        map_encapsulation_base,
        layer,
        subject
):
    key = 'test'
    observer = Observer()
    map_encapsulation_base.bind(changed=observer.endpoint)
    item = StringMock('test')
    map_encapsulation_base.add_item(key, item)

    assert observer.last_call[0][0] == subject
    assert layer.get_stats(item)[0] == 1


def test_can_get_repr(map_encapsulation_base):
    representation: str = map_encapsulation_base.__repr__()
    assert representation.startswith('MapEncapsulationBase(')
