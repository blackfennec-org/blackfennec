# -*- coding: utf-8 -*-
"""InterpretationService Tests.

This module contains the unit-tests of the InterpretationService class."""

import unittest

from doubles.core.auction.auctioneer import AuctioneerMock
from doubles.core.types.info_view_factory import InfoViewFactoryMock
from doubles.dummy import Dummy
from src.core.interpretation import Interpretation
from src.core.interpretation_service import InterpretationService


class InterpretationServiceTestSuite(unittest.TestCase):
    """Class containing the TestSuite with the individual unit-tests."""

    def test_create_interpreter(self):
        """InterpretationService instantiation test.

        This unit-test tests whether all constructor arguments of the
        InterpretationService class are saved to the corresponding internal
        member variable
        """
        navigation_service = Dummy("nav")
        auctioneer = Dummy("auctioneer")
        interpreter = InterpretationService(navigation_service, auctioneer)
        self.assertEqual(
            interpreter._navigation_service,
            navigation_service,
            msg="InterpretationService has not initialized " +
                "_navigation_service correctly"
        )
        self.assertEqual(
            interpreter._auctioneer,
            auctioneer,
            msg="InterpretationService has not initialized " +
                "_auctioneer correctly"
        )

    def test_can_create_interpretation(self):
        """InterpretationService.interpret function test.

        This unit-test tests whether the member function
        interpret of the InterpretationService creates the info_view
        as expected, and whether an interpretation is returned
        """
        navigation_service = Dummy("nav")
        info = Dummy("info")

        factories = [InfoViewFactoryMock()]

        auctioneer = AuctioneerMock(factories)
        interpreter = InterpretationService(navigation_service, auctioneer)
        interpretation = interpreter.interpret(info)
        self.assertIsInstance(
            interpretation,
            Interpretation,
            msg="InterpretationService did not return " +
                "interpretation after interpreting"
        )
        self.assertEqual(
            factories[0].creation_count,
            1,
            msg="InterpretationService did not create info_view from factory"
        )
        self.assertEqual(
            auctioneer.auction_count,
            1
        )
        self.assertEqual(
            auctioneer.auction_last_subject,
            info
        )
