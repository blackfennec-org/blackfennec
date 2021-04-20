# -*- coding: utf-8 -*-
import logging
from src.structure.info import Info
from src.interpretation.interpretation import Interpretation

logger = logging.getLogger(__name__)

class NavigationProxy:
    """A proxy for navigation requests.

    The navigation proxy dispatches requests to another interpretation.
    """
    def __init__(self, interpretation: Interpretation):
        """Construct NavigationProxy.

        Args:
            interpretation (Interpretation): The interpretation to which
                requests are dipached. In the end, the navigation service
                configured in the interpretation is used.
        """
        self._interpretation = interpretation

    def navigate(self, unused_sender: Interpretation, destination: Info):
        """Navigate to destination, sender is ignored.

        This function dispatches the navigation request to the configured
        interpretation, discarding the sender

        Args:
            sender (Interpretation): Ignored
            destination (Info): destination which will be passed on
        """
        self._interpretation.navigate(destination)
