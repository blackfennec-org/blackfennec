# -*- coding: utf-8 -*-
import logging

from src.black_fennec.interpretation.auction.offer import Offer
from src.black_fennec.structure.info import Info
from src.visualisation.base.person.person import Person
from src.visualisation.base.person.person_view_factory import PersonViewFactory

logger = logging.getLogger(__name__)


class PersonBidder:
    """The bidding service for the base type `Person`.
    """

    def bid(self, subject: Info):
        """"Produces an offer for a given object.

        Args:
            subject (Info): The Info for which an
                offer should be produced.

        Returns:
            Offer: Offer that this type offers for
                the received subject.
        """
        logger.info('bidding on object')
        return Offer(subject, 1, Person.TEMPLATE, PersonViewFactory())
