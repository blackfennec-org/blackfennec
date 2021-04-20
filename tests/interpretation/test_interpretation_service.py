# -*- coding: utf-8 -*-
"""InterpretationService Tests.

This module contains the unit-tests of the InterpretationService class."""

import unittest

from doubles.interpretation.auction.auctioneer import AuctioneerMock
from doubles.type_system.info_view_factory import InfoViewFactoryMock
from doubles.dummy import Dummy
from src.interpretation.interpretation import Interpretation
from src.interpretation.interpretation_service import InterpretationService


class InterpretationServiceTestSuite(unittest.TestCase):
    """Class containing the TestSuite with the individual unit-tests."""

    def test_create_interpreter(self):
        """InterpretationService instantiation test.

        This unit-test tests whether all constructor arguments of the
        InterpretationService class are saved to the corresponding internal
        member variable
        """
        auctioneer = Dummy("auctioneer")
        interpreter = InterpretationService(auctioneer)
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
        info = Dummy("info")

        factories = [InfoViewFactoryMock()]

        auctioneer = AuctioneerMock(factories)
        interpreter = InterpretationService(auctioneer)
        interpretation = interpreter.interpret(info)
        self.assertIsInstance(interpretation, Interpretation)
        self.assertIn(factories[0], interpretation._factories)
        self.assertEqual(1, auctioneer.auction_count)
        self.assertEqual(info, auctioneer.auction_last_subject)
