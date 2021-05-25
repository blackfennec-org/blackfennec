from src.black_fennec.structure.info import Info
from src.black_fennec.type_system.template_registry import TemplateRegistry
from src.black_fennec.interpretation.interpretation_service import InterpretationService
from src.visualisation.core.map.map_template import MapTemplate
from src.visualisation.core.map.map_view_factory import MapViewFactory
from src.black_fennec.interpretation.auction.offer import Offer

import logging

logger = logging.getLogger(__name__)


class MapBidder:
    """The bidding service for the core type Map."""
    def __init__(
            self,
            interpretation_service: InterpretationService,
            template_registry: TemplateRegistry):

        """Construct map bidder.

        Args:
            interpretation_service (InterpretationService): used in map view
                model to create children previews
            template_registry (TemplateRegistry): used in map view model to
                add new items.

        """
        self._factory = MapViewFactory(
            interpretation_service,
            template_registry )


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
