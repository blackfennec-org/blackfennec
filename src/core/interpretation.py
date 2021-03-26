# -*- coding: utf-8 -*-
class Interpretation:
    """Interpretation Class.

    Is produced by the Interpreter. Contains info_view and info
    obtained through dependency injection. Dispatches navigation
    requests to navigation_service

    Attributes:
        _navigation_service (NavigationService): stores injected navigation service
        _info (Info): stores injected info
        _info_view (InfoView): stores injected info

    Todo:
        * Add types to function parameters
    """
    def __init__(self, navigation_service, info, info_view):
        """Interpretation constructor.

        Args:
            navigation_service (NavigationService): service to navigate
            info (Info): info lying behind interpretation
            info_view (InfoView): Created view of info
        """
        self._navigation_service = navigation_service
        self._info_view = info_view
        self._info = info

    @property
    def info(self):
        """info getter

        Returns:
            Info: info property set by constructor
        """
        return self._info

    @property
    def info_view(self):
        """info_view getter

        Returns:
            InfoView: info_view property set by constructor
        """
        return self._info_view

    def navigate(self, destination):
        """Navigation dispatch.

        Args:
            destination (Info): where to navigate to

        Navigation request is dispatched to navigation_service
        with self as sender"""
        self._navigation_service.navigate(self, destination)
