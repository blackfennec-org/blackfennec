# -*- coding: utf-8 -*-
import unittest

from collections import deque

from blackfennec_doubles.double_dummy import Dummy
from blackfennec_doubles.interpretation.double_interpretation import InterpretationMock
from blackfennec_doubles.interpretation.double_interpretation_service import InterpretationServiceMock
from blackfennec_doubles.structure.double_structure import StructureMock
from core.column_based_presenter.column_based_presenter_view_model import ColumnBasedPresenterViewModel


class ColumnBasedPresenterViewModelTestSuite(unittest.TestCase):
    def test_can_construct(self):
        ColumnBasedPresenterViewModel(
            Dummy('interpretation_service'),
            Dummy('navigation_service'))

    def test_show(self):
        structure = StructureMock()
        interpretation = InterpretationMock(structure)
        interpreter = InterpretationServiceMock(deque([interpretation]))
        navigator = Dummy('navigation_service')
        presenter = ColumnBasedPresenterViewModel(interpreter, navigator)

        presenter.show(None, structure)
        self.assertIn(interpretation, presenter.interpretations)
        self.assertEqual(1, interpreter.interpret_count)
        self.assertEqual(interpreter.last_interpreted_structure, structure)

    def test_show_multiple(self):
        structure = StructureMock()
        root_interpretation = InterpretationMock(structure)
        parent_interpretation = InterpretationMock(structure)
        interpretations_queue = deque([
            root_interpretation,
            parent_interpretation])
        interpreter = InterpretationServiceMock(interpretations_queue)
        navigator = Dummy('navigation_service')
        presenter = ColumnBasedPresenterViewModel(interpreter, navigator)

        presenter.show(None, structure)
        presenter.show(root_interpretation, structure)
        self.assertEqual(2, len(presenter.interpretations))
        self.assertIn(parent_interpretation, presenter.interpretations)

    def test_show_with_cut_at(self):
        structure = StructureMock()
        root_interpretation = InterpretationMock(structure)
        parent_interpretation = InterpretationMock(structure)
        child_interpretation = InterpretationMock(structure)
        interpretations_queue = deque([
            root_interpretation,
            parent_interpretation,
            child_interpretation,
            parent_interpretation])
        interpreter = InterpretationServiceMock(interpretations_queue)
        navigator = Dummy('navigation_service')
        presenter = ColumnBasedPresenterViewModel(interpreter, navigator)

        presenter.show(None, structure)
        presenter.show(root_interpretation, structure)
        presenter.show(parent_interpretation, structure)
        presenter.show(root_interpretation, structure)
        self.assertEqual(2, len(presenter.interpretations))
        self.assertNotIn(child_interpretation, presenter.interpretations)
        self.assertIn(parent_interpretation, presenter.interpretations)

    def test_show_sibling(self):
        structure = StructureMock()
        root_interpretation = InterpretationMock(structure)
        parent_interpretation = InterpretationMock(structure)
        child_interpretation = InterpretationMock(structure)
        sibling_interpretation = InterpretationMock(structure)
        interpretations_queue = deque([
            root_interpretation,
            parent_interpretation,
            child_interpretation,
            sibling_interpretation])
        interpreter = InterpretationServiceMock(interpretations_queue)
        navigator = Dummy('navigation_service')
        presenter = ColumnBasedPresenterViewModel(interpreter, navigator)

        presenter.show(None, structure)
        presenter.show(root_interpretation, structure)
        presenter.show(parent_interpretation, structure)
        presenter.show(parent_interpretation, structure)
        self.assertIn(parent_interpretation, presenter.interpretations)
        self.assertIn(sibling_interpretation, presenter.interpretations)
        self.assertNotIn(child_interpretation, presenter.interpretations)
