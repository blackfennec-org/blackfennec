# -*- coding: utf-8 -*-
from blackfennec.util.observable import Observable


class ObservableMock(Observable):
    @property
    def i_notify_observers(self):
        return True

    @i_notify_observers.setter
    def i_notify_observers(self, new_value):
        self._notify(new_value, "i_notify_observers")
