from doubles.presentation.column_based_presenter.double_column_based_presenter_view_model import \
    ColumnBasedPresenterViewModelMock
from doubles.presentation.column_based_presenter.double_presenter_view import PresenterViewMock


class PresenterFactoryMock:
    def __init__(self):
        self.interpretation_service = None
        self.navigation_service = None
        self.create_call_count = 0

    def create(self, interpretation_service, navigation_service):
        self.interpretation_service = interpretation_service
        self.navigation_service = navigation_service
        self.create_call_count += 1

        return PresenterViewMock()
