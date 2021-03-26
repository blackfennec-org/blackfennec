# -*- coding: utf-8 -*-
class Interpretation:
    """Interpretation Class.

    Is produced by the Interpreter. Contains info_view and info
    obtained through dependency injection. Dispatches navigation
    requests to navigation_service"""
    def __init__(self, navigation_service, info, info_view):
        self._navigation_service = navigation_service
        self._info_view = info_view
        self._info = info

    @property
    def info(self):
        return self._info

    @property
    def info_view(self):
        return self._info_view

    def navigate(self, destination):
        """Navigation dispatch.

        Navigation request is dispatched to navigation_service
        with self as sender"""
        self._navigation_service.navigate(self, destination)
