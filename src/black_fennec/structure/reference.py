# -*- coding: utf-8 -*-
import logging

from uri import URI

from doubles.double_dummy import Dummy
from src.black_fennec.structure.structure import Structure
from src.black_fennec.util.json.json_reference_resolving_service import JsonReferenceResolvingService

logger = logging.getLogger(__name__)


class Reference(Structure):
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
        Structure.__init__(self, reference)
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
    def destination(self) -> Structure:
        """Getter for destination

        Automatically resolves underlying reference
        
        Returns:
            Structure: destination to which the reference points
        """
        if self.value:
            return self._json_reference_resolve_service.resolve(
                self.value,
                self
            )

    def __str__(self) -> str:
        """Convert to string"""
        return str(self.value)

    def __repr__(self) -> str:
        """Create representation for pretty printing"""
        return f'Reference({self.value})'

    def accept(self, visitor):
        return visitor.visit_reference(self)


Reference.TEMPLATE = Reference(Dummy('ReferenceResolvingService'))
