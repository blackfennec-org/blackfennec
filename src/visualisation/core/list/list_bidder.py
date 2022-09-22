import logging

from src.black_fennec.interpretation.auction.offer import Offer
from src.black_fennec.interpretation.interpretation_service import \
    InterpretationService
from src.black_fennec.structure.structure import Structure
from src.black_fennec.type_system.type_registry import TypeRegistry
from src.black_fennec.structure.type.list_type import ListType
from src.visualisation.core.list.list_view_factory import ListViewFactory

logger = logging.getLogger(__name__)


class ListBidder:
    """The bidding service for the core type `List`."""

    def __init__(
            self,
            interpretation_service: InterpretationService,
            type_registry: TypeRegistry
    ):
        """Construct list bidder.

        Args:
            interpretation_service (InterpretationService): used in list view
                model to create children previews
            type_registry (TypeRegistry): used in list view model to
                add new items.
        """
        self._factory = ListViewFactory(
            interpretation_service,
            type_registry
        )

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
        return Offer(subject, 0, ListType(), self._factory)
