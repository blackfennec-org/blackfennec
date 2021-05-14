# -*- coding: utf-8 -*-
'''InterpretationService Tests.

This module contains the unit-tests of the Interpretation class.'''

import unittest

from doubles.double_dummy import Dummy
from doubles.type_system.double_info_view_factory import InfoViewFactoryMock
from doubles.navigation.double_navigation_service import NavigationServiceMock
from src.interpretation.interpretation import Interpretation


class InterpretationTestSuite(unittest.TestCase):
    def test_create_interpretation(self):
        info = Dummy('info')
        specification = Dummy('specification')
        factories = Dummy('factories')
        interpretation = Interpretation(info, specification, factories)
        self.assertIsNotNone(interpretation)


    def test_info_getter(self):
        info = Dummy('info')
        specification = Dummy('specification')
        factories = Dummy('factories')
        interpretation = Interpretation(info, specification, factories)
        self.assertEqual(info, interpretation.info)

    def test_view_getter(self):
        info = Dummy('info')
        view = Dummy('view')
        specification = Dummy('specification')
        factories = [InfoViewFactoryMock(view=view)]
        interpretation = Interpretation(info, specification, factories)
        self.assertEqual(view, interpretation.view)

    def test_navigation_sender_is_interpretation(self):
        info = Dummy('info')
        specification = Dummy('specification')
        factories = Dummy('factories')
        interpretation = Interpretation(info, specification, factories)
        navigation_service = NavigationServiceMock()
        interpretation.set_navigation_service(navigation_service)
        destination = Dummy('destination')
        interpretation.navigate(destination)
        self.assertEqual(navigation_service.sender, interpretation)

    def test_navigation_destination_is_argument(self):
        info = Dummy('info')
        specification = Dummy('specification')
        factories = Dummy('factories')
        interpretation = Interpretation(info, specification, factories)
        navigation_service = NavigationServiceMock()
        interpretation.set_navigation_service(navigation_service)
        destination = Dummy('destination')
        interpretation.navigate(destination)
        self.assertEqual(navigation_service.destination, destination)

    def test_navigation_request_is_dispatched(self):
        info = Dummy('info')
        specification = Dummy('specification')
        factories = Dummy('factories')
        interpretation = Interpretation(info, specification, factories)
        navigation_service = NavigationServiceMock()
        interpretation.set_navigation_service(navigation_service)
        destination = Dummy('destination')
        interpretation.navigate(destination)
        self.assertEqual(1, navigation_service.navigation_count)

    def test_set_navigation_service(self):
        info = Dummy('info')
        specification = Dummy('specification')
        factories = Dummy('factories')
        destination = Dummy('destination')
        interpretation = Interpretation(info, specification, factories)
        navigation_service1 = NavigationServiceMock()
        interpretation.set_navigation_service(navigation_service1)
        interpretation.navigate(destination)
        navigation_service2 = NavigationServiceMock()
        interpretation.set_navigation_service(navigation_service2)
        interpretation.navigate(destination)
        self.assertEqual(1, navigation_service1.navigation_count)
        self.assertEqual(1, navigation_service2.navigation_count)
