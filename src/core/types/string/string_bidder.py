from src.core.types.info import Info
from src.core.types.string import String, StringViewFactory
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
        return Offer(subject, 0, String(), StringViewFactory())
