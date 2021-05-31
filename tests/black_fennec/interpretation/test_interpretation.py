# -*- coding: utf-8 -*-
'''InterpretationService Tests.

This module contains the unit-tests of the Interpretation class.'''

import unittest

from doubles.double_dummy import Dummy
from doubles.visualisation.double_structure_view_factory import StructureViewFactoryMock
from doubles.black_fennec.navigation.double_navigation_service import NavigationServiceMock
from src.black_fennec.interpretation.interpretation import Interpretation


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

    def test_view_getter(self):
        structure = Dummy('structure')
        view = Dummy('view')
        specification = Dummy('specification')
        factories = [StructureViewFactoryMock(view=view)]
        interpretation = Interpretation(structure, specification, factories)
        self.assertEqual(view, interpretation.view)

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
