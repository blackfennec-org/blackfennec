# -*- coding: utf-8 -*-
from core.column_based_presenter.column_based_presenter_view import ColumnBasedPresenterView
from core.column_based_presenter.column_based_presenter_view_model import ColumnBasedPresenterViewModel


class ColumnBasedPresenterViewFactory:
    """Creator or the ColumnBasedPresenterView"""

    def __init__(self, interpretation_service, view_factory):
        self._interpretation_service = interpretation_service
        self._view_factory = view_factory

    def create(self, navigation_service) -> ColumnBasedPresenterView:
        """Create column based presenter view

        Returns:
            ColumnBasedPresenterView: The column based presenter view.
                Can be used as presenter in the main UI.
        """
        view_model = ColumnBasedPresenterViewModel(
            self._interpretation_service,
            navigation_service
        )
        return ColumnBasedPresenterView(view_model, self._view_factory)
