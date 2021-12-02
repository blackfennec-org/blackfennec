import logging

from src.black_fennec.interpretation.auction.offer import Offer
from src.black_fennec.structure.structure import Structure
from src.visualisation.core.string.string_template import StringTemplate
from src.visualisation.core.string.string_view_factory import StringViewFactory

logger = logging.getLogger(__name__)


class StringBidder:
    """The bidding service for the core type `String`."""

    def bid(self, subject: Structure):
        """"Produces an offer for a given object.

        Args:
            subject (Structure): The Structure for
                which an offer should be produced.

        Returns:
            Offer: Offer that this type offers for
                the received subject.
        """
        logger.info('bidding on object')
        return Offer(subject, 0, StringTemplate(), StringViewFactory())
