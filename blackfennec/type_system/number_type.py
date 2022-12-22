# -*- coding: utf-8 -*-

import logging

from blackfennec.type_system.interpretation.coverage import Coverage
from blackfennec.structure.null import Null
from blackfennec.structure.number import Number
from blackfennec.structure.map import Map
from blackfennec.structure.string import String
from .type import Type

logger = logging.getLogger(__name__)


class NumberType(Type[Number]):
    """Base Class for Type of a Number."""

    def __init__(self, subject: Map = None):
        subject = subject or self._type_structure()
        Type.__init__(self, subject)

    @staticmethod
    def _type_structure():
        return Map({"type": String("Number"), "super": Null()})

    @property
    def default(self) -> Number:
        if 'default' in self.subject.value:
            return Number(self.subject.value['default'].value)
        return Number()

    @property
    def minimum(self):
        if 'minimum' in self.subject.value:
            return self.subject.value['minimum'].value
        return None

    @minimum.setter
    def minimum(self, value):
        if not self.minimum:
            self.subject.remove_item('minimum')
            self.subject.add_item('minimum', Number())
        self.subject.value['minimum'].value = value

    @property
    def maximum(self):
        if 'maximum' in self.subject.value:
            return self.subject.value['maximum'].value
        return None

    @maximum.setter
    def maximum(self, value):
        if not self.maximum:
            self.subject.remove_item('maximum')
            self.subject.add_item('maximum', Number())
        self.subject.value['maximum'].value = value

    def visit_number(self, subject: Number) -> Coverage:
        if self.minimum and subject.value < self.minimum:
            return Coverage.NOT_COVERED
        if self.maximum and subject.value > self.maximum:
            return Coverage.NOT_COVERED
        return Coverage.COVERED

    def __repr__(self):
        return f'NumberType({self.subject.__repr__()})'
