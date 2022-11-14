class ChangeNotification:
    def __init__(self, old_value, new_value):
        self._old_value = old_value
        self._new_value = new_value

    @property
    def old_value(self):
        return self._old_value

    @property
    def new_value(self):
        return self._new_value

    @new_value.setter
    def new_value(self, new_value):
        self._new_value = new_value
