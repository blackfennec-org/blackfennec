# -*- coding: utf-8 -*-
import unittest

from blackfennec_doubles.interpretation.double_interpretation import InterpretationMock
from blackfennec_doubles.double_dummy import Dummy
from blackfennec.navigation.navigation_proxy import NavigationProxy


class NavigationProxyTestSuite(unittest.TestCase):
    def test_create_navigation_proxy(self):
        navigation_proxy = NavigationProxy()
        self.assertIsNotNone(navigation_proxy)

    def test_navigate(self):
        class Observer:
            def navigate(self, sender, destination):
                self.sender = sender
                self.destination = destination
        sender = Dummy('Interpretation')
        destination = Dummy('Structure')
        interpretation = InterpretationMock()
        observer = Observer()
        navigation_proxy = NavigationProxy()
        navigation_proxy.bind(navigation_request=observer.navigate)
        navigation_proxy.navigate(sender, destination)
        self.assertEqual(sender, observer.sender)
        self.assertEqual(destination, observer.destination)
