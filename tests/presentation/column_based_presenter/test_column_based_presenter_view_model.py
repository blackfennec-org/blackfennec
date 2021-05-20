# -*- coding: utf-8 -*-
import unittest

from collections import deque

from doubles.double_dummy import Dummy
from doubles.black_fennec.interpretation.double_interpretation import InterpretationMock
from doubles.black_fennec.interpretation.double_interpretation_service import InterpretationServiceMock
from doubles.black_fennec.structure.double_info import InfoMock
from src.presentation.column_based_presenter.column_based_presenter_view_model import ColumnBasedPresenterViewModel


class ColumnBasedPresenterViewModelTestSuite(unittest.TestCase):
    def test_can_construct(self):
        ColumnBasedPresenterViewModel(
            Dummy('interpretation_service'),
            Dummy('navigation_service'))

    def test_show(self):
        info = InfoMock()
        interpretation = InterpretationMock(info)
        interpreter = InterpretationServiceMock(deque([interpretation]))
        navigator = Dummy('navigation_service')
        presenter = ColumnBasedPresenterViewModel(interpreter, navigator)

        presenter.show(None, info)
        self.assertIn(interpretation, presenter.interpretations)
        self.assertEqual(1, interpreter.interpret_count)
        self.assertEqual(interpreter.last_interpreted_info, info)

    def test_show_multiple(self):
        info = InfoMock()
        root_interpretation = InterpretationMock(info)
        parent_interpretation = InterpretationMock(info)
        interpretations_queue = deque([
            root_interpretation,
            parent_interpretation])
        interpreter = InterpretationServiceMock(interpretations_queue)
        navigator = Dummy('navigation_service')
        presenter = ColumnBasedPresenterViewModel(interpreter, navigator)

        presenter.show(None, info)
        presenter.show(root_interpretation, info)
        self.assertEqual(2, len(presenter.interpretations))
        self.assertIn(parent_interpretation, presenter.interpretations)

    def test_show_with_cut_at(self):
        info = InfoMock()
        root_interpretation = InterpretationMock(info)
        parent_interpretation = InterpretationMock(info)
        child_interpretation = InterpretationMock(info)
        interpretations_queue = deque([
            root_interpretation,
            parent_interpretation,
            child_interpretation,
            parent_interpretation])
        interpreter = InterpretationServiceMock(interpretations_queue)
        navigator = Dummy('navigation_service')
        presenter = ColumnBasedPresenterViewModel(interpreter, navigator)

        presenter.show(None, info)
        presenter.show(root_interpretation, info)
        presenter.show(parent_interpretation, info)
        presenter.show(root_interpretation, info)
        self.assertEqual(2, len(presenter.interpretations))
        self.assertNotIn(child_interpretation, presenter.interpretations)
        self.assertIn(parent_interpretation, presenter.interpretations)

    def test_show_sibling(self):
        info = InfoMock()
        root_interpretation = InterpretationMock(info)
        parent_interpretation = InterpretationMock(info)
        child_interpretation = InterpretationMock(info)
        sibling_interpretation = InterpretationMock(info)
        interpretations_queue = deque([
            root_interpretation,
            parent_interpretation,
            child_interpretation,
            sibling_interpretation])
        interpreter = InterpretationServiceMock(interpretations_queue)
        navigator = Dummy('navigation_service')
        presenter = ColumnBasedPresenterViewModel(interpreter, navigator)

        presenter.show(None, info)
        presenter.show(root_interpretation, info)
        presenter.show(parent_interpretation, info)
        presenter.show(parent_interpretation, info)
        self.assertIn(parent_interpretation, presenter.interpretations)
        self.assertIn(sibling_interpretation, presenter.interpretations)
        self.assertNotIn(child_interpretation, presenter.interpretations)
