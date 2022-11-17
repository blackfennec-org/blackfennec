# -*- coding: utf-8 -*-
import logging

from blackfennec.layers.history.history import History
from blackfennec.layers.history.history_factory_visitor import \
    HistoryFactoryVisitor
from blackfennec.structure.structure import Structure
from blackfennec.interpretation.interpretation import Interpretation
from blackfennec.interpretation.interpretation_service import \
    InterpretationService
from blackfennec.interpretation.specification import Specification
from blackfennec.navigation.navigation_service import NavigationService
from blackfennec.layers.overlay.overlay_factory_visitor import \
    OverlayFactoryVisitor
from blackfennec.util.observable import Observable

logger = logging.getLogger(__name__)


class ColumnBasedPresenterViewModel(Observable):
    """Column-Based Presenter View Model class.

    View model of ColumnBasedPresenterView containing interpretations.
    Inherits from observable, to allow ColumnBasedPresenterView to
    bind to interpretations to be notified of changes by this class.

    Attributes:
        interpretations (list): stores list of interpretations
            notifies on changes in attribute.
    """

    def __init__(self,
                 interpretation_service: InterpretationService,
                 navigation_service: NavigationService,
                 history: History):
        """Constructor of Column-Based Presenter View Model

        A presenter that arranges interpretations in columns.
            Similar to the MacOS finder, which displays folder hierarchy
            in a similar fassion. This is the default presenter.

        Args:
            interpretation_service (InterpretationService): required for the
                interpretation of structures.
            navigation_service (NavigationService): currently required because
                interpretation service does not configure navigation service
                for new interpretations.
        """
        super().__init__()
        assert interpretation_service, 'interpretation service must not be None'
        assert navigation_service, 'navigation_service must not be None'
        self.interpretations = []
        self._interpretation_service = interpretation_service
        self._navigation_service = navigation_service
        self._history = history

    def set_structure(
            self,
            structure: Structure
    ):
        history_visitor = HistoryFactoryVisitor(self._history)
        historizable = structure.accept(history_visitor)
        overlay_visitor = OverlayFactoryVisitor()
        overlay = historizable.accept(overlay_visitor)
        self.show(None, overlay)

    def show(
            self,
            sender: Interpretation,
            structure: Structure):
        """Show of interpretation.

        Procedure invoked by navigation service to navigate
        in data structure.

        Args:
            sender (Interpretation): interpretation calling navigation
            structure (Structure): structure corresponding
                with interpretation_service
        """
        logger.debug('show structure (%s) for sender (%s)', structure, sender)
        self._try_cut_interpretations_at(sender)
        interpretation = self._interpretation_service.interpret(structure,
                                                                Specification())
        interpretation.set_navigation_service(self._navigation_service)
        self._add_interpretation(interpretation)

    def _try_cut_interpretations_at(self, sender: Interpretation) -> None:
        """Removal of interpretations after sender.

        Cuts interpretation list at position of `sender`, meaning
        succeeding interpretations are removed. Notifies observers.

        Args:
            sender (Interpretation): the callee of the navigation request.
        """
        if sender in self.interpretations:
            index = self.interpretations.index(sender) + 1
            logger.debug(
                '_try_cut_interpretations_at(sender: %s => index: %i)',
                sender, index)
            self.interpretations = self.interpretations[:index]
            self._notify('interpretations', self.interpretations)

    def _add_interpretation(self, interpretation: Interpretation):
        """Append interpretation to interpretations attribute.

        Appends interpretation at the end of the interpretations
        attribute and notifies observers of change.

        Args:
            interpretation (Interpretation): interpretation to be inserted
        """
        logger.debug('_add_interpretation(%s)', interpretation)
        self.interpretations.append(interpretation)
        self._notify('interpretations', self.interpretations)
