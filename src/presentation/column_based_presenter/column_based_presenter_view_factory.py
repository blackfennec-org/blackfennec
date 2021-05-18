# -*- coding: utf-8 -*-
from src.presentation.column_based_presenter.column_based_presenter_view import ColumnBasedPresenterView
from src.presentation.column_based_presenter.column_based_presenter_view_model import ColumnBasedPresenterViewModel


class ColumnBasedPresenterViewFactory:
    """Creator or the ColumnBasedPresenterView"""
    def __init__(self, interpretation_service, navigation_service):
        self._interpretation_service = interpretation_service
        self._navigation_service = navigation_service

    def create(self) -> ColumnBasedPresenterView:
        """Create column based presenter view

        Returns:
            ColumnBasedPresenterView: The column based presenter view.
                Can be used as presenter in the main UI.
        """
        view_model = ColumnBasedPresenterViewModel(
            self._interpretation_service,
            self._navigation_service
        )
        return ColumnBasedPresenterView(view_model)
