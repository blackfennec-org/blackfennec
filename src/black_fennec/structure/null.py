# -*- coding: utf-8 -*-
from typing import TypeVar
from src.black_fennec.structure.structure import Structure
from src.black_fennec.structure.visitor import Visitor

TVisitor = TypeVar('TVisitor')


class Null(Structure[None]):
    """Core Type Boolean, represents booleans in the domain model."""

    def __init__(self):
        """Construct Boolean with value `value`.

        Args:
            value (bool, optional): The value of the `Boolean`.
                Default item is `False`
        """
        Structure.__init__(self, None)
    

    @property
    def value(self) -> None:
        return None

    @value.setter
    def value(self, value: None):
        assert value == None, "Null cannot have a value"

    def accept(self, visitor: Visitor[TVisitor]) -> TVisitor:
        return visitor.visit_null(self)

    def __repr__(self) -> str:
        """Create representation for pretty printing"""
        return f'Null'
