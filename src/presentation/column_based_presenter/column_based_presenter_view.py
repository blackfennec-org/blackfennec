# -*- coding: utf-8 -*-
import logging

from gi.repository import Gtk
from src.presentation.column_based_presenter.column_based_presenter_view_model import ColumnBasedPresenterViewModel
from src.black_fennec.interpretation.interpretation import Interpretation
from src.presentation.column_based_presenter.column_view import ColumnView

logger = logging.getLogger(__name__)


@Gtk.Template(
    filename="src/presentation/column_based_presenter/column_based_presenter.glade")  # pylint: disable=line-too-long
class ColumnBasedPresenterView(Gtk.Box):
    """ColumnBasedPresenterView Code behind.

    Code behind of the column based presenter. Has ViewModel
    lying behind that is an observable observed by this class.

    Attributes:
        _view_model (ColumnBasedPresenterViewModel): stores injected
            view model
        interpretations ([Interpretation]): stores list of interpretations
            shown at the moment. Is updated via view model
    """
    __gtype_name__ = "ColumnBasedPresenterView"
    _empty_list_pattern = Gtk.Template.Child()

    def __init__(self, view_model: ColumnBasedPresenterViewModel, view_factory):
        """ColumnBasedPresenterView constructor.

        Args:
            view_model (ColumnBasedPresenterViewModel): view model
        """
        super().__init__()
        self._view_model = view_model
        self._view_factory = view_factory
        self._view_model.bind(interpretations=self._update_interpretations)
        self.interpretations = []
        self._root_column = None

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
            self.remove(self._root_column)
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
            self.add(column)
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
            self.add(self._empty_list_pattern)
            self._empty_list_pattern.show_all()
        else:
            logger.debug("hide empty list pattern")
            self.remove(self._empty_list_pattern)
            self._empty_list_pattern.hide()

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
