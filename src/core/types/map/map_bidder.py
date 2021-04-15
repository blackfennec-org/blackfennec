from src.core.info import Info
from src.core.types.map import Map, MapViewFactory
from src.core.auction import Offer

import logging

logger = logging.getLogger(__name__)


class MapBidder:
    """The bidding service for the core type `Map`."""

    def bid(self, subject: Info):
        """"Produces an offer for a given object.

        Args:
            obj (:obj:`Info`): The Info for which an offer should be produced.
        """
        logger.info('bidding on object')
        return Offer(subject, 0, Map(), MapViewFactory())
