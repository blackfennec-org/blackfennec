# -*- coding: utf-8 -*-
import logging

from src.interpretation.auction import Offer
from src.structure.info import Info
from src.type_system.base.address.address import Address
from src.type_system.base.address.address_view_factory import AddressViewFactory
from src.structure.map import Map
from src.structure.string import String

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
