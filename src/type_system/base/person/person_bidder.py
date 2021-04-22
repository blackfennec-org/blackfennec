# -*- coding: utf-8 -*-
import logging

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
        template = Map()
        template['courtesy_title'] = String()
        template['first_name'] = String()
        template['middle_name'] = String()
        template['last_name'] = String()
        template['suffix'] = String()
        template['gender'] = String()
        template['sex'] = String()
        template['marital_status'] = String()
        template['nationality'] = String()

        return Offer(subject, 1, template, PersonViewFactory())
