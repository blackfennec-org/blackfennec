# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar, Optional
from blackfennec.structure.visitor import Visitor
from blackfennec.util.observable import Observable

T = TypeVar('T')
TVisitor = TypeVar('TVisitor')


class Structure(Observable, Generic[T], metaclass=ABCMeta):
    """Abstract base class for all types (Structures)."""

    def __init__(self):
        """Create Structure with parent.

        Args:
            value (T): The value of this structure.
        """
        super().__init__()
        self._parent: Optional[Structure] = None

    @property
    @abstractmethod
    def value(self) -> T:
        """Property for value of this structure."""
        ...

    @value.setter
    @abstractmethod
    def value(self, value: T):
        """Setter for value of this structure."""
        ...

    @property
    def parent(self) -> Optional['Structure']:
        """Property for parent of this structure."""
        return self._parent

    @parent.setter
    def parent(self, parent: 'Structure'):
        self._parent = parent

    def get_root(self) -> Optional['Root']:
        """Readonly property for `Root` of this structure."""
        if self.parent is None:
            return None
        return self.parent.get_root()

    @property
    def structure(self):
        return self

    @abstractmethod
    def accept(self, visitor: Visitor[TVisitor]) -> TVisitor:
        ...

    @abstractmethod
    def __repr__(self) -> str:
        ...

class ValueStructure(Structure[T], metaclass=ABCMeta):
    """Abstract base class for all structures that have a value."""

    def __init__(self, value: T):
        """Create ValueStructure with parent.

        Args:
            value (T): The value of this structure.
        """
        super().__init__()
        self._value = value

    @property
    def value(self) -> T:
        return self._value

    @value.setter
    def value(self, value: T):
        self._value = value
        self._notify(self.value, 'value')
