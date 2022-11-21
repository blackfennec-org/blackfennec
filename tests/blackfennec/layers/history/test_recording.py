import pytest

from blackfennec.layers.history.recording import RecordingLayer

from blackfennec_doubles.layers.history.double_history import HistoryMock
from blackfennec_doubles.structure.double_string import StringMock
from blackfennec_doubles.layers.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock

@pytest.fixture
def history():
    return HistoryMock()

@pytest.fixture
def recording(history):
    return RecordingLayer(history)

def test_can_construct(recording):
    assert recording

def test_can_apply(recording):
    expected = StringMock()
    recording._factory = FactoryBaseVisitorMock(returns=expected)
    structure = StringMock()
    assert recording.apply(structure) == expected

def test_can_remember_structure(recording):
    expected = StringMock()
    structure = StringMock()
    recording._factory = FactoryBaseVisitorMock(returns=expected)
    assert recording.apply(structure) == expected
    recording._factory = FactoryBaseVisitorMock(returns=None)
    assert recording.apply(structure) == expected
