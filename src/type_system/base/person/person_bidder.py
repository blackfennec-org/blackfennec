# -*- coding: utf-8 -*-
import logging

from src.type_system.base.person.person import Person
from src.type_system.base.person.person_view_factory import PersonViewFactory
from src.interpretation.auction import Offer
from src.structure.info import Info
from src.structure.map import Map
from src.structure.string import String

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
