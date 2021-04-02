# -*- coding: utf-8 -*-
"""InfoViewFactory Doubles.

In this module any Doubles used for testing components using
the InfoViewFactory are contained to ensure that unit-tests
only test a single component."""

class InfoViewFactoryMock:
    """Class represents a Mock Double for the InfoViewFactory.

    With this class it can be tested whether an info_view
    was created."""
    def __init__(self):
        self.creation_count = 0
        self.interpretation = None

    def create(self, interpretation):
        """InfoViewFactory.create method mock.

        Counts amount of times create has been called"""
        self.creation_count += 1
        self.interpretation = interpretation
