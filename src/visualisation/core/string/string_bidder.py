from src.black_fennec.structure.structure import Structure
from src.black_fennec.structure.string import String
from src.black_fennec.structure.template.template_factory_visitor import TemplateFactoryVisitor
from src.visualisation.core.string.string_view_factory import StringViewFactory
from src.black_fennec.interpretation.auction.offer import Offer
import logging

logger = logging.getLogger(__name__)


def create_string_template():
    template_factory = TemplateFactoryVisitor()
    template = String().accept(template_factory)
    return template


class StringBidder:
    """The bidding service for the core type `String`."""

    def bid(self, subject: Structure):
        """"Produces an offer for a given object.

        Args:
            subject (Structure): The Structure for which an offer should be produced.

        Returns:
            Offer: Offer that this type offers for
                the received subject.
        """
        logger.info('bidding on object')
        return Offer(subject, 0, create_string_template(), StringViewFactory())
