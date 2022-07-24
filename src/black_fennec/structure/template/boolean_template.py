# -*- coding: utf-8 -*-

import logging

from src.black_fennec.interpretation.auction.coverage import Coverage
from src.black_fennec.structure.boolean import Boolean
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.template.template_base import TemplateBase

logger = logging.getLogger(__name__)


class BooleanTemplate(TemplateBase):
    """Base Class for Template of a Boolean."""

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
            return Boolean(self.subject.value['default'].value)
        return Boolean(False)

    def visit_boolean(self, subject_boolean: Boolean) -> Coverage:
        coverage = Coverage.COVERED
        return coverage

    def __repr__(self):
        return f'BooleanTemplate({self.subject.__repr__()})'
