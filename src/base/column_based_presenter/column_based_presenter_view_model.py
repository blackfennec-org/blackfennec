# -*- coding: utf-8 -*-
import logging

from src.core.types.info import Info
from src.core.interpretation import Interpretation
from src.core.interpretation_service import InterpretationService
from src.util.observable import Observable

logger = logging.getLogger(__name__)


class ColumnBasedPresenterViewModel(Observable):
    """Column-Based Presenter View Model class.

    View model of ColumnBasedPresenterView containing interpretations.
    Inherits from observable, to allow ColumnBasedPresenterView to
    bind to interpretations to be notified of changes by this class.

    Attributes:
        __infos (dict): stores infos of corresponding interpretation
        interpretations (list): stores list of interpretations
            notifies on changes in attribute.
    """

    def __init__(self):
        """ColumnBasedPresenterViewModel constructor.

        Initialises attributes with empty dict/list
        """
        super().__init__()
        self.__infos = dict()
        self.interpretations = list()

    def show(
            self,
            sender: Interpretation,
            info: Info,
            interpretation_service: InterpretationService
    ):
        """Show of interpretation.

        Procedure invoked by navigation service to navigate
        in data structure.

        Args:
            sender (Interpretation): interpretation calling navigation
            info (Info): info corresponding with interpretation_service
            interpretation_service (InterpretationService): Producer of interpretation for
                info passed.
        """
        logger.debug("show info (%s) for sender (%s)", info, sender)
        self._try_cut_interpretations_at(sender)
        interpretation = interpretation_service.interpret(info)
        self._add_interpretation(interpretation)

    def _try_cut_interpretations_at(self, sender: Interpretation):
        """Removal of interpretation after sender.

        Cuts interpretations attribute at sender position meaning
        succeeding interpretations are removed. After removal
        notifies observers.

        Args:
            sender (Interpretation): interpretation calling navigation
        """
        if sender in self.__infos:
            index = self.__infos[sender]
            logger.debug(
                "_try_cut_interpretations_at(sender: %s => index: %i)",
                sender, index)
            self.interpretations = self.interpretations[:index]
            self._notify(self.interpretations, "interpretations")

    def _add_interpretation(self, interpretation: Interpretation):
        """Append interpretation to interpretations attribute.

        Appends interpretation at the end of the interpretations
        attribute and notifies observers of change.

        Args:
            interpretation (Interpretation): interpretation to be inserted
        """
        logger.debug("_add_interpretation(%s)", interpretation)
        self.interpretations.append(interpretation)
        self.__infos[interpretation] = len(self.interpretations)
        self._notify(self.interpretations, "interpretations")
