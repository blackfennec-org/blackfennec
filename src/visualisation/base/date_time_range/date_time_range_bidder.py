# -*- coding: utf-8 -*-
import logging

from src.black_fennec.interpretation.auction.offer import Offer
from src.black_fennec.structure.structure import Structure
from src.visualisation.base.date_time_range.date_time_range import DateTimeRange
from src.visualisation.base.date_time_range.date_time_range_view_factory import DateTimeRangeViewFactory

logger = logging.getLogger(__name__)


class DateTimeRangeBidder:
    """The bidding service for the base type `DateTimeRange`.
    """

    def bid(self, subject: Structure):
        """"Produces an offer for a given object.

        Args:
            subject (Structure): The Structure for which an
                offer should be produced.

        Returns:
            Offer: with how well the type can handle the passed
                subject.
        """
        logger.info('bidding on object')
        return Offer(subject, 1, DateTimeRange.TEMPLATE,
                     DateTimeRangeViewFactory())
