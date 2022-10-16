# -*- coding: utf-8 -*-
import numbers
from typing import TypeVar
from src.black_fennec.structure.structure import ValueStructure
from src.black_fennec.structure.visitor import Visitor

TVisitor = TypeVar('TVisitor')
numb = int | float

class Number(ValueStructure[numb]):
    """Core Type Number, represents numbers in the domain model."""

    def __init__(self, value: numb = 0):
        """Construct Number with item `item`.

        Args:
            value (numbers.Number, optional): The item of the `Number`.
                By default "" (empty number)
        """
        super().__init__(value)

    def accept(self, visitor: Visitor[TVisitor]) -> TVisitor:
        return visitor.visit_number(self)

    def __repr__(self) -> str:
        """Create representation for pretty printing"""
        return f'Number({self.value})'

    def __eq__(self, o):
        return self.value == o.value
