from doubles.core.info import InfoMock

class InterprationMock:
    def __init__(self, info = None):
        self.navigation_requests = list()
        self._view_property_access_count = 0
        self._info_property_access_count = 0
        self._info = InfoMock() if info is None else info

    def navigate(self, info):
        self.navigation_requests.append(info)

    @property
    def view(self):
        self._view_property_access_count += 1

    @property
    def info(self):
        self._info_property_access_count += 1
        return self._info
