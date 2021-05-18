# -*- coding: utf-8 -*-
import logging

from src.interpretation.auction import Offer
from src.structure.info import Info
from src.type_system.base.file.file import File
from src.type_system.base.file.file_view_factory import FileViewFactory

logger = logging.getLogger(__name__)


class FileBidder:
    """The bidding service for the base type `File`.
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
        return Offer(subject, 1, File.TEMPLATE, FileViewFactory())
