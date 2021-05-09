from doubles.double_dummy import Dummy
from src.structure.info import Info
from src.structure.reference import Reference
from src.structure.template.template_factory_visitor import TemplateFactoryVisitor
from src.type_system.core.reference.reference_view_factory import ReferenceViewFactory
from src.interpretation.auction import Offer

import logging

logger = logging.getLogger(__name__)


def create_reference_template():
    template_factory = TemplateFactoryVisitor()
    template = Reference(Dummy('ReferenceResolvingService')).accept(template_factory)
    return template


class ReferenceBidder:
    """The bidding service for the core type Reference."""
    def __init__(self):
        """Construct reference bidder."""
        self._factory = ReferenceViewFactory()

    def bid(self, subject: Info):
        """"Produces an offer for a given object.

        Args:
            subject (Info): The Info for which an offer should be produced.

        Returns:
            Offer: that this bidder made on the subject passed.
        """
        logger.info('bidding on object')
        return Offer(subject, 0, create_reference_template(), self._factory)
