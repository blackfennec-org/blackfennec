from src.structure.info import Info
from src.structure.reference import Reference
from src.type_system.core.reference.reference_view_factory import ReferenceViewFactory
from src.interpretation.auction import Offer

import logging

logger = logging.getLogger(__name__)


class ReferenceBidder:
    """The bidding service for the core type Reference."""
    def __init__(self):
        """Construct reference bidder."""
        self._factory = ReferenceViewFactory()

    def bid(self, subject: Info):
        """"Produces an offer for a given object.

        Args:
            subject (Info): The Info for which an offer should be produced.

        Returns:
            Offer: that this bidder made on the subject passed.
        """
        logger.info('bidding on object')
        return Offer(subject, 0, Reference.TEMPLATE, self._factory)
