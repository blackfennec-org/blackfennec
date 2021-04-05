# -*- coding: utf-8 -*-
import unittest

from src.base.column_based_presenter import ColumnBasedPresenterViewFactory, ColumnBasedPresenterView


class ColumnBasedPresenterViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        ColumnBasedPresenterViewFactory()

    def test_can_create_column_based_presenter_view(self):
        factory = ColumnBasedPresenterViewFactory()
        view = factory.create()
        self.assertIsInstance(view, ColumnBasedPresenterView)
