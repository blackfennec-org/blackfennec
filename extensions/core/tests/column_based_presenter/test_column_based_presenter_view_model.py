# -*- coding: utf-8 -*-
from collections import deque

import pytest

from blackfennec_doubles.interpretation.double_interpretation import \
    InterpretationMock
from blackfennec_doubles.interpretation.double_interpretation_service import \
    InterpretationServiceMock
from blackfennec_doubles.layers.history.double_history import HistoryMock
from blackfennec_doubles.navigation.double_navigation_service import \
    NavigationServiceMock
from blackfennec_doubles.structure.double_structure import StructureMock
from core.column_based_presenter.column_based_presenter_view_model import \
    ColumnBasedPresenterViewModel


@pytest.fixture
def structure():
    return StructureMock()


@pytest.fixture
def interpretation(structure):
    return InterpretationMock(structure)


@pytest.fixture
def interpretation_service(interpretation):
    return InterpretationServiceMock(deque([interpretation]))


@pytest.fixture
def navigation_service():
    return NavigationServiceMock()


@pytest.fixture
def history():
    return HistoryMock()


@pytest.fixture
def column_based_presenter_view_model(
        interpretation_service,
        navigation_service, history
):
    return ColumnBasedPresenterViewModel(
        interpretation_service,
        navigation_service,
        history
    )


def test_can_construct(column_based_presenter_view_model):
    assert isinstance(
        column_based_presenter_view_model,
        ColumnBasedPresenterViewModel
    )


def test_show(
        column_based_presenter_view_model,
        interpretation_service,
        interpretation,
        structure
):
    column_based_presenter_view_model.show(None, structure)

    assert interpretation in column_based_presenter_view_model.interpretations
    assert interpretation_service.interpret_count == 1
    assert interpretation_service.last_interpreted_structure == structure


def test_show_multiple(
        column_based_presenter_view_model,
        interpretation_service,
        structure
):
    root_interpretation = InterpretationMock(structure)
    parent_interpretation = InterpretationMock(structure)
    interpretations_queue = deque([
        root_interpretation,
        parent_interpretation]
    )
    interpretation_service.interpretations = interpretations_queue

    column_based_presenter_view_model.show(None, structure)
    column_based_presenter_view_model.show(root_interpretation, structure)

    assert len(column_based_presenter_view_model.interpretations) == 2
    assert parent_interpretation in column_based_presenter_view_model \
        .interpretations


def test_show_with_cut_at(
        column_based_presenter_view_model,
        interpretation_service,
        structure
):
    root_interpretation = InterpretationMock(structure)
    parent_interpretation = InterpretationMock(structure)
    child_interpretation = InterpretationMock(structure)
    interpretations_queue = deque([
        root_interpretation,
        parent_interpretation,
        child_interpretation,
        parent_interpretation
    ])
    interpretation_service.interpretations = interpretations_queue

    column_based_presenter_view_model.show(None, structure)
    column_based_presenter_view_model.show(root_interpretation, structure)
    column_based_presenter_view_model.show(parent_interpretation, structure)
    column_based_presenter_view_model.show(root_interpretation, structure)

    assert len(column_based_presenter_view_model.interpretations) == 2
    assert child_interpretation not in column_based_presenter_view_model \
        .interpretations
    assert parent_interpretation in column_based_presenter_view_model \
        .interpretations


def test_show_sibling(
        column_based_presenter_view_model,
        interpretation_service,
        structure
):
    root_interpretation = InterpretationMock(structure)
    parent_interpretation = InterpretationMock(structure)
    child_interpretation = InterpretationMock(structure)
    sibling_interpretation = InterpretationMock(structure)
    interpretations_queue = deque([
        root_interpretation,
        parent_interpretation,
        child_interpretation,
        sibling_interpretation])
    interpretation_service.interpretations = interpretations_queue

    column_based_presenter_view_model.show(None, structure)
    column_based_presenter_view_model.show(root_interpretation, structure)
    column_based_presenter_view_model.show(parent_interpretation, structure)
    column_based_presenter_view_model.show(parent_interpretation, structure)

    assert parent_interpretation in column_based_presenter_view_model \
        .interpretations
    assert sibling_interpretation in column_based_presenter_view_model \
        .interpretations
    assert child_interpretation not in column_based_presenter_view_model \
        .interpretations


def test_set_structure(
        column_based_presenter_view_model,
        interpretation_service,
        structure
):
    column_based_presenter_view_model.set_structure(structure)

    assert interpretation_service.interpret_count == 1
    assert interpretation_service.last_interpreted_structure.structure == structure
