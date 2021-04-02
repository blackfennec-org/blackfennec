# -*- coding: utf-8 -*-
from src.base.column_based_presenter.column_based_presenter_view import ColumnBasedPresenterView
from src.base.column_based_presenter.column_based_presenter_view_model import ColumnBasedPresenterViewModel


class ColumnBasedPresenterViewFactory:
    """Creator or the ColumnBasedPresenterView"""

    def create(self) -> ColumnBasedPresenterView:
        """creates a ColumnBasedPresenterView

        Returns:
            ColumnBasedPresenterView: with initialised ViewModel
        """
        view_model = ColumnBasedPresenterViewModel()
        return ColumnBasedPresenterView(view_model)
