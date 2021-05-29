# -*- coding: utf-8 -*-
"""NavigationService Doubles.

In this module any Doubles used for testing components using
the NavigationService are contained to ensure that unit-tests
only test a single component."""


class NavigationServiceMock:
    """Class represents a Mock Double for the NavigationService.

    With this class it can be tested whether the navigate
    member function was called in the correct way, and how many
    times it was executed."""
    def __init__(self):
        self.destination = None
        self.sender = None
        self.navigation_count = 0

    def navigate(self, sender, destination):
        """StructureViewFactory.create method mock.

        Args:
            sender (Any): sender interpretation which initiated navigation
            destination (Any): structure to navigate to

        Saves passed argument on class to enable user to see passed arguments.
        Counts amount of times navigate has been called."""
        self.navigation_count += 1
        self.destination = destination
        self.sender = sender
