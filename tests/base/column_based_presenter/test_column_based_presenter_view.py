# -*- coding: utf-8 -*-
import unittest

from doubles.base.column_based_presenter_view_model import ColumnBasedPresenterViewModelMock
from doubles.core import InterpretationMock
from doubles.core.info_view import InfoViewDummy
from src.base.column_based_presenter import ColumnBasedPresenterView


class ColumnBasedPresenterViewTestSuite(unittest.TestCase):
    def test_can_construct(self):
        ColumnBasedPresenterView(ColumnBasedPresenterViewModelMock())

    def test_view_model_update(self):
        interpretations = list()
        first_info_view = InfoViewDummy()
        first_interpretation = InterpretationMock(first_info_view)
        interpretations.append(first_interpretation)
        view_model = ColumnBasedPresenterViewModelMock(interpretations)
        ColumnBasedPresenterView(view_model)
        view_model._notify(view_model.interpretations, 'interpretations')
        second_info_view = InfoViewDummy()
        second_interpretation = InterpretationMock(second_info_view)
        view_model.interpretations.clear()
        view_model.interpretations.append(second_interpretation)
        view_model._notify(view_model.interpretations, 'interpretations')
        self.assertEqual(
            first_interpretation.view_property_access_count,
            2,
            msg='Expected view property access count to be two, '
                'once for creation and once for removal of the info view'
        )
        self.assertEqual(
            second_interpretation.view_property_access_count,
            1
        )
