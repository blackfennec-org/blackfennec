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
    def default(self):
        if 'default' in self.subject.value:
            return Number(self.subject.value['default'].value)
        return Number(0)

    def visit_number(self, subject_number: Number) -> Coverage:
        coverage = Coverage.COVERED
        return coverage

    def __repr__(self):
        return f'NumberTemplate({self.subject.__repr__()})'
