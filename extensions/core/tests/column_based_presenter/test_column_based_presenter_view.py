# -*- coding: utf-8 -*-
import pytest

from blackfennec_doubles.extension.double_view_factory import ViewFactoryMock
from blackfennec_doubles.interpretation.double_interpretation import InterpretationMock
from blackfennec_doubles.extension.double_presenter_view_model import \
    PresenterViewModelMock
from blackfennec_doubles.extension.double_structure_view import StructureViewDummy
from core.column_based_presenter.column_based_presenter_view import ColumnBasedPresenterView


def test_can_construct():
    ColumnBasedPresenterView(PresenterViewModelMock(), ViewFactoryMock())


def test_view_model_update():
    interpretations = list()
    first_structure_view = StructureViewDummy()
    first_interpretation = InterpretationMock(first_structure_view)
    second_structure_view = StructureViewDummy()
    second_interpretation = InterpretationMock(second_structure_view)
    view_model = PresenterViewModelMock(interpretations)
    view_factory = ViewFactoryMock()
    ColumnBasedPresenterView(view_model, view_factory)

    interpretations.append(first_interpretation)
    view_model._notify(view_model.interpretations, 'interpretations')
    view_model.interpretations.clear()
    view_model.interpretations.append(second_interpretation)
    view_model._notify(view_model.interpretations, 'interpretations')

    assert view_factory.create_call_count == 2
