# -*- coding: utf-8 -*-
import numbers
from typing import TypeVar
from src.black_fennec.structure.structure import Structure
from src.black_fennec.structure.visitor import Visitor

TVisitor = TypeVar('TVisitor')


class Number(Structure[numbers.Number]):
    """Core Type Number, represents numbers in the domain model."""

    def __init__(self, value: numbers.Number = 0):
        """Construct Number with item `item`.

        Args:
            value (numbers.Number, optional): The item of the `Number`.
                By default "" (empty number)
        """
        Structure.__init__(self, value)

    def accept(self, visitor: Visitor[TVisitor]) -> TVisitor:
        return visitor.visit_number(self)

    def __repr__(self) -> str:
        """Create representation for pretty printing"""
        return f'Number({self.value})'
