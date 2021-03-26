# -*- coding: utf-8 -*-
"""Interpreter Tests.

This module contains the unit-tests of the Interpreter class."""

import unittest

from doubles.base.info_view_factory import InfoViewFactoryMock
from doubles.dummy import Dummy
from src.core.interpretation import Interpretation
from src.core.interpreter import Interpreter


class InterpreterTestSuite(unittest.TestCase):
    """Class containing the TestSuite with the individual unit-tests."""

    def test_create_interpreter(self):
        """Interpreter instantiation test.

        This unit-test tests whether all constructor arguments of the
        Interpreter class are saved to the corresponding internal
        member variable
        """
        navigation_service = Dummy("nav")
        factories = Dummy("factories")
        interpreter = Interpreter(navigation_service, factories)
        self.assertEqual(
            interpreter._navigation_service,
            navigation_service,
            msg="Interpreter has not initialized " +
                "_navigation_service correctly"
        )
        self.assertEqual(
            interpreter._factories,
            factories,
            msg="Interpreter has not initialized " +
                "_factories correctly"
        )

    def test_interpretation(self):
        """Interpreter.interpret function test.

        This unit-test tests whether the member function
        interpret of the Interpreter creates the info_view
        as expected, and whether an interpretation is returned
        """
        navigation_service = Dummy("nav")
        info = Dummy("info")
        factories = [InfoViewFactoryMock()]
        interpreter = Interpreter(navigation_service, factories)
        interpretation = interpreter.interpret(info)
        self.assertIsInstance(
            interpretation,
            Interpretation,
            msg="Interpreter did not return " +
                "interpretation after interpreting"
        )
        self.assertEqual(
            factories[0].creation_count,
            1,
            msg="Interpreter did not create info_view from factory"
        )
