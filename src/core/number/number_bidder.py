from src.core.info import Info
from src.core.number import Number

import logging

logger = logging.getLogger(__name__)


class NumberBidder:
    """The bidding service for the core type `Number`."""

    def bid(self, obj: Info):
        """"Produces an offer for a given object.

        Args:
            obj (:obj:`Info`): The Info for which an offer should be produced.
        """
        logger.info('bidding on object')

        return isinstance(obj, Number)
