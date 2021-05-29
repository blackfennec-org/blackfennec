# -*- coding: utf-8 -*-
import unittest

from doubles.black_fennec.interpretation.double_interpretation import InterpretationMock
from doubles.presentation.column_based_presenter.double_column_based_presenter_view_model import ColumnBasedPresenterViewModelMock
from doubles.visualisation.double_structure_view import StructureViewDummy
from src.presentation.column_based_presenter.column_based_presenter_view import ColumnBasedPresenterView


class ColumnBasedPresenterViewTestSuite(unittest.TestCase):
    def test_can_construct(self):
        ColumnBasedPresenterView(ColumnBasedPresenterViewModelMock())

    def test_view_model_update(self):
        interpretations = list()
        first_structure_view = StructureViewDummy()
        first_interpretation = InterpretationMock(first_structure_view)
        second_structure_view = StructureViewDummy()
        second_interpretation = InterpretationMock(second_structure_view)
        view_model = ColumnBasedPresenterViewModelMock(interpretations)
        ColumnBasedPresenterView(view_model)

        interpretations.append(first_interpretation)
        view_model._notify(view_model.interpretations, 'interpretations')
        view_model.interpretations.clear()
        view_model.interpretations.append(second_interpretation)
        view_model._notify(view_model.interpretations, 'interpretations')

        self.assertEqual(first_interpretation.view_property_access_count, 1)
        self.assertEqual(second_interpretation.view_property_access_count, 1)
