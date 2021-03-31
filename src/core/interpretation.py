# -*- coding: utf-8 -*-
class Interpretation:
    """Interpretation Class.

    Is produced by the Interpreter. Contains info_view and info
    obtained through dependency injection. Dispatches navigation
    requests to navigation_service

    Attributes:
        _navigation_service (NavigationService): stores injected navigation service
        _info (Info): stores injected info
        _info_views (InfoView): stores injected info

    Todo:
        * Add types to function parameters
    """
    def __init__(self, navigation_service, info, info_views):
        """Interpretation constructor.

        Args:
            navigation_service (NavigationService): service to navigate
            info (Info): info lying behind interpretation
            info_views (InfoView): Created view of info
        """
        self._navigation_service = navigation_service
        self._info_views = info_views
        self._info = info

    @property
    def info(self):
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

    def navigate(self, destination):
        """Navigation dispatch.

        Args:
            destination (Info): where to navigate to

        Navigation request is dispatched to navigation_service
        with self as sender"""
        self._navigation_service.navigate(self, destination)
