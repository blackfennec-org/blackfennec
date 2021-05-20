# -*- coding: utf-8 -*-
import logging

from src.black_fennec.structure.number import Number
from src.black_fennec.structure.template.template_base import TemplateBase

logger = logging.getLogger(__name__)


class NumberTemplate(TemplateBase):
    """Base Class for Template of a Number."""
    def __init__(
            self,
            visitor: 'TemplateFactoryVisitor',
            subject: Number,
    ):
        TemplateBase.__init__(
            self,
            visitor,
            subject
        )

    def visit_number(self, subject: Number):
        return super().visit_number(subject)

    def __repr__(self):
        return f'NumberTemplate({self.subject.__repr__()})'
