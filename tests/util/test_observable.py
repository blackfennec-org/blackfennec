# -*- coding: utf-8 -*-
import unittest

from doubles.util.observable import ObservableMock


class ObservableTestSuite(unittest.TestCase):
    def test_bind_kwargs(self):
        observable = ObservableMock()
        called = False

        def callback(sender, event): # pylint: disable=unused-argument
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
