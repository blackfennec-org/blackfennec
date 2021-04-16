# -*- coding: utf-8 -*-
import unittest

from doubles.interpretation.interpretation import InterpretationMock
from doubles.interpretation.interpretation_service import InterpretationServiceMock
from doubles.structure.info import InfoMock
from src.presentation.column_based_presenter.column_based_presenter_view_model import ColumnBasedPresenterViewModel


class ColumnBasedPresenterViewModelTestSuite(unittest.TestCase):
    def test_can_construct(self):
        ColumnBasedPresenterViewModel()

    def test_show(self):
        column_based_presenter_view_model = ColumnBasedPresenterViewModel()
        info = InfoMock()
        sender = InterpretationMock(info)
        interpreter = InterpretationServiceMock(sender)
        column_based_presenter_view_model.show(sender, info, interpreter)
        self.assertIn(
            sender,
            column_based_presenter_view_model.interpretations
        )
        self.assertEqual(
            interpreter.interpret_count,
            1
        )
        self.assertEqual(
            interpreter.last_interpreted_info,
            info
        )

    def test_show_with_cut_at(self):
        column_based_presenter_view_model = ColumnBasedPresenterViewModel()
        info = InfoMock()
        root = InterpretationMock(info)
        root_interpreter = InterpretationServiceMock(root)
        column_based_presenter_view_model.show(root, info, root_interpreter)
        parent_interpretation = InterpretationMock(info)
        parent_interpreter = InterpretationServiceMock(parent_interpretation)
        column_based_presenter_view_model.show(root, info, parent_interpreter)
        self.assertEqual(
            len(column_based_presenter_view_model.interpretations),
            2
        )
        child_interpretation = InterpretationMock(info)
        child_interpreter = InterpretationServiceMock(child_interpretation)
        column_based_presenter_view_model.show(
            parent_interpretation,
            info,
            child_interpreter
        )
        self.assertEqual(
            len(column_based_presenter_view_model.interpretations),
            3
        )
        column_based_presenter_view_model.show(root, info, parent_interpreter)
        self.assertEqual(
            len(column_based_presenter_view_model.interpretations),
            2
        )
        self.assertNotIn(
            child_interpretation,
            column_based_presenter_view_model.interpretations
        )
        self.assertIn(
            parent_interpretation,
            column_based_presenter_view_model.interpretations
        )
        self.assertEqual(root_interpreter.interpret_count, 1)
        self.assertEqual(root_interpreter.last_interpreted_info, info)
        self.assertEqual(parent_interpreter.interpret_count, 2)
        self.assertEqual(parent_interpreter.last_interpreted_info, info)
        self.assertEqual(child_interpreter.interpret_count, 1)
        self.assertEqual(child_interpreter.last_interpreted_info, info)
