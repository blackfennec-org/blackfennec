# -*- coding: utf-8 -*-
import logging

from src.type_system.base.file.file import File
from src.type_system.base.file.file_view_factory import FileViewFactory
from src.interpretation.auction import Offer
from src.structure.info import Info
from src.structure.map import Map
from src.structure.string import String

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
