# -*- coding: utf-8 -*-
import unittest

from blackfennec_doubles.extension.double_structure_presenter import StructurePresenterMock
from blackfennec_doubles.double_dummy import Dummy
from blackfennec.presentation_system.navigation_service.navigation_service \
    import NavigationService


class NavigationServiceTestSuite(unittest.TestCase):
    def test_create_navigation_service(self):
        presenter = Dummy('StructurePresenter')
        navigation_service = NavigationService()
        navigation_service.set_presenter(presenter)
        self.assertEqual(presenter, navigation_service._presenter)

    def test_navigate(self):
        sender = Dummy('Interpretation')
        destination = Dummy('Structure')
        presenter = StructurePresenterMock()
        navigation_service = NavigationService()
        navigation_service.set_presenter(presenter)
        navigation_service.navigate(sender, destination)
        self.assertEqual(1, presenter.show_count)
        self.assertEqual(sender, presenter.show_last_sender)
        self.assertEqual(presenter.show_last_destination, destination)

    def test_navigate_without_presenter(self):
        sender = Dummy('Interpretation')
        destination = Dummy('Structure')
        navigation_service = NavigationService()
        with self.assertRaises(AssertionError):
            navigation_service.navigate(sender, destination)
