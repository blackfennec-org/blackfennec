from src.interpretation.interpretation_service import InterpretationService
from src.structure.info import Info
from src.structure.list import List
from src.structure.template.template_factory_visitor import TemplateFactoryVisitor
from src.type_system.core.list.list_view_factory import ListViewFactory
from src.interpretation.auction import Offer

import logging

logger = logging.getLogger(__name__)


def create_list_template():
    template_factory = TemplateFactoryVisitor()
    template = List().accept(template_factory)
    return template


class ListBidder:
    """The bidding service for the core type `List`."""
    def __init__(self, interpretation_service: InterpretationService):
        """Construct list bidder.

        Args:
            interpretation_service (InterpretationService): dependency of
            list view factory
        """
        self._factory = ListViewFactory(interpretation_service)

    def bid(self, subject: Info):
        """"Produces an offer for a given object.

        Args:
            subject (Info): The Info for which an offer should be produced.

        Returns:
            Offer: Offer that this type offers for
                the received subject.
        """
        logger.info('bidding on object')
        return Offer(subject, 0, create_list_template(), self._factory)
