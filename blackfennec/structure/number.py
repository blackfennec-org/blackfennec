# -*- coding: utf-8 -*-
from typing import TypeVar
from blackfennec.structure.structure import ValueStructure
from blackfennec.structure.visitor import Visitor

TVisitor = TypeVar('TVisitor')
numb = int | float

class Number(ValueStructure[numb]):
    """Core Type Number, represents numbers in the domain model."""

    def __init__(self, value: numb = 0):
        """Construct Number with item `item`.

        Args:
            value (int, float, optional): The item of the `Number`.
                By default 0
        """
        super().__init__(value)

    def accept(self, visitor: Visitor[TVisitor]) -> TVisitor:
        return visitor.visit_number(self)

    def __repr__(self) -> str:
        """Create representation for pretty printing"""
        return f'Number({self.value})'
