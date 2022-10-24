# -*- coding: utf-8 -*-
'''InterpretationService Tests.

This module contains the unit-tests of the Interpretation class.'''

import unittest

from blackfennec_doubles.double_dummy import Dummy
from blackfennec_doubles.extension.double_structure_view_factory import StructureViewFactoryMock
from blackfennec_doubles.navigation.double_navigation_service import NavigationServiceMock
from blackfennec.interpretation.interpretation import Interpretation


class InterpretationTestSuite(unittest.TestCase):
    def test_create_interpretation(self):
        structure = Dummy('structure')
        specification = Dummy('specification')
        factories = Dummy('factories')
        interpretation = Interpretation(structure, specification, factories)
        self.assertIsNotNone(interpretation)


    def test_structure_getter(self):
        structure = Dummy('structure')
        specification = Dummy('specification')
        factories = Dummy('factories')
        interpretation = Interpretation(structure, specification, factories)
        self.assertEqual(structure, interpretation.structure)


    def test_navigation_sender_is_interpretation(self):
        structure = Dummy('structure')
        specification = Dummy('specification')
        factories = Dummy('factories')
        interpretation = Interpretation(structure, specification, factories)
        navigation_service = NavigationServiceMock()
        interpretation.set_navigation_service(navigation_service)
        destination = Dummy('destination')
        interpretation.navigate(destination)
        self.assertEqual(navigation_service.sender, interpretation)

    def test_navigation_destination_is_argument(self):
        structure = Dummy('structure')
        specification = Dummy('specification')
        factories = Dummy('factories')
        interpretation = Interpretation(structure, specification, factories)
        navigation_service = NavigationServiceMock()
        interpretation.set_navigation_service(navigation_service)
        destination = Dummy('destination')
        interpretation.navigate(destination)
        self.assertEqual(navigation_service.destination, destination)

    def test_navigation_request_is_dispatched(self):
        structure = Dummy('structure')
        specification = Dummy('specification')
        factories = Dummy('factories')
        interpretation = Interpretation(structure, specification, factories)
        navigation_service = NavigationServiceMock()
        interpretation.set_navigation_service(navigation_service)
        destination = Dummy('destination')
        interpretation.navigate(destination)
        self.assertEqual(1, navigation_service.navigation_count)

    def test_set_navigation_service(self):
        structure = Dummy('structure')
        specification = Dummy('specification')
        factories = Dummy('factories')
        destination = Dummy('destination')
        interpretation = Interpretation(structure, specification, factories)
        navigation_service1 = NavigationServiceMock()
        interpretation.set_navigation_service(navigation_service1)
        interpretation.navigate(destination)
        navigation_service2 = NavigationServiceMock()
        interpretation.set_navigation_service(navigation_service2)
        interpretation.navigate(destination)
        self.assertEqual(1, navigation_service1.navigation_count)
        self.assertEqual(1, navigation_service2.navigation_count)
