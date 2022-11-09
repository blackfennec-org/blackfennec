# -*- coding: utf-8 -*-
from typing import TypeVar
from blackfennec.structure.structure import Structure
from blackfennec.structure.visitor import Visitor

TVisitor = TypeVar('TVisitor')


class Null(Structure[None]):
    """Core Type Null, represents null values in the domain model."""

    @property
    def value(self) -> None:
        return None

    @value.setter
    def value(self, value: None):
        assert value is None, "Null cannot have a value"
        self._notify(self.value, 'value')

    def accept(self, visitor: Visitor[TVisitor]) -> TVisitor:
        return visitor.visit_null(self)

    def __repr__(self) -> str:
        """Create representation for pretty printing"""
        return 'Null'
