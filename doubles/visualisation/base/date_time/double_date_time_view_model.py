from datetime import datetime

from src.black_fennec.util.observable import Observable


class DateTimeViewModelMock(Observable):
    def __init__(self, date_time=None):
        super().__init__()
        self.date_time = date_time or datetime.min

    def notify(self, changed_property, name):
        self._notify(changed_property, name, self)
