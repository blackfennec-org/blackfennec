from blackfennec_doubles.extension.double_presenter_view import PresenterViewMock


class PresenterFactoryMock:
    def __init__(self):
        self.interpretation_service = None
        self.navigation_service = None
        self.create_call_count = 0

    def create(self, navigation_service):
        self.navigation_service = navigation_service
        self.create_call_count += 1

        return PresenterViewMock()
