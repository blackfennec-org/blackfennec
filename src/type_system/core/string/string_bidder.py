from src.structure.info import Info
from src.structure.string import String
from src.type_system.core.string.string_view_factory import StringViewFactory
from src.interpretation.auction import Offer
import logging

logger = logging.getLogger(__name__)


class StringBidder:
    """The bidding service for the core type `String`."""

    def bid(self, subject: Info):
        """"Produces an offer for a given object.

        Args:
            subject (Info): The Info for which an offer should be produced.

        Returns:
            Offer: Offer that this type offers for
                the received subject.
        """
        logger.info('bidding on object')
        return Offer(subject, 0, String(), StringViewFactory())
