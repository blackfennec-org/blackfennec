# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

class Visitor(Generic[T], metaclass=ABCMeta):
    """Base class for all visitors as defined by the visitor pattern.

    This class is generic in T, the return type of the visit_* methods.
    """
    @abstractmethod
    def visit_string(self, subject: 'String') -> T:
        ...

    @abstractmethod
    def visit_number(self, subject: 'Number') -> T:
        ...

    @abstractmethod
    def visit_boolean(self, subject: 'Boolean') -> T:
        ...

    @abstractmethod
    def visit_reference(self, subject: 'Reference') -> T:
        ...

    @abstractmethod
    def visit_list(self, subject: 'List') -> T:
        ...

    @abstractmethod
    def visit_map(self, subject: 'Map') -> T:
        ...
