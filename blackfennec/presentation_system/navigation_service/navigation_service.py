# -*- coding: utf-8 -*-
import logging
from blackfennec.structure.structure import Structure
from blackfennec.type_system.interpretation.interpretation import Interpretation

logger = logging.getLogger(__name__)


class NavigationService:
    """Navigation Service Class.

    Can be called by an interpretation for navigational purposes.
    Class resolves route through auctioneer and dispatches navigation
    request to structure presenter.

    Attributes:
        _presenter (StructurePresenter): stores injected
            structure presenter
    """

    def __init__(self):
        """Navigation Service constructor."""
        self._presenter = None

    def set_presenter(self, presenter):
        """Set target for navigation requests

        Args:
            presenter: The presenter must have the `show` method
        """
        self._presenter = presenter

    def navigate(self, sender: Interpretation, destination: Structure):
        """Navigation request dispatch

        Dispatches navigation request received by Interpretation
        to column_based_presenter to show navigation with the help
        of the received interpretation_service

        Args:
            sender (Interpretation): Interpretation which invoked navigation
            destination (Structure): Destination to which shall be navigated

        Raises:
            AssertionError: if no presenter is set for navigation_service.
                can be done with set_presenter()
        """
        logger.info('%s requested navigation to %s', sender, destination)
        if not self._presenter:
            message = 'Navigate called without presenter set'
            logger.error(message)
            raise AssertionError(message)
        self._presenter.show(sender, destination)
