# -*- coding: utf-8 -*-
import logging

from src.base.types.file.file import File
from src.base.types.file.file_view_factory import FileViewFactory
from src.core import Info, Offer
from src.core.map import Map
from src.core.string import String

logger = logging.getLogger(__name__)


class FileBidder:
    """The bidding service for the base type `File`.
    """

    def bid(self, subject: Info):
        """"Produces an offer for a given object.

        Args:
            subject (Info): The Info for which an
                offer should be produced.
        """
        logger.info('bidding on object')
        template = Map()
        template[File.FILE_PATH_KEY] = String()
        template[File.FILE_TYPE_KEY] = String()

        return Offer(subject, 1, template, FileViewFactory())
