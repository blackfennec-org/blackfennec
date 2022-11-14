# -*- coding: utf-8 -*-
import logging
from blackfennec.util.observable import Observable
from blackfennec.structure.structure import Structure
from blackfennec.interpretation.interpretation import Interpretation

logger = logging.getLogger(__name__)


class NavigationProxy(Observable):
    """A proxy for navigation requests.

    The navigation proxy dispatches requests to another interpretation.
    """

    def __init__(self):
        """Construct NavigationProxy.

        Args:
            interpretation (Interpretation): The interpretation to which
                requests are dispatched. In the end, the navigation service
                configured in the interpretation is used.
        """
        Observable.__init__(self)

    def navigate(self, sender: Interpretation, destination: Structure):
        """Navigate to destination, sender is ignored.

        This function dispatches the navigation request to the configured
        interpretation, discarding the sender

        Args:
            sender (Interpretation): Ignored
            destination (Structure): destination which will be passed on
        """
        self._notify('navigation_request', destination, sender)
