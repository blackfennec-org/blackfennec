# -*- coding: utf-8 -*-
import logging
from typing import TypeVar

from blackfennec.structure.string import String
from blackfennec.structure.structure import Structure
from blackfennec.structure.visitor import Visitor
from blackfennec.structure.reference_navigation.navigator import Navigator
from blackfennec.util.change_notification import ChangeNotification

logger = logging.getLogger(__name__)
TVisitor = TypeVar('TVisitor')


class Reference(Structure[list[Navigator]]):
    """Core Type Reference, represents references in the domain model."""
    TYPE = None

    def __init__(
            self,
            navigators: list[Navigator]
    ):
        """Reference Constructor.

        Args:
            navigation (list[Navigator]): list of Navigators
        """
        super().__init__()
        self._navigators = navigators

    @property
    def value(self) -> list[Navigator]:
        return self._navigators

    @value.setter
    def value(self, value: list[Navigator]):
        notification = ChangeNotification(self.value, value)
        self._navigators = value
        self._notify('changed', notification)

    def resolve(self) -> Structure:
        """Resolves Reference navigation

        Returns:
            Structure: destination to which the reference_navigation points
        """
        current_structure: Structure = self
        for navigator in self.value:
            current_structure = navigator.navigate(current_structure)
        if current_structure == self:
            message = "Reference was not resolved correctly"
            logger.warning(message)
            return String(message)
        return current_structure

    def accept(self, visitor: Visitor[TVisitor]) -> TVisitor:
        return visitor.visit_reference(self)

    def __repr__(self) -> str:
        """Create representation for pretty printing"""
        return f'Reference({self.value})'
