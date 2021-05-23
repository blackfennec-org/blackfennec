from src.black_fennec.structure.info import Info
from src.black_fennec.interpretation.interpretation_service import InterpretationService
from src.visualisation.core.map.map_template import MapTemplate
from src.visualisation.core.map.map_view_factory import MapViewFactory
from src.black_fennec.interpretation.auction.offer import Offer

import logging

logger = logging.getLogger(__name__)


class MapBidder:
    """The bidding service for the core type Map."""
    def __init__(self, interpretation_service: InterpretationService):
        """Construct map bidder.

        Args:
            interpretation_service (InterpretationService): dependency of
                map view factory
        """
        self._factory = MapViewFactory(interpretation_service)

    def bid(self, subject: Info):
        """"Produces an offer for a given object.

        Args:
            subject (Info): The Info for which an offer should be produced.

        Returns:
            Offer: Offer that this type offers for
                the received subject.
        """
        logger.info('bidding on object')
        return Offer(subject, 0, MapTemplate(), self._factory)
