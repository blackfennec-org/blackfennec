# -*- coding: utf-8 -*-
"""Interpreter Tests.

This module contains the unit-tests of the Interpretation class."""

import unittest

from doubles.dummy import Dummy
from doubles.core.navigation.navigation_service import NavigationServiceMock
from src.core.interpretation import Interpretation


class InterpretationTestSuite(unittest.TestCase):
    """Class containing the TestSuite with the individual unit-tests."""

    def test_create_interpretation(self):
        """Interpreter instantiation test.

        This unit-test tests whether all constructor arguments of the
        Interpretation class are saved to the corresponding internal
        member variable
        """
        navigation_service = Dummy("nav")
        info = Dummy("info")
        info_views = Dummy("info_view")
        interpretation = Interpretation(navigation_service, info, info_views)
        self.assertEqual(
            interpretation._navigation_service,
            navigation_service,
            msg="Interpretation has not initialized" +
                " _navigation_service correctly"
        )
        self.assertEqual(
            interpretation._info,
            info,
            msg="Interpretation has not initialized " +
                "_info correctly"
        )
        self.assertEqual(
            interpretation._info_views,
            info_views,
            msg="Interpretation has not initialized " +
                "_info_view correctly"
        )

    def test_info_getter(self):
        """Interpreter.info getter test.

        This unit-test tests whether the info getter
        returns the expected value."""
        navigation_service = Dummy("nav")
        info = Dummy("info")
        info_views = [Dummy("info_view")]
        interpretation = Interpretation(navigation_service, info, info_views)
        self.assertEqual(
            interpretation.info,
            info,
            msg="Interpretation info getter has not " +
                "returned passed info correctly"
        )

    def test_info_view_getter(self):
        """Interpreter.info_view getter test.

        This unit-test tests whether the info_view getter
        returns the expected value."""
        navigation_service = Dummy("nav")
        info = Dummy("info")
        info_views = Dummy("info_view")
        interpretation = Interpretation(navigation_service, info, info_views)
        self.assertEqual(
            interpretation.info_views,
            info_views,
            msg="Interpretation info_view getter has not" +
                " returned passed info_view correctly"
        )

    def test_navigation(self):
        """Interpreter.navigate function test.

        This unit-test tests whether the member function
        navigate of the Interpretation dispatches the
        navigation as expected to the NavigationService.
        """
        navigation_service = NavigationServiceMock()
        info = Dummy("info")
        info_view = Dummy("info_view")
        destination = Dummy("destination")
        interpretation = Interpretation(navigation_service, info, info_view)
        interpretation.navigate(destination)
        self.assertEqual(
            navigation_service.sender,
            interpretation,
            msg="Interpretation has not executed navigate function " +
                "on NavigationService with the sender argument"
        )
        self.assertEqual(
            navigation_service.destination,
            destination,
            msg="Interpretation has not executed navigate function " +
                "on NavigationService with the destination argument"
        )
        self.assertEqual(
            navigation_service.navigation_count,
            1,
            msg="Interpretation has not executed navigate function " +
                "on NavigationService the amount expected"
        )
