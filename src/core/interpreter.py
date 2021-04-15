# -*- coding: utf-8 -*-
import logging

from src.core.types.info import Info
from src.core.interpretation import Interpretation

logger = logging.getLogger(__name__)


class Interpreter:
    """Interpreter Class.

    Is produced during the selection process and is the
    Creator of Interpretations

    Attributes:
        _navigation_service (NavigationService): stores injected
            navigation service
        _auctioneer (Auctioneer): stores injected auctioneer
    """
    def __init__(self, navigation_service, auctioneer):
        """Interpretation constructor.

        Args:
            navigation_service (NavigationService): service to navigate
            auctioneer (Auctioneer): Auctioneer returning list
                of factories, used to create info_view
        """
        self._navigation_service = navigation_service
        self._auctioneer = auctioneer

    def _retrieve_factories(self, subject: Info):
        """Retrieval of factories

        Start auction on auctioneer to receive list of factories

        Args:
            subject (Info): Target to which shall be navigated
        """
        factories = self._auctioneer.auction(subject)
        return factories

    def _create_info_views(self, info, interpretation):
        """Internal function to create info_views.

        Creates info_views.

        Args:
            info (Info): Info to create info_views to
            interpretation (Interpretation): interpretation with which
                the info_views are created

        Returns:
            [InfoView]: created with factories passed to interpreter
        """
        info_views = []
        for factory in self._retrieve_factories(info):
            info_views.append(factory.create(interpretation))
            logger.debug(
                'creating info_view with factory %s',
                factory
            )
        return info_views

    def interpret(self, info: Info) -> Interpretation:
        """interpretation creation function.

        Creates Interpretation with created info_view

        Args:
            info (Info): info to create interpretation from

        Returns:
            Interpretation: including created info_views
        """
        interpretation = Interpretation(self._navigation_service, info)
        info_views = self._create_info_views(info, interpretation)
        logger.debug(
            'creating interpretation of info %s with views %s',
            info,
            info_views
        )
        interpretation.info_views = info_views
        return interpretation
