# -*- coding: utf-8 -*-
import logging

from src.base.types.image.image import Image
from src.base.types.image.image_view_factory import ImageViewFactory
from src.core import Info, Offer
from src.core.types.map import Map
from src.core.types.string import String

logger = logging.getLogger(__name__)


class ImageBidder:
    """The bidding service for the base type `Image`.
    """

    def bid(self, subject: Info):
        """"Produces an offer for a given object.

        Args:
            subject (Info): The Info for which an
                offer should be produced.
        """
        logger.info('bidding on object')
        template = Map()
        template[Image.FILE_PATH_KEY] = String()
        template[Image.FILE_TYPE_KEY] = String('image/')

        return Offer(subject, 2, template, ImageViewFactory())
