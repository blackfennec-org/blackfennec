from src.black_fennec.structure.info import Info
from src.black_fennec.structure.boolean import Boolean
from src.black_fennec.structure.template.template_factory_visitor import TemplateFactoryVisitor
from src.visualisation.core.boolean.boolean_view_factory import BooleanViewFactory
from src.black_fennec.interpretation.auction.offer import Offer

import logging

logger = logging.getLogger(__name__)


def create_boolean_template():
    template_factory = TemplateFactoryVisitor()
    template = Boolean().accept(template_factory)
    return template


class BooleanBidder:
    """The bidding service for the core type `Boolean`.
    """

    def bid(self, subject: Info):
        """"Produces an offer for a given object.

        Args:
            subject (:obj:`Info`): The Info for which an
                offer should be produced.

        Returns:
            Offer: Offer that this type offers for
                the received subject.
        """
        logger.info('bidding on object')
        return Offer(
            subject,
            0,
            create_boolean_template(),
            BooleanViewFactory()
        )
