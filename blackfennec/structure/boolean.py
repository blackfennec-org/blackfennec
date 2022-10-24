# -*- coding: utf-8 -*-
from typing import TypeVar
from blackfennec.structure.structure import ValueStructure
from blackfennec.structure.visitor import Visitor

TVisitor = TypeVar('TVisitor')


class Boolean(ValueStructure[bool]):
    """Core Type Boolean, represents booleans in the domain model."""

    def __init__(self, value: bool = False):
        """Construct Boolean with value `value`.

        Args:
            value (bool, optional): The value of the `Boolean`.
                Default item is `False`
        """
        super().__init__(value)

    def accept(self, visitor: Visitor[TVisitor]) -> TVisitor:
        return visitor.visit_boolean(self)

    def __repr__(self) -> str:
        """Create representation for pretty printing"""
        return f'Boolean({self.value})'
