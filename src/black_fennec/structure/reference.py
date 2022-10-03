# -*- coding: utf-8 -*-
import logging
from typing import TypeVar

from src.black_fennec.structure.string import String
from src.black_fennec.structure.structure import Structure
from src.black_fennec.structure.visitor import Visitor
from src.black_fennec.structure.reference_navigation.navigator import Navigator

logger = logging.getLogger(__name__)
TVisitor = TypeVar('TVisitor')


class Reference(Structure[list[Navigator]]):
    """Core Type Reference, represents references in the domain model."""
    TYPE = None

    def __init__(
            self,
            navigation: list[Navigator]
    ):
        """Reference Constructor.

        Args:
            navigation (list[Navigator]): list of Navigators
        """
        Structure.__init__(self, navigation)

    def resolve(self) -> Structure:
        """Resolves Reference navigation

        Returns:
            Structure: destination to which the reference_navigation points
        """
        current_structure = self
        for navigator in self.value:
            current_structure = navigator.navigate(current_structure)
        if current_structure == self:
            return String("Reference was not resolved correctly")
        return current_structure

    def accept(self, visitor: Visitor[TVisitor]) -> TVisitor:
        return visitor.visit_reference(self)

    def __repr__(self) -> str:
        """Create representation for pretty printing"""
        return f'Reference({self.value})'


Reference.TEMPLATE = Reference([])
