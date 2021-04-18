# -*- coding: utf-8 -*-
import logging
from src.structure.info import Info
#from src.navigation.navigation_service import NavigationService

logger = logging.getLogger(__name__)

class Interpretation:
    """Interpretation Class.

    Is produced by the InterpretationService. Contains info_view and info
    obtained through dependency injection. Dispatches navigation
    requests to navigation_service

    Attributes:
        _navigation_service (NavigationService): stores injected
            navigation service
        _info (Info): stores injected info
        _info_views (InfoView): stores injected info

    Todo:
        * Add types to function parameters
    """
    def __init__(self, info: Info):
        """Interpretation constructor.

        Args:
            navigation_service (NavigationService): service to navigate
            info (Info): info lying behind interpretation
            info_views (InfoView): Created view of info
        """
        self._navigation_service = None
        self._info_views = list()
        self._info = info
        self._view = None

    def set_navigation_service(self, navigation_service):
        self._navigation_service = navigation_service


    @property
    def info(self) -> Info:
        """info getter

        Returns:
            Info: info property set by constructor
        """
        return self._info

    @property
    def info_views(self):
        """info_views getter

        Returns:
            [InfoView]: info_views property set by constructor
        """
        return self._info_views

    @info_views.setter
    def info_views(self, info_views):
        self._info_views = info_views

    @property
    def view(self):
        if not self._view:
            self._view = self._info_views[0]
            logger.debug("creating view from %s", self._view)
        return self._view

    def navigate(self, destination: Info):
        """Navigation dispatch.

        Args:
            destination (Info): where to navigate to

        Navigation request is dispatched to navigation_service
        with self as sender"""
        self._navigation_service.navigate(self, destination)
