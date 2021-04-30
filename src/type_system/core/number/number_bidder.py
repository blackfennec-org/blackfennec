from src.structure.info import Info
from src.structure.number import Number
from src.type_system.core.number.number_view_factory import NumberViewFactory
from src.interpretation.auction import Offer

import logging

logger = logging.getLogger(__name__)


class NumberBidder:
    """The bidding service for the core type `Number`."""

    def bid(self, subject: Info):
        """"Produces an offer for a given object.

        Args:
            subject (Info): The Info for which an offer should be produced.

        Returns:
            Offer: Offer that this type offers for
                the received subject.
        """
        logger.info('bidding on object')
        return Offer(subject, 0, Number(), NumberViewFactory())
