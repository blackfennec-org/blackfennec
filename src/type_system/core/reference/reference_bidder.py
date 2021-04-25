from src.structure.info import Info
from src.structure.reference import Reference
from src.interpretation.interpretation_service import InterpretationService
from src.type_system.core.reference.reference_view_factory import ReferenceViewFactory
from src.interpretation.auction import Offer

import logging

logger = logging.getLogger(__name__)


class ReferenceBidder:
    """The bidding service for the core type Reference."""
    def __init__(self, interpretation_service: InterpretationService):
        """Construct reference bidder.

        Args:
            interpretation_service (InterpretationService): dependency of
                reference view factory
        """
        self._factory = ReferenceViewFactory(interpretation_service)

    def bid(self, subject: Info):
        """"Produces an offer for a given object.

        Args:
            subject (Info): The Info for which an offer should be produced.
        """
        logger.info('bidding on object')
        return Offer(subject, 1, Reference.TEMPLATE, self._factory)
