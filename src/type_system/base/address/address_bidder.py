# -*- coding: utf-8 -*-
import logging

from src.interpretation.auction import Offer
from src.structure.info import Info
from src.type_system.base.address.address import Address
from src.type_system.base.address.address_view_factory import AddressViewFactory

logger = logging.getLogger(__name__)


class AddressBidder:
    """The bidding service for the base type `Address`.
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
        return Offer(subject, 1, Address.TEMPLATE, AddressViewFactory())
