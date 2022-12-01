from blackfennec.util.observable import Observable


class UiServiceMock(Observable):
    def __init__(self):
        super().__init__()
        self._count_copy = 0
        self._count_show_message = 0
        self._show_message_parameter = None

    def copy(self):
        self._count_copy += 1
        return self

    def show_message(self, message):
        self._count_show_message += 1
        self._show_message_parameter = message
