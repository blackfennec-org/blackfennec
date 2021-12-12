# -*- coding: utf-8 -*-
from typing import TypeVar
from src.black_fennec.structure.structure import Structure
from src.black_fennec.structure.visitor import Visitor

TVisitor = TypeVar('TVisitor')


class Boolean(Structure[bool]):
    """Core Type Boolean, represents booleans in the domain model."""

    def __init__(self, value: bool = False):
        """Construct Boolean with value `value`.

        Args:
            value (bool, optional): The value of the `Boolean`.
                Default item is `False`
        """
        Structure.__init__(self, value)

    def accept(self, visitor: Visitor[TVisitor]) -> TVisitor:
        return visitor.visit_boolean(self)

    def __repr__(self) -> str:
        """Create representation for pretty printing"""
        return f'Boolean({self.value})'
