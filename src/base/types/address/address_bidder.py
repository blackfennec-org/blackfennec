# -*- coding: utf-8 -*-
import logging

from src.base.types.address.address import Address
from src.base.types.address.address_view_factory import AddressViewFactory
from src.core import Info, Offer
from src.core.types.map import Map
from src.core.types.string import String

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
        template[Address.FIRST_NAME_KEY] = String()
        template[Address.LAST_NAME_KEY] = String()
        template[Address.STREET_KEY] = String()
        template[Address.STREET_NUMBER_KEY] = String()
        template[Address.CITY_KEY] = String()

        return Offer(subject, 1, template, AddressViewFactory())
