from src.core.info import Info
from src.core.list import List

import logging

logger = logging.getLogger(__name__)


class ListBidder:
    """The bidding service for the core type `List`."""

    def bid(self, obj: Info):
        """"Produces an offer for a given object.

        Args:
            obj (:obj:`Info`): The Info for which an offer should be produced.
        """
        logger.info('bidding on object')

        return isinstance(obj, List)
