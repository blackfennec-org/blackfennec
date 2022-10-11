# -*- coding: utf-8 -*-
from abc import ABCMeta
from typing import Generic, TypeVar

T = TypeVar('T')


class Visitor(Generic[T], metaclass=ABCMeta):
    """Base class for all visitors as defined by the visitor pattern.

    This class is generic in T, the return type of the visit_* methods.
    """
    def visit_structure(self, subject: 'Structure') -> T:
        raise AssertionError('This method should never be called.')

    def visit_string(self, subject: 'String') -> T:
        return self.visit_structure(subject)

    def visit_number(self, subject: 'Number') -> T:
        return self.visit_structure(subject)

    def visit_boolean(self, subject: 'Boolean') -> T:
        return self.visit_structure(subject)

    def visit_reference(self, subject: 'Reference') -> T:
        return self.visit_structure(subject)

    def visit_list(self, subject: 'List') -> T:
        return self.visit_structure(subject)

    def visit_map(self, subject: 'Map') -> T:
        return self.visit_structure(subject)

    def visit_null(self, subject: 'Null'):
        return self.visit_structure(subject)
