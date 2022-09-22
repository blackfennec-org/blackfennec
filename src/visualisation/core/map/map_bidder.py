import logging

from src.black_fennec.interpretation.auction.offer import Offer
from src.black_fennec.interpretation.interpretation_service import \
    InterpretationService
from src.black_fennec.structure.structure import Structure
from src.black_fennec.type_system.type_registry import TypeRegistry
from src.black_fennec.structure.type.map_type import MapType
from src.visualisation.core.map.map_view_factory import MapViewFactory

logger = logging.getLogger(__name__)


class MapBidder:
    """The bidding service for the core type Map."""

    def __init__(
            self,
            interpretation_service: InterpretationService,
            type_registry: TypeRegistry):
        """Construct map bidder.

        Args:
            interpretation_service (InterpretationService): used in map view
                model to create children previews
            type_registry (TypeRegistry): used in map view model to
                add new items.

        """
        self._factory = MapViewFactory(
            interpretation_service,
            type_registry)

    def bid(self, subject: Structure):
        """"Produces an offer for a given object.

        Args:
            subject (Structure): The Structure for
                which an offer should be produced.

        Returns:
            Offer: Offer that this type offers for
                the received subject.
        """
        logger.info('bidding on object')
        return Offer(subject, 0, MapType(), self._factory)
