# -*- coding: utf-8 -*-
import unittest
from doubles.double_dummy import Dummy
from src.presentation.column_based_presenter.column_based_presenter_view import ColumnBasedPresenterView
from src.presentation.column_based_presenter.column_based_presenter_view_factory import ColumnBasedPresenterViewFactory


class ColumnBasedPresenterViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        ColumnBasedPresenterViewFactory(
            Dummy('interpretation_service'),
            Dummy('navigation_service')
        )

    def test_can_create_column_based_presenter_view(self):
        factory = ColumnBasedPresenterViewFactory(
            Dummy('interpretation_service'),
            Dummy('navigation_service')
        )
        view = factory.create()
        self.assertIsInstance(view, ColumnBasedPresenterView)
