from src.black_fennec.structure.structure import Structure
from src.black_fennec.structure.map import Map
from src.black_fennec.interpretation.interpretation_service import InterpretationService
from src.black_fennec.structure.template.template_factory_visitor import TemplateFactoryVisitor
from src.visualisation.core.map.map_view_factory import MapViewFactory
from src.black_fennec.interpretation.auction.offer import Offer

import logging

logger = logging.getLogger(__name__)


def create_map_template():
    template_factory = TemplateFactoryVisitor()
    template = Map().accept(template_factory)
    return template


class MapBidder:
    """The bidding service for the core type Map."""
    def __init__(self, interpretation_service: InterpretationService):
        """Construct map bidder.

        Args:
            interpretation_service (InterpretationService): dependency of
                map view factory
        """
        self._factory = MapViewFactory(interpretation_service)

    def bid(self, subject: Structure):
        """"Produces an offer for a given object.

        Args:
            subject (Structure): The Structure for which an offer should be produced.

        Returns:
            Offer: Offer that this type offers for
                the received subject.
        """
        logger.info('bidding on object')
        return Offer(subject, 0, create_map_template(), self._factory)
