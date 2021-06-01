import logging

from src.black_fennec.interpretation.auction.offer import Offer
from src.black_fennec.interpretation.interpretation_service import \
    InterpretationService
from src.black_fennec.structure.structure import Structure
from src.black_fennec.type_system.template_registry import TemplateRegistry
from src.visualisation.core.list.list_template import ListTemplate
from src.visualisation.core.list.list_view_factory import ListViewFactory

logger = logging.getLogger(__name__)


class ListBidder:
    """The bidding service for the core type `List`."""
    def __init__(
            self,
            interpretation_service: InterpretationService,
            template_registry: TemplateRegistry
    ):
        """Construct list bidder.

        Args:
            interpretation_service (InterpretationService): used in list view
                model to create children previews
            template_registry (TemplateRegistry): used in list view model to
                add new items.
        """
        self._factory = ListViewFactory(
            interpretation_service,
            template_registry
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
        return Offer(subject, 0, ListTemplate(), self._factory)
