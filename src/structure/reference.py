# -*- coding: utf-8 -*-
import logging

from uri import URI

from doubles.double_dummy import Dummy
from src.structure.info import Info
from src.structure.map import Map
from src.structure.string import String
from src.util.json.json_reference_resolving_service import JsonReferenceResolvingService

logger = logging.getLogger(__name__)


class Reference(Info):
    """Core Type Reference, represents references in the domain model."""
    TEMPLATE = None

    def __init__(
            self,
            json_reference_resolve_service: JsonReferenceResolvingService,
            reference: URI = URI('')
    ):
        """Reference Constructor.

        Args:
            reference (str): string containing a json reference
        """
        Info.__init__(self, reference)
        self._json_reference_resolve_service = json_reference_resolve_service

    @property
    def value(self) -> URI:
        """Reference getter.

        JsonReference object is cached, and reset
            if item in underlying dictionary is changed.

        Returns:
            JsonReference: which is contained in reference
        """
        return self._value

    @value.setter
    def value(self, value: URI):
        """Reference setter.

        Args:
            value (str): which is contained in reference
        """
        self._value = value

    @property
    def children(self) -> list:
        """Readonly property for children of References"""
        if self.destination:
            return self.destination.children
        else:
            return list()

    @property
    def destination(self) -> Info:
        """Getter for destination

        Automatically resolves underlying reference
        Returns:
            Info: destination to which the reference
                points
        """
        if self.value:
            return self._json_reference_resolve_service.resolve(
                self.value,
                self
            )

    def __eq__(self, other) -> bool:
        return (
                   self.value
               ) == (
                   other.value
               )

    def __ne__(self, other) -> bool:
        return not self == other

    def __str__(self) -> str:
        """Convert to string"""
        return str(self.value)

    def __repr__(self) -> str:
        """Create representation for pretty printing"""
        return f'Reference({self.value})'

    def accept(self, visitor):
        return visitor.visit_reference(self)


Reference.TEMPLATE = Reference(Dummy('ReferenceResolvingService'))
