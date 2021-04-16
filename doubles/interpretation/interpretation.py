from doubles.structure.info import InfoMock
from doubles.type_system.info_view import InfoViewDummy


class InterpretationMock:
    def __init__(self, info = None, info_view = None):
        self.navigation_requests = list()
        self.view_property_access_count = 0
        self.info_property_access_count = 0
        self._info = InfoMock() if info is None else info
        self.info_view = InfoViewDummy() if info_view is None else info_view

    def navigate(self, info):
        self.navigation_requests.append(info)

    @property
    def view(self):
        self.view_property_access_count += 1
        return self.info_view

    @property
    def info(self):
        self.info_property_access_count += 1
        return self._info
