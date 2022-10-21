import pytest

from doubles.black_fennec.interpretation.double_interpretation import InterpretationMock
from doubles.visualisation.double_view_factory import ViewFactoryMock
from src.presentation.column_based_presenter.column_view import ColumnView
from gi.repository import Gtk


@pytest.fixture()
def interpretation():
    return InterpretationMock()


@pytest.fixture()
def view_factory():
    return ViewFactoryMock()


@pytest.fixture
def column_view(interpretation, view_factory):
    return ColumnView(interpretation, view_factory)


def test_can_construct_column_view(column_view):
    assert isinstance(column_view, ColumnView)


def test_add_column(column_view):
    column_view.add_column(Gtk.Label())


def test_remove_column(column_view, interpretation):
    label = Gtk.Label()
    label.i_host_interpretation = lambda x: interpretation
    column_view.add_column(label)
    column_view.remove_column(interpretation)
