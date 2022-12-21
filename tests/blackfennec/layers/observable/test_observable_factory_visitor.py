import pytest

from blackfennec.layers.observable.observable_factory_visitor import ObservableFactoryVisitor

from blackfennec_doubles.presentation_system.double_history_service import HistoryServiceMock


@pytest.fixture
def history():
    return HistoryServiceMock()

@pytest.fixture
def visitor(history):
    return ObservableFactoryVisitor(history)

def test_can_construct(visitor):
    assert visitor
