from datetime import datetime

from blackfennec.util.observable import Observable


class DateTimeViewModelMock(Observable):
    def __init__(self, date_time=None):
        super().__init__()
        self.date_time = date_time or datetime.min

    def notify(self, changed_property, name):
        self._notify(name, changed_property, self)
