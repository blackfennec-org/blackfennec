# -*- coding: utf-8 -*-
import unittest

from doubles.interpretation.interpretation import InterpretationMock
from doubles.dummy import Dummy
from src.navigation.navigation_proxy import NavigationProxy


class NavigationProxyTestSuite(unittest.TestCase):
    def test_create_navigation_proxy(self):
        interpretation = Dummy('interpretation')
        navigation_proxy = NavigationProxy(interpretation)
        self.assertIsNotNone(navigation_proxy)

    def test_navigate(self):
        sender = Dummy('Interpretation')
        destination = Dummy('Info')
        interpretation = InterpretationMock()
        navigation_proxy = NavigationProxy(interpretation)
        navigation_proxy.navigate(sender, destination)
        self.assertListEqual([destination], interpretation.navigation_requests)
