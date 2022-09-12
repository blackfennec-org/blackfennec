# -*- coding: utf-8 -*-

import logging

from src.black_fennec.interpretation.auction.coverage import Coverage
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.map import Map

from .template import Template

logger = logging.getLogger(__name__)


class NumberTemplate(Template[Number]):
    """Base Class for Template of a Number."""

    def __init__(
            self,
            visitor: "TemplateParser",
            subject: Map
    ):
        Template.__init__(self, visitor, subject)

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
        if not self.minimum:
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
        return f'NumberTemplate({self.subject.__repr__()})'
