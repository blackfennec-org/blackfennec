from src.core.info import Info
from src.core.boolean import Boolean, BooleanViewFactory
from src.core.auction import Offer

import logging

logger = logging.getLogger(__name__)


class BooleanBidder:
    """The bidding service for the core type `Boolean`.
    """

    def bid(self, subject: Info):
        """"Produces an offer for a given object.

        Args:
            subject (:obj:`Info`): The Info for which an
                offer should be produced.
        """
        logger.info('bidding on object')

        if isinstance(subject, Boolean):
            return Offer(subject, 0, 1.0, BooleanViewFactory())
        return Offer(subject, 0, 0, BooleanViewFactory())
