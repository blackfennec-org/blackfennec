# -*- coding: utf-8 -*-

import logging

from src.black_fennec.interpretation.auction.coverage import Coverage
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.template.template_base import TemplateBase

logger = logging.getLogger(__name__)


class NumberTemplate(TemplateBase):
    """Base Class for Template of a Number."""

    def __init__(
            self,
            visitor: 'TemplateFactoryVisitor',
            subject: Map,
            is_optional: bool = False,
    ):
        TemplateBase.__init__(
            self,
            visitor,
            subject,
            is_optional
        )

    def create_instance(self):
        return self.default

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
