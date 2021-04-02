from src.core.info import Info
from src.core.string import String
from src.core.auction import Offer
import logging

logger = logging.getLogger(__name__)


class StringBidder:
    """The bidding service for the core type `String`."""

    def bid(self, subject: Info):
        """"Produces an offer for a given object.

        Args:
            obj (:obj:`Info`): The Info for which an offer should be produced.
        """
        logger.info('bidding on object')

        if isinstance(subject, String):
            return Offer(subject, 0, 1.0)
        return Offer(subject, 0, 0)
