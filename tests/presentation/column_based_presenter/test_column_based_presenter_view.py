# -*- coding: utf-8 -*-
import pytest

from doubles.visualisation.double_view_factory import ViewFactoryMock
from doubles.black_fennec.interpretation.double_interpretation import InterpretationMock
from doubles.presentation.column_based_presenter.double_column_based_presenter_view_model import \
    ColumnBasedPresenterViewModelMock
from doubles.visualisation.double_structure_view import StructureViewDummy
from src.presentation.column_based_presenter.column_based_presenter_view import ColumnBasedPresenterView


def test_can_construct():
    ColumnBasedPresenterView(ColumnBasedPresenterViewModelMock(), ViewFactoryMock())


def test_view_model_update():
    interpretations = list()
    first_structure_view = StructureViewDummy()
    first_interpretation = InterpretationMock(first_structure_view)
    second_structure_view = StructureViewDummy()
    second_interpretation = InterpretationMock(second_structure_view)
    view_model = ColumnBasedPresenterViewModelMock(interpretations)
    view_factory = ViewFactoryMock()
    ColumnBasedPresenterView(view_model, view_factory)

    interpretations.append(first_interpretation)
    view_model._notify(view_model.interpretations, 'interpretations')
    view_model.interpretations.clear()
    view_model.interpretations.append(second_interpretation)
    view_model._notify(view_model.interpretations, 'interpretations')

    assert view_factory.create_call_count == 2
