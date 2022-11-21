import pytest

from blackfennec.layers.history.history_factory_visitor import HistoryFactoryVisitor

from blackfennec_doubles.layers.history.double_history import HistoryMock


@pytest.fixture
def history():
    return HistoryMock()

@pytest.fixture
def visitor(history):
    return HistoryFactoryVisitor(history)

def test_can_construct(visitor):
    assert visitor
