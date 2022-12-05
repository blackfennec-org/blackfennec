from blackfennec.util.observable import Observable


class UiServiceMock(Observable):
    def __init__(self):
        super().__init__()
        self.copy_count = 0
        self.show_message_count = 0
        self._show_message_parameter = None

    def copy(self):
        self.copy_count += 1
        return self

    def show_message(self, message):
        self.show_message_count += 1
        self._show_message_parameter = message
