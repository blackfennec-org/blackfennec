# -*- coding: utf-8 -*-
import unittest

from src.util.observable import Observable


class ObservableMock(Observable):
    def __init__(self):
        super().__init__()

    @property
    def i_notify_observers(self):
        return True

    @i_notify_observers.setter
    def i_notify_observers(self, new_value):
        self._notify(new_value, "i_notify_observers")


class ObservableTestSuite(unittest.TestCase):
    def test_bind_kwargs(self):
        observable = ObservableMock()
        called = False

        def callback(sender, event):
            nonlocal called
            called = True

        observable.bind(i_notify_observers=callback)
        observable.i_notify_observers = None
        self.assertTrue(called)

    def test_bind_to_no_existing_property(self):
        observable = ObservableMock()
        self.assertRaises(
            KeyError,
            lambda: observable.bind(i_do_not_exist=None))
