from src.core.info import Info
from src.core.types.list import List, ListViewFactory
from src.core.auction import Offer

import logging

logger = logging.getLogger(__name__)


class ListBidder:
    """The bidding service for the core type `List`."""

    def bid(self, subject: Info):
        """"Produces an offer for a given object.

        Args:
            obj (:obj:`Info`): The Info for which an offer should be produced.
        """
        logger.info('bidding on object')
        return Offer(subject, 0, List(), ListViewFactory())
