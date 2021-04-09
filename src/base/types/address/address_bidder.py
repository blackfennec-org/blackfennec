# -*- coding: utf-8 -*-
import logging

from src.base.types.address.address_view_factory import AddressViewFactory
from src.core import Info, Offer
from src.core.map import Map
from src.core.string import String

logger = logging.getLogger(__name__)


class AddressBidder:
    """The bidding service for the base type `Address`.
    """

    def bid(self, subject: Info):
        """"Produces an offer for a given object.

        Args:
            subject (Info): The Info for which an
                offer should be produced.
        """
        logger.info('bidding on object')
        template = Map()
        template['first_name'] = String()
        template['last_name'] = String()
        template['street'] = String()
        template['street_nr'] = String()
        template['city'] = String()

        return Offer(subject, 1, template, AddressViewFactory())
