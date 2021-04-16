# -*- coding: utf-8 -*-
import logging

from src.type_system.base.date_time.date_time import DateTime
from src.type_system.base.date_time.date_time_view_factory import DateTimeViewFactory
from src.interpretation.auction import Offer
from src.structure.info import Info
from src.structure.map import Map
from src.structure.string import String

logger = logging.getLogger(__name__)


class DateTimeBidder:
    """The bidding service for the base type `DateTime`.
    """

    def bid(self, subject: Info):
        """"Produces an offer for a given object.

        Args:
            subject (Info): The Info for which an
                offer should be produced.
        """
        logger.info('bidding on object')
        template = Map()
        template[DateTime.DATE_TIME_KEY] = String()

        return Offer(subject, 1, template, DateTimeViewFactory())
