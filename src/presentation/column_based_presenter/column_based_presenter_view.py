# -*- coding: utf-8 -*-
import logging
from pathlib import Path

from gi.repository import Gtk, Adw
from src.presentation.column_based_presenter.column_based_presenter_view_model import ColumnBasedPresenterViewModel
from src.black_fennec.interpretation.interpretation import Interpretation
from src.presentation.column_based_presenter.column_view import ColumnView

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('column_based_presenter.ui'))


@Gtk.Template(filename=UI_TEMPLATE)
class ColumnBasedPresenterView(Gtk.ScrolledWindow):
    """ColumnBasedPresenterView Code behind.

    Code behind of the column based presenter. Has ViewModel
    lying behind that is an observable observed by this class.

    Attributes:
        view_model (ColumnBasedPresenterViewModel): stores injected
            view model
        interpretations ([Interpretation]): stores list of interpretations
            shown at the moment. Is updated via view model
    """
    __gtype_name__ = "ColumnBasedPresenterView"
    _empty_list_pattern: Adw.StatusPage = Gtk.Template.Child()
    _loading: Adw.StatusPage = Gtk.Template.Child()
    _error: Adw.StatusPage = Gtk.Template.Child()
    _container: Gtk.Box = Gtk.Template.Child()

    def __init__(self, view_model: ColumnBasedPresenterViewModel, view_factory):
        """ColumnBasedPresenterView constructor.

        Args:
            view_model (ColumnBasedPresenterViewModel): view model
        """
        super().__init__()
        self._view_model = view_model
        self._view_factory = view_factory
        self.view_model = view_model
        self.view_model.bind(interpretations=self._update_interpretations)
        self.interpretations = []
        self._root_column = None

    def set_error(self, error_message):
        """Shows error placeholder"""
        self._empty_list_pattern.set_visible(False)
        self._loading.set_visible(False)
        self._error.set_description(error_message)
        self._error.set_visible(True)

    def _update_interpretations(self, unused_sender, interpretations):
        """interpretation update.

        listener to changes on view_model interpretations property.
        Is registered in constructor to invoke on notifications by
        view model. Only updates if required by searching for
        differences.

        Args:
            sender (): Sender filled by Observable
            interpretations ([interpretations]): updated list of interpretations
        """
        pivot = self._diff_interpretations(
            self.interpretations,
            interpretations)

        for i in range(len(self.interpretations) - 1, pivot - 1, -1):
            current = self.interpretations[i]
            self._remove_interpretation(current)

        for i in range(pivot, len(interpretations)):
            current = interpretations[i]
            self._add_interpretation(current)

    def _remove_interpretation(self, interpretation: Interpretation):
        """interpretation removal.

        Removes interpretation from interpretations attribute
        and view and toggles empty list pattern.

        Args:
            interpretation (Interpretation): interpretation to remove
        """
        logger.debug("remove interpretation %s", interpretation)
        assert self._root_column
        if self._root_column.i_host_interpretation(interpretation):
            self._container.remove(self._root_column)
            self._root_column = None
        else:
            self._root_column.remove_column(interpretation)

        self.interpretations.remove(interpretation)
        self._toggle_empty_list_pattern()

    def _add_interpretation(self, interpretation: Interpretation):
        """interpretation add.

        Adds interpretation to interpretations attribute
        and view and toggles empty list pattern.

        Args:
            interpretation (Interpretation): interpretation to add
        """
        logger.debug("add interpretation %s", interpretation)
        column = ColumnView(interpretation, self._view_factory)
        self.interpretations.append(interpretation)
        if self._root_column is None:
            self._container.append(column)
            self._root_column = column
        else:
            self._root_column.add_column(column)

        self._toggle_empty_list_pattern()

    def _toggle_empty_list_pattern(self):
        """empty list pattern toggle.

        Checks whether interpretations attribute is empty
        or not and show or hides empty list placeholder.
        """
        if not self.interpretations:
            logger.debug("show empty list pattern")
            self._container.set_visible(False)
            self._empty_list_pattern.set_visible(True)
            self._loading.set_visible(False)
            self._error.set_visible(False)
        else:
            logger.debug("hide empty list pattern")
            self._container.set_visible(True)
            self._empty_list_pattern.set_visible(False)
            self._loading.set_visible(False)
            self._error.set_visible(False)

    @staticmethod
    def _diff_interpretations(old, new) -> int:
        """interpretation differences.

        Returns index of first interpretation that is
        different from old interpretations list.

        Args:
            old ([Interpretation]): old interpretation list
            new ([Interpretation]): new interpretation list

        Returns:
            int: index of first interpretation different from
                old interpretation list
        """
        length = min(len(old), len(new))
        for i in range(length):
            current_old = old[i]
            current_new = new[i]
            if not current_new == current_old:
                return i
        return length
