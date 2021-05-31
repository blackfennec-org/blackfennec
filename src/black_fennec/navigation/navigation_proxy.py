# -*- coding: utf-8 -*-
import logging
from src.black_fennec.structure.structure import Structure
from src.black_fennec.interpretation.interpretation import Interpretation

logger = logging.getLogger(__name__)

class NavigationProxy:
    """A proxy for navigation requests.

    The navigation proxy dispatches requests to another interpretation.
    """
    def __init__(self, interpretation: Interpretation):
        """Construct NavigationProxy.

        Args:
            interpretation (Interpretation): The interpretation to which
                requests are dispatched. In the end, the navigation service
                configured in the interpretation is used.
        """
        self._interpretation = interpretation

    def navigate(self, unused_sender: Interpretation, destination: Structure):
        """Navigate to destination, sender is ignored.

        This function dispatches the navigation request to the configured
        interpretation, discarding the sender

        Args:
            unused_sender (Interpretation): Ignored
            destination (Structure): destination which will be passed on
        """
        self._interpretation.navigate(destination)
