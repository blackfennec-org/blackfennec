# -*- coding: utf-8 -*-
from typing import TypeVar
from src.black_fennec.structure.structure import Structure
from src.black_fennec.structure.visitor import Visitor

TVisitor = TypeVar('TVisitor')


class String(Structure):
    """Core Type String, represents strings in the domain model."""

    def __init__(self, value: str = ''):
        """Construct String with item `item`.

        Args:
            value (str, optional): The item of the `String`.
                By default "" (empty string)
        """
        Structure.__init__(self, value)

    def accept(self, visitor: Visitor[TVisitor]) -> TVisitor:
        return visitor.visit_string(self)

    def __repr__(self) -> str:
        """Create representation for pretty printing"""
        return f'String({self.value})'
