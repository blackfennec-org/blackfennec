from src.core.info import Info
from src.core.boolean import Boolean

import logging

logger = logging.getLogger(__name__)


class BooleanBidder:
    """The bidding service for the core type `Boolean`."""

    def bid(self, obj: Info):
        """"Produces an offer for a given object.

        Args:
            obj (:obj:`Info`): The Info for which an offer should be produced.
        """
        logger.info('bidding on object')

        return isinstance(obj, Boolean)
