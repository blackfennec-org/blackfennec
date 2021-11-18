# -*- coding: utf-8 -*-
import logging
from src.black_fennec.structure.structure import Structure

# from src.navigation.navigation_service import NavigationService

logger = logging.getLogger(__name__)


class Interpretation:
    """Interpretation Class.

    Is produced by the InterpretationService. Contains the relevant structure
    and can create a view. Dispatches navigation requests to navigation_service.
    """

    def __init__(self, structure: Structure, specification, factories):
        """Interpretation constructor.

        Args:
            structure (Structure): structure lying behind interpretation
            specification (Specification): the requested specification for this
                interpretation
            factories ([ViewFactories]): the view factories from which the view
                will be constructed.
        """
        self._navigation_service = None
        self._specification = specification
        self._factories = factories
        self._structure_views = []
        self._structure = structure
        self._view = None

    def set_navigation_service(self, navigation_service) -> None:
        """Set navigation service to be used.

        Args:
            navigation_service (NavigationService): The navigation service.
                Must not be None.
        """
        assert navigation_service, 'navigation service must not be None'
        self._navigation_service = navigation_service

    @property
    def structure(self) -> Structure:
        """structure getter

        Returns:
            Structure: the structure that is represented by this interpretation.
        """
        return self._structure

    @property
    def view(self):
        if not self._view:
            self._view = self._factories[0].create(self, self._specification)
            logger.debug('creating view from %s', self._view)
        return self._view

    def navigate(self, destination: Structure):
        """Navigation dispatch.

        Navigation request is dispatched to navigation_service.
        The sender is set to self.

        Args:
            destination (Structure): where to navigate to
        """
        assert self._navigation_service, 'no navigation service configured'
        self._navigation_service.navigate(self, destination)
