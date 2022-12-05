from blackfennec_doubles.facade.ui_service.double_ui_service import \
    UiServiceMock


class UiServiceRegistryMock:
    def __init__(self, ui_service=None, ui_service_key=None):
        self._ui_service = ui_service or UiServiceMock()
        self._ui_service_key = ui_service_key
        self.register_count = 0

    @property
    def services(self):
        return {self._ui_service_key: self._ui_service}

    def register(self, window, service):
        self.register_count += 1
