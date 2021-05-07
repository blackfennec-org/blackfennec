# -*- coding: utf-8 -*-
import logging

from doubles.double_dummy import Dummy
from src.structure.info import Info
from src.structure.map import Map
from src.structure.string import String
from src.util.json.json_reference_resolving_service import JsonReferenceResolvingService

logger = logging.getLogger(__name__)


class Reference(Map):
    """Core Type Reference, represents references in the domain model."""
    REFERENCE_KEY = '$ref'
    TEMPLATE = None

    def __init__(
            self,
            json_reference_resolve_service: JsonReferenceResolvingService,
            reference: str = ''
    ):
        """Reference Constructor.

        Args:
            reference (str): string containing a json reference
        """
        self._json_reference_resolve_service = json_reference_resolve_service
        Map.__init__(self, {Reference.REFERENCE_KEY: String(reference)})

    @property
    def value(self) -> str:
        """Reference getter.

        JsonReference object is cached, and reset
            if item in underlying dictionary is changed.

        Returns:
            JsonReference: which is contained in reference
        """
        return self[Reference.REFERENCE_KEY].value

    @value.setter
    def value(self, value: str):
        """Reference setter.

        Args:
            value (str): which is contained in reference
        """
        self[Reference.REFERENCE_KEY].value = value

    @property
    def children(self) -> list:
        """Readonly property for children of References, by default empty."""
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

    @staticmethod
    def is_json_reference(dictionary: dict):
        return Reference.REFERENCE_KEY in dictionary

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


Reference.TEMPLATE = Reference(Dummy())
