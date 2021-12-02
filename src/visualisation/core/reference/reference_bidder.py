import logging

from src.black_fennec.interpretation.auction.offer import Offer
from src.black_fennec.structure.structure import Structure
from src.visualisation.core.reference.reference_template import \
    ReferenceTemplate
from src.visualisation.core.reference.reference_view_factory import \
    ReferenceViewFactory

logger = logging.getLogger(__name__)


class ReferenceBidder:
    """The bidding service for the core type Reference."""

    def __init__(self):
        """Construct reference bidder."""
        self._factory = ReferenceViewFactory()

    def bid(self, subject: Structure):
        """"Produces an offer for a given object.

        Args:
            subject (Structure): The Structure for
                which an offer should be produced.

        Returns:
            Offer: that this bidder made on the subject passed.
        """
        logger.info('bidding on object')
        return Offer(subject, 0, ReferenceTemplate(), self._factory)
