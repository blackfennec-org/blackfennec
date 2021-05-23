from src.black_fennec.structure.info import Info
from src.visualisation.core.reference.reference_template import ReferenceTemplate
from src.visualisation.core.reference.reference_view_factory import ReferenceViewFactory
from src.black_fennec.interpretation.auction.offer import Offer

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
        return Offer(subject, 0, ReferenceTemplate(), self._factory)
