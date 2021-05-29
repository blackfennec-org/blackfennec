import logging

from src.black_fennec.interpretation.auction.offer import Offer
from src.black_fennec.structure.structure import Structure
from src.visualisation.core.number.number_template import NumberTemplate
from src.visualisation.core.number.number_view_factory import NumberViewFactory

logger = logging.getLogger(__name__)


class NumberBidder:
    """The bidding service for the core type `Number`."""

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
        return Offer(subject, 0, NumberTemplate(), NumberViewFactory())
