# -*- coding: utf-8 -*-
import logging
from src.core.interpretation import Interpretation

logger = logging.getLogger(__name__)


class Interpreter:
    """Interpreter Class.

    Is produced during the selection process and is the
    Creator of Interpretations

    Attributes:
        _navigation_service (NavigationService): stores injected navigation service
        _factories ([InfoViewFactory]): stores injected factory list

    Todo:
        * Add types to function parameters
    """
    def __init__(self, navigation_service, factories):
        """Interpretation constructor.

        Args:
            navigation_service (NavigationService): service to navigate
            factories ([InfoViewFactory]): list of factories, used to create info_view
        """
        assert factories, "No factories provided to interpreter"
        self._navigation_service = navigation_service
        self._factories = factories

    def _create_info_view(self):
        """Internal function to create info_view.

        Contains logic to decide which factory is used
        to create info_view.

        Returns:
            InfoView: created with factory passed to interpreter
        """
        return self._factories[0].create()

    def interpret(self, info):
        """interpretation creation function.

        Creates Interpretation with created info_view

        Args:
            info (Info): info to create interpretation from

        Returns:
            Interpretation: including created info_view
        """
        info_view = self._create_info_view()
        logger.debug(
            "creating interpretation of info %s with view %s",
            info,
            info_view
        )
        return Interpretation(self._navigation_service, info, info_view)
