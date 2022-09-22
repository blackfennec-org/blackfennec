from src.black_fennec.structure.structure import Structure
from src.black_fennec.structure.type.boolean_type import BooleanType
from src.visualisation.core.boolean.boolean_view_factory import BooleanViewFactory
from src.black_fennec.interpretation.auction.offer import Offer

import logging

logger = logging.getLogger(__name__)


class BooleanBidder:
    """The bidding service for the core type `Boolean`.
    """

    def bid(self, subject: Structure):
        """"Produces an offer for a given object.

        Args:
            subject (Structure): The Structure for which an
                offer should be produced.

        Returns:
            Offer: Offer that this type offers for
                the received subject.
        """
        logger.info('bidding on object')
        return Offer(
            subject,
            0,
            BooleanType(),
            BooleanViewFactory()
        )
