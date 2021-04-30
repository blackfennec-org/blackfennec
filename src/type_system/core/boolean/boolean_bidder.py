from src.structure.info import Info
from src.structure.boolean import Boolean
from src.type_system.core.boolean.boolean_view_factory import BooleanViewFactory
from src.interpretation.auction import Offer

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

        Returns:
            Offer: Offer that this type offers for
                the received subject.
        """
        logger.info('bidding on object')
        return Offer(subject, 0, Boolean(), BooleanViewFactory())