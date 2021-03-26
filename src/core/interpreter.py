# -*- coding: utf-8 -*-
import logging
from src.core.interpretation import Interpretation

logger = logging.getLogger(__name__)


class Interpreter:
    """Interpreter Class.

    Is produced during the selection process and is the
    Creator of Interpretations"""
    def __init__(self, navigation_service, factories):

        assert factories, "No factories provided to interpreter"
        self._navigation_service = navigation_service
        self._factories = factories
        pass

    def __create_info_view(self):
        """Internal function to create info_view.

        Contains logic to decide which factory is used
        to create info_view."""
        return self._factories[0].create()

    def interpret(self, info):
        """interpretation creation function.

        Creates Interpretation with created info_view"""
        info_view = self.__create_info_view()
        logger.debug(
            "creating interpretation of info %s with view %s",
            info,
            info_view
        )
        return Interpretation(self._navigation_service, info, info_view)
