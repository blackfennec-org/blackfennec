from src.black_fennec.structure.info import Info
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.template.template_factory_visitor import TemplateFactoryVisitor
from src.visualisation.core.number.number_view_factory import NumberViewFactory
from src.black_fennec.interpretation.auction.offer import Offer

import logging

logger = logging.getLogger(__name__)


def create_number_template():
    template_factory = TemplateFactoryVisitor()
    template = Number().accept(template_factory)
    return template


class NumberBidder:
    """The bidding service for the core type `Number`."""

    def bid(self, subject: Info):
        """"Produces an offer for a given object.

        Args:
            subject (Info): The Info for which an offer should be produced.

        Returns:
            Offer: Offer that this type offers for
                the received subject.
        """
        logger.info('bidding on object')
        return Offer(subject, 0, create_number_template(), NumberViewFactory())
