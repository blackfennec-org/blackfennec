# -*- coding: utf-8 -*-
import logging

from src.core.info import Info
from src.core.interpretation import Interpretation

logger = logging.getLogger(__name__)


class Interpreter:
    """Interpreter Class.

    Is produced during the selection process and is the
    Creator of Interpretations

    Attributes:
        _navigation_service (NavigationService): stores injected
            navigation service
        _factories ([InfoViewFactory]): stores injected factory list

    Todo:
        * Add types to function parameters
    """
    def __init__(self, navigation_service, factories):
        """Interpretation constructor.

        Args:
            navigation_service (NavigationService): service to navigate
            factories ([InfoViewFactory]): list of factories, used to
                create info_view
        """
        assert factories, 'No factories provided to interpreter'
        self._navigation_service = navigation_service
        self._factories = factories

    def _create_info_views(self, interpretation):
        """Internal function to create info_views.

        Creates info_views.

        Returns:
            [InfoView]: created with factories passed to interpreter
        """
        info_views = []
        for factory in self._factories:
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
        info_views = self._create_info_views(interpretation)
        logger.debug(
            'creating interpretation of info %s with views %s',
            info,
            info_views
        )
        interpretation.info_views = info_views
        return interpretation
