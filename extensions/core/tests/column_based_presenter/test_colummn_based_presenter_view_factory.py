# -*- coding: utf-8 -*-
import pytest
from blackfennec_doubles.double_dummy import Dummy
from core.column_based_presenter.column_based_presenter_view import \
    ColumnBasedPresenterView
from core.column_based_presenter.column_based_presenter_view_factory import \
    ColumnBasedPresenterViewFactory


@pytest.fixture
def factory():
    return ColumnBasedPresenterViewFactory(
        Dummy('interpretation_service'), Dummy('view_factory'))


def test_can_construct(factory):
    assert factory is not None


def test_can_create_column_based_presenter_view(factory):
    view = factory.create(Dummy('navigation_service'), Dummy('history'))
    assert isinstance(view, ColumnBasedPresenterView)
