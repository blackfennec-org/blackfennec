# -*- coding: utf-8 -*-
import logging
from typing import TypeVar

from doubles.double_dummy import Dummy
from src.black_fennec.structure.structure import Structure
from src.black_fennec.structure.visitor import Visitor
from src.black_fennec.util.json.json_reference_resolving_service import JsonReferenceResolvingService

logger = logging.getLogger(__name__)
TVisitor = TypeVar('TVisitor')


class Reference(Structure[str]):
    """Core Type Reference, represents references in the domain model."""
    TEMPLATE = None

    def __init__(
            self,
            json_reference_resolve_service: JsonReferenceResolvingService,
            reference: str = ''
    ):
        """Reference Constructor.

        Args:
            reference (str): uri containing a json reference
        """
        Structure.__init__(self, reference)
        self._json_reference_resolve_service = json_reference_resolve_service

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

    def accept(self, visitor: Visitor[TVisitor]) -> TVisitor:
        return visitor.visit_reference(self)

    def __repr__(self) -> str:
        """Create representation for pretty printing"""
        return f'Reference({self.value})'


Reference.TEMPLATE = Reference(Dummy('ReferenceResolvingService'))
