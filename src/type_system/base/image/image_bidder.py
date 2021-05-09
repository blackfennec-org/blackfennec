# -*- coding: utf-8 -*-
import logging

from src.type_system.base.image.image import Image
from src.type_system.base.image.image_view_factory import ImageViewFactory
from src.interpretation.auction import Offer
from src.structure.info import Info
from src.structure.map import Map
from src.structure.string import String

logger = logging.getLogger(__name__)


class ImageBidder:
    """The bidding service for the base type `Image`.
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
        return Offer(subject, 2, Image.TEMPLATE, ImageViewFactory())
